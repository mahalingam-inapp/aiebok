"""Generate concept cards, knowledge areas, labs, patterns, and architecture studios."""
from __future__ import annotations

import re
import textwrap
from pathlib import Path

from concept_card_enrichments import card_enrichment
from generate_books import BOOKS, slug
from topic_knowledge import TOPIC_FACTS, get_topic_entry, normalize

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CONCEPTS = DOCS / "concepts" / "cards"
LABS = ROOT / "labs"
DOCS_LABS = DOCS / "labs"
PATTERNS = DOCS / "patterns"
ARCH = DOCS / "architectures"
KA = DOCS / "knowledge-areas"

EXISTING_CONCEPTS = {
    "tokens", "embeddings", "rag", "evaluation", "skills-harnesses",
    "attention", "kv-cache", "prompt-injection", "agents", "structured-output",
    "chunking", "reranking", "tool-calling", "fine-tuning",
}


def title_from_slug(s: str) -> str:
    return " ".join(w if w.isupper() and len(w) <= 4 else w.capitalize() for w in s.split("-"))


def render_concept_card(topic: str) -> str:
    key = normalize(topic)
    explanation, example, evidence = get_topic_entry(topic)
    title = title_from_slug(key)
    extra = card_enrichment(key)
    when_use = extra["when_to_use"]
    when_not = extra["when_not"]
    failures = "\n".join(f"- {f}" for f in extra["failure_modes"])
    checklist = "\n".join(f"- {c}" for c in extra["checklist"])
    chapters = extra["chapters"]
    chapter_block = ""
    if chapters:
        chapter_block = "\n## Related chapters\n\n" + "\n".join(
            f"- [{Path(c).name.replace('.md', '').replace('-', ' ').title()}]({c.replace('../books/', '../../books/')})"
            for c in chapters
        ) + "\n"
    related = extra["related"]
    related_block = ""
    if related:
        related_block = "\n## Related concepts\n\n" + "\n".join(
            f"- [{title_from_slug(r)}](../../concepts/cards/{r}.md)" for r in related if r in TOPIC_FACTS
        ) + "\n"
    return f"""# {title}

**Purpose:** Reference card for **{title.lower()}** used across AIEBOK books and knowledge areas.

## Core explanation

{explanation}

## Example

{example}

## When to use

{when_use}

## When not to use

{when_not}

## Engineering checklist

{checklist}

## Evidence of understanding

{evidence}

## Common failure modes

{failures}

## Trade-offs

No mechanism is universal. Compare {title.lower()} against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.
{related_block}{chapter_block}
## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
"""


def generate_concept_cards() -> int:
    CONCEPTS.mkdir(parents=True, exist_ok=True)
    count = 0
    lines = ["# Concept Card Index", "", "Alphabetical reference cards for catalog topics.", ""]
    for key in sorted(TOPIC_FACTS):
        path = CONCEPTS / f"{key}.md"
        topic = title_from_slug(key)
        path.write_text(render_concept_card(topic), encoding="utf-8")
        lines.append(f"- [{topic}]({key}.md)")
        count += 1
    (CONCEPTS / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return count


KA_CONTENT: dict[str, str] = {
    "00-foundations": """# KA 00 — Foundations

## Purpose

Build a vocabulary for intelligence, learning, reasoning, memory, feedback, and optimization before treating language models as magic.

## What you should be able to do

- Decompose a task into perception, representation, memory, learning, planning, action, and feedback
- Implement search and planning on a bounded state space
- Explain why fluent language is not evidence of reliable decision-making
- Connect classical AI ideas to modern ML and agent systems

## Core mechanisms

| Mechanism | Engineering role | Common failure |
|---|---|---|
| Goal-directed behavior | Defines success criteria | Optimizing prose instead of outcomes |
| Search & planning | Explores action sequences | Missing stopping rules and costs |
| Learning | Generalizes from data | Overfitting and distribution shift |
| Feedback | Closes control loops | No channel from production errors to updates |

## Guided path

1. [Book 1 — Foundations of Intelligence](../books/01-foundations-of-intelligence/index.md)
2. Labs: `labs/01-*` through `labs/06-*`
3. Concepts: [goal-directed behavior](../concepts/cards/goal-directed-behavior.md), [A*](../concepts/cards/a.md), [feedback](../concepts/cards/feedback.md)

## Architecture studio

Given a decision problem, separate what should be deterministic, learned, retrieved, or reviewed by a human. Document the boundary in an ADR with eval evidence.

## Practice project

Build and compare a rule-based solver, search-based solver, and learned predictor for one bounded routing or classification problem. Report where each approach wins and fails.
""",
}


def concept_md_link(topic: str) -> str:
    key = normalize(topic)
    if (CONCEPTS / f"{key}.md").exists():
        return f"../concepts/cards/{key}.md"
    featured = DOCS / "concepts" / f"{key}.md"
    if featured.exists():
        return f"../concepts/{key}.md"
    aliases = {
        "tokenization": "tokens",
        "embeddings": "embeddings",
        "structured output": "structured-output",
        "tool calling": "tool-calling",
        "fine tuning": "fine-tuning",
        "kv cache": "kv-cache",
    }
    alias = aliases.get(topic.lower())
    if alias and (DOCS / "concepts" / f"{alias}.md").exists():
        return f"../concepts/{alias}.md"
    return f"../concepts/cards/{key}.md"


def ka_template(ka_id: str, title: str, purpose: str, book_link: str, topics: list[str], project: str) -> str:
    topic_links = "\n".join(f"- [{t}]({concept_md_link(t)})" for t in topics[:8])
    return f"""# {title}

## Purpose

{purpose}

## What you should be able to do

- Explain the central mechanisms without vendor-specific jargon
- Build or inspect a minimal implementation for each core mechanism
- Evaluate quality, latency, cost, safety, and operational consequences
- Defend architecture choices with measured evidence

## Core topics

{topic_links}

## Guided path

- Primary book: [{book_link}](../books/{book_link}/index.md)
- Concept cards: [cards index](../concepts/cards/index.md)
- Matching labs: search `labs/` for this knowledge area number

## Architecture studio

Apply the enterprise and reference architectures in [architectures/](../architectures/index.md) to a realistic scenario. Threat-model authorization, failure, and cost.

## Practice project

{project}
"""


def generate_knowledge_areas() -> int:
    from ka_deep_content import all_ka_pages

    pages = all_ka_pages()
    for ka_file, text in pages.items():
        (KA / f"{ka_file}.md").write_text(text, encoding="utf-8")
    return len(pages)


def lab_slug(book_no: int, chapter_no: int, title: str) -> str:
    return f"{book_no:02d}{chapter_no:02d}-{slug(title)}"[:48].strip("-")


def generate_labs() -> int:
    from chapter_catalog import CHAPTER_HOOKS

    count = 0
    doc_lines = ["# Lab Catalog", "", "One lab per guided book chapter.", ""]
    for book_no, book in enumerate(BOOKS, 1):
        for chapter_no, chapter in enumerate(book["chapters"], 1):
            title = chapter[0]
            ls = lab_slug(book_no, chapter_no, title)
            lab_dir = LABS / ls
            lab_dir.mkdir(parents=True, exist_ok=True)
            hook = CHAPTER_HOOKS.get((book_no, chapter_no), "print('lab stub')")
            main_py = f'"""Lab {book_no}.{chapter_no}: {title}"""\n\n' + hook + "\n"
            (lab_dir / "main.py").write_text(main_py, encoding="utf-8")
            readme = f"# Lab {book_no}.{chapter_no} — {title}\n\nRun `python main.py` from this directory.\n\nPractice: {chapter[3]}\n"
            (lab_dir / "README.md").write_text(readme, encoding="utf-8")
            doc_path = DOCS_LABS / f"{ls}.md"
            doc_path.write_text(
                f"# Lab {book_no}.{chapter_no} — {title}\n\n"
                f"**Book:** {book['title']}  \n"
                f"**Practice:** {chapter[3]}\n\n"
                f"```bash\npython labs/{ls}/main.py\n```\n",
                encoding="utf-8",
            )
            doc_lines.append(f"- [Lab {book_no}.{chapter_no} — {title}]({ls}.md)")
            count += 1
    (DOCS_LABS / "catalog.md").write_text("\n".join(doc_lines) + "\n", encoding="utf-8")
    return count


PATTERN_SPECS = [
    ("hybrid-retrieval", "Hybrid Retrieval", "Combine lexical and dense retrievers when queries mix identifiers and paraphrases.", "Use reciprocal rank fusion or learned reranking after dual retrieval.", "Better recall across query types.", "Extra latency, index complexity, tuning burden.", "Single-method retrieval suffices for uniform query distribution."),
    ("retrieve-then-rerank", "Retrieve Then Rerank", "Fast first-stage retrieval followed by cross-encoder reranking.", "Retrieve top-N quickly; rerank top-M before generation.", "Improved precision@k.", "Added model call and latency.", "Small corpora where brute-force scoring is cheap."),
    ("human-approval-gate", "Human Approval Gate", "Pause agent loops before irreversible or high-cost actions.", "Require explicit approval token before side-effect tools run.", "Reduced catastrophic automation errors.", "Throughput and operator load.", "Read-only or fully reversible actions."),
    ("supervisor-worker", "Supervisor–Worker", "Delegate subtasks from a coordinator to specialized workers.", "Supervisor plans; workers execute bounded tools; results aggregate.", "Parallelism and separation of concerns.", "Coordination overhead and failure modes.", "Single-agent loop with parallel tool calls is enough."),
    ("eval-gated-release", "Eval-Gated Release", "Block release until predefined eval slices pass.", "CI runs component and end-to-end evals with thresholds.", "Safer deployment of probabilistic systems.", "Slower release cadence; eval maintenance.", "Non-production experiments without user impact."),
    ("prompt-versioning", "Prompt Versioning", "Treat prompts as versioned code with regression tests.", "Store prompts in repo; run eval harness on change.", "Traceability and rollback.", "Process overhead for small teams.", "Throwaway prototypes not entering production."),
    ("context-budget-packing", "Context Budget Packing", "Allocate fixed token budgets per context section by priority.", "Rank sections; truncate or summarize low-priority blocks.", "Predictable cost and fewer overflow failures.", "Lost nuance from truncation.", "Short contexts where everything fits."),
    ("structured-output-validation", "Structured Output Validation", "Parse and validate model JSON against schemas before use.", "Schema validate; repair or reject; never trust raw strings.", "Safer integration with business logic.", "Parse failures on ambiguous extractions.", "Fully free-form chat UX."),
    ("checkpoint-resume", "Checkpoint Resume", "Persist agent state to survive interruptions.", "Save state after each step; resume idempotently.", "Reliable long-running workflows.", "Storage and consistency complexity.", "Sub-minute synchronous tasks."),
    ("model-routing", "Model Routing", "Route requests to models by risk, cost, and capability.", "Classifier or rules pick model tier per request.", "Cost control with quality where needed.", "Routing errors and operational complexity.", "Single model meets all slices."),
    ("slice-based-eval", "Slice-Based Evaluation", "Report metrics per subpopulation, not aggregates alone.", "Define slices upfront; gate release on worst-slice performance.", "Surfaces hidden failures.", "More labels and analysis time.", "Homogeneous low-risk workloads."),
    ("citation-grounded-answer", "Citation-Grounded Answer", "Require claims to link to retrieved passages.", "Generate with citations; validate alignment post-hoc.", "Improved auditability.", "Citation theater if validation is weak.", "Creative tasks without factual claims."),
    ("tool-sandbox", "Tool Sandbox", "Run tools with least privilege and typed arguments.", "Validate args; enforce ACL; timeout and audit.", "Limits blast radius of tool abuse.", "Integration friction.", "Trusted fixed-parameter internal calls."),
    ("semantic-cache", "Semantic Cache", "Reuse prior answers for similar queries.", "Embed query; lookup near-duplicates above threshold.", "Latency and cost savings.", "Stale or wrong cache hits.", "Highly unique or regulated queries."),
    ("spec-driven-ai-feature", "Spec-Driven AI Feature", "Write executable specs before model integration.", "Examples define acceptance; tests drive implementation.", "Aligns PM, eng, and evals.", "Upfront writing cost.", "Exploratory research spikes."),
    ("durable-agent-queue", "Durable Agent Queue", "Orchestrate long agents with queues and leases.", "Queue steps; lease workers; renew or reclaim.", "Scalable long-running automation.", "Distributed systems complexity.", "Short synchronous agent demos."),
    ("multi-tenant-retrieval", "Multi-Tenant Retrieval", "Isolate retrieval indexes and ACLs per tenant.", "Filter every query by tenant and role metadata.", "Prevents cross-tenant leakage.", "Index duplication and ops cost.", "Single-tenant internal tools."),
    ("adversarial-eval-suite", "Adversarial Eval Suite", "Red-team prompts and retrieved poison in CI.", "Maintain attack set; run before release.", "Catches known failure classes early.", "Arms race with new attacks.", "Low-risk internal summarization only."),
    ("fallback-degrade", "Fallback Degrade", "Graceful degradation when models or retrieval fail.", "Define cheaper/safer fallback path with user messaging.", "Availability during incidents.", "Reduced quality in fallback mode.", "Hard-fail acceptable for batch jobs."),
    ("observability-traces", "Observability Traces", "Trace retrieval, prompts, tools, and outputs per request.", "Structured spans with versions and latencies.", "Debuggability in production.", "Storage cost and PII risk.", "Offline batch without SLOs."),
    ("router-pattern", "Router", "Classify requests to specialized handlers or models.", "Lightweight classifier routes by intent or risk tier.", "Right-sized processing per request.", "Misroutes if classifier drifts.", "Single handler suffices."),
    ("fallback-cascade", "Fallback Cascade", "Try primary path then ordered fallbacks.", "Define fallback chain with explicit user messaging.", "Higher availability.", "Complexity and opaque behavior.", "Hard failure acceptable."),
    ("evaluator-optimizer", "Evaluator–Optimizer", "Generate candidates then score with independent evaluator.", "Sample N; evaluate; pick best.", "Quality gains on hard tasks.", "N× cost.", "Cheap verifier exists."),
    ("map-reduce-llm", "Map–Reduce LLM", "Split large inputs, process chunks, merge results.", "Map per chunk; reduce with structured merge.", "Handles long corpora.", "Merge errors and cost.", "Input fits context."),
    ("context-compressor", "Context Compressor", "Summarize or extract before main model call.", "Compress low-priority history to fixed budget.", "Fits more effective context.", "Information loss.", "Short sessions only."),
    ("retrieval-fusion", "Retrieval Fusion", "Merge multiple retriever lists without score calibration.", "RRF or learned fusion over ranked lists.", "Robust across retriever types.", "Tuning needed.", "One retriever dominates all queries."),
    ("citation-validator", "Citation Validator", "Verify generated claims against cited passages.", "Align spans; flag unsupported sentences.", "Reduces hallucinated citations.", "False rejects on paraphrase.", "No factual claims required."),
    ("tool-adapter", "Tool Adapter", "Wrap legacy APIs as typed model tools.", "Schema + auth + error mapping layer.", "Safer integrations.", "Maintenance of adapters.", "Greenfield typed APIs exist."),
    ("durable-checkpoint", "Durable Checkpoint", "Persist agent state after each external effect.", "Write checkpoint before/after side effects.", "Resumable workflows.", "Storage and idempotency requirements.", "Ephemeral demos."),
    ("circuit-breaker-model", "Circuit Breaker", "Stop calling failing model or tool temporarily.", "Open circuit on error rate threshold.", "Protects downstream systems.", "Delayed recovery detection.", "Batch offline jobs."),
    ("best-of-n-sample", "Best-of-N Sampling", "Generate N outputs; select with verifier or reward.", "Parallel samples; independent scoring.", "Higher quality on verifiable tasks.", "Linear cost in N.", "Strong verifier unavailable."),
    ("self-consistency", "Self-Consistency", "Majority vote over diverse reasoning paths.", "Sample multiple chains; aggregate answer.", "Improves math-like tasks.", "Cost and tie-breaking issues.", "Single pass is calibrated enough."),
    ("query-decomposition", "Query Decomposition", "Split complex user questions into sub-queries.", "Planner emits sub-queries; merge results.", "Better multi-hop coverage.", "Error propagation.", "Single-hop retrieval works."),
    ("parent-child-chunks", "Parent–Child Chunks", "Index small chunks; retrieve parents for context.", "Child for search; parent for generation.", "Precision plus context.", "Join complexity.", "Chunks already self-contained."),
    ("metadata-filter-first", "Metadata Filter First", "Apply ACL and facet filters before vector search.", "Hard filters shrink candidate set.", "Security and relevance.", "Over-filtering empty results.", "Open internal corpus."),
    ("prompt-injection-guard", "Prompt Injection Guard", "Separate trusted instructions from untrusted data.", "Delimiters + policy + output validation.", "Reduces injection success.", "Not foolproof alone.", "No external content in context."),
    ("human-review-queue", "Human Review Queue", "Queue low-confidence outputs for review.", "Score confidence; route below threshold.", "Quality on hard cases.", "Operational load.", "Low stakes automation."),
    ("offline-eval-regression", "Offline Eval Regression", "Run eval harness on every prompt/model change.", "CI dataset with thresholds.", "Prevents silent regressions.", "Dataset maintenance.", "Non-production sandboxes."),
    ("online-canary", "Online Canary", "Route small traffic fraction to candidate version.", "Compare live metrics with guardrails.", "Real-world validation.", "User impact if guardrails fail.", "Pre-production only testing."),
    ("feature-flag-model", "Feature-Flagged Model", "Toggle models or prompts without redeploy.", "Flag controls routing in gateway.", "Fast rollback.", "Flag misconfiguration risk.", "Static deployments OK."),
    ("batch-inference-window", "Batch Inference Window", "Accumulate requests for efficient GPU batches.", "Micro-batch within latency SLO.", "Higher throughput.", "Tail latency.", "Strict sub-second SLAs."),
    ("streaming-partial-ui", "Streaming Partial UI", "Show tokens progressively with cancel option.", "Stream deltas; allow stop.", "Better perceived latency.", "Harder to validate mid-stream.", "Batch response sufficient."),
    ("uncertainty-disclosure", "Uncertainty Disclosure", "Show confidence and sources to users.", "Calibrated scores + citations in UI.", "Trust and correction.", "Users may over-trust scores.", "Expert-only tools."),
    ("undo-ai-action", "Undo AI Action", "Make model-driven changes reversible.", "Store before-state; offer undo window.", "Safer automation.", "State management cost.", "Read-only assistants."),
    ("data-card-gate", "Data Card Gate", "Block training data use without documented card.", "Require lineage, consent, eval splits.", "Governance.", "Process friction.", "Internal experimental data only."),
    ("adapter-swapping", "Adapter Swapping", "Serve LoRA adapters per tenant or task.", "Load adapters dynamically on base model.", "Customization without full fine-tunes.", "Ops complexity.", "Single behavior everywhere."),
    ("speculative-decode", "Speculative Decoding", "Draft model proposes; target model verifies.", "Small draft + parallel verification.", "Faster decode.", "Implementation complexity.", "Latency already sufficient."),
    ("graph-retrieval-augment", "Graph Retrieval Augment", "Combine graph traversal with vector hits.", "Entities from graph; text from vectors.", "Multi-hop structured knowledge.", "Graph maintenance.", "Flat documents enough."),
    ("temporal-freshness-index", "Temporal Freshness Index", "Prefer recent documents when freshness matters.", "Boost by timestamp or version.", "Up-to-date answers.", "Wrong boost hurts evergreen docs.", "Static knowledge base."),
    ("llm-judge-calibration", "LLM Judge Calibration", "Calibrate automated judges against human ratings.", "Sample cases for dual review; fit calibration curve.", "Scalable eval.", "Judge bias.", "Human review is cheap enough."),
]

EXTRA_PATTERN_SPECS = [
    ("request-idempotency", "Request Idempotency", "Duplicate agent or API calls must not double-charge or double-write.", "Idempotency keys on side-effect tools.", "Safer retries.", "Key storage overhead.", "Read-only idempotent reads only."),
    ("prompt-cache-key", "Prompt Cache Key", "Reuse prefix KV cache across similar requests.", "Hash stable system prefix; cache by tenant.", "Lower latency/cost.", "Stale policy if prefix changes silently.", "Unique prompts every request."),
    ("tenant-rate-limit", "Tenant Rate Limit", "Fair usage across customers on shared models.", "Token bucket per tenant with burst.", "Protects platform.", "Throttling complaints.", "Single-tenant deployment."),
    ("output-schema-repair", "Output Schema Repair", "One repair attempt before failing structured output.", "Validate JSON; re-prompt with errors.", "Higher success rate.", "Extra latency.", "Free-form chat."),
    ("retrieval-cache", "Retrieval Cache", "Cache retrieval results for hot queries.", "TTL cache keyed by query+filters.", "Latency savings.", "Stale answers.", "Highly dynamic corpora."),
    ("embedding-drift-monitor", "Embedding Drift Monitor", "Detect when query/doc embedding distribution shifts.", "Track centroid distance and recall proxies.", "Early reindex signal.", "Alert noise.", "Static corpus."),
    ("dual-write-index", "Dual-Write Index", "Write new and old indexes during embedding migration.", "Query both; compare; cutover with flag.", "Safe migrations.", "Double write cost.", "No index migrations."),
    ("shadow-model", "Shadow Model", "Run candidate model without serving responses.", "Log shadow outputs; compare offline.", "Safe evaluation.", "Compute cost.", "Pre-prod only testing sufficient."),
    ("tool-result-truncation", "Tool Result Truncation", "Bound tool output size entering context.", "Summarize or clip with pointer to full payload.", "Prevents context blow-up.", "Lost detail.", "Tiny tool payloads."),
    ("conversation-summary-memory", "Conversation Summary Memory", "Compress older turns into rolling summary.", "Summarize after N turns; keep recent verbatim.", "Longer effective sessions.", "Summary errors compound.", "Short chats only."),
    ("policy-as-code", "Policy as Code", "Encode AI policies in testable rules.", "OPA/Rego or CI policy checks on configs.", "Auditable governance.", "Maintenance burden.", "Informal policy docs enough."),
    ("secrets-scopes", "Secrets Scopes", "Scope API keys per tool and environment.", "Separate keys; rotate; deny cross-env.", "Limits blast radius.", "Key sprawl.", "Single shared key internal only."),
    ("grounded-refusal", "Grounded Refusal", "Refuse when retrieval confidence is low.", "Threshold on retrieval score; templated refusal.", "Reduces hallucination.", "Lower answer rate.", "Creative writing tasks."),
    ("answer-ensemble", "Answer Ensemble", "Combine multiple retrieval or model paths.", "Vote or merge with verifier.", "Robustness.", "Cost.", "Single path calibrated."),
    ("doc-version-pin", "Document Version Pin", "Pin answers to explicit corpus version.", "Expose version in UI and logs.", "Auditability.", "UX complexity.", "Static FAQ."),
    ("latency-budget-router", "Latency Budget Router", "Pick model path by remaining SLA budget.", "Fast path when budget low.", "Meets SLO.", "Quality variance.", "Batch offline."),
    ("feedback-to-eval", "Feedback to Eval", "Promote production failures into eval sets.", "Weekly triage of bad traces into cases.", "Living eval set.", "Labeling cost.", "Stable workload."),
    ("pii-redaction", "PII Redaction", "Redact sensitive spans before logging or training.", "Detect/redact; store mapping securely.", "Compliance.", "Redaction errors.", "No PII workloads."),
    ("tool-timeout-cascade", "Tool Timeout Cascade", "Short timeouts with fallback tools.", "Primary tool timeout → secondary → human.", "Resilience.", "Complex flows.", "Single reliable tool."),
    ("chunk-overlap-tune", "Chunk Overlap Tuning", "Tune overlap for recall vs redundancy.", "Grid search overlap on eval queries.", "Better recall.", "Token waste.", "Small corpus brute force OK."),
    ("query-rewrite-cache", "Query Rewrite Cache", "Cache rewritten queries for repeat intents.", "Store rewrite+results for session.", "Latency.", "Wrong rewrite stuck.", "Highly diverse queries."),
    ("model-warm-pool", "Model Warm Pool", "Keep minimum replicas warm.", "HPA with min replicas > 0.", "Stable tail latency.", "Idle cost.", "Sporadic batch jobs."),
    ("gradual-rollout", "Gradual Rollout", "Increase traffic to new version slowly.", "5→25→50→100 with gates.", "Limits incident blast.", "Slower releases.", "Low traffic features."),
    ("trace-sampling", "Trace Sampling", "Sample traces for cost while keeping errors.", "100% errors; sample successes.", "Affordable observability.", "Miss rare bugs.", "Full trace budget available."),
    ("index-compaction", "Index Compaction", "Periodic compaction of vector segments.", "Scheduled merge jobs.", "Stable query perf.", "Ops work.", "Tiny indexes."),
    ("role-based-prompts", "Role-Based Prompts", "Different system prompts by user role.", "RBAC selects prompt template.", "Least privilege answers.", "Template sprawl.", "Uniform users."),
    ("structured-logging", "Structured Logging", "Log JSON fields for retrieval and generation.", "Standard schema across services.", "Queryable ops.", "Volume.", "Prototype only."),
    ("batch-embed-pipeline", "Batch Embed Pipeline", "Embed documents in offline batches.", "Queue docs; batch embed; atomic index swap.", "Cost efficient.", "Ingest lag.", "Real-time ingest required."),
    ("answer-diff-review", "Answer Diff Review", "Show diff when model changes answer on rerun.", "Highlight changed spans to user.", "Trust.", "UI noise.", "Deterministic systems."),
    ("confidence-calibration", "Confidence Calibration", "Map scores to calibrated probabilities.", "Isotonic regression on held-out set.", "Better thresholds.", "Data needs.", "Ordinal scores enough."),
    ("tool-allowlist", "Tool Allowlist", "Explicit allowlist per agent profile.", "Config declares permitted tools.", "Security.", "Rigid.", "Fully trusted env."),
    ("session-affinity", "Session Affinity", "Route returning users to warm context.", "Sticky routing to cached prefix.", "Latency.", "Imbalanced load.", "Stateless OK."),
    ("negative-feedback-loop", "Negative Feedback Loop", "Use thumbs-down to block similar failures.", "Embed complaint; nearest-neighbor block or finetune.", "Quality improvement.", "Feedback bias.", "No user feedback channel."),
    ("schema-first-tools", "Schema-First Tools", "Design tools from OpenAPI/JSON Schema first.", "Generate tool defs from schema.", "Consistency.", "Upfront design.", "Ad-hoc scripts."),
    ("retrieval-explain", "Retrieval Explain", "Show why passages were retrieved.", "Log scores and matched terms.", "Debuggability.", "UI clutter.", "Internal tools only."),
    ("multi-index-query", "Multi-Index Query", "Query product, policy, and ticket indexes.", "Parallel retrieval with merge.", "Coverage.", "Complexity.", "Single index sufficient."),
    ("token-budget-forecast", "Token Budget Forecast", "Estimate tokens before calling model.", "Pre-count sections; drop lowest priority.", "Fewer overflows.", "Estimation error.", "Tiny prompts."),
    ("human-in-loop-train", "Human-in-Loop Training", "Collect edits for SFT/DPO datasets.", "Capture accepted edits with consent.", "Improving models.", "Privacy/process.", "No retraining planned."),
    ("eval-data-versioning", "Eval Data Versioning", "Version eval sets like code.", "Git LFS or DVC for eval JSONL.", "Reproducible gates.", "Storage.", "Ad-hoc spreadsheets."),
    ("service-level-objectives", "SLO-Driven AI Ops", "Define SLOs for quality, latency, cost.", "Error budgets for releases.", "Operational clarity.", "Overhead.", "Research prototypes."),
    ("cross-encoder-gate", "Cross-Encoder Gate", "Cheap bi-encoder then expensive rerank.", "Two-stage with cutoff.", "Cost/quality balance.", "Tuning.", "Small corpora."),
    ("prompt-lint", "Prompt Lint", "Static checks on prompt templates.", "CI rules for banned phrases and PII.", "Safer prompts.", "False positives.", "Single static prompt."),
    ("agent-heartbeat", "Agent Heartbeat", "Detect stuck agents via heartbeat.", "Timeout if no progress events.", "Ops visibility.", "False timeouts.", "Sub-second tasks."),
    ("data-residency-route", "Data Residency Route", "Route requests to region-specific stacks.", "Geo DNS + regional indexes.", "Compliance.", "Duplicated infra.", "Single region OK."),
    ("model-terms-filter", "Model Terms Filter", "Block requests violating model AUP.", "Pre-filter inputs/outputs.", "Policy compliance.", "Over-blocking.", "Internal unrestricted use."),
    ("workflow-deterministic-core", "Deterministic Workflow Core", "Keep billing/auth deterministic; LLM at edges.", "Orchestrator code owns critical path.", "Safety.", "Less 'agent magic'.", "Fully exploratory chat."),
    ("incremental-index-update", "Incremental Index Update", "Update index incrementally on doc changes.", "CDC stream to chunk pipeline.", "Freshness.", "Complexity.", "Batch nightly enough."),
    ("quality-tier-routing", "Quality Tier Routing", "Premium vs standard model tiers.", "Route by subscription or risk.", "Cost control.", "Perceived unfairness.", "Flat tier product."),
]


def generate_patterns() -> int:
    all_patterns = PATTERN_SPECS + EXTRA_PATTERN_SPECS
    lines = ["# Pattern Catalog", "", "Reusable architecture patterns for AI systems.", ""]
    for ps, name, ctx, sol, pos, neg, avoid in all_patterns:
        text = f"""# {name}

## Context

{ctx}

## Solution

{sol}

## Consequences

{pos} {neg}

## Do not use when

{avoid}
"""
        (PATTERNS / f"{ps}.md").write_text(text, encoding="utf-8")
        lines.append(f"- [{name}]({ps}.md)")
    (PATTERNS / "catalog.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(all_patterns)


ARCH_SPECS = [
    ("enterprise-rag", "Enterprise RAG", "Authorized hybrid retrieval with citations and stage evals."),
    ("agent-platform", "Agent Platform", "Bounded agents with tools, checkpoints, and approval gates."),
    ("model-serving", "Model Serving", "Routed inference with batching, caching, and fallbacks."),
    ("eval-harness-platform", "Eval Harness Platform", "Component and E2E evals gating release."),
    ("prompt-context-service", "Prompt Context Service", "Versioned prompts, memory policies, and token budgets."),
    ("coding-agent-workspace", "Coding Agent Workspace", "Repo instructions, skills, and review gates for AI coding."),
    ("multimodal-document-ai", "Multimodal Document AI", "OCR, layout, extraction with provenance."),
    ("enterprise-ai-gateway", "Enterprise AI Gateway", "Central model access, policy, and observability."),
    ("fine-tuning-pipeline", "Fine-Tuning Pipeline", "Data cards, training, eval, and registry."),
    ("multi-cloud-ai-landing-zone", "Multi-Cloud AI Landing Zone", "Portable logical architecture across providers."),
    ("security-red-team-assistant", "Security Red-Team Assistant", "Tool-enabled assistant with sandbox and audit."),
    ("human-in-loop-operations", "Human-in-Loop Operations", "Approval workflows for high-impact actions."),
    ("semantic-search-engine", "Semantic Search Engine", "Lexical + vector indexes with eval loop."),
    ("llmops-control-plane", "LLMOps Control Plane", "Tracing, canaries, rollback, and FinOps."),
    ("research-reproduction-workbench", "Research Reproduction Workbench", "Baseline comparisons for frontier claims."),
    ("customer-support-copilot", "Customer Support Copilot", "Grounded replies with escalation paths."),
    ("data-governance-for-ai", "Data Governance for AI", "Lineage, residency, retention for training and RAG."),
    ("real-time-voice-agent", "Real-Time Voice Agent", "Streaming ASR/TTS with safety and latency SLOs."),
    ("batch-inference-factory", "Batch Inference Factory", "Offline large-scale inference with cost controls."),
    ("feature-store-for-ml", "Feature Store for ML", "Consistent features between training and serving."),
    ("graph-augmented-rag", "Graph-Augmented RAG", "Graph retrieval combined with vector search."),
    ("policy-as-code-ai", "Policy-as-Code AI", "Automated policy checks on prompts, tools, and outputs."),
    ("edge-ai-deployment", "Edge AI Deployment", "Quantized models on constrained devices."),
    ("federated-evaluation-grid", "Federated Evaluation Grid", "Slice evals across regions and tenants."),
    ("ai-product-experimentation", "AI Product Experimentation", "A/B infra with guardrails for AI features."),
]


def generate_architectures() -> int:
    lines = ["# Architecture Studio Catalog", "", "Reference architectures for design studios.", ""]
    for asn, name, goal in ARCH_SPECS:
        text = f"""# {name}

## Goal

{goal}

## Logical components

| Component | Responsibility |
|---|---|
| Ingress | AuthN/Z, rate limits, request routing |
| Context | Prompt assembly, memory, retrieval |
| Model access | Inference routing, caching, fallbacks |
| Tools | Typed integrations with audit |
| Validation | Schema, policy, citation checks |
| Observability | Traces, metrics, eval sampling |

## Critical decisions

Document ADRs for tenancy, retrieval strategy, model hosting, human oversight, and eval gates.

## Failure scenarios

Unauthorized access, stale knowledge, tool abuse, invalid structured output, provider outage, eval blind spots.

## Evaluation

Define component-level and journey-level metrics before choosing vendors or frameworks.
"""
        (ARCH / f"{asn}.md").write_text(text, encoding="utf-8")
        lines.append(f"- [{name}]({asn}.md)")
    (ARCH / "catalog.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(ARCH_SPECS)


def update_concept_library_links() -> None:
    lib = ROOT / "scripts" / "concept_library.py"
    text = lib.read_text(encoding="utf-8")
    if "cards/" in text:
        return
    text = text.replace(
        '"../../concepts/rag.md"',
        '"../../concepts/rag.md"',
    )
    # Point all concept links to cards when available
    old = '''def concept_link(topic: str) -> str | None:
    """Return a relative concept-card link when one exists."""
    key = normalize(topic)
    cards = {'''
    new = '''def concept_link(topic: str) -> str | None:
    """Return a relative concept-card link when one exists."""
    key = normalize(topic)
    card_path = f"../../concepts/cards/{key}.md"
    if (Path(__file__).resolve().parents[1] / "docs" / "concepts" / "cards" / f"{key}.md").exists():
        return card_path
    cards = {'''
    if old in text:
        text = text.replace(old, new)
        if "from pathlib import Path" not in text:
            text = text.replace("from functools import lru_cache", "from functools import lru_cache\nfrom pathlib import Path")
        lib.write_text(text, encoding="utf-8")


def update_index_pages(cards: int, labs: int, patterns: int, arch: int) -> None:
    (DOCS / "concepts" / "index.md").write_text(
        f"""# Concept Cards

Curated deep-dive cards plus **{cards} generated reference cards** in [cards/index.md](cards/index.md).

## Featured cards

- [Tokens](tokens.md), [Embeddings](embeddings.md), [RAG](rag.md), [Evaluation](evaluation.md)
- [Attention](attention.md), [KV Cache](kv-cache.md), [Agents](agents.md)
- [Prompt Injection](prompt-injection.md), [Structured Output](structured-output.md)
- [Tool Calling](tool-calling.md), [Fine-Tuning](fine-tuning.md), [Chunking](chunking.md), [Reranking](reranking.md)
- [Skills & Harnesses](skills-harnesses.md)

See the [full card index](cards/index.md) for every catalog topic.
""",
        encoding="utf-8",
    )
    (DOCS_LABS / "index.md").write_text(
        f"""# Lab Guide

**{labs} chapter labs** plus five foundational starter labs. See [catalog.md](catalog.md) for the full list.

| Starter | Concept | Run |
|---:|---|---|
| 01 | Cosine similarity | `python labs/01-cosine-similarity/main.py` |
| 02 | Semantic search | `python labs/02-semantic-search/main.py` |
| 03 | Basic RAG stages | `python labs/03-basic-rag/main.py` |
| 04 | Bounded agent loop | `python labs/04-agent-loop/main.py` |
| 05 | Evaluation harness | `python labs/05-eval-harness/main.py` |

Chapter labs follow `labs/BBCC-topic/main.py` where `BB` is book number and `CC` is chapter number.

## Lab standard

Every lab includes a runnable `main.py`, README, and docs page with practice alignment to the matching book chapter.
""",
        encoding="utf-8",
    )
    (PATTERNS / "index.md").write_text(
        f"""# Pattern Library

**{patterns} patterns** documented. Starters: [planner–executor](planner-executor.md), [human approval](human-approval.md).

See [catalog.md](catalog.md) for the full pattern list.
""",
        encoding="utf-8",
    )
    (ARCH / "index.md").write_text(
        f"""# Architecture Studios

**{arch} reference architectures** for design studios and ADRs.

- [Enterprise RAG](enterprise-rag.md)
- [catalog.md](catalog.md) — full list
""",
        encoding="utf-8",
    )


def main() -> None:
    cards = generate_concept_cards()
    kas = generate_knowledge_areas()
    labs = generate_labs()
    patterns = generate_patterns()
    arch = generate_architectures()
    update_concept_library_links()
    update_index_pages(cards, labs, patterns, arch)
    print(f"Generated {cards} concept cards, {kas} knowledge areas, {labs} labs, {patterns} patterns, {arch} architectures.")


if __name__ == "__main__":
    main()
