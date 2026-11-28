register("brief", "01 · Frame the service", "Define the request, the existing workflow, the intended decision, and who owns the handoff.", [], ({ input }) => {
  return {
    service: "HarborLink transit support",
    user: input.role,
    task: "Answer a station access or fare question with evidence, or route it to a person.",
    manualBaseline: "A dispatcher searches the handbook and calls the owning team when needed.",
    ownerFor: serviceOwners,
    acceptance: acceptanceCriteria,
    primaryMetric: "Correct and usable responses / submitted requests",
    guardrail: "Zero restricted disclosures on the fixed test cases",
  };
});

register("modalities", "02 · Collect evidence and provenance", "Bring document, speech and image observations into one record format using bundled, pre-extracted fixtures.", [], () => {
  const observations = mediaFixtures();
  return { observations, editorialRule: "Confirm uncertain extractions against the source before publishing.",
    transfer: "Replace either fixture with an OCR or speech adapter that returns the same provenance fields. Generated media needs its own provenance and review." };
});

register("corpus", "03 · Ingest and version the handbook", "Normalize text while preserving record ID, audience, effective date and evidence location.", ["modalities"], ({ dependencies }) => {
  return buildCorpus(dependencies.modalities.observations);
});

register("language", "04 · Represent language and similarity", "Inspect word tokens, character fragments, lexical overlap and a hand-built dense concept vector.", [], ({ input }) => {
  const language = languageTools(input.question);
  const characterPairs = language.tokens.slice(0, 3).flatMap((word) => {
    const chars = Array.from(word);
    return chars.slice(1).map((char, i) => chars[i] + char);
  });
  return { ...language, characterPairs };
});

register("learning", "05 · Train a routing baseline", "Train a small logistic classifier and compare its held-out routing decisions with the majority baseline.", ["language"], ({ dependencies }) => {
  const training = [{ x: 0, y: 0 }, { x: 1, y: 1 }, { x: 0, y: 0 }, { x: 1, y: 1 }, { x: 0, y: 0 }];
  const test = [{ query: "How do I get my fare back?", y: 0 }, { query: "Wheelchair access during elevator outage", y: 1 },
    { query: "Can I get a student pass?", y: 0 }, { query: "Step-free access to the lift", y: 1 }];
  let weight = 0;
  let bias = 0;
  const predict = (x) => 1 / (1 + Math.exp(-Math.max(-40, Math.min(40, weight * x + bias))));
  for (let epoch = 0; epoch < 80; epoch += 1) {
    for (const row of training) {
      const error = predict(row.x) - row.y;
      weight -= 0.12 * error * row.x;
      bias -= 0.12 * error;
    }
  }
  const feature = (vector) => Number(vector[1] > 0);
  const cases = test.map(({ query, y }) => {
    const score = predict(feature(dependencies.language.embed(query)));
    return { query, expected: y, predicted: Number(score >= 0.5) };
  });
  const selected = predict(feature(dependencies.language.vector));
  return {
    trained: { weight, bias }, cases,
    accuracy: cases.filter((row) => row.expected === row.predicted).length / cases.length,
    majorityAccuracy: test.filter((row) => row.y === 0).length / test.length,
    accessScore: selected, route: selected >= 0.5 ? "Accessibility review" : "General support",
    note: "Toy point estimate, not a calibrated probability for real rider requests.",
  };
});

register("attention", "06 · Inspect attention and token choice", "Calculate masked scaled dot-product attention, a residual update, and temperature-adjusted next-token probabilities.", ["language"], ({ dependencies }) => {
  const softmax = (values) => {
    const maximum = Math.max(...values);
    const terms = values.map((value) => Math.exp(value - maximum));
    return terms.map((term) => term / terms.reduce((sum, value) => sum + value, 0));
  };
  const keys = [[1, 0], [0, 1], [1, 1]];
  const values = [[0.2, 0.8], [0.8, 0.2], [0, 1]];
  const query = dependencies.language.vector[1] > 0 ? [0, 1] : [1, 0];
  const logits = keys.map((key, i) => i === 2 ? -Infinity :
    key.reduce((sum, value, j) => sum + value * query[j], 0) / Math.sqrt(key.length));
  const weights = softmax(logits);
  const routed = query.map((value, j) => value + values.reduce((sum, vector, i) => sum + vector[j] * weights[i], 0));
  const vocabulary = ["Answer", "Check", "Escalate"];
  const tokenLogits = [routed[0], routed[1], -0.1];
  const distribution = (temperature) => Object.fromEntries(vocabulary.map((token, i) => [
    token, softmax(tokenLogits.map((logit) => logit / temperature))[i],
  ]));
  return { query, weights, residual: routed, cold: distribution(0.5), warm: distribution(1.5),
    note: "One hand-specified attention head; this cell does not run a pretrained model." };
});

register("retrieve", "07 · Retrieve scoped, current evidence", "Select the effective revision first, apply audience scope, then compare lexical, cosine and hybrid rankings.", ["corpus", "language"], ({ input, dependencies }) => {
  const candidates = currentPolicies(input, dependencies.corpus.records);
  const { cosine, embed, overlap } = dependencies.language;
  const scores = candidates.map((record) => {
    const lexical = overlap(input.question, record.text);
    const dense = cosine(dependencies.language.vector, embed(record.text));
    const comparable = lexical / Math.max(1, dependencies.language.tokens.length);
    const score = input.ranking === "lexical" ? comparable : input.ranking === "dense" ? dense : 0.55 * comparable + 0.45 * dense;
    return { ...record, lexical, dense, score };
  }).filter((record) => record.score > 0).sort((a, b) => b.score - a.score || a.id.localeCompare(b.id));
  // A single matching concept is required for a definitive answer. Ranking can still surface clues.
  const topic = requestedTopic(input, dependencies.language);
  const eligible = topic.index !== null
    ? scores.filter((record) => embed(record.text)[topic.index] > 0)
    : [];
  return { ranking: input.ranking, candidates: scores.map(({ id, lexical, dense, score }) => ({ id, lexical, dense, score })),
    chosen: eligible.slice(0, 1), ambiguous: topic.ambiguous };
});

register("context", "08 · Assemble the prompt and evidence", "Separate product instructions from the request and evidence. Keep complete passages within the word budget.", ["retrieve"], ({ input, dependencies }) => {
  const context = packEvidence(input, dependencies.retrieve);
  return { ...context, modelInputExample: [{ role: "system", content: context.instructions },
    { role: "user", content: JSON.stringify({
      question: context.question, evidence: context.supplied.map(({ id, text }) => ({ id, text })),
    }) }], contextRule: "The word budget covers instructions, question and passage text. Provider token counts also depend on the message format." };
});

register("answer", "09 · Ground and validate the answer", "Use an extractive answer. Verify exact support, authorized audience and effective date before returning a citation.", ["context"], ({ input, dependencies }) => {
  return groundAnswer(input, dependencies.context);
});

register("workflow", "10 · Plan a bounded handoff", "Use a typed local tool, inspect the trace, checkpoint an approved action and reject a duplicate.", ["answer", "learning", "brief"], ({ input, dependencies }) => {
  const tools = {
    draftHandoff: { description: "Draft an internal review note in this workbook", input: { reason: "string", owner: "string" } },
  };
  const owner = dependencies.learning.route === "Accessibility review"
    ? dependencies.brief.ownerFor.access : "Service desk";
  if (input.outage) return { state: "paused", owner: "Service desk", steps: [], effects: [], toolDefinitions: tools };
  if (dependencies.answer.status !== "handoff") return { state: "complete", steps: ["read", "verify"], toolDefinitions: tools };
  const proposal = { reason: dependencies.answer.text, owner };
  const steps = ["read", "verify", "draft"];
  if (!(input.role === "staff" && input.approved)) {
    return { state: "awaiting review", owner, steps, proposal, toolDefinitions: tools };
  }
  const checkpoint = JSON.stringify({ proposal, steps });
  const restored = JSON.parse(checkpoint);
  const completed = new Set();
  const effects = [];
  const operation = JSON.stringify([input.question, input.date, restored.proposal]);
  function apply(id, draft) {
    if (completed.has(id)) return "replay ignored";
    if (typeof draft.reason !== "string" || typeof draft.owner !== "string") throw new Error("Invalid handoff");
    completed.add(id);
    effects.push({ owner: draft.owner, reason: draft.reason });
    return "local note recorded";
  }
  const first = apply(operation, restored.proposal);
  const replay = apply(operation, restored.proposal);
  return { state: "local note recorded", owner, steps: [...restored.steps, "approved", "recorded"],
    effects, replay, first, toolDefinitions: tools, scope: "Simulated local effect, no messages or writes to external systems." };
});

register("adapt", "11 · Compare adaptation and quantization", "Train a rank-one correction on a synthetic two-label task, compare against a frozen baseline, then measure integer approximation.", [], () => {
  const examples = [{ x: -1.0, y: 0 }, { x: -0.8, y: 0 }, { x: 0.7, y: 1 }, { x: 1, y: 1 }];
  const heldOut = [{ x: -0.4, y: 0 }, { x: 0.4, y: 1 }];
  const sigmoid = (x) => 1 / (1 + Math.exp(-x));
  const base = 0.15;
  let a = 0.2;
  let b = 0.2;
  for (let step = 0; step < 50; step += 1) {
    for (const { x, y } of examples) {
      const difference = sigmoid(base + a * b * x) - y;
      const deltaA = difference * b * x;
      const deltaB = difference * a * x;
      a -= 0.15 * deltaA;
      b -= 0.15 * deltaB;
    }
  }
  const original = new Float32Array([a, b]);
  const scale = Math.max(Math.abs(a), Math.abs(b)) / 127;
  const packed = Int8Array.from(original, (value) => Math.round(value / scale));
  const restored = [...packed].map((value) => value * scale);
  const loss = (left, right) => heldOut.reduce((sum, { x, y }) => {
    const probability = sigmoid(base + left * right * x);
    return sum - Math.log(y === 1 ? probability : 1 - probability);
  }, 0) / heldOut.length;
  return { baselineLoss: loss(0, 0), adapterLoss: loss(a, b), quantizedLoss: loss(...restored),
    payloadBytes: { float32: original.byteLength, int8WithFloat32Scale: packed.byteLength + 4 },
    note: "Synthetic rank-one correction with frozen bias; size counts this adapter only. A quantized value is simulated by dequantizing it before scoring." };
});

register("serve", "12 · Deliver the service response", "Present the actual scoped answer, a review handoff, or a safe service-degraded response.", ["answer", "workflow"], ({ input, dependencies }) => {
  const result = presentResponse(input, dependencies.answer, dependencies.workflow);
  return { ...result, trace: { answerStatus: dependencies.answer.status, workflowState: dependencies.workflow.state } };
});

register("evaluate", "13 · Evaluate decisions and release gates", "Run a frozen set of critical cases through the current service. Compare lexical and hybrid retrieval when ranked retrieval is active.", [], ({ input, evaluate, isActive }) => {
  const cases = [
    { label: "Current fare version", question: "fare refund", date: "2026-11-21", role: "public", source: "fare-v2" },
    { label: "Historical fare version", question: "fare refund", date: "2026-03-01", role: "public", source: "fare-v1" },
    { label: "Accessibility paraphrase", question: "elevator", date: "2026-11-21", role: "public", source: "notice-lift" },
    { label: "Restricted policy", question: "ledger reconciliation", date: "2026-11-21", role: "public", source: null, critical: true },
    { label: "Authorized staff", question: "ledger reconciliation", date: "2026-11-21", role: "staff", source: "staff-review" },
    { label: "Missing evidence", question: "weather forecast", date: "2026-11-21", role: "public", source: null, critical: true },
    { label: "Tight context budget", question: "fare refund", date: "2026-11-21", role: "public", source: null, budget: 10, critical: true },
    { label: "Safe fallback", question: "fare refund", date: "2026-11-21", role: "public", source: null, outage: true, critical: true },
  ];
  function compare(ranking) {
    const results = cases.map((test) => {
      const result = evaluate({ ...input, ...test, budget: test.budget ?? 80, ranking, approved: false, outage: !!test.outage }, "serve");
      const actual = result.citations[0]?.id || null;
      const pass = actual === test.source && result.status === (test.source ? "answered" : "handoff");
      return { case: test.label, expected: test.source || "handoff", actual: actual || result.status, critical: !!test.critical, pass };
    });
    return { ranking, results, passRate: results.filter(({ pass }) => pass).length / results.length,
      criticalPass: results.filter(({ critical }) => critical).every(({ pass }) => pass) };
  }
  if (!isActive("retrieve")) return { topicLookup: compare("topic lookup"), recommended: "No ranking comparison in topic lookup mode" };
  const lexical = compare("lexical");
  const hybrid = compare("hybrid");
  return { lexical, hybrid, recommended: hybrid.criticalPass && hybrid.passRate >= lexical.passRate ? "hybrid" : "hold",
    uncertainty: "A small deterministic fixture establishes only the listed behaviors." };
});

function currentChecks(evaluation) {
  return evaluation?.hybrid ?? evaluation?.topicLookup;
}

register("operations", "14 · Operate and recover", "Instrument the visible request, calculate canary burn rates from modeled events, and record a rollback decision.", ["serve", "evaluate"], ({ dependencies }) => {
  const exampleWindow = { goal: 0.99, control: { attempts: 100, good: 99 }, canary: { attempts: 20, good: 16 } };
  function rate({ attempts, good }) {
    const failure = (attempts - good) / attempts;
    return { attempts, good, success: good / attempts, burn: failure / (1 - exampleWindow.goal) };
  }
  const control = rate(exampleWindow.control);
  const canary = rate(exampleWindow.canary);
  return { currentRequest: { status: dependencies.serve.status, fallback: dependencies.serve.withFallback },
    simulatedWindow: { control, canary }, gate: canary.burn > 2 || !currentChecks(dependencies.evaluate)?.criticalPass ? "Hold and restore stable" : "Continue limited rollout",
    verifyRecovery: "Run a known query through the stable serving route and check both its source ID and status.",
    costModel: { labeledAsEstimate: true, servedRequests: 120, costPerRequest: 0.002, total: 120 * 0.002 } };
});

register("enterprise", "15 · Map the enterprise boundary", "Compare replaceable capabilities and validate who owns identity, storage, model serving, telemetry and recovery.", [], () => {
  const capabilities = [
    { capability: "identity", owner: "Service access team", contract: "Tenant and role from trusted identity provider" },
    { capability: "storage", owner: "Policy steward", contract: "Versioned source and retention policy" },
    { capability: "serving", owner: "Platform team", contract: "Versioned response and safe fallback" },
    { capability: "telemetry", owner: "Operations", contract: "Privacy-aware stage events" },
    { capability: "recovery", owner: "On-call lead", contract: "Restore plus tenant-isolation smoke test" },
  ];
  const mappings = {
    aws: ["IAM", "S3", "Bedrock or model endpoint", "CloudWatch", "Versioned backup and drill"],
    azure: ["Entra ID", "Blob Storage", "Azure model deployment", "Azure Monitor", "Versioned backup and drill"],
    googleCloud: ["Cloud IAM", "Cloud Storage", "Vertex AI endpoint", "Cloud Monitoring", "Versioned backup and drill"],
  };
  const compatible = Object.values(mappings).every((list) => list.length === capabilities.length);
  return { capabilities, mappings, compatible, scope: "Illustrative capability map. No cloud services are contacted or provisioned." };
});

register("delivery", "16 · Decide what ships", "Combine the measured fixture evidence with a specification, an operator handoff and a human-owned release decision.", ["brief", "serve", "evaluate", "operations", "enterprise"], ({ dependencies }) => {
  const release = currentChecks(dependencies.evaluate)?.criticalPass === true && dependencies.enterprise?.compatible === true;
  return { owners: dependencies.brief.ownerFor, spec: dependencies.brief.acceptance,
    releaseEvidenceReady: release, currentStatus: dependencies.serve.status, rollout: dependencies.operations?.gate ?? "Hold pending operations evidence",
    decision: release ? "Runnable prototype. Stage and review before real use." : "Hold pending passing checks and architecture review.",
    operatorPacket: ["Scope and owner", "Corpus and model versions", "Failure examples", "Manual intake and restore procedure"],
    nextExperiment: "Use real, approved representative data to compare a staffed baseline, the scoped assistant and a human review queue." };
});

register("reason", "17 · Search the decision space", "Find the shortest allowed plan and compare what happens when a key observation is unavailable.", ["answer"], ({ input, dependencies }) => {
  const graph = {
    intake: ["evidence", "manual"],
    evidence: ["verified"],
    verified: ["done"],
    manual: ["review", "evidence"],
    review: ["done"],
    done: [],
  };
  const evidence = dependencies.answer.status === "answered" && !input.outage;
  const destination = "done";
  const pending = [["intake"]];
  const seen = new Set(["intake"]);
  while (pending.length) {
    const path = pending.shift();
    const state = path.at(-1);
    if (state === destination) return { plan: path, transitions: path.length - 1, examined: [...seen],
      rule: "Evidence verification is unavailable on unsupported or degraded requests." };
    for (const step of graph[state]) {
      if (seen.has(step) || (step === "evidence" && !evidence)) continue;
      seen.add(step);
      pending.push([...path, step]);
    }
  }
  return { plan: [], reason: "No allowed route" };
});

register("serving", "18 · Batch and cache conservatively", "Group synthetic requests and use a scoped cache key that separates role, date, corpus version, budget and retrieval configuration.", ["corpus"], ({ input, dependencies, evaluate }) => {
  const cache = new Map();
  const sameQuery = { ...input, approved: false };
  const workload = [sameQuery, sameQuery, { ...sameQuery, role: input.role === "public" ? "staff" : "public" }];
  function cached(request) {
    const key = JSON.stringify([dependencies.corpus.schemaVersion, request.role, request.date,
      request.question, request.ranking, request.budget, !!request.outage]);
    if (cache.has(key)) return { cached: true, status: cache.get(key).status };
    const result = evaluate(request, "serve");
    cache.set(key, result);
    return { cached: false, status: result.status };
  }
  const batches = [workload.slice(0, 2), workload.slice(2)];
  return { batchSizes: batches.map((batch) => batch.length), outcomes: batches.flatMap((batch) => batch.map(cached)),
    transfer: "Real service caches also key by tenant and source revision. This per-run cache never stores generated answers across workbook runs." };
});

register("governance", "19 · Audit permissions and release evidence", "Compare critical fixture results with deployment controls, record owners, and keep modeled evidence separate from production claims.", ["evaluate", "enterprise"], ({ dependencies }) => {
  const authority = dependencies.enterprise?.capabilities.find(({ capability }) => capability === "identity");
  const critical = currentChecks(dependencies.evaluate)?.results.filter((entry) => entry.critical) ?? [];
  return { record: { version: "harborlink-prototype-1", accountableOwner: authority?.owner ?? "Unassigned pending architecture review",
      protectedData: "No real rider data. All handbook entries and role selections are synthetic.",
      decision: "Use only as a local prototype pending a real privacy, accessibility and reliability review." },
    critical: critical.map(({ case: name, pass }) => ({ name, pass })),
    consentAndAppeal: "A rider can ask a staffed desk to review a handoff or correct a policy reference.",
    releaseRelevantEvidence: critical.length > 0 && critical.every(({ pass }) => pass) };
});

register("frontier", "20 · Test a frontier claim", "Ablate the semantic ranking signal on fixed requests and record where the proposed capability still needs real evidence.", ["evaluate", "modalities"], ({ dependencies }) => {
  const { lexical, hybrid } = dependencies.evaluate ?? {};
  const comparison = lexical && hybrid ? { compared: ["lexical", "hybrid"], sameCases: lexical.results.length,
    netGain: hybrid.passRate - lexical.passRate,
    changed: hybrid.results.filter(({ pass }, index) => pass !== lexical.results[index].pass).map((entry) => entry.case) } :
    { compared: [], reason: "Open ranked retrieval and evaluation to run the ablation." };
  return { ...comparison,
    modalities: dependencies.modalities.observations.map(({ kind, extractedBy }) => ({ kind, extractedBy })),
    followUp: "Measure on unseen, representative station and language slices. Image generation, audio recognition and computer-use require separately supplied adapters and validation." };
});

register("experts", "21 · Route work inside a sparse layer", "Compare active and resident parameters, then check how a skewed batch loads the experts.", [], () => {
  const experts = [2, 6, 11, 15];
  const scores = [Math.log(3), 0, -1, -2];
  const chosen = scores.map((score, expert) => ({ score, expert })).sort((a, b) => b.score - a.score).slice(0, 2);
  const weighted = chosen.map(({ score, expert }) => ({ value: experts[expert], weight: Math.exp(score) }));
  const total = weighted.reduce((sum, item) => sum + item.weight, 0);
  const mixed = weighted.reduce((sum, { value, weight }) => sum + value * weight / total, 0);

  // This top-1 load fixture is separate from the single-token top-2 calculation.
  const arrivals = [0, 0, 0, 0, 0, 0, 1, 1];
  const counts = experts.map((_, expert) => arrivals.filter((chosenExpert) => chosenExpert === expert).length);
  const capacity = 4;
  return { mixed, routedExperts: chosen.map(({ expert }) => expert), activeParameters: 100 + chosen.length * 400,
    residentParameters: 100 + experts.length * 400, topOneBatch: { counts, capacity,
      overflow: counts.reduce((sum, count) => sum + Math.max(0, count - capacity), 0) } };
});

register("budgets", "22 · Spend inference compute selectively", "Compare an evidence-checked cascade with fixed budgets, then inspect one greedy draft verification.", [], () => {
  const fixtures = [{ cheap: true, expensive: true }, { cheap: true, expensive: true },
    { cheap: false, expensive: true }, { cheap: false, expensive: false }];
  function evaluateBudget(mode) {
    const verified = fixtures.filter(({ cheap, expensive }) => mode === "cheap" ? cheap :
      mode === "expensive" ? expensive : cheap || expensive).length;
    const escalations = mode === "cascade" ? fixtures.filter(({ cheap }) => !cheap).length : 0;
    const spend = mode === "expensive" ? fixtures.length * 4 : fixtures.length + 4 * escalations;
    return { verified, spend, escalations, spendPerVerified: spend / verified };
  }
  const draft = ["within", "14", "business", "days"];
  const target = ["within", "14", "calendar", "days"];
  const mismatch = draft.findIndex((token, index) => token !== target[index]);
  const committed = mismatch < 0 ? draft : [...draft.slice(0, mismatch), target[mismatch]];
  return { budgets: Object.fromEntries(["cheap", "expensive", "cascade"].map((mode) => [mode, evaluateBudget(mode)])),
    greedyCheck: { draft, target, committed }, unit: "Synthetic compute units" };
});

register("decisions", "23 · Turn scores into constrained decisions", "Compare action and review costs, then choose a feasible plan under a two-slot maintenance budget.", [], () => {
  const probability = 0.19;
  const options = [["act", (1 - probability) * 2], ["wait", probability * 8], ["review", 0.5]];
  const preferred = [...options].sort((a, b) => a[1] - b[1])[0][0];
  const jobs = [{ id: "large", slots: 2, benefit: 9 }, { id: "small-a", slots: 1, benefit: 6 },
    { id: "small-b", slots: 1, benefit: 6 }];
  const plans = jobs.reduce((all, job) => [...all, ...all.map((plan) => [...plan, job])], [[]]);
  const ranked = plans.filter((plan) => plan.reduce((sum, job) => sum + job.slots, 0) <= 2)
    .map((plan) => ({ jobs: plan.map(({ id }) => id), value: plan.reduce((sum, job) => sum + job.benefit, 0) }))
    .sort((a, b) => b.value - a.value);
  return { probability, expectedCosts: Object.fromEntries(options), preferred, optimalPlan: ranked[0],
    greedyPlan: { jobs: ["large"], value: 9 } };
});
