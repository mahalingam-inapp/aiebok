# Pattern Library

**Browse collapsed groups** below — each table summarizes patterns inline. Use site **search** (`/` ) for a specific name, or expand a group to scan.

Starter deep-dives: [Planner–Executor](planner-executor.md) · [Human Approval](human-approval.md)

??? abstract "Agents & orchestration (19)"
    | Pattern | Context | Solution | Skip when |
    | --- | --- | --- | --- |
    | [Agent Heartbeat](agent-heartbeat.md) | Detect stuck agents via heartbeat. | Timeout if no progress events. | Sub-second tasks. |
    | [Checkpoint Resume](checkpoint-resume.md) | Persist agent state to survive interruptions. | Save state after each step; resume idempotently. | Sub-minute synchronous tasks. |
    | [Deterministic Workflow Core](workflow-deterministic-core.md) | Keep billing/auth deterministic; LLM at edges. | Orchestrator code owns critical path. | Fully exploratory chat. |
    | [Durable Agent Queue](durable-agent-queue.md) | Orchestrate long agents with queues and leases. | Queue steps; lease workers; renew or reclaim. | Short synchronous agent demos. |
    | [Durable Checkpoint](durable-checkpoint.md) | Persist agent state after each external effect. | Write checkpoint before/after side effects. | Ephemeral demos. |
    | [Evaluator–Optimizer](evaluator-optimizer.md) | Generate candidates then score with independent evaluator. | Sample N; evaluate; pick best. | Cheap verifier exists. |
    | [Human Approval Gate](human-approval-gate.md) | Pause agent loops before irreversible or high-cost actions. | Require explicit approval token before side-effect tools run. | Read-only or fully reversible actions. |
    | [Human Review Queue](human-review-queue.md) | Queue low-confidence outputs for review. | Score confidence; route below threshold. | Low stakes automation. |
    | [Human-in-Loop Training](human-in-loop-train.md) | Collect edits for SFT/DPO datasets. | Capture accepted edits with consent. | No retraining planned. |
    | [Latency Budget Router](latency-budget-router.md) | Pick model path by remaining SLA budget. | Fast path when budget low. | Batch offline. |
    | [Map–Reduce LLM](map-reduce-llm.md) | Split large inputs, process chunks, merge results. | Map per chunk; reduce with structured merge. | Input fits context. |
    | [Router](router-pattern.md) | Classify requests to specialized handlers or models. | Lightweight classifier routes by intent or risk tier. | Single handler suffices. |
    | [Schema-First Tools](schema-first-tools.md) | Design tools from OpenAPI/JSON Schema first. | Generate tool defs from schema. | Ad-hoc scripts. |
    | [Supervisor–Worker](supervisor-worker.md) | Delegate subtasks from a coordinator to specialized workers. | Supervisor plans; workers execute bounded tools; results aggregate. | Single-agent loop with parallel tool calls is enough. |
    | [Tool Adapter](tool-adapter.md) | Wrap legacy APIs as typed model tools. | Schema + auth + error mapping layer. | Greenfield typed APIs exist. |
    | [Tool Allowlist](tool-allowlist.md) | Explicit allowlist per agent profile. | Config declares permitted tools. | Fully trusted env. |
    | [Tool Result Truncation](tool-result-truncation.md) | Bound tool output size entering context. | Summarize or clip with pointer to full payload. | Tiny tool payloads. |
    | [Tool Sandbox](tool-sandbox.md) | Run tools with least privilege and typed arguments. | Validate args; enforce ACL; timeout and audit. | Trusted fixed-parameter internal calls. |
    | [Tool Timeout Cascade](tool-timeout-cascade.md) | Short timeouts with fallback tools. | Primary tool timeout → secondary → human. | Single reliable tool. |

??? abstract "Evaluation & observability (16)"
    | Pattern | Context | Solution | Skip when |
    | --- | --- | --- | --- |
    | [Adversarial Eval Suite](adversarial-eval-suite.md) | Red-team prompts and retrieved poison in CI. | Maintain attack set; run before release. | Low-risk internal summarization only. |
    | [Confidence Calibration](confidence-calibration.md) | Map scores to calibrated probabilities. | Isotonic regression on held-out set. | Ordinal scores enough. |
    | [Data Card Gate](data-card-gate.md) | Block training data use without documented card. | Require lineage, consent, eval splits. | Internal experimental data only. |
    | [Eval Data Versioning](eval-data-versioning.md) | Version eval sets like code. | Git LFS or DVC for eval JSONL. | Ad-hoc spreadsheets. |
    | [Eval-Gated Release](eval-gated-release.md) | Block release until predefined eval slices pass. | CI runs component and end-to-end evals with thresholds. | Non-production experiments without user impact. |
    | [Feature-Flagged Model](feature-flag-model.md) | Toggle models or prompts without redeploy. | Flag controls routing in gateway. | Static deployments OK. |
    | [Feedback to Eval](feedback-to-eval.md) | Promote production failures into eval sets. | Weekly triage of bad traces into cases. | Stable workload. |
    | [Gradual Rollout](gradual-rollout.md) | Increase traffic to new version slowly. | 5→25→50→100 with gates. | Low traffic features. |
    | [LLM Judge Calibration](llm-judge-calibration.md) | Calibrate automated judges against human ratings. | Sample cases for dual review; fit calibration curve. | Human review is cheap enough. |
    | [Negative Feedback Loop](negative-feedback-loop.md) | Use thumbs-down to block similar failures. | Embed complaint; nearest-neighbor block or finetune. | No user feedback channel. |
    | [Observability Traces](observability-traces.md) | Trace retrieval, prompts, tools, and outputs per request. | Structured spans with versions and latencies. | Offline batch without SLOs. |
    | [Offline Eval Regression](offline-eval-regression.md) | Run eval harness on every prompt/model change. | CI dataset with thresholds. | Non-production sandboxes. |
    | [Online Canary](online-canary.md) | Route small traffic fraction to candidate version. | Compare live metrics with guardrails. | Pre-production only testing. |
    | [Shadow Model](shadow-model.md) | Run candidate model without serving responses. | Log shadow outputs; compare offline. | Pre-prod only testing sufficient. |
    | [Slice-Based Evaluation](slice-based-eval.md) | Report metrics per subpopulation, not aggregates alone. | Define slices upfront; gate release on worst-slice performance. | Homogeneous low-risk workloads. |
    | [Trace Sampling](trace-sampling.md) | Sample traces for cost while keeping errors. | 100% errors; sample successes. | Full trace budget available. |

??? abstract "Platform & operations (7)"
    | Pattern | Context | Solution | Skip when |
    | --- | --- | --- | --- |
    | [Answer Diff Review](answer-diff-review.md) | Show diff when model changes answer on rerun. | Highlight changed spans to user. | Deterministic systems. |
    | [Answer Ensemble](answer-ensemble.md) | Combine multiple retrieval or model paths. | Vote or merge with verifier. | Single path calibrated. |
    | [Best-of-N Sampling](best-of-n-sample.md) | Generate N outputs; select with verifier or reward. | Parallel samples; independent scoring. | Strong verifier unavailable. |
    | [Conversation Summary Memory](conversation-summary-memory.md) | Compress older turns into rolling summary. | Summarize after N turns; keep recent verbatim. | Short chats only. |
    | [SLO-Driven AI Ops](service-level-objectives.md) | Define SLOs for quality, latency, cost. | Error budgets for releases. | Research prototypes. |
    | [Self-Consistency](self-consistency.md) | Majority vote over diverse reasoning paths. | Sample multiple chains; aggregate answer. | Single pass is calibrated enough. |
    | [Spec-Driven AI Feature](spec-driven-ai-feature.md) | Write executable specs before model integration. | Examples define acceptance; tests drive implementation. | Exploratory research spikes. |

??? abstract "Prompts, context & routing (25)"
    | Pattern | Context | Solution | Skip when |
    | --- | --- | --- | --- |
    | [Adapter Swapping](adapter-swapping.md) | Serve LoRA adapters per tenant or task. | Load adapters dynamically on base model. | Single behavior everywhere. |
    | [Batch Inference Window](batch-inference-window.md) | Accumulate requests for efficient GPU batches. | Micro-batch within latency SLO. | Strict sub-second SLAs. |
    | [Circuit Breaker](circuit-breaker-model.md) | Stop calling failing model or tool temporarily. | Open circuit on error rate threshold. | Batch offline jobs. |
    | [Context Budget Packing](context-budget-packing.md) | Allocate fixed token budgets per context section by priority. | Rank sections; truncate or summarize low-priority blocks. | Short contexts where everything fits. |
    | [Context Compressor](context-compressor.md) | Summarize or extract before main model call. | Compress low-priority history to fixed budget. | Short sessions only. |
    | [Fallback Cascade](fallback-cascade.md) | Try primary path then ordered fallbacks. | Define fallback chain with explicit user messaging. | Hard failure acceptable. |
    | [Fallback Degrade](fallback-degrade.md) | Graceful degradation when models or retrieval fail. | Define cheaper/safer fallback path with user messaging. | Hard-fail acceptable for batch jobs. |
    | [Model Routing](model-routing.md) | Route requests to models by risk, cost, and capability. | Classifier or rules pick model tier per request. | Single model meets all slices. |
    | [Model Warm Pool](model-warm-pool.md) | Keep minimum replicas warm. | HPA with min replicas > 0. | Sporadic batch jobs. |
    | [Output Schema Repair](output-schema-repair.md) | One repair attempt before failing structured output. | Validate JSON; re-prompt with errors. | Free-form chat. |
    | [Prompt Cache Key](prompt-cache-key.md) | Reuse prefix KV cache across similar requests. | Hash stable system prefix; cache by tenant. | Unique prompts every request. |
    | [Prompt Injection Guard](prompt-injection-guard.md) | Separate trusted instructions from untrusted data. | Delimiters + policy + output validation. | No external content in context. |
    | [Prompt Lint](prompt-lint.md) | Static checks on prompt templates. | CI rules for banned phrases and PII. | Single static prompt. |
    | [Prompt Versioning](prompt-versioning.md) | Treat prompts as versioned code with regression tests. | Store prompts in repo; run eval harness on change. | Throwaway prototypes not entering production. |
    | [Quality Tier Routing](quality-tier-routing.md) | Premium vs standard model tiers. | Route by subscription or risk. | Flat tier product. |
    | [Request Idempotency](request-idempotency.md) | Duplicate agent or API calls must not double-charge or double-write. | Idempotency keys on side-effect tools. | Read-only idempotent reads only. |
    | [Role-Based Prompts](role-based-prompts.md) | Different system prompts by user role. | RBAC selects prompt template. | Uniform users. |
    | [Session Affinity](session-affinity.md) | Route returning users to warm context. | Sticky routing to cached prefix. | Stateless OK. |
    | [Speculative Decoding](speculative-decode.md) | Draft model proposes; target model verifies. | Small draft + parallel verification. | Latency already sufficient. |
    | [Streaming Partial UI](streaming-partial-ui.md) | Show tokens progressively with cancel option. | Stream deltas; allow stop. | Batch response sufficient. |
    | [Structured Logging](structured-logging.md) | Log JSON fields for retrieval and generation. | Standard schema across services. | Prototype only. |
    | [Structured Output Validation](structured-output-validation.md) | Parse and validate model JSON against schemas before use. | Schema validate; repair or reject; never trust raw strings. | Fully free-form chat UX. |
    | [Tenant Rate Limit](tenant-rate-limit.md) | Fair usage across customers on shared models. | Token bucket per tenant with burst. | Single-tenant deployment. |
    | [Token Budget Forecast](token-budget-forecast.md) | Estimate tokens before calling model. | Pre-count sections; drop lowest priority. | Tiny prompts. |
    | [Undo AI Action](undo-ai-action.md) | Make model-driven changes reversible. | Store before-state; offer undo window. | Read-only assistants. |

??? abstract "Retrieval & knowledge (25)"
    | Pattern | Context | Solution | Skip when |
    | --- | --- | --- | --- |
    | [Batch Embed Pipeline](batch-embed-pipeline.md) | Embed documents in offline batches. | Queue docs; batch embed; atomic index swap. | Real-time ingest required. |
    | [Chunk Overlap Tuning](chunk-overlap-tune.md) | Tune overlap for recall vs redundancy. | Grid search overlap on eval queries. | Small corpus brute force OK. |
    | [Citation Validator](citation-validator.md) | Verify generated claims against cited passages. | Align spans; flag unsupported sentences. | No factual claims required. |
    | [Citation-Grounded Answer](citation-grounded-answer.md) | Require claims to link to retrieved passages. | Generate with citations; validate alignment post-hoc. | Creative tasks without factual claims. |
    | [Cross-Encoder Gate](cross-encoder-gate.md) | Cheap bi-encoder then expensive rerank. | Two-stage with cutoff. | Small corpora. |
    | [Document Version Pin](doc-version-pin.md) | Pin answers to explicit corpus version. | Expose version in UI and logs. | Static FAQ. |
    | [Dual-Write Index](dual-write-index.md) | Write new and old indexes during embedding migration. | Query both; compare; cutover with flag. | No index migrations. |
    | [Embedding Drift Monitor](embedding-drift-monitor.md) | Detect when query/doc embedding distribution shifts. | Track centroid distance and recall proxies. | Static corpus. |
    | [Graph Retrieval Augment](graph-retrieval-augment.md) | Combine graph traversal with vector hits. | Entities from graph; text from vectors. | Flat documents enough. |
    | [Grounded Refusal](grounded-refusal.md) | Refuse when retrieval confidence is low. | Threshold on retrieval score; templated refusal. | Creative writing tasks. |
    | [Hybrid Retrieval](hybrid-retrieval.md) | Combine lexical and dense retrievers when queries mix identifiers and paraphrases. | Use reciprocal rank fusion or learned reranking after dual retrieval. | Single-method retrieval suffices for uniform query distribution. |
    | [Incremental Index Update](incremental-index-update.md) | Update index incrementally on doc changes. | CDC stream to chunk pipeline. | Batch nightly enough. |
    | [Index Compaction](index-compaction.md) | Periodic compaction of vector segments. | Scheduled merge jobs. | Tiny indexes. |
    | [Metadata Filter First](metadata-filter-first.md) | Apply ACL and facet filters before vector search. | Hard filters shrink candidate set. | Open internal corpus. |
    | [Multi-Index Query](multi-index-query.md) | Query product, policy, and ticket indexes. | Parallel retrieval with merge. | Single index sufficient. |
    | [Multi-Tenant Retrieval](multi-tenant-retrieval.md) | Isolate retrieval indexes and ACLs per tenant. | Filter every query by tenant and role metadata. | Single-tenant internal tools. |
    | [Parent–Child Chunks](parent-child-chunks.md) | Index small chunks; retrieve parents for context. | Child for search; parent for generation. | Chunks already self-contained. |
    | [Query Decomposition](query-decomposition.md) | Split complex user questions into sub-queries. | Planner emits sub-queries; merge results. | Single-hop retrieval works. |
    | [Query Rewrite Cache](query-rewrite-cache.md) | Cache rewritten queries for repeat intents. | Store rewrite+results for session. | Highly diverse queries. |
    | [Retrieval Cache](retrieval-cache.md) | Cache retrieval results for hot queries. | TTL cache keyed by query+filters. | Highly dynamic corpora. |
    | [Retrieval Explain](retrieval-explain.md) | Show why passages were retrieved. | Log scores and matched terms. | Internal tools only. |
    | [Retrieval Fusion](retrieval-fusion.md) | Merge multiple retriever lists without score calibration. | RRF or learned fusion over ranked lists. | One retriever dominates all queries. |
    | [Retrieve Then Rerank](retrieve-then-rerank.md) | Fast first-stage retrieval followed by cross-encoder reranking. | Retrieve top-N quickly; rerank top-M before generation. | Small corpora where brute-force scoring is cheap. |
    | [Semantic Cache](semantic-cache.md) | Reuse prior answers for similar queries. | Embed query; lookup near-duplicates above threshold. | Highly unique or regulated queries. |
    | [Temporal Freshness Index](temporal-freshness-index.md) | Prefer recent documents when freshness matters. | Boost by timestamp or version. | Static knowledge base. |

??? abstract "Safety & governance (6)"
    | Pattern | Context | Solution | Skip when |
    | --- | --- | --- | --- |
    | [Data Residency Route](data-residency-route.md) | Route requests to region-specific stacks. | Geo DNS + regional indexes. | Single region OK. |
    | [Model Terms Filter](model-terms-filter.md) | Block requests violating model AUP. | Pre-filter inputs/outputs. | Internal unrestricted use. |
    | [PII Redaction](pii-redaction.md) | Redact sensitive spans before logging or training. | Detect/redact; store mapping securely. | No PII workloads. |
    | [Policy as Code](policy-as-code.md) | Encode AI policies in testable rules. | OPA/Rego or CI policy checks on configs. | Informal policy docs enough. |
    | [Secrets Scopes](secrets-scopes.md) | Scope API keys per tool and environment. | Separate keys; rotate; deny cross-env. | Single shared key internal only. |
    | [Uncertainty Disclosure](uncertainty-disclosure.md) | Show confidence and sources to users. | Calibrated scores + citations in UI. | Expert-only tools. |

