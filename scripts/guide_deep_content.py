"""Step-by-step substantive build guide content for generate_maturity_content.py."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GuidePhase:
    name: str
    goal: str
    steps: list[str]
    acceptance: list[str]
    commands: list[str] | None = None


@dataclass(frozen=True)
class GuideDetail:
    overview: str
    architecture_notes: str
    phases: list[GuidePhase]
    troubleshooting: list[str]
    related_patterns: list[str]
    related_labs: list[str]


GUIDE_DETAILS: dict[str, GuideDetail] = {
    "enterprise-rag-end-to-end": GuideDetail(
        overview=(
            "Build a production-shaped RAG pipeline from document ingestion through "
            "grounded answers with verifiable citations. You will wire hybrid retrieval, "
            "reranking, and stage-specific evals so every release is backed by measurable evidence."
        ),
        architecture_notes=(
            "Separate ingestion, retrieval, generation, and validation into distinct services "
            "with typed contracts. The ingestion worker writes normalized chunks and metadata to "
            "object storage and registers them in a manifest table. The query path runs "
            "authorization filters first, then hybrid retrieval, reranking, context assembly, "
            "and finally generation behind a gateway that logs traces and enforces token budgets."
        ),
        phases=[
            GuidePhase(
                name="Ingestion manifest",
                goal="Produce a reproducible, auditable corpus with chunk lineage.",
                steps=[
                    "Define a source manifest schema: source_id, uri, checksum, acl_tags, ingested_at.",
                    "Implement a chunker that emits parent/child chunks with stable chunk_id hashes.",
                    "Write ingestion jobs that idempotently upsert manifest rows and chunk artifacts.",
                    "Add a dry-run mode that validates ACL tags and rejects documents missing required metadata.",
                ],
                acceptance=[
                    "Re-running ingestion on unchanged sources produces zero duplicate chunks.",
                    "Every chunk traceable to source_id, page/section, and ingestion job version.",
                    "Manifest query returns only documents authorized for a test principal.",
                ],
                commands=[
                    "python -m scripts.ingest --manifest data/sources.yaml --dry-run",
                    "python -c \"from ingest.manifest import load; print(len(load('data/sources.yaml')))\"",
                    "pytest tests/test_ingestion_manifest.py -q",
                ],
            ),
            GuidePhase(
                name="Hybrid retrieval",
                goal="Combine lexical and dense recall with metadata filters.",
                steps=[
                    "Build a BM25 index over chunk text with stored metadata fields.",
                    "Embed chunks with a local sentence-transformer and load vectors into an ANN index.",
                    "Implement metadata-filter-first query routing (tenant, acl_tags, doc_type).",
                    "Fuse BM25 and dense hits with reciprocal rank fusion (RRF).",
                ],
                acceptance=[
                    "Recall@20 on a held-out query set exceeds BM25-only baseline.",
                    "Queries with acl_tags never return chunks from unauthorized sources.",
                    "P95 retrieval latency under 200 ms on the local benchmark corpus.",
                ],
                commands=[
                    "python retrieval/build_bm25.py --corpus data/chunks.jsonl --out indexes/bm25",
                    "python retrieval/build_vectors.py --corpus data/chunks.jsonl --out indexes/faiss",
                    "python retrieval/search.py --query \"refund policy\" --k 20 --hybrid",
                ],
            ),
            GuidePhase(
                name="Reranker",
                goal="Improve precision of top-k context with a cross-encoder or lightweight reranker.",
                steps=[
                    "Collect 50–100 query–passage relevance labels from your eval set.",
                    "Wire a cross-encoder reranker that scores fused candidates.",
                    "Truncate to top-N passages after rerank while respecting token budget headroom.",
                    "Log rerank scores and rank deltas for offline analysis.",
                ],
                acceptance=[
                    "MRR@5 improves over RRF-only fusion on the labeled set.",
                    "Top-8 passages fit within 70% of the context token budget.",
                    "Reranker failures fall back to RRF ordering without empty context.",
                ],
                commands=[
                    "python retrieval/rerank.py --query \"SLA breach\" --candidates tmp/hits.json",
                    "python eval/rerank_ablation.py --baseline rrf --candidate cross-encoder",
                ],
            ),
            GuidePhase(
                name="Grounded generation",
                goal="Generate answers constrained to retrieved evidence.",
                steps=[
                    "Assemble a context block with numbered passage citations [1]..[N].",
                    "Use a system prompt that forbids claims without citation markers.",
                    "Route generation through a gateway that records prompt hash and model version.",
                    "Return structured output: answer text, cited chunk_ids, abstention flag.",
                ],
                acceptance=[
                    "Every factual sentence in the answer maps to at least one citation marker.",
                    "Abstention triggers when retrieval confidence score is below threshold.",
                    "Generation trace includes prompt version, model id, and token counts.",
                ],
                commands=[
                    "python rag/generate.py --query \"data retention\" --context ctx.json --out answer.json",
                    "python -m pytest tests/test_grounded_generation.py -k citation_required -q",
                ],
            ),
            GuidePhase(
                name="Citation validator",
                goal="Verify that cited passages support the claims in the answer.",
                steps=[
                    "Parse citation markers and resolve them to chunk text.",
                    "Run an entailment or overlap check between each claim span and its cited passage.",
                    "Flag unsupported claims and optionally trigger a repair pass with stricter prompt.",
                    "Emit a validation report attached to the response metadata.",
                ],
                acceptance=[
                    "Validator catches deliberately hallucinated citations in adversarial test cases.",
                    "Supported-claim ratio reported per request in structured metadata.",
                    "Failed validation downgrades to abstention rather than ungrounded output.",
                ],
                commands=[
                    "python rag/validate_citations.py --answer answer.json --chunks data/chunks.jsonl",
                    "python eval/citation_suite.py --cases tests/adversarial_citations.jsonl",
                ],
            ),
            GuidePhase(
                name="Release gate",
                goal="Block deploys that regress retrieval, grounding, or latency SLOs.",
                steps=[
                    "Define gold cases with expected citations and slice tags (domain, difficulty).",
                    "Run stage evals: retrieval recall, citation precision, end-to-end answer quality.",
                    "Set threshold gates per slice; fail CI if any critical slice regresses.",
                    "Archive eval artifacts (metrics JSON, sample traces) with the release tag.",
                ],
                acceptance=[
                    "CI fails when citation precision drops more than 2 points on any slice.",
                    "Release artifact bundle includes eval report and rollback instructions.",
                    "Canary config ready before merge to main.",
                ],
                commands=[
                    "python eval/run_stage_evals.py --suite gold --out reports/stage_eval.json",
                    "python eval/release_gate.py --report reports/stage_eval.json --thresholds config/thresholds.yaml",
                ],
            ),
        ],
        troubleshooting=[
            "Retrieval returns irrelevant passages: inspect chunk size, metadata filters, and embedding model mismatch between index and query time.",
            "Answers cite wrong chunks: verify citation numbering in context assembly and that chunk_ids survive reranking.",
            "High latency: profile ANN index size, reranker batch size, and generation token limits separately.",
            "Eval flakiness: pin model and index versions; ensure gold cases use frozen corpus snapshots.",
        ],
        related_patterns=[
            "hybrid-retrieval",
            "retrieve-then-rerank",
            "citation-validator",
            "citation-grounded-answer",
            "eval-gated-release",
        ],
        related_labs=[
            "0602-document-ingestion",
            "0603-retrieval",
            "0604-ranking-and-context-selection",
            "0605-rag-generation-and-citations",
        ],
    ),
    "bounded-agent-assistant": GuideDetail(
        overview=(
            "Implement a multi-step assistant that plans, calls typed tools, and pauses for "
            "human approval on sensitive actions. Checkpoints make runs resumable and eval "
            "traces make behavior auditable."
        ),
        architecture_notes=(
            "The agent runtime is a finite state machine: plan, act, observe, approve, complete. "
            "Tools expose JSON Schema contracts and run in a sandbox with explicit timeouts. "
            "Checkpoints persist state to durable storage after each tool call. A separate "
            "approval service gates destructive or high-cost actions before execution resumes."
        ),
        phases=[
            GuidePhase(
                name="State machine",
                goal="Define explicit agent states and transitions with no hidden loops.",
                steps=[
                    "Model states: idle, planning, awaiting_tool, awaiting_approval, completed, failed.",
                    "Implement transition guards: max steps, max tool calls, budget exhaustion.",
                    "Emit structured events on every transition for trace reconstruction.",
                    "Add a cancel path that cleanly terminates in-flight tool calls.",
                ],
                acceptance=[
                    "Every run ends in a terminal state within the configured step budget.",
                    "Transition log replay reconstructs the full run without re-invoking tools.",
                    "Cancel from any non-terminal state within 2 seconds.",
                ],
                commands=[
                    "python agent/fsm.py --demo --max-steps 10",
                    "python -m pytest tests/test_agent_fsm.py -q",
                ],
            ),
            GuidePhase(
                name="Tool schemas",
                goal="Register tools with typed inputs, outputs, and capability tags.",
                steps=[
                    "Define JSON Schema for each tool's arguments and return type.",
                    "Tag tools with capability labels: read, write, external, destructive.",
                    "Implement a tool registry that validates args before dispatch.",
                    "Add mock implementations for local development without external APIs.",
                ],
                acceptance=[
                    "Invalid tool args rejected before dispatch with schema error details.",
                    "Registry lists capability tags consumable by the approval policy.",
                    "Mock tools return deterministic fixtures for eval replay.",
                ],
                commands=[
                    "python tools/validate_schema.py --tool search_docs --args '{\"query\": \"test\"}'",
                    "python agent/run.py --tools mock --goal \"summarize open tickets\"",
                ],
            ),
            GuidePhase(
                name="Human approval",
                goal="Pause destructive or ambiguous actions until a human approves.",
                steps=[
                    "Define approval rules keyed on capability tags and estimated cost.",
                    "Serialize pending action payload for reviewer UI or CLI prompt.",
                    "Implement approve/reject/edit paths that resume or replan the run.",
                    "Log approver identity, timestamp, and decision rationale.",
                ],
                acceptance=[
                    "Write-capable tools never execute without an approval record.",
                    "Rejected actions trigger replan without corrupting checkpoint state.",
                    "Approval timeout defaults to safe abort, not auto-approve.",
                ],
                commands=[
                    "python agent/run.py --require-approval --goal \"delete temp files\"",
                    "python approval/cli.py --pending runs/latest/pending.json",
                ],
            ),
            GuidePhase(
                name="Checkpoint store",
                goal="Persist resumable state after each tool observation.",
                steps=[
                    "Design checkpoint schema: run_id, step, messages, tool_results, pending_action.",
                    "Write checkpoints to SQLite or local JSON with atomic rename.",
                    "Implement resume-from-checkpoint that skips completed tool calls.",
                    "Add retention policy and purge for completed runs older than N days.",
                ],
                acceptance=[
                    "Killing the process mid-run and resuming produces identical final output.",
                    "Checkpoint size bounded; large tool outputs stored by reference.",
                    "No duplicate tool side effects on resume.",
                ],
                commands=[
                    "python agent/run.py --checkpoint-dir tmp/checkpoints --goal \"file inventory\"",
                    "python agent/resume.py --run-id abc123",
                ],
            ),
            GuidePhase(
                name="Eval traces",
                goal="Score agent runs on task success, tool discipline, and safety.",
                steps=[
                    "Record full traces: states, tool calls, approvals, final outcome.",
                    "Build eval cases with expected tool sequences and forbidden actions.",
                    "Score success rate, unnecessary tool calls, and approval bypass attempts.",
                    "Integrate trace eval into CI with regression thresholds.",
                ],
                acceptance=[
                    "Eval suite covers happy path, approval-required, and budget-exceeded cases.",
                    "Trace diff highlights tool sequence changes between agent versions.",
                    "CI fails on approval-bypass or destructive-action-without-approval.",
                ],
                commands=[
                    "python eval/agent_traces.py --cases tests/agent_cases.jsonl --out reports/traces.json",
                    "python eval/score_traces.py --report reports/traces.json --min-success 0.85",
                ],
            ),
        ],
        troubleshooting=[
            "Agent loops on the same tool: tighten transition guards and add duplicate-call detection in the FSM.",
            "Checkpoint resume duplicates side effects: store tool call ids and skip already-completed calls.",
            "Approval stalls block UX: set timeouts, surface pending actions in a queue, and allow delegated approvers.",
            "Eval traces too large: store tool outputs by reference and truncate observation payloads in logs.",
        ],
        related_patterns=[
            "planner-executor",
            "human-approval-gate",
            "durable-checkpoint",
            "tool-sandbox",
            "observability-traces",
        ],
        related_labs=[
            "0802-the-agent-loop",
            "0803-agent-memory-and-recovery",
            "0804-agent-patterns",
            "0704-tools-as-capability-boundaries",
        ],
    ),
    "context-engine-with-tests": GuideDetail(
        overview=(
            "Build a versioned context assembly layer that packs prompts, memory, and "
            "retrieved sections under explicit token budgets. Regression tests lock behavior "
            "so prompt or policy changes do not silently shift outputs."
        ),
        architecture_notes=(
            "The context engine sits between upstream data sources and the model gateway. "
            "It loads prompt templates by version, applies section-specific budgets, and "
            "emits a deterministic context bundle. Memory policy decides what persists "
            "across turns. A fixture-based eval dataset compares assembled contexts and "
            "downstream outputs before merge."
        ),
        phases=[
            GuidePhase(
                name="Context builder",
                goal="Assemble multi-section prompts from templates and dynamic inputs.",
                steps=[
                    "Define section types: system, instructions, memory, retrieval, user.",
                    "Implement a builder that merges sections in fixed priority order.",
                    "Support variable substitution with explicit missing-key errors.",
                    "Serialize output as messages[] plus metadata (versions, token estimate).",
                ],
                acceptance=[
                    "Same inputs and versions produce byte-identical context bundles.",
                    "Missing required variables fail fast with section name in error.",
                    "Builder unit tests cover all section types and edge cases.",
                ],
                commands=[
                    "python context/build.py --template prompts/v1.yaml --vars vars.json --out ctx.json",
                    "python -m pytest tests/test_context_builder.py -q",
                ],
            ),
            GuidePhase(
                name="Section budgets",
                goal="Enforce per-section and total token limits with graceful truncation.",
                steps=[
                    "Assign max tokens per section based on task priority.",
                    "Implement truncation strategies: tail-keep for memory, head-keep for retrieval.",
                    "Reserve headroom for model completion tokens in total budget math.",
                    "Log which sections were truncated and by how many tokens.",
                ],
                acceptance=[
                    "Assembled context never exceeds configured total token budget.",
                    "Truncation order respects priority: system > instructions > retrieval > memory.",
                    "Truncation metadata present in output for debugging.",
                ],
                commands=[
                    "python context/build.py --budget 4096 --vars vars.json | python context/token_report.py",
                    "python eval/budget_cases.py --suite tests/budget_overflow.jsonl",
                ],
            ),
            GuidePhase(
                name="Prompt versions",
                goal="Pin and migrate prompt templates without breaking callers.",
                steps=[
                    "Store templates in versioned files: prompts/{name}/v{semver}.yaml.",
                    "Expose a version resolver: explicit pin, latest stable, or canary tag.",
                    "Document changelog entries when template semantics change.",
                    "Add compatibility tests that old pinned versions still parse.",
                ],
                acceptance=[
                    "Callers can pin prompt_version and get stable behavior across deploys.",
                    "Canary tag routes a configurable fraction of traffic to draft templates.",
                    "Breaking template changes require a major version bump in changelog.",
                ],
                commands=[
                    "python prompts/list_versions.py --name support_assistant",
                    "python context/build.py --template support_assistant --version 2.1.0",
                ],
            ),
            GuidePhase(
                name="Eval dataset",
                goal="Regression-test context assembly and downstream behavior.",
                steps=[
                    "Curate cases: input vars, expected section presence, forbidden content.",
                    "Snapshot assembled contexts; diff on CI when builder logic changes.",
                    "Add optional model-in-the-loop checks with a local mock LLM.",
                    "Tag cases by slice: language, domain, long-context, adversarial injection.",
                ],
                acceptance=[
                    "CI fails when context snapshot diff exceeds approved baseline.",
                    "At least 20 cases covering truncation, missing vars, and injection attempts.",
                    "Slice report shows no regression on critical tags.",
                ],
                commands=[
                    "python eval/context_regression.py --update-snapshots",
                    "python eval/context_regression.py --check",
                    "python -m pytest tests/test_context_eval.py -q",
                ],
            ),
        ],
        troubleshooting=[
            "Token counts drift from provider: reconcile with the same tokenizer the gateway uses and add a calibration offset.",
            "Snapshots churn on ordering: sort retrieval sections by score and stabilize tie-breaking.",
            "Memory bloat evicts retrieval: lower memory budget or summarize older turns before assembly.",
            "Injection in user content reaches system section: sanitize or delimit untrusted sections explicitly.",
        ],
        related_patterns=[
            "context-budget-packing",
            "prompt-versioning",
            "context-compressor",
            "offline-eval-regression",
        ],
        related_labs=[
            "0503-context-construction",
            "0504-conversation-and-memory",
            "0506-prompt-and-context-operations",
            "0505-context-failure-and-security",
        ],
    ),
    "model-selection-harness": GuideDetail(
        overview=(
            "Build a vendor-neutral benchmark harness that scores candidate models on your "
            "real tasks, logging quality, latency, and cost. The output is a selection ADR "
            "grounded in measured trade-offs, not vendor marketing."
        ),
        architecture_notes=(
            "The harness loads a fixed task dataset and routes each case to candidate model "
            "adapters behind a common interface. A run logger captures tokens, latency, and "
            "scores. Adapters wrap local mocks, open-weight endpoints, or API stubs so CI "
            "does not require live keys. Results feed a comparison report and ADR template."
        ),
        phases=[
            GuidePhase(
                name="Task dataset",
                goal="Define representative tasks with gold references and scoring rubrics.",
                steps=[
                    "Collect 30–100 cases spanning normal, boundary, and failure-prone inputs.",
                    "Attach expected outputs or rubric criteria per case.",
                    "Tag cases by slice: latency-sensitive, reasoning-heavy, structured output.",
                    "Freeze dataset version with checksum for reproducible runs.",
                ],
                acceptance=[
                    "Dataset manifest includes version, checksum, and slice tag definitions.",
                    "Each case has an automated scorer or LLM-judge prompt with calibration set.",
                    "No duplicate or near-duplicate cases without explicit justification.",
                ],
                commands=[
                    "python harness/validate_dataset.py --path data/model_tasks.jsonl",
                    "python -c \"import json; print(len(list(open('data/model_tasks.jsonl'))))\"",
                ],
            ),
            GuidePhase(
                name="Candidate models",
                goal="Register models through a uniform adapter interface.",
                steps=[
                    "Define adapter contract: complete(prompt, params) -> text, usage, latency_ms.",
                    "Implement adapters for local mock, small open-weight, and one API stub.",
                    "Configure per-model defaults: max_tokens, temperature, timeout.",
                    "Support batch mode for offline eval and single-case debug mode.",
                ],
                acceptance=[
                    "All candidates pass a smoke test on three fixed prompts.",
                    "Adapter errors classified: timeout, rate_limit, invalid_output.",
                    "Mock adapter returns deterministic outputs for CI.",
                ],
                commands=[
                    "python harness/adapters/mock.py --smoke",
                    "python harness/run.py --model mock-small --cases data/model_tasks.jsonl --limit 5",
                ],
            ),
            GuidePhase(
                name="Cost/latency log",
                goal="Record operational metrics alongside quality scores.",
                steps=[
                    "Log per-case: input_tokens, output_tokens, latency_ms, estimated_cost_usd.",
                    "Aggregate p50/p95 latency and cost per model and slice.",
                    "Flag cases where quality gains do not justify latency or cost increase.",
                    "Export run logs as JSONL for downstream dashboards.",
                ],
                acceptance=[
                    "Every completed case has non-null latency and token counts.",
                    "Summary report includes quality, p95 latency, and cost per 1k cases.",
                    "Run reproducible with pinned dataset and adapter versions.",
                ],
                commands=[
                    "python harness/run.py --models mock-small,mock-large --out logs/run.jsonl",
                    "python harness/summarize.py --log logs/run.jsonl --out reports/compare.md",
                ],
            ),
            GuidePhase(
                name="Selection ADR",
                goal="Document the chosen model with evidence and rejected alternatives.",
                steps=[
                    "Generate comparison table from run summaries.",
                    "Write ADR: context, decision, consequences, rejected options with metrics.",
                    "Define fallback model and routing rules for slice-specific overrides.",
                    "Link ADR to dataset version and harness commit hash.",
                ],
                acceptance=[
                    "ADR cites numeric evidence for the primary model choice.",
                    "At least one alternative rejected with measured reason.",
                    "Fallback and override rules documented for ops handoff.",
                ],
                commands=[
                    "python harness/adr_from_report.py --report reports/compare.md --out docs/adr/model-choice.md",
                ],
            ),
        ],
        troubleshooting=[
            "Scores incomparable across models: normalize prompts and decoding params; use same tokenizer for length limits.",
            "Mock results mislead selection: reserve a held-out live eval for final sign-off even if CI uses mocks.",
            "High variance on small sets: increase case count or run multiple seeds and report confidence intervals.",
            "Latency dominated by cold start: warm up adapters before timed runs and report separately.",
        ],
        related_patterns=[
            "model-routing",
            "fallback-cascade",
            "llm-judge-calibration",
            "adapter-swapping",
        ],
        related_labs=[
            "0405-inference-and-sampling",
            "0406-model-families-and-selection",
            "1101-choosing-adaptation",
            "1002-metrics-and-human-judgment",
        ],
    ),
    "eval-gated-release": GuideDetail(
        overview=(
            "Wire evaluation into CI so no model, prompt, or retrieval change ships without "
            "passing slice-aware thresholds. Canary plans and rollback evidence make releases "
            " reversible when live metrics diverge."
        ),
        architecture_notes=(
            "The release pipeline runs gold-case evals, computes slice metrics, and compares "
            "against baselines stored per environment. A gate service returns pass/fail with "
            "reason codes. Approved releases attach evidence bundles. Canary configuration "
            "routes a small traffic fraction to the candidate while comparing live slice metrics."
        ),
        phases=[
            GuidePhase(
                name="Gold cases",
                goal="Maintain authoritative eval cases tied to product requirements.",
                steps=[
                    "Map each requirement to at least one gold case with expected behavior.",
                    "Version gold cases; require review for additions or semantic edits.",
                    "Include adversarial and regression cases for past production incidents.",
                    "Store cases as JSONL with slice tags and severity levels.",
                ],
                acceptance=[
                    "Gold suite covers all P0 requirements documented in the spec.",
                    "Case edits require PR review and version bump in manifest.",
                    "Adversarial subset runs on every CI build.",
                ],
                commands=[
                    "python eval/validate_gold.py --path data/gold_cases.jsonl",
                    "python eval/run_gold.py --cases data/gold_cases.jsonl --out reports/gold.json",
                ],
            ),
            GuidePhase(
                name="Slice metrics",
                goal="Measure quality per segment, not only aggregate averages.",
                steps=[
                    "Define slices: domain, language, user tier, query length, data vintage.",
                    "Compute metrics per slice: accuracy, citation precision, abstention rate.",
                    "Compare candidate vs baseline with minimum sample size guards.",
                    "Highlight slices with >2pt regression in the CI summary.",
                ],
                acceptance=[
                    "Report includes per-slice metrics with sample counts.",
                    "Slices with n<5 flagged as low-confidence, not silently ignored.",
                    "Regression detection configurable per slice severity.",
                ],
                commands=[
                    "python eval/slice_metrics.py --report reports/gold.json --slices config/slices.yaml",
                    "python eval/diff_baselines.py --candidate reports/gold.json --baseline reports/baseline.json",
                ],
            ),
            GuidePhase(
                name="Release gate",
                goal="Automate pass/fail decisions with auditable reason codes.",
                steps=[
                    "Define thresholds per metric and slice in YAML.",
                    "Implement gate logic: fail on any P0 slice regression or global critical miss.",
                    "Emit structured pass/fail with reason codes for CI and dashboards.",
                    "Block merge/deploy when gate fails unless explicit override with ticket.",
                ],
                acceptance=[
                    "Gate fails closed when eval artifacts missing or malformed.",
                    "Override path requires documented ticket id and expires after one deploy.",
                    "Pass/fail JSON archived with git sha and artifact urls.",
                ],
                commands=[
                    "python eval/release_gate.py --report reports/gold.json --thresholds config/thresholds.yaml",
                    "python eval/release_gate.py --report reports/gold.json --thresholds config/thresholds.yaml --strict",
                ],
            ),
            GuidePhase(
                name="Canary plan",
                goal="Roll out gradually with live metric comparison and rollback triggers.",
                steps=[
                    "Document canary stages: 1%, 5%, 25%, 100% with soak durations.",
                    "Define live metrics to watch: error rate, latency p95, quality proxy.",
                    "Set automatic rollback triggers tied to slice-specific live dashboards.",
                    "Write rollback runbook: flag flip, cache invalidation, stakeholder notify.",
                ],
                acceptance=[
                    "Canary plan linked from release PR and evidence bundle.",
                    "Rollback executable in under 5 minutes without redeploy.",
                    "Live dashboard compares canary vs control on matching slices.",
                ],
                commands=[
                    "python deploy/canary_plan.py --version v1.2.3 --out deploy/canary.yaml",
                    "python deploy/rollback.py --feature new-reranker --dry-run",
                ],
            ),
        ],
        troubleshooting=[
            "Gate passes but production fails: live metrics differ from offline gold; add production-shadow eval.",
            "Slice sample too small: merge low-traffic slices or lengthen collection window before gating.",
            "Flaky LLM-judge scores: calibrate judges on a human-labeled subset and use median-of-three.",
            "Override culture erodes gate: audit overrides monthly and tie to incident postmortems.",
        ],
        related_patterns=[
            "eval-gated-release",
            "slice-based-eval",
            "online-canary",
            "offline-eval-regression",
        ],
        related_labs=[
            "1001-evaluation-as-requirements",
            "1003-evaluation-by-system-stage",
            "1002-metrics-and-human-judgment",
            "1006-governance-and-assurance",
        ],
    ),
    "hybrid-search-engine": GuideDetail(
        overview=(
            "Implement lexical plus dense search with score fusion and offline recall "
            "measurement. The result is a search service you can tune with evidence instead "
            "of intuition."
        ),
        architecture_notes=(
            "Indexing and query paths are separate binaries sharing a chunk schema. BM25 and "
            "vector indexes update from the same corpus snapshot. The query API accepts "
            "filters, runs both retrievers, fuses with RRF, and returns ranked hits with "
            "scores and source metadata. Offline eval computes recall@k on labeled queries."
        ),
        phases=[
            GuidePhase(
                name="BM25 index",
                goal="Build a lexical index with metadata filters.",
                steps=[
                    "Tokenize and index chunk text with Pyserini or a lightweight BM25 implementation.",
                    "Store doc_id, chunk_id, and filter fields alongside postings.",
                    "Support incremental rebuild from corpus JSONL snapshots.",
                    "Expose search CLI with query, k, and filter flags.",
                ],
                acceptance=[
                    "BM25 search returns deterministic ranks for fixed corpus and query.",
                    "Metadata filters reduce candidate set before scoring.",
                    "Index build completes on sample corpus in under 60 seconds.",
                ],
                commands=[
                    "python search/build_bm25.py --corpus data/chunks.jsonl --out indexes/bm25",
                    "python search/query_bm25.py --index indexes/bm25 --query \"hybrid fusion\" -k 10",
                ],
            ),
            GuidePhase(
                name="Vector index",
                goal="Embed chunks and serve approximate nearest neighbor search.",
                steps=[
                    "Embed chunks with a local sentence-transformer model.",
                    "Build FAISS or hnswlib index with normalized vectors.",
                    "Persist embedding model version alongside index artifacts.",
                    "Implement batch embedding for rebuild throughput.",
                ],
                acceptance=[
                    "Vector search returns top-k with cosine similarity scores.",
                    "Query embedding uses same model version as index metadata.",
                    "ANN index recall within 2% of brute-force on validation sample.",
                ],
                commands=[
                    "python search/build_vectors.py --corpus data/chunks.jsonl --out indexes/faiss",
                    "python search/query_vectors.py --index indexes/faiss --query \"hybrid fusion\" -k 10",
                ],
            ),
            GuidePhase(
                name="RRF fusion",
                goal="Merge ranked lists without calibrating incompatible scores.",
                steps=[
                    "Retrieve top-k from BM25 and vector indexes independently.",
                    "Apply reciprocal rank fusion with configurable k constant (default 60).",
                    "Deduplicate by chunk_id, keeping best fused rank.",
                    "Return fused list with component ranks for debugging.",
                ],
                acceptance=[
                    "Fusion improves recall@10 vs either single retriever on labeled set.",
                    "Duplicate chunks appear once in fused output.",
                    "Fusion weights tunable via config without code change.",
                ],
                commands=[
                    "python search/hybrid_query.py --query \"token budget\" -k 10",
                    "python eval/fusion_grid.py --queries data/labeled_queries.jsonl",
                ],
            ),
            GuidePhase(
                name="recall@k eval",
                goal="Measure retrieval quality offline before shipping ranking changes.",
                steps=[
                    "Prepare labeled qrels: query_id, relevant chunk_ids.",
                    "Run batch retrieval for k in {1, 5, 10, 20}.",
                    "Compute recall@k and MRR; breakdown by query category.",
                    "Store eval results with index version and fusion config hash.",
                ],
                acceptance=[
                    "Eval script outputs recall@5 and recall@10 with confidence over query count.",
                    "Regression vs baseline flagged when recall@10 drops >1 point.",
                    "Results reproducible from pinned corpus and index artifacts.",
                ],
                commands=[
                    "python eval/recall_at_k.py --queries data/labeled_queries.jsonl --k 5,10,20",
                    "python eval/recall_at_k.py --index-version sha256:abc123 --out reports/recall.json",
                ],
            ),
        ],
        troubleshooting=[
            "Dense recall weak on rare tokens: increase k before fusion or add synonym expansion on BM25 path.",
            "RRF hurts precision: reduce k or apply reranker after fusion on top-20 only.",
            "Filter excludes all hits: validate filter schema at index time vs query time.",
            "Slow rebuilds: embed in batches and parallelize BM25 and vector builds from same snapshot.",
        ],
        related_patterns=[
            "hybrid-retrieval",
            "retrieval-fusion",
            "metadata-filter-first",
            "retrieve-then-rerank",
        ],
        related_labs=[
            "0603-retrieval",
            "0305-similarity-and-vector-search",
            "0306-embedding-systems-in-production",
            "0604-ranking-and-context-selection",
        ],
    ),
    "structured-extraction-api": GuideDetail(
        overview=(
            "Expose schema-validated structured extraction behind a REST boundary with a "
            "repair loop for malformed model output. Adversarial tests prove the API rejects "
            "injection and schema drift before production traffic arrives."
        ),
        architecture_notes=(
            "The API accepts documents or text plus a JSON Schema id. An extractor prompt "
            "requests structured output; a validator enforces the schema; a repair loop "
            "re-prompts on failure with error context. Responses include validation status, "
            "parsed object, and repair attempt count. Adversarial tests run in CI."
        ),
        phases=[
            GuidePhase(
                name="JSON Schema",
                goal="Define strict extraction targets with documented fields.",
                steps=[
                    "Author schemas per extraction task with required fields and enums.",
                    "Register schemas in a catalog with version ids.",
                    "Add examples and counterexamples in schema descriptions for prompt grounding.",
                    "Validate schemas themselves with ajv or jsonschema CLI.",
                ],
                acceptance=[
                    "Every production schema has version semver and changelog entry.",
                    "Schemas reject additionalProperties unless explicitly allowed.",
                    "Example instances validate successfully against their schema.",
                ],
                commands=[
                    "python schemas/validate.py --schema schemas/invoice/v1.json",
                    "python schemas/catalog.py --list",
                ],
            ),
            GuidePhase(
                name="Validator",
                goal="Parse and validate model output before returning to clients.",
                steps=[
                    "Extract JSON from model response (strip markdown fences if present).",
                    "Run jsonschema validation; collect structured error paths.",
                    "Map validation failures to 422 responses with field-level detail.",
                    "Log raw model output only in secure debug mode.",
                ],
                acceptance=[
                    "Valid outputs pass; missing required fields fail with explicit paths.",
                    "Validator handles unicode, nested objects, and array constraints.",
                    "No unvalidated JSON returned on success path.",
                ],
                commands=[
                    "python extract/validate.py --schema invoice/v1 --input samples/raw_llm.txt",
                    "python -m pytest tests/test_validator.py -q",
                ],
            ),
            GuidePhase(
                name="Repair loop",
                goal="Recover from minor formatting errors without user intervention.",
                steps=[
                    "On validation failure, re-prompt with schema errors and prior output.",
                    "Cap repair attempts at 2; fail closed after exhaustion.",
                    "Track repair count in response metadata for quality monitoring.",
                    "Short-circuit if errors are non-recoverable (wrong types on root fields).",
                ],
                acceptance=[
                    "Recoverable cases (truncated JSON, extra prose) succeed within 2 repairs.",
                    "Repair loop never infinite-loops; attempts bounded and logged.",
                    "Success rate on noisy sample set improves vs single-pass baseline.",
                ],
                commands=[
                    "python extract/run.py --text samples/invoice.txt --schema invoice/v1 --repair",
                    "python eval/repair_ablation.py --cases data/extraction_failures.jsonl",
                ],
            ),
            GuidePhase(
                name="Adversarial tests",
                goal="Verify resistance to injection and schema escape attempts.",
                steps=[
                    "Build cases: instruction injection in source text, schema override attempts.",
                    "Assert API returns validation failure or sanitized output, never silent drift.",
                    "Test oversized inputs and nested depth limits.",
                    "Run adversarial suite in CI on every PR.",
                ],
                acceptance=[
                    "Injection cases do not produce fields outside schema.",
                    "Oversized input rejected with 413 or truncated per policy.",
                    "CI fails on any adversarial case regression.",
                ],
                commands=[
                    "python -m pytest tests/test_extraction_adversarial.py -q",
                    "python eval/adversarial_extract.py --suite data/adversarial_extract.jsonl",
                ],
            ),
        ],
        troubleshooting=[
            "Repair loop oscillates: include diff of prior errors and forbid repeating same malformed keys.",
            "Schema too strict for real documents: relax optional fields and use post-validation normalization.",
            "JSON buried in markdown: strengthen extraction regex and add a json-repair pre-pass.",
            "Latency spikes on repairs: cache schema compilation and parallelize only first pass in sync API.",
        ],
        related_patterns=[
            "structured-output-validation",
            "evaluator-optimizer",
            "adversarial-eval-suite",
            "prompt-injection-guard",
        ],
        related_labs=[
            "0502-structured-generation",
            "0501-instructions-that-work",
            "1004-security-of-ai-systems",
            "1301-vision-and-document-intelligence",
        ],
    ),
    "multi-tenant-retrieval": GuideDetail(
        overview=(
            "Build retrieval infrastructure where every query is scoped to tenant identity, "
            "authorization filters, and auditable access. Isolation tests prove one tenant "
            "cannot retrieve another's documents."
        ),
        architecture_notes=(
            "Tenant metadata lives in a registry mapping tenant_id to index partitions, "
            "ACL policies, and quotas. The query API authenticates callers, resolves tenant "
            "context, and applies AuthZ filters before retrieval executes. Audit logs record "
            "query text hash, tenant, result ids, and principal. Isolation tests run "
            "cross-tenant negative cases in CI."
        ),
        phases=[
            GuidePhase(
                name="Tenant metadata",
                goal="Model tenants, index partitions, and policy attachments.",
                steps=[
                    "Define tenant record: tenant_id, plan, index_prefix, default_acl.",
                    "Register document sources with tenant_id and resource-level acl_tags.",
                    "Enforce quota fields: max documents, queries per minute.",
                    "Expose admin CLI to create tenants and attach policies.",
                ],
                acceptance=[
                    "Every indexed chunk carries tenant_id and acl_tags in metadata.",
                    "Unknown tenant_id rejected at API boundary with 404.",
                    "Tenant registry changes audited with actor and timestamp.",
                ],
                commands=[
                    "python tenants/register.py --tenant acme --plan standard",
                    "python tenants/show.py --tenant acme",
                ],
            ),
            GuidePhase(
                name="AuthZ filters",
                goal="Apply authorization before search executes.",
                steps=[
                    "Resolve principal roles and permitted acl_tags from token claims.",
                    "Inject mandatory filters into BM25 and vector queries.",
                    "Deny queries that specify tenant_id mismatched with token.",
                    "Return empty results rather than partial leaks on filter parse errors.",
                ],
                acceptance=[
                    "Queries never return chunks whose acl_tags are not permitted for principal.",
                    "Cross-tenant filter injection attempts fail closed.",
                    "Filter application logged per request for audit.",
                ],
                commands=[
                    "python search/query.py --tenant acme --token tests/fixtures/user.jwt --query \"policy\"",
                    "python -m pytest tests/test_authz_filters.py -q",
                ],
            ),
            GuidePhase(
                name="Isolation tests",
                goal="Prove tenant boundaries with automated negative tests.",
                steps=[
                    "Seed two tenants with overlapping topic but distinct documents.",
                    "Run queries as tenant A principal; assert zero results from tenant B.",
                    "Attempt filter bypass via crafted query parameters and document ids.",
                    "Include audit log assertion: no B chunk ids in A's access log.",
                ],
                acceptance=[
                    "100% pass on cross-tenant leakage test matrix.",
                    "Bypass attempts produce 403 or empty results, never mixed-tenant hits.",
                    "Isolation tests run on every index rebuild in CI.",
                ],
                commands=[
                    "python -m pytest tests/test_tenant_isolation.py -q",
                    "python eval/isolation_matrix.py --tenants acme,beta --out reports/isolation.json",
                ],
            ),
        ],
        troubleshooting=[
            "Leaked chunk via mis-tagged ingestion: validate tenant_id at ingest and reject mismatched source paths.",
            "Empty results for valid users: debug acl_tag intersection between principal and document tags.",
            "Audit logs too verbose: log chunk id hashes and query fingerprint, not full document text.",
            "Index sharing across tenants: prefer partition prefixes or separate collections over filter-only isolation.",
        ],
        related_patterns=[
            "multi-tenant-retrieval",
            "metadata-filter-first",
            "audit-evidence",
            "human-approval-gate",
        ],
        related_labs=[
            "1202-identity-data-and-trust-boundaries",
            "1201-enterprise-ai-building-blocks",
            "0606-advanced-and-enterprise-rag",
            "1006-governance-and-assurance",
        ],
    ),
    "coding-agent-workspace": GuideDetail(
        overview=(
            "Configure a repository for AI-assisted development with explicit agent "
            "instructions, reusable skills, CI guardrails, and a code review rubric. The "
            "goal is predictable agent behavior that passes the same quality gates as human contributors."
        ),
        architecture_notes=(
            "AGENTS.md defines repo conventions, test commands, and forbidden paths. Skills "
            "package repeatable workflows as markdown instructions with scoped tools. CI runs "
            "lint, tests, and optional agent-eval fixtures. The review rubric scores diffs "
            "for correctness, test coverage, scope discipline, and security."
        ),
        phases=[
            GuidePhase(
                name="AGENTS.md",
                goal="Document how agents should navigate and change the repo.",
                steps=[
                    "List build/test commands, directory ownership, and formatting rules.",
                    "Specify files agents must not edit (.env, secrets, generated locks).",
                    "Define branch naming, commit message format, and PR checklist.",
                    "Include examples of good vs over-scoped agent diffs.",
                    "Add spec-driven rules: read specs/ and openspec/changes/ before implementation.",
                ],
                acceptance=[
                    "New agent session can run tests using only AGENTS.md instructions.",
                    "Forbidden paths explicitly listed with rationale.",
                    "Document updated when repo layout or test entrypoints change.",
                    "AGENTS.md links to spec-driven workflow and OpenSpec/Cursor commands.",
                ],
                commands=[
                    "cat AGENTS.md",
                    "python -m pytest -q  # verify documented test command works",
                    "cp templates/spec-driven/cursor-spec-driven.mdc .cursor/rules/spec-driven.mdc",
                    "npm install -g @fission-ai/openspec@latest && openspec init",
                ],
            ),
            GuidePhase(
                name="OpenSpec + Cursor alignment",
                goal="Wire repo-level specs (OpenSpec) to editor agents (Cursor).",
                steps=[
                    "Initialize OpenSpec so openspec/specs/ holds current behavior by domain.",
                    "Copy templates/spec-driven/cursor-spec-driven.mdc into .cursor/rules/.",
                    "Practice /opsx:explore then /opsx:propose on one lab or feature change.",
                    "Require /opsx:apply only after proposal and delta specs are reviewed.",
                    "Archive completed changes so specs merge into openspec/specs/.",
                ],
                acceptance=[
                    "Active change folder contains proposal.md, tasks.md, and delta specs.",
                    "Cursor Plan mode can read the same acceptance YAML as OpenSpec requirements.",
                    "pytest (or documented test command) gates /opsx:archive.",
                ],
                commands=[
                    "openspec init && openspec update",
                    "# Assistant: /opsx:explore then /opsx:propose <change title>",
                    "cursor .",
                    "python -m pytest labs/0902-specification-driven-development/test_lab.py -q",
                    "# Assistant: /opsx:apply then /opsx:archive when green",
                ],
            ),
            GuidePhase(
                name="Skills",
                goal="Package repeatable agent workflows as reusable skill files.",
                steps=[
                    "Identify frequent tasks: add endpoint, fix CI, write migration.",
                    "Author SKILL.md per task with steps, constraints, and verification commands.",
                    "Keep skills focused; split when workflow exceeds one screen.",
                    "Reference skills from AGENTS.md with trigger phrases.",
                ],
                acceptance=[
                    "At least three skills cover test-fix, feature-add, and refactor paths.",
                    "Each skill ends with verification commands and expected outputs.",
                    "Skills do not duplicate conflicting instructions.",
                ],
                commands=[
                    "ls .cursor/skills/",
                    "head -40 .cursor/skills/add-api-endpoint/SKILL.md",
                ],
            ),
            GuidePhase(
                name="CI checks",
                goal="Enforce automated quality gates on agent-generated PRs.",
                steps=[
                    "Ensure CI runs lint, typecheck, and unit tests on every PR.",
                    "Add diff size or path allowlist checks for agent branches if needed.",
                    "Optional: run agent-eval fixtures that simulate common tasks.",
                    "Fail CI with actionable logs; link fix commands in AGENTS.md.",
                ],
                acceptance=[
                    "CI green required before merge; no skipped required checks.",
                    "Failed CI output references local repro command.",
                    "Agent-eval job completes in under 10 minutes on mock tasks.",
                ],
                commands=[
                    "python -m pytest -q",
                    "ruff check .",
                    "python scripts/agent_eval_smoke.py",
                ],
            ),
            GuidePhase(
                name="Review rubric",
                goal="Score agent diffs consistently for human or automated review.",
                steps=[
                    "Define rubric dimensions: correctness, tests, scope, security, docs.",
                    "Write scoring guide: what earns pass vs request-changes per dimension.",
                    "Apply rubric to sample agent PRs and calibrate among reviewers.",
                    "Publish rubric in docs/review/agent-rubric.md.",
                ],
                acceptance=[
                    "Rubric used on at least five sample PRs with inter-rater notes.",
                    "Security dimension catches secrets and missing input validation.",
                    "Scope dimension flags unrelated file changes.",
                ],
                commands=[
                    "python scripts/score_pr_rubric.py --diff patches/sample.patch",
                ],
            ),
        ],
        troubleshooting=[
            "Agent ignores AGENTS.md: shorten file, put test command at top, and reference skills inline.",
            "CI passes but production breaks: add integration tests and staging deploy step to rubric.",
            "Skills conflict with cursor rules: reconcile into one authoritative section per topic.",
            "Over-scoped diffs: add explicit 'minimal diff' rule and CI path filter for sensitive dirs.",
        ],
        related_patterns=[
            "spec-driven-ai-feature",
            "observability-traces",
            "adversarial-eval-suite",
            "human-review-queue",
        ],
        related_labs=[
            "0903-ai-native-development-workflow",
            "0902-specification-driven-development",
            "0904-testing-ai-systems",
            "0801-agent-or-workflow",
        ],
    ),
    "fine-tune-and-serve": GuideDetail(
        overview=(
            "Adapt a small open-weight model with LoRA, evaluate against a baseline, register "
            "the artifact, and serve it behind a versioned endpoint with rollback. Data "
            "cards and eval reports make the adaptation auditable."
        ),
        architecture_notes=(
            "Training reads a versioned dataset with a data card describing provenance and "
            "limitations. LoRA adapters train against a frozen base; checkpoints register "
            "in a local model registry. Eval compares adapter vs base on task-specific "
            "metrics. Serving loads base plus adapter with health checks and a rollback "
            "pointer to the prior version."
        ),
        phases=[
            GuidePhase(
                name="Data card",
                goal="Document dataset provenance, composition, and known biases.",
                steps=[
                    "Record sources, collection method, PII handling, and license.",
                    "Summarize label distribution and known gaps.",
                    "Version dataset with checksum; link to training config.",
                    "Add acceptance checklist: consent, deduplication, held-out test split.",
                ],
                acceptance=[
                    "Data card complete for all fields required by team template.",
                    "Dataset checksum matches manifest referenced in training config.",
                    "Held-out test split never used in training runs.",
                ],
                commands=[
                    "python data/build_card.py --dataset data/train.jsonl --out data/DATA_CARD.md",
                    "python data/verify_split.py --train data/train.jsonl --test data/test.jsonl",
                ],
            ),
            GuidePhase(
                name="LoRA train",
                goal="Train a low-rank adapter on the frozen base model.",
                steps=[
                    "Configure LoRA rank, target modules, learning rate, and epochs.",
                    "Train on local GPU or CPU with reduced batch for smoke runs.",
                    "Save adapter weights and training log with git sha and data version.",
                    "Run smoke inference on three prompts before eval.",
                ],
                acceptance=[
                    "Training reproducible from config file and pinned base model hash.",
                    "Adapter size small relative to base; loads independently.",
                    "Smoke inference produces coherent output on task-specific prompts.",
                ],
                commands=[
                    "python train/lora.py --config configs/lora.yaml --out artifacts/adapter-v1",
                    "python infer/smoke.py --base models/tiny-llm --adapter artifacts/adapter-v1",
                ],
            ),
            GuidePhase(
                name="Eval report",
                goal="Demonstrate adapter improvement over base without regressions.",
                steps=[
                    "Run held-out test set through base and adapter.",
                    "Compute task metrics and slice breakdowns.",
                    "Check for catastrophic forgetting on general prompts.",
                    "Write eval report JSON and human-readable summary.",
                ],
                acceptance=[
                    "Adapter beats base on primary metric by pre-defined margin.",
                    "No slice regresses more than agreed tolerance vs base.",
                    "Report archived with adapter version and dataset checksum.",
                ],
                commands=[
                    "python eval/compare_models.py --base models/tiny-llm --adapter artifacts/adapter-v1 --test data/test.jsonl",
                    "python eval/report.py --results results/compare.json --out reports/lora_eval.md",
                ],
            ),
            GuidePhase(
                name="Serving endpoint",
                goal="Serve adapter behind a versioned API with rollback.",
                steps=[
                    "Implement loader that composes base model plus LoRA adapter.",
                    "Expose /v1/complete with model version header and health check.",
                    "Register version in local registry; keep previous version for rollback.",
                    "Document deploy, warm-up, and rollback commands.",
                ],
                acceptance=[
                    "Health check passes; version endpoint returns active adapter id.",
                    "Rollback switches version in under one minute without rebuild.",
                    "Requests log model version and latency for monitoring.",
                ],
                commands=[
                    "python serve/app.py --base models/tiny-llm --adapter artifacts/adapter-v1 --port 8080",
                    "curl -s localhost:8080/health | python -m json.tool",
                    "python serve/rollback.py --to adapter-v0",
                ],
            ),
        ],
        troubleshooting=[
            "Adapter overfits: reduce epochs, increase dropout, or expand training diversity.",
            "Serving OOM: merge adapter for inference or quantize base; reduce concurrent requests.",
            "Eval gain not visible live: confirm serving loads correct adapter version and prompt matches eval.",
            "Data leakage: audit train/test splits for duplicate inputs and near-duplicates.",
        ],
        related_patterns=[
            "data-card-gate",
            "feature-flag-model",
            "fallback-cascade",
            "eval-gated-release",
        ],
        related_labs=[
            "1102-post-training-methods",
            "1103-dataset-engineering",
            "1104-inference-infrastructure",
            "1105-deployment-and-routing",
        ],
    ),
    "red-team-security-harness": GuideDetail(
        overview=(
            "Automate prompt injection, tool abuse, and data exfiltration tests in CI. "
            "Pair attack cases with mitigations and an incident runbook so failures are "
            "detected before attackers find them."
        ),
        architecture_notes=(
            "The harness loads an attack set categorized by technique: direct injection, "
            "indirect injection via retrieved content, tool parameter abuse, and jailbreak "
            "variants. Tests run against the full stack with mitigations enabled. Failures "
            "map to mitigation controls and runbook steps. Reports feed security review gates."
        ),
        phases=[
            GuidePhase(
                name="Attack set",
                goal="Catalog realistic attacks aligned to system boundaries.",
                steps=[
                    "Collect attacks per surface: user input, retrieved docs, tool args, system prompts.",
                    "Tag cases: severity, expected behavior (block, sanitize, abstain).",
                    "Include variants from public benchmarks adapted to your domain.",
                    "Version attack set; review additions like production incident cases.",
                ],
                acceptance=[
                    "At least 40 cases covering all exposed surfaces.",
                    "Each case documents expected safe behavior, not just 'should not crash'.",
                    "Attack set checksum pinned in CI config.",
                ],
                commands=[
                    "python security/validate_attacks.py --path data/attacks.jsonl",
                    "python security/run_redteam.py --suite data/attacks.jsonl --out reports/redteam.json",
                ],
            ),
            GuidePhase(
                name="Mitigations",
                goal="Implement and test controls for each attack category.",
                steps=[
                    "Map attacks to controls: input delimiters, retrieval sanitization, tool allowlists.",
                    "Implement policy checks before model and tool execution.",
                    "Verify mitigations with targeted unit tests per control.",
                    "Document residual risk where mitigations are partial.",
                ],
                acceptance=[
                    "Every P0 attack category has at least one enforced mitigation.",
                    "Mitigation bypass attempts fail closed in harness runs.",
                    "Control mapping published in security/architecture.md.",
                ],
                commands=[
                    "python -m pytest tests/test_injection_guard.py -q",
                    "python security/run_redteam.py --suite data/attacks.jsonl --mitigations on",
                ],
            ),
            GuidePhase(
                name="Incident runbook",
                goal="Prepare response steps when red-team or live incidents occur.",
                steps=[
                    "Define severity levels and on-call escalation paths.",
                    "Write runbook: isolate feature flag, preserve logs, notify stakeholders.",
                    "Include template comms and post-incident eval additions.",
                    "Run tabletop exercise against a simulated harness failure.",
                ],
                acceptance=[
                    "Runbook executable in dry-run: flag off, logs captured, ticket filed.",
                    "Post-incident step adds failing case to attack set.",
                    "Tabletop completed with timed actions under 30 minutes.",
                ],
                commands=[
                    "python security/tabletop.py --scenario injection_bypass --dry-run",
                    "python deploy/feature_flag.py --disable risky-tool --dry-run",
                ],
            ),
        ],
        troubleshooting=[
            "Harness passes but manual jailbreaks succeed: expand attack set with compositional and multilingual cases.",
            "Mitigation breaks UX: tune sanitize vs block thresholds per surface.",
            "Flaky tool-abuse tests: mock tools in CI; run full-stack red-team nightly.",
            "Runbook stale after refactor: link runbook controls to harness case ids for auto-reminders.",
        ],
        related_patterns=[
            "prompt-injection-guard",
            "tool-sandbox",
            "adversarial-eval-suite",
            "human-approval-gate",
        ],
        related_labs=[
            "1004-security-of-ai-systems",
            "0505-context-failure-and-security",
            "0704-tools-as-capability-boundaries",
            "1005-responsible-ai-and-risk",
        ],
    ),
    "multimodal-document-pipeline": GuideDetail(
        overview=(
            "Build a pipeline that parses documents with OCR and layout analysis, extracts "
            "structured fields, and attaches provenance metadata for every value. Field-level "
            "eval measures extraction quality before downstream consumers trust the output."
        ),
        architecture_notes=(
            "Ingestion normalizes PDFs and images into page artifacts with layout blocks. "
            "OCR runs on scanned regions; digital text bypasses OCR where possible. "
            "Extraction models or rules map blocks to schema fields. Provenance records "
            "page, bbox, confidence, and pipeline version per field."
        ),
        phases=[
            GuidePhase(
                name="Parse/OCR",
                goal="Convert documents into layout-aware text blocks.",
                steps=[
                    "Detect digital text vs scanned regions per page.",
                    "Run OCR on scanned areas with local tesseract or mock OCR for CI.",
                    "Emit layout JSON: page, bbox, text, block_type.",
                    "Handle multi-column and table regions with basic structure tags.",
                ],
                acceptance=[
                    "Digital PDFs preserve text without unnecessary OCR.",
                    "OCR output includes confidence scores per block.",
                    "Layout JSON validates against internal schema.",
                ],
                commands=[
                    "python doc/parse.py --input samples/invoice.pdf --out tmp/layout.json",
                    "python doc/ocr.py --image samples/scan.png --out tmp/ocr.json",
                    "python -m pytest tests/test_parse_ocr.py -q",
                ],
            ),
            GuidePhase(
                name="Field eval",
                goal="Measure extraction accuracy per field on labeled documents.",
                steps=[
                    "Label gold set with field values and acceptable normalization rules.",
                    "Run extraction pipeline; compare with fuzzy match for dates and amounts.",
                    "Report precision/recall per field and per document type.",
                    "Add regression cases for past extraction failures.",
                ],
                acceptance=[
                    "Primary fields (total, date, vendor) meet F1 threshold on gold set.",
                    "Eval distinguishes OCR errors from extraction logic errors.",
                    "Field metrics exported JSON for CI gate.",
                ],
                commands=[
                    "python eval/field_eval.py --gold data/doc_gold.jsonl --pred tmp/extracted.jsonl",
                    "python eval/field_eval.py --report --out reports/field_eval.json",
                ],
            ),
            GuidePhase(
                name="Provenance metadata",
                goal="Attach traceable source pointers to every extracted field.",
                steps=[
                    "Define provenance schema: field, value, page, bbox, source_block_id, pipeline_version.",
                    "Populate provenance during extraction from layout block references.",
                    "Expose provenance in API response for UI highlighting.",
                    "Verify provenance resolves to existing blocks on validation pass.",
                ],
                acceptance=[
                    "Every non-null field includes provenance with valid block reference.",
                    "UI or CLI can highlight source region from provenance alone.",
                    "Pipeline version recorded for audit replay.",
                ],
                commands=[
                    "python extract/run.py --layout tmp/layout.json --schema invoice/v1 --out tmp/extracted.json",
                    "python provenance/verify.py --extracted tmp/extracted.json --layout tmp/layout.json",
                ],
            ),
        ],
        troubleshooting=[
            "OCR garbage on tables: detect table regions and route to specialized parser.",
            "Field eval inflated by easy digital PDFs: stratify metrics by scan vs digital subsets.",
            "Provenance bbox drift: store normalized coordinates relative to page dimensions.",
            "Slow pipeline: cache layout JSON and parallelize per-page OCR.",
        ],
        related_patterns=[
            "structured-output-validation",
            "human-review-queue",
            "parent-child-chunks",
            "uncertainty-disclosure",
        ],
        related_labs=[
            "1301-vision-and-document-intelligence",
            "0602-document-ingestion",
            "0502-structured-generation",
            "1002-metrics-and-human-judgment",
        ],
    ),
    "spec-to-production-feature": GuideDetail(
        overview=(
            "Take an AI feature from problem discovery through executable spec, "
            "implementation, eval, and gradual rollout. Each stage produces artifacts "
            "that gate the next, reducing rework and unmeasured launches."
        ),
        architecture_notes=(
            "The workflow starts with a problem brief tied to user evidence, not model "
            "capability. An executable spec defines inputs, outputs, eval cases, and "
            "non-goals. Implementation sits behind a feature flag with eval-gated CI. "
            "Rollout stages traffic while comparing slice metrics to a control."
        ),
        phases=[
            GuidePhase(
                name="Problem brief",
                goal="Validate that the problem warrants an AI solution.",
                steps=[
                    "Document user pain with quotes, frequency, and cost of status quo.",
                    "List non-AI alternatives considered and why insufficient.",
                    "Define success metrics tied to user outcomes, not model scores alone.",
                    "Get stakeholder sign-off before spec work begins.",
                ],
                acceptance=[
                    "Brief cites at least three user evidence points or support tickets.",
                    "Success metric has baseline measurement from current workflow.",
                    "Explicit non-goals prevent scope creep.",
                ],
                commands=[
                    "python specs/new_brief.py --template templates/problem_brief.md --out docs/briefs/feature-x.md",
                ],
            ),
            GuidePhase(
                name="Executable spec",
                goal="Write a testable spec with eval cases and acceptance thresholds.",
                steps=[
                    "Specify API contract, error modes, and latency budget.",
                    "Attach eval cases derived from brief scenarios.",
                    "Define acceptance thresholds per slice and abstention policy.",
                    "Review spec with eng, product, and eval owners.",
                ],
                acceptance=[
                    "Every acceptance criterion maps to an automated or scripted check.",
                    "Spec includes rollback and fallback behavior.",
                    "Review recorded with approvers named in spec header.",
                ],
                commands=[
                    "python specs/validate.py --spec specs/feature-x.yaml",
                    "python eval/run_from_spec.py --spec specs/feature-x.yaml --out reports/spec_eval.json",
                    "npm install -g @fission-ai/openspec@latest && openspec init",
                    "# In Cursor or supported assistant: /opsx:propose Add feature-x acceptance spec",
                    "openspec validate",
                    "cp templates/spec-driven/lab-acceptance.yaml specs/feature-x-acceptance.yaml",
                ],
            ),
            GuidePhase(
                name="Feature flag rollout",
                goal="Ship gradually with measurement and fast rollback.",
                steps=[
                    "Implement feature behind flag default-off in production config.",
                    "Run spec evals in CI; block merge on threshold failures.",
                    "Roll out 1% → 10% → 50% → 100% with soak periods.",
                    "Compare treatment vs control on brief success metrics and eval proxies.",
                ],
                acceptance=[
                    "Flag off restores baseline behavior within one config push.",
                    "Rollout pauses automatically if error rate or primary metric regresses.",
                    "Final report links brief, spec, eval results, and rollout timeline.",
                ],
                commands=[
                    "python deploy/feature_flag.py --enable feature-x --percent 5 --dry-run",
                    "python eval/compare_rollout.py --metric support_deflection --control control --treatment feature-x",
                ],
            ),
        ],
        troubleshooting=[
            "Spec evals pass but users unhappy: success metrics in brief diverged from eval proxies; realign.",
            "Rollout stuck at low percent: insufficient traffic for slices; extend soak or widen cohort.",
            "Flag toggles wrong environment: namespace flags per env and add startup log of active flags.",
            "Scope creep mid-implementation: enforce non-goals in spec review and reject untracked cases.",
        ],
        related_patterns=[
            "spec-driven-ai-feature",
            "feature-flag-model",
            "eval-gated-release",
            "online-canary",
        ],
        related_labs=[
            "0901-discovering-the-right-problem",
            "0902-specification-driven-development",
            "0906-experiments-adoption-and-value",
            "0904-testing-ai-systems",
        ],
    ),
}
