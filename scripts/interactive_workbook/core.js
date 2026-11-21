function mediaFixtures() {
  return [
    { id: "notice-lift", kind: "image", extractedBy: "synthetic OCR fixture", position: "page 1 · sign region",
      text: "For a lift outage at North Pier, ask station staff for the step-free route.", family: "lift-notice", topic: "access",
      from: "2026-01-01", role: "public" },
    { id: "audio-lost", kind: "audio", extractedBy: "synthetic transcript fixture", position: "00:14–00:22",
      text: "Found items can be collected from the Lost Property desk after confirmation.", family: "lost-notice", topic: "lost",
      from: "2026-01-01", role: "public" },
  ];
}

function buildCorpus(observations) {
  const records = [
    { id: "fare-v1", family: "fare-refund", topic: "fare", from: "2026-01-01", role: "public",
      text: "Submit a fare refund request within 30 days of purchase." },
    { id: "fare-v2", family: "fare-refund", topic: "fare", from: "2026-07-01", role: "public",
      text: "Submit a fare refund request within 14 days of purchase." },
    { id: "staff-review", family: "internal-reconciliation", topic: "ledger", from: "2026-01-01", role: "staff",
      text: "Send ledger reconciliation cases to the internal Finance review queue." },
    { id: "student-pass", family: "student-pass", topic: "pass", from: "2026-01-01", role: "public",
      text: "Show proof of enrollment at the ticket office to collect a student pass." },
  ];
  return {
    records: [...records, ...observations].map((record) => ({
      ...record,
      kind: record.kind || "document",
      position: record.position || "handbook · " + record.family,
      normalized: record.text.normalize("NFKC").toLowerCase(),
    })),
    schemaVersion: 1,
  };
}

function languageTools(question) {
  const groups = [
    ["refund", "refunds", "reimbursement", "fare"],
    ["lift", "elevator", "outage", "wheelchair", "step", "accessibility"],
    ["ledger", "reconciliation", "reconcile", "internal"],
    ["enrollment", "student", "pass"],
    ["lost", "found", "items", "property"],
  ];
  const stop = new Set(["a", "an", "the", "i", "for", "to", "in", "on", "is", "my", "what", "how", "can", "do", "of", "at", "days"]);
  function tokenize(text) {
    return (text.normalize("NFKC").toLowerCase().match(/[\p{L}\p{N}]+/gu) || []).filter((term) => !stop.has(term));
  }
  function embed(text) {
    const terms = new Set(tokenize(text));
    return groups.map((group) => group.reduce((n, word) => n + Number(terms.has(word)), 0));
  }
  function cosine(left, right) {
    const norm = Math.hypot(...left) * Math.hypot(...right);
    return norm ? left.reduce((sum, x, i) => sum + x * right[i], 0) / norm : 0;
  }
  function overlap(left, right) {
    const terms = new Set(tokenize(right));
    return [...new Set(tokenize(left))].filter((text) => terms.has(text)).length;
  }
  return { tokens: tokenize(question), vector: embed(question), tokenize, embed, cosine, overlap };
}

function currentPolicies(input, records) {
  const newest = new Map();
  records.forEach((record) => {
    if (record.from <= input.date && (newest.get(record.family)?.from || "") < record.from) newest.set(record.family, record);
  });
  return [...newest.values()].filter((record) => record.role === "public" || input.role === "staff");
}

function requestedTopic(input, language) {
  const requested = language.vector.map((weight, i) => ({ weight, i })).filter(({ weight }) => weight > 0);
  const unsupportedFareQuestion = requested.some(({ i }) => i === 0)
    && /\b(price|cost|amount|fee|fees|charge|how much)\b/i.test(input.question);
  return { index: requested.length === 1 && !unsupportedFareQuestion ? requested[0].i : null,
    ambiguous: requested.length > 1 };
}

function packEvidence(input, retrieval) {
  const instructions = "Use only the supplied policy evidence. Keep its conditions, then cite its source ID.";
  const question = input.question.trim();
  const count = (text) => text.trim().split(/\s+/).filter(Boolean).length;
  const fixedWords = count(instructions) + count(question);
  let remaining = Math.max(0, input.budget - fixedWords);
  const supplied = [];
  for (const record of retrieval.chosen) {
    const words = count(record.text);
    if (words <= remaining) {
      supplied.push(record);
      remaining -= words;
    }
  }
  return { instructions, question, budget: input.budget, fixedWords, evidenceWords: input.budget - Math.min(input.budget, fixedWords) - remaining,
    supplied, ambiguous: retrieval.ambiguous, truncated: fixedWords > input.budget || retrieval.chosen.length > supplied.length };
}

function groundAnswer(input, context) {
  const source = context.supplied[0];
  if (!source) {
    const reason = context.truncated ? "Evidence does not fit the context budget." :
      context.ambiguous ? "Separate the topics or ask a person to review both." :
      "No relevant, currently valid evidence is available for this request.";
    return { status: "handoff", text: reason, citations: [] };
  }
  const proposed = { status: "answered", text: source.text, citations: [{
    id: source.id, source: source.position, kind: source.kind, effective: source.from,
  }] };
  const valid = proposed.citations.every((citation) => context.supplied.some((record) =>
    record.id === citation.id && record.text === proposed.text && record.from <= input.date &&
    (record.role === "public" || input.role === "staff")));
  return valid ? proposed : { status: "handoff", text: "The source verification failed.", citations: [] };
}

const serviceOwners = Object.freeze({ policy: "Finance support", maintenance: "Station operations", access: "Accessibility desk" });
const acceptanceCriteria = Object.freeze(["Current source matches request date", "Caller can see all cited evidence",
  "Unresolved requests reach the manual queue", "No change to live transit records"]);

function presentResponse(input, outcome, workflow) {
  if (input.outage) return { status: "handoff", text: "Live lookup is paused in this simulation. Contact the staffed service desk.",
    citations: [], next: "Service desk", withFallback: true };
  if (outcome.status === "answered") return { ...outcome, next: "Review the source and effective date", withFallback: false };
  return { ...outcome, next: workflow.owner,
    review: workflow.state, withFallback: false };
}

// These implementations form the standalone service. They have no dependency on cell bodies.
const baseline = new Map(Object.entries({
  brief: { requires: [], run: () => ({ ownerFor: serviceOwners, acceptance: acceptanceCriteria }) },
  modalities: { requires: [], run: () => ({ observations: mediaFixtures() }) },
  corpus: { requires: ["modalities"], run: ({ dependencies }) => buildCorpus(dependencies.modalities.observations) },
  language: { requires: [], run: ({ input }) => languageTools(input.question) },
  learning: { requires: [], run: () => ({ route: "General support" }) },
  retrieve: { requires: ["corpus", "language"], run: ({ input, dependencies }) => {
    const topic = requestedTopic(input, dependencies.language);
    const topicName = ["fare", "access", "ledger", "pass", "lost"][topic.index];
    const chosen = currentPolicies(input, dependencies.corpus.records)
      .filter((record) => record.topic === topicName).slice(0, 1);
    return { ranking: "topic lookup", chosen, ambiguous: topic.ambiguous };
  } },
  context: { requires: ["retrieve"], run: ({ input, dependencies }) => packEvidence(input, dependencies.retrieve) },
  answer: { requires: ["context"], run: ({ input, dependencies }) => groundAnswer(input, dependencies.context) },
  workflow: { requires: ["answer"], run: ({ input, dependencies }) => ({ owner: "Service desk", effects: [],
    state: input.outage ? "paused" : dependencies.answer.status === "answered" ? "complete" : "manual review" }) },
  serve: { requires: ["answer", "workflow"], run: ({ input, dependencies }) =>
    presentResponse(input, dependencies.answer, dependencies.workflow) },
}));
