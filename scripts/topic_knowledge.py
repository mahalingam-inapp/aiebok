"""Topic knowledge entries for every AIEBOK catalog topic.

Each entry provides (explanation, example, evidence) for use in
enrichment, validation, and concept rendering.
"""
from __future__ import annotations

import re


def normalize(topic: str) -> str:
    """Normalize a topic label to a lowercase hyphenated slug."""
    return re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")


TOPIC_FACTS: dict[str, tuple[str, str, str]] = {
    "a": (
        'A* expands the lowest estimated total-cost node first, combining path cost g(n) with heuristic h(n) toward the goal. With an admissible heuristic it finds optimal paths while often expanding fewer nodes than BFS.',
        'In a grid maze, A* with Manhattan distance typically expands fewer cells than BFS while returning the same shortest path.',
        'Compare expanded node counts for BFS and A* on identical inputs and verify equal path cost.',
    ),
    "a-b-testing": (
        'A/B testing compares product variants on live users with ethical guardrails and pre-registered metrics.',
        'Test copilot placement in workflow A versus B measuring task completion time.',
        'Pre-register sample size, primary metric, and stop rules; monitor guardrails.',
    ),
    "a-b-tests": (
        'A/B tests compare prompt or context variants on live traffic with guardrail metrics. They need sufficient power and ethical review for user-facing experiments.',
        'Testing two retrieval packing orders measures answer quality impact on 5% of queries.',
        'Pre-register primary metric, minimum detectable effect, and stopping rules before launch.',
    ),
    "ablations": (
        'Ablations remove components to measure contribution—essential for judging which mechanism drives reported gains.',
        'Paper claims graph RAG helps; ablation removing graph should show drop if claim holds.',
        'Require ablation table or run own component removal on reproduction attempt.',
    ),
    "abstention": (
        'Abstention lets a system refuse or defer when confidence is insufficient, routing cases to humans or safer paths. It prevents forced wrong answers on ambiguous inputs.',
        'A benefits bot abstains on incomplete forms instead of guessing eligibility that triggers appeals.',
        'Measure coverage (non-abstain rate) versus accuracy on handled cases and set abstention to hit a risk target.',
    ),
    "acceptance-criteria": (
        'Acceptance criteria are pass/fail conditions for feature completion—testable, unambiguous, tied to user value.',
        'Given ambiguous date, system asks clarifying question rather than guessing—100% on test set.',
        'Convert each criterion into an automated or manual test case with owner.',
    ),
    "accessibility": (
        'Accessibility ensures AI features work with screen readers, keyboard navigation, and assistive tech—not only visual chat UIs.',
        'Streaming tokens must announce sensibly; citation links need accessible labels.',
        'Run WCAG-oriented audit on primary AI flows and fix P1 issues before launch.',
    ),
    "action-spaces": (
        'Action spaces define allowed agent operations—click, type, scroll, API call—with granularity affecting reliability.',
        "Semantic actions ('open_settings') beat raw coordinates when UI reskins change layout.",
        'Compare success rate semantic versus coordinate actions after UI theme change.',
    ),
    "activations": (
        'Activation functions introduce nonlinearity—ReLU, GELU, sigmoid—without which deep networks collapse to linear maps. Choice affects gradient flow and training stability.',
        'GELU in transformers smooths gradients compared to ReLU for language modeling at scale.',
        'Compare training convergence with ReLU versus GELU on the same architecture and seed.',
    ),
    "adaptive-rag": (
        'Adaptive RAG chooses retrieval depth, query rewrite, or no retrieval based on question type and confidence. It saves cost on simple queries while going deep on hard ones.',
        'Greetings skip retrieval; compliance questions trigger hybrid search plus rerank.',
        'Compare average latency and accuracy versus always-retrieve baseline on mixed query set.',
    ),
    "adoption": (
        'Adoption tracks who uses the feature, how often, and whether usage persists after novelty fades.',
        '80% weekly active support agents using suggest-reply after 60 days indicates adoption.',
        'Plot cohort retention curve at 7, 30, and 90 days post-launch.',
    ),
    "adversarial-tests": (
        'Adversarial tests probe injection, jailbreaks, edge inputs, and abuse scenarios. They belong in release gates for user-facing AI.',
        'Prompt injection via ticket body attempting credential exfil must fail closed.',
        'Maintain adversarial suite; require 100% pass on P0 cases before deploy.',
    ),
    "agency": (
        'Agency is goal-directed action selection in a loop—observe, decide, act—rather than a single model call. It implies autonomy bounded by policy, tools, and termination rules.',
        'An agent chooses which tool to call next based on observations, unlike a fixed workflow script.',
        'Compare task completion on variable inputs between scripted workflow and agent with same tools.',
    ),
    "ai-coding-agents": (
        'AI coding agents autonomously edit repositories given goals, tools, and constraints. They amplify throughput but require specs, tests, and human review.',
        'Agent implements feature branch with tests; human reviews diff before merge.',
        'Track defect density and review time per agent-generated PR versus human-only.',
    ),
    "ai-gateways": (
        'AI gateways centralize model access with auth, rate limits, logging, routing, and policy enforcement for enterprise teams.',
        'All Bedrock and OpenAI calls flow through gateway applying PII scrub and budget caps.',
        'Block direct model endpoint access; verify 100% traffic appears in gateway logs.',
    ),
    "ai-inventory": (
        'AI inventory catalogs models, datasets, prompts, and features with owners, risk tier, and dependencies. You cannot govern what you cannot find.',
        'Registry lists prod chatbot v3, embedding model e5-v2, fine-tune data v1.4 with owners.',
        'Quarterly audit: every production AI surface appears in inventory with current owner.',
    ),
    "aks-and-functions": (
        'AKS and Azure Functions run containerized model servers and event-driven AI glue code on Azure.',
        'Function triggers on blob upload; AKS serves GPU embedding model with HPA.',
        'Compare cold start and cost for Functions versus always-on AKS for ingest path.',
    ),
    "amazon-bedrock": (
        'Amazon Bedrock provides managed access to foundation models from multiple providers via unified AWS APIs with IAM integration and private networking.',
        'Invoke Claude and Titan through Bedrock in VPC without exposing keys on laptops.',
        'Compare Bedrock latency and cost versus self-hosted on same region for target workload.',
    ),
    "ambiguity": (
        'Ambiguity arises when the same text supports multiple interpretations without disambiguating context. Production systems need clarification, abstention, or retrieval—not forced guesses.',
        "'Reset my password' versus 'reset the server password' differ by scope; missing context causes wrong runbooks.",
        'Collect ten ambiguous user queries and measure how often the system asks clarifying questions.',
    ),
    "ann-indexes": (
        'Approximate nearest neighbor indexes—HNSW, IVF, LSH—trade recall for speed at million-plus scale. Index parameters must be tuned on representative queries.',
        'HNSW with efSearch=100 may hit 98% recall@10 at 5ms versus 50ms exact on 1M vectors.',
        'Plot latency versus recall@k for three index configurations on production query sample.',
    ),
    "answer-validation": (
        'Answer validation runs programmatic checks—schema, arithmetic, citation alignment—on model outputs before display. It catches errors sampling alone misses.',
        'Verify cited policy IDs exist and quoted numbers match source tables.',
        'Report validation failure rate by category on production sample weekly.',
    ),
    "approval-gates": (
        'Approval gates pause execution until authorized humans confirm high-impact actions. They convert autonomy into supervised autonomy.',
        'Production deploy agent waits for manager click before kubectl apply.',
        'Verify gate cannot be bypassed via prompt injection or direct tool URL.',
    ),
    "attention-masks": (
        'Attention masks zero out disallowed positions—future tokens in decoding, padding, or cross-segment boundaries. Masks enforce causality and ignore irrelevant tokens.',
        'Causal masks prevent a language model from peeking at answer tokens during training.',
        'Apply a causal mask and confirm no weight connects position i to j > i.',
    ),
    "audit": (
        'Audit logs record who accessed which models, documents, and tools with immutable retention for compliance.',
        'Log entry: user, query hash, retrieved doc IDs, model version, timestamp.',
        'Simulate auditor request; produce complete trail for sample user within SLA.',
    ),
    "audit-evidence": (
        'Audit evidence collects eval reports, approvals, change logs, and incident records demonstrating controlled AI delivery.',
        'Release ticket links eval v47 pass, security review, and canary metrics.',
        'Auditor can trace any prod model version to eval artifact and approver within 15 minutes.',
    ),
    "authentication": (
        'Authentication verifies identity of users, clients, and services before access to models, tools, or data. It applies equally to MCP sessions, enterprise assistants, and REST APIs.',
        'OAuth tokens gate MCP server access; SSO identifies employees before internal doc retrieval.',
        'Reject unauthenticated requests and verify token expiry across MCP and HTTP entry points.',
    ),
    "authorization": (
        'Authorization ensures retrieved and acted-upon data respects user permissions—not just authentication. RAG without authZ leaks restricted documents into answers.',
        'An employee should not retrieve executive compensation docs via semantic search without role checks.',
        'Run queries as low-privilege users and confirm zero restricted chunks appear in context.',
    ),
    "autoencoders": (
        'Autoencoders learn compressed representations by reconstructing inputs through a bottleneck layer. They support anomaly detection and pretraining when labels are scarce.',
        'Reconstruction error spikes on malformed log lines that never appeared in training—useful for anomaly alerts.',
        'Flag the top 1% reconstruction errors and measure precision of true anomalies among them.',
    ),
    "autonomy": (
        'Autonomy is how much discretion the system has to choose actions without human approval. More autonomy demands stronger evals, budgets, and rollback.',
        'Auto-closing duplicate tickets is low autonomy; auto-issuing refunds is high and needs gates.',
        'Document autonomy level per action type and map each to required approval policy.',
    ),
    "autoscaling": (
        'Autoscaling adjusts inference replica count based on CPU, GPU utilization, or queue depth.',
        'Scale GPU pods from 2 to 10 when p95 queue wait exceeds 500ms.',
        'Load spike test verifies scale-up within target minutes without error burst.',
    ),
    "azure-ai-foundry": (
        "Azure AI Foundry is Microsoft's unified portal for model deployment, fine-tuning, evaluation, and agent tooling integrated with Azure services.",
        'Deploy GPT-4o mini, run eval flow, and promote to managed endpoint from Foundry pipeline.',
        'Trace model from Foundry project through to production endpoint with eval artifact link.',
    ),
    "azure-ai-search": (
        'Azure AI Search provides hybrid lexical-vector search, semantic ranker, and skill pipelines for RAG on Azure.',
        'Indexer pipeline OCRs PDFs, enriches metadata, and indexes vectors for copilot retrieval.',
        'Measure indexer lag from blob upload to searchable document against freshness SLA.',
    ),
    "azure-openai": (
        'Azure OpenAI Service hosts OpenAI models in Azure regions with private networking, content filters, and Entra ID auth.',
        'Enterprise chatbot calls gpt-4o in tenant VNet with content safety filters enabled.',
        'Verify no traffic bypasses Azure content filter policy on red-team prompt set.',
    ),
    "backpropagation": (
        'Backpropagation applies the chain rule to compute gradients through layered computations efficiently. It enables training deep networks but requires careful initialization and normalization.',
        'One backward pass from loss to weights updates every layer in a classifier simultaneously.',
        'Verify gradients with finite differences on a tiny network for one batch.',
    ),
    "backtracking": (
        'Backtracking abandons partial solutions that fail constraints and returns to earlier choices. Essential when early greedy decisions lock in errors.',
        'If tool call returns 404, backtrack to alternate query formulation instead of hallucinating data.',
        'Log backtrack events and measure recovery rate on injected tool failures.',
    ),
    "baseline-workflow": (
        'Baseline workflow documents how users solve the task today—time, errors, tools—before AI intervention. Improvement requires beating this baseline.',
        'Manual ticket tagging takes 45s each; AI must beat accuracy and time with correction cost included.',
        'Measure baseline task time and error rate on ten representative sessions.',
    ),
    "baselines": (
        'Baselines are simple reference methods—majority class, linear model, keyword rules—that quantify what complexity must beat. Without them, teams cannot justify neural networks or LLMs.',
        'A TF–IDF logistic regression baseline on ticket routing sets the bar before trying embeddings.',
        'Report baseline and candidate metrics on identical splits; require statistically meaningful uplift for release.',
    ),
    "batching": (
        'Batching groups requests to amortize GPU kernel overhead, improving throughput at possible latency cost. Continuous batching in servers interleaves sequences of different lengths.',
        'Batch size 32 may double throughput versus batch 1 but increase p95 latency for short prompts.',
        'Load-test at concurrency 1, 8, and 32; report throughput and p95 latency.',
    ),
    "behavior-versus-knowledge": (
        'Behavior changes how the model acts—tone, format, policy—while knowledge is factual content. RAG adds knowledge; fine-tuning often shifts behavior.',
        'Model knows refunds exist but needs SFT to always ask order ID first—that is behavior.',
        'Classify ten requirements as behavior or knowledge and map to prompt, RAG, or fine-tune.',
    ),
    "benchmarks": (
        'Benchmarks standardize task comparisons—MMLU, HumanEval, BEIR—but may not reflect your production distribution.',
        'High MMLU does not guarantee payroll policy QA performance.',
        'Reproduce one benchmark subset plus in-domain eval before vendor selection.',
    ),
    "best-of-n": (
        'Best-of-N generates N candidates and selects the best by a scorer or verifier. Quality rises with N but so do cost and latency.',
        'Generate ten JSON plans; pick the one passing all schema and dependency checks.',
        'Plot task success versus N and identify diminishing returns knee.',
    ),
    "bias-and-variance": (
        'Bias is systematic underfitting from overly simple models; variance is sensitivity to training noise from overly complex ones. Tuning trades these errors against compute and data volume.',
        'A linear model underfits nonlinear fraud patterns (high bias); a huge tree overfits small samples (high variance).',
        'Plot error versus model capacity and identify the knee where validation error stops improving.',
    ),
    "bm25": (
        'BM25 ranks documents by weighted term frequency with length normalization and term-frequency saturation. Extra keyword repetition helps less over time compared to raw TF.',
        'A policy ID in the query should rank the exact section above generic overview pages.',
        'Report recall@k on identifier-heavy queries versus a dense-only retriever.',
    ),
    "bottlenecks": (
        'Information bottlenecks force compressive representations—fixed-size context vectors or limited bandwidth channels. They create trade-offs between memory and expressiveness.',
        'Early seq2seq used a single context vector for entire sentences, losing detail on long inputs.',
        'Compare output quality on 50-token versus 500-token inputs through a fixed bottleneck.',
    ),
    "bounded-rationality": (
        'Bounded rationality acknowledges limited compute, time, memory, and information—systems must satisfice within budgets. Production AI rarely has the luxury of exhaustive search or perfect retrieval.',
        'An on-call copilot stops after three retrieval attempts within a 5-second latency SLO instead of searching until theoretical certainty.',
        'Document the stopping budget and demonstrate a case where more compute would help but violates the SLO.',
    ),
    "bpe": (
        'Byte-pair encoding iteratively merges frequent symbol pairs to build a subword vocabulary from corpus statistics. It balances compression and interpretability for LLM tokenizers.',
        "Training BPE on code-heavy corpora merges operators like '=>' into single tokens, saving context budget.",
        'Train a toy BPE on 1MB text and report compression ratio versus character count.',
    ),
    "breadth-first-search": (
        'Breadth-first search expands nodes level by level, guaranteeing shortest path in unweighted graphs. It is the baseline for optimal reachability before adding heuristics.',
        'In a grid maze, BFS finds the minimum-step route from start to exit by exploring all distance-1 cells before distance-2.',
        'Run BFS on a fixed maze and verify path length equals the known shortest distance.',
    ),
    "budgets": (
        'Budgets cap tokens, tool calls, wall time, or dollars per task or session. Hard budgets prevent runaway agents and make economics predictable.',
        'A research agent stops after $0.50 API spend or ten tool calls, whichever comes first.',
        'Verify 100% of runs respect budget caps in stress tests with tempting infinite loops.',
    ),
    "build-versus-buy": (
        'Build versus buy weighs custom AI development against vendor APIs and platforms on control, cost, and time-to-value.',
        'Buy GPT-4 API for prototype; build fine-tuned model when volume makes unit economics favorable.',
        'ADR comparing three-year TCO and risk for build versus buy options.',
    ),
    "caching": (
        'Caching stores prompt prefixes, embeddings, or completions to cut latency and cost. Cache keys must include model version and prompt hash to avoid stale wrong answers.',
        'Caching the system prompt KV states saves compute on every request with identical instructions.',
        'Measure cache hit rate and verify cache invalidation when prompt version changes.',
    ),
    "calibration": (
        'Calibration means predicted probabilities align with observed frequencies—70% confidence should be right about 70% of the time. Uncalibrated scores mislead threshold and cost decisions.',
        'A medical triage model with miscalibrated probabilities causes undertriage when 0.9 confidence actually means 0.6 accuracy.',
        'Plot a reliability diagram and report expected calibration error before setting production thresholds.',
    ),
    "canaries": (
        'Canaries route small traffic percentage to new versions before full rollout.',
        '5% traffic to new embedding index for 24h comparing recall and latency.',
        'Auto-rollback canary if error rate or primary metric degrades beyond bound.',
    ),
    "cancellation": (
        'Cancellation stops in-flight agent work cleanly—revoke leases, abort tool calls, compensate partial effects. Users need cancel when plans change.',
        'User cancels long research job; system stops tools and marks run cancelled, not failed.',
        'Cancel at random steps and verify no orphaned side effects remain.',
    ),
    "capability-decomposition": (
        'Capability decomposition splits intelligence into perception, memory, learning, planning, and action so teams can own, test, and debug each part. Without it, fluent outputs hide which capability failed.',
        'Incident routing can fail in classification while generation still reads naturally—decomposition exposes the failing box.',
        'Draw a capability map and mark which component owns each failure from a real incident postmortem.',
    ),
    "checkpoints": (
        'Checkpoints persist durable agent state so interrupted runs resume without repeating side effects.',
        'After approval gate, checkpoint stores pending payment until human approves, then continues.',
        'Kill run mid-loop, restore checkpoint, verify idempotent tools are not duplicated.',
    ),
    "chunking": (
        'Chunking splits documents into index units sized for retrieval precision and generation context. Boundaries should respect sections, not arbitrary token counts alone.',
        'Splitting mid-table separates headers from values, producing useless retrieval hits.',
        'Compare recall@5 with fixed-size versus section-aware chunking on table-heavy docs.',
    ),
    "citation-precision": (
        'Citation precision measures whether cited sources actually support the adjacent claims. Wrong citations destroy trust faster than no citations.',
        'Linking a harassment policy to answer a parking question is high-recall citation but zero precision.',
        'Manually audit 50 claim–citation pairs and report precision and unsupported-claim rate.',
    ),
    "citations": (
        'Citations link UI claims to source passages users can verify. They must be accurate, clickable, and adjacent to the supported statement.',
        'Refund policy answer includes link jumping to handbook section 4.2.',
        'Audit 50 UI citations for precision and broken links monthly.',
    ),
    "classification": (
        'Classification assigns inputs to discrete categories via scores converted to labels. Thresholds, class imbalance, and cost asymmetry matter as much as raw accuracy.',
        'Binary fraud classification at 0.5 default threshold wastes money when false positives cost $2 and false negatives cost $200.',
        'Publish confusion matrix and per-class recall on a stratified validation set.',
    ),
    "cloud-iam": (
        'Google Cloud IAM binds roles to identities for least-privilege access to Vertex, Storage, and BigQuery in AI pipelines.',
        'Service account invokes Vertex prediction only; humans cannot read raw training bucket.',
        'IAM policy audit: no allUsers on AI artifact buckets.',
    ),
    "cloud-run-and-gke": (
        'Cloud Run and GKE deploy serverless containers and Kubernetes GPU workloads on Google Cloud.',
        'Cloud Run serves CPU embedding API; GKE Autopilot runs LLM inference with TPU/GPU node pools.',
        'Document when Cloud Run max duration forces move to GKE for long jobs.',
    ),
    "cloudwatch-and-iam": (
        'CloudWatch and IAM deliver AWS monitoring, alerting, and access control for AI workloads—metrics, logs, roles, policies.',
        'IAM role grants Bedrock invoke only; CloudWatch alarm on 5xx rate triggers runbook.',
        'Least-privilege IAM review quarterly; zero overly broad bedrock:* on human roles.',
    ),
    "clustering": (
        'Clustering groups unlabeled points by similarity—k-means, hierarchical, or density methods. Clusters are hypotheses about structure that require domain validation.',
        'Grouping support tickets by embedding clusters reveals recurring themes but does not automatically name them correctly.',
        'Measure cluster stability under bootstrap resampling and have a domain expert label ten clusters for coherence.',
    ),
    "code-review": (
        'Code review evaluates correctness, security, and maintainability of changes—including agent-written code. It remains accountability gate before merge.',
        'Reviewer checks agent did not skip auth on new endpoint despite passing happy-path tests.',
        'Measure post-merge incident rate for agent-authored versus human-authored merges.',
    ),
    "compensation": (
        'Compensation undo or offsets partial effects when later steps fail—Saga pattern for agents. Without it, retries duplicate charges or records.',
        'Failed booking after charge triggers automatic refund compensation transaction.',
        'Simulate mid-saga failure and verify compensation returns system to pre-transaction state.',
    ),
    "component-evals": (
        'Component evals test retrieval, generation, tools, and UX stages independently before end-to-end runs. They localize failures.',
        'Retrieval recall@10 evaluated separately from answer faithfulness on same queries.',
        'Build failure attribution matrix mapping end-to-end misses to component scores.',
    ),
    "compression": (
        'Context compression summarizes, extracts, or prunes evidence to fit token limits while preserving decision-critical facts. Lossy compression can drop citations or qualifiers.',
        'Summarizing ten pages into bullet points may omit exception clauses unless extraction is structured.',
        'Measure citation recall and answer correctness before and after compression at fixed budget.',
    ),
    "computer-use": (
        'Computer use agents perceive screens and emit mouse/keyboard actions to complete software tasks.',
        'Agent fills expense form in internal web app from receipt image with confirmation gates.',
        'Task success rate on sandboxed UI benchmark with zero unauthorized actions.',
    ),
    "conditioning": (
        'Conditioning steers generation with extra inputs—text, masks, ControlNet edges, brand assets.',
        'Logo placement conditioned via layout mask keeps brand mark in safe zone.',
        'Ablation: compare output compliance with versus without layout conditioning.',
    ),
    "confidence-intervals": (
        'Confidence intervals quantify uncertainty in metric estimates from finite eval sets. Comparing models requires overlapping intervals or formal tests.',
        'Model A at 82% ± 3% versus Model B at 85% ± 4% may not be significantly different.',
        'Report 95% CI for primary metrics; require non-overlap for major release claims.',
    ),
    "confusion-matrix": (
        'A confusion matrix counts predicted versus actual classes, exposing which errors dominate. It is essential when classes are imbalanced or costs asymmetric.',
        "A router may confuse 'billing' with 'refund' while rarely missing 'outage'—the matrix shows where to invest labeling.",
        'Compute per-class precision and recall from the matrix on a stratified test set.',
    ),
    "consensus": (
        'Consensus protocols align multiple agents on a decision before action—voting, debate, or judge model. Useful when single-agent judgment is unreliable.',
        'Three agents vote on classification before automated ticket routing proceeds.',
        'Compare accuracy of consensus versus single agent on ambiguous case set.',
    ),
    "constraints": (
        'Constraints specify forbidden actions, length limits, formats, and scope boundaries in prompts. They reduce search space but must be testable.',
        "'Do not mention competitors' and 'max 100 words' are enforceable constraints for eval.",
        'Run constraint-violation checks on 100 outputs and track violation rate per release.',
    ),
    "containers": (
        'Containers package model servers with dependencies for reproducible deployment across environments.',
        'Docker image pins CUDA, Python, and model weights hash for prod inference.',
        'Scan container image for CVEs; block deploy on critical unfixed vulnerabilities.',
    ),
    "contamination": (
        'Contamination occurs when eval examples leak into training data, inflating benchmark scores.',
        'Near-duplicate test questions in fine-tune set invalidate held-out claims.',
        'Run n-gram or embedding overlap check between train and eval; zero high overlap pairs.',
    ),
    "context-assembly": (
        'Context assembly is the pipeline that gathers instructions, state, evidence, tools, and examples into the final prompt. Order and separation affect model behavior.',
        'Placing evidence after instructions but before the user question reduces instruction drift in long contexts.',
        "Trace one request's assembly stages and verify each section matches the spec template.",
    ),
    "context-files": (
        'Context files—.cursorrules, architecture docs—supply persistent project knowledge to coding agents. Stale context misleads worse than no context.',
        'Architecture.md describes service boundaries so agent edits correct package.',
        'Update context file when ADR changes and note version in agent traces.',
    ),
    "context-packing": (
        'Context packing fits selected passages into the token window respecting priority, citation needs, and truncation rules. Packing order affects what the model emphasizes.',
        'Place highest-scored evidence first when middle-context attention is weaker in long windows.',
        'Compare faithfulness when critical passage is first versus last at equal total tokens.',
    ),
    "context-poisoning": (
        'Context poisoning inserts false or misleading evidence into retrieval or memory stores to manipulate outputs. Integrity controls on indexes and ingestion are defenses.',
        'An attacker uploads a fake policy PDF to skew answers about refund eligibility.',
        'Monitor ingest sources, sign documents, and detect anomalous embedding clusters post-ingest.',
    ),
    "context-traces": (
        'Context traces log the assembled prompt sections, token counts, and sources for debugging and compliance. They make probabilistic failures reproducible.',
        'Replaying a failed answer with its trace shows whether retrieval or ranking dropped the key passage.',
        'Sample 1% of requests with full traces retained for 30 days minimum.',
    ),
    "context-windows": (
        'Context windows cap tokens the model attends to in one forward pass—prompt, evidence, tools, and output compete for this budget.',
        'A 128k window still requires prioritization when ten long documents are retrieved.',
        'Measure task quality versus tokens used and find the knee of the curve for your workload.',
    ),
    "continual-learning": (
        'Continual learning updates models on new data without catastrophic forgetting of prior tasks. Production systems often prefer explicit versioning and retraining over true continual learning today.',
        'Adding new product SKUs to classifier without retraining on old SKUs should not collapse accuracy on legacy labels.',
        'Measure accuracy on old and new task slices after incremental update versus full retrain baseline.',
    ),
    "continuous-evaluation": (
        'Continuous evaluation runs production or shadow traffic against eval suites to detect drift post-release.',
        'Nightly job scores 500 sampled prod queries with LLM judge against rubric.',
        'Alert when rolling 7-day faithfulness drops below threshold versus launch baseline.',
    ),
    "contract-tests": (
        'Contract tests verify integrations between services—API schemas, tool responses—without full end-to-end runs. They catch breaking changes early.',
        'Consumer test asserts search API returns fields reranker expects.',
        'Run contract tests in CI on every API schema change.',
    ),
    "control": (
        'Control mechanisms—approvals, rate limits, tool allowlists— constrain agent behavior within safe envelopes. Control is designed, not emergent from prompts alone.',
        'Payments above $500 require human approval even if the agent recommends proceed.',
        'Attempt forbidden actions in red-team tests and verify control layer blocks 100%.',
    ),
    "coordination": (
        'Coordination synchronizes multiple agents—shared queues, locks, message passing—to avoid conflicting actions. It adds latency and failure modes.',
        'Two workers must not edit the same document; lease coordinates exclusive access.',
        'Stress test concurrent agents and measure conflict rate with and without coordination.',
    ),
    "corpora": (
        'Corpora are curated text collections whose composition, licensing, and bias shape every downstream model. Provenance and consent determine legal and ethical use.',
        'Training on public forums without filtering includes toxic threads that surface in generations.',
        'Document source, license, date range, and language distribution in a corpus card.',
    ),
    "correction": (
        'Correction flows let users fix wrong AI outputs and feed improvements—labels, prompts, or models. Without correction, errors repeat silently.',
        'Thumbs-down on answer captures expected response for eval set addition.',
        'Track correction rate and time-to-incorporate into eval or training.',
    ),
    "cosine-similarity": (
        'Cosine similarity measures the angle between vectors, ignoring magnitude—standard for normalized embeddings in retrieval.',
        'Two policy summaries of different lengths can match semantically when cosine is high despite different norms.',
        'Verify identical rankings after L2-normalizing embeddings versus raw cosine computation.',
    ),
    "cost-quality-curves": (
        'Cost-quality curves plot spend—tokens, GPU seconds, API dollars—against task metrics. They guide routing and when to stop adding compute.',
        'Best-of-N may lift accuracy 2 points for 4× cost—acceptable only above a revenue threshold.',
        'Generate curve points for three strategies and document chosen operating point rationale.',
    ),
    "critique": (
        'Critique models or rubrics evaluate drafts and suggest fixes before finalization. Separating generation from critique reduces shared blind spots.',
        'A critic flags unsupported claims in a research draft before user delivery.',
        'Measure error reduction with generate-then-critique versus single-pass on 50 tasks.',
    ),
    "cross-validation": (
        'Cross-validation rotates train and validation folds to estimate performance variance with limited data. It reduces luck from a single split but must respect temporal or group structure when required.',
        'K-fold on i.i.d. tabular data estimates variance; time-series tasks need forward-chaining instead.',
        'Report mean and standard deviation of the metric across folds, not just the best fold.',
    ),
    "data-cards": (
        'Data cards document dataset sources, collection, demographics, limitations, and recommended uses—parallel to model cards.',
        'Fine-tune data card lists languages, date range, PII handling, and opt-out process.',
        'Publish data card with every dataset version in registry.',
    ),
    "data-curation": (
        'Data curation selects, cleans, and balances training examples for quality over quantity. Garbage data teaches garbage behavior.',
        'Removing toxic and duplicate examples improves fine-tune safety more than doubling raw size.',
        'Document inclusion rules and manual audit sample of 100 rows pre-training.',
    ),
    "data-exfiltration": (
        'Data exfiltration via AI occurs when prompts or tools leak secrets, PII, or restricted docs to unauthorized parties.',
        'Injection tricking model to dump system prompt or customer list into chat.',
        'Red-team exfil scenarios; verify DLP blocks and zero successful leaks in test.',
    ),
    "data-leakage": (
        'Data leakage lets information from the target or future timesteps into features or labels during training. It inflates offline metrics while production performance collapses.',
        "Including the support agent's resolution note written after closure as a feature perfectly predicts reopen—uselessly.",
        'Run a feature audit: remove each suspicious column and watch for unrealistic AUC drops that signal leakage.',
    ),
    "data-mixtures": (
        'Data mixtures blend corpora—web, code, books, dialog—at tuned ratios during pretraining. Mixture proportions strongly affect capabilities and biases.',
        'Over-weighting code improves programming but may hurt conversational tone.',
        'Ablate one corpus slice from the mixture and measure task-specific eval deltas.',
    ),
    "data-provenance": (
        'Data provenance records origin, transformations, timestamps, and responsible parties for each document. It enables audit, takedown, and debugging retrieval mistakes.',
        'Knowing a policy chunk came from v3.2 PDF page 14—not an outdated wiki—fixes wrong answers.',
        'Every retrieved chunk should carry source URI, version, and ingest timestamp in metadata.',
    ),
    "data-residency": (
        'Data residency restricts processing and storage to approved geographic regions for legal compliance.',
        'EU customer prompts and indexes stay in eu-west inference and storage only.',
        'Validate data plane region tags on every storage and inference resource.',
    ),
    "data-validation": (
        'Data validation checks schema, ranges, distributions, and freshness of incoming data before training or inference. Silent schema drift breaks pipelines quietly.',
        'A new optional field arriving as null for 40% of rows should block training until investigated.',
        'Run validation rules on daily ingest and alert when any column exceeds drift thresholds.',
    ),
    "decision-thresholds": (
        'Decision thresholds turn continuous scores into actions—approve, escalate, or abstain. They encode business costs and should be tuned on validation data, not defaults.',
        'Raising a fraud threshold reduces false positives but increases missed fraud; the optimum depends on chargeback cost.',
        'Sweep thresholds on a validation set and plot precision-recall against expected dollar cost.',
    ),
    "decomposition": (
        'Decomposition breaks complex tasks into subtasks with clearer stopping criteria and verifiable intermediate results. It enables parallel work and localized retries.',
        'Research splits into search, read, synthesize, and cite—each subtask has its own eval.',
        'Compare success rate on compound tasks with monolithic prompts versus explicit decomposition.',
    ),
    "deduplication": (
        'Deduplication removes near-duplicate training examples that inflate metrics and memorization.',
        'Duplicate FAQ pairs in SFT data cause verbatim regurgitation in deployment.',
        'Report duplicate rate before/after MinHash dedup on training corpus.',
    ),
    "deep-learning": (
        'Deep learning stacks differentiable layers that learn hierarchical features from raw inputs. It excels when hand-crafted features are incomplete but demands data, compute, and careful evaluation.',
        'Vision models learn edge and shape detectors automatically where manual feature design for every object class is infeasible.',
        'Compare a linear baseline to a small network on the same split and justify the added complexity with slice metrics.',
    ),
    "delegation": (
        'Delegation assigns subtasks to specialized agents or tools with scoped permissions. Poor delegation boundaries cause duplicated work or authority gaps.',
        'Legal sub-agent handles contract clauses; main agent cannot invoke legal tools directly.',
        'Audit delegation graph for cycles and privilege escalation paths.',
    ),
    "delimiters": (
        'Delimiters—XML tags, markdown fences, triple quotes—separate instructions from data so models parse structure reliably. Consistent delimiters reduce instruction–content bleed.',
        'Wrapping user HTML in <document> tags prevents tags from being interpreted as instructions.',
        'Test ten adversarial documents with and without delimiters and count instruction-following errors.',
    ),
    "dense-retrieval": (
        'Dense retrieval embeds queries and documents into the same vector space and returns nearest neighbors by similarity.',
        "A query about 'application unavailable' retrieves 'service is down' without lexical overlap.",
        'Build a 30-query eval with paraphrases and hard negatives; report recall@5 and MRR.',
    ),
    "dependencies": (
        'Dependencies constrain execution order—step B requires output or state from step A. Violating them causes flaky failures or data corruption.',
        'Sending customer emails before database migration commits references wrong product IDs.',
        'Topological sort the plan and simulate; flag any out-of-order execution.',
    ),
    "deterministic-metrics": (
        'Deterministic metrics—exact match, F1 on spans, JSON validity—give reproducible scores without sampling variance.',
        'Schema validation pass rate is deterministic; helpfulness often is not.',
        'Prefer deterministic metrics for CI gates; use statistical metrics with confidence intervals for quality tracking.',
    ),
    "diarization": (
        'Diarization labels who spoke when in multi-speaker audio—essential for meetings and support calls.',
        'Support call transcript tags agent versus customer utterances for QA scoring.',
        'Diarization error rate on labeled two-speaker test set ≤ target before deploy.',
    ),
    "diffusion": (
        'Diffusion models generate images by iterative denoising from noise, conditioning on text or layout.',
        'Marketing generates product hero images from prompt plus brand color conditioning.',
        'FID or human preference eval versus baseline; scan outputs for policy violations.',
    ),
    "dimensionality-reduction": (
        'Dimensionality reduction projects high-dimensional data to fewer dimensions for visualization, compression, or denoising—PCA, t-SNE, UMAP. Preserved geometry depends on the method.',
        'PCA on ticket embeddings for dashboard visualization may linearly mix topics; UMAP preserves local neighborhoods differently.',
        'Compare reconstruction error (PCA) or neighborhood preservation metrics on a fixed sample.',
    ),
    "discourse": (
        'Discourse connects sentences across turns and documents—coreference, topic continuity, rhetorical structure. Long interactions fail when each turn is processed in isolation.',
        "'It' in turn three refers to the outage mentioned in turn one only if discourse state is preserved.",
        'Run a coreference test set and report F1 on pronouns spanning three or more turns.',
    ),
    "distillation": (
        'Distillation trains smaller student models to mimic larger teachers, trading capability for cost and speed.',
        'Student classifier matches teacher on 95% of eval at 5× lower latency.',
        'Measure student versus teacher gap on full eval and acceptable degradation threshold.',
    ),
    "distribution-shift": (
        'Distribution shift occurs when deployment data differs from training data in language, demographics, seasonality, or product mix. Models degrade silently when shift is unmonitored.',
        "A model trained pre-acquisition fails on the acquired company's ticket vocabulary until retrained or augmented.",
        'Monitor slice metrics weekly and alert when any slice drops more than five points from its baseline.',
    ),
    "diversity": (
        'Diversity in context selection avoids redundant passages that waste tokens on repeated facts. Maximal marginal relevance is a common heuristic.',
        'Three chunks saying the same PTO limit add no value; one plus related exceptions is better.',
        'Compare unique fact coverage at fixed token budget with and without MMR selection.',
    ),
    "document-ai": (
        'Document AI pipelines combine OCR, layout, extraction, and validation for structured data from unstructured files.',
        'Extract vendor, line items, tax from PDF invoices into ERP JSON with confidence scores.',
        'Report field-level accuracy and human review rate on production document sample.',
    ),
    "dot-product": (
        'Dot product measures alignment between vectors—used in attention scores and similarity when magnitudes carry signal. Scale affects ranking unless normalized.',
        'Unnormalized dot products favor longer document embeddings; cosine similarity removes length bias.',
        'Compare ranking order for ten queries using dot product versus cosine on the same vectors.',
    ),
    "dpo": (
        'Direct Preference Optimization aligns models from pairwise preferences without explicit reward model training.',
        'Prefer concise accurate answers over verbose wrong ones via DPO preference pairs.',
        'Win-rate versus base model on preference eval set ≥ target before deploy.',
    ),
    "drift": (
        'Drift is change in input or label distributions over time—covariate, prior, or concept drift. Unmonitored drift erodes model value without code changes.',
        'New product vocabulary after a launch shifts ticket text while labels stay stable—covariate drift.',
        'Monitor population stability index or embedding centroid shift weekly with alert thresholds.',
    ),
    "durable-execution": (
        'Durable execution persists workflow state across process restarts and deploys—Temporal, Step Functions patterns. Long agents need this, not in-memory loops alone.',
        'Day-long onboarding workflow survives server restart and resumes at last checkpoint.',
        'Kill worker mid-run twice and verify exactly-once side effects for non-idempotent steps.',
    ),
    "embedding-evaluation": (
        'Embedding evaluation measures retrieval quality—recall, MRR, nDCG—on realistic queries with hard negatives. Benchmarks must mirror production language and domains.',
        'Evaluating only easy paraphrases overstates performance versus queries with acronyms and typos.',
        'Build 50 queries with annotated gold passages and hard negatives; report recall@5 and MRR.',
    ),
    "end-to-end-evals": (
        'End-to-end evals measure full pipeline outcomes on realistic inputs including latency and cost.',
        'User question to cited answer passes only if retrieval, generation, and citation all succeed.',
        'Run weekly end-to-end suite with production config hash in report.',
    ),
    "entra-id-and-monitor": (
        'Microsoft Entra ID and Azure Monitor provide identity, RBAC, and observability for Azure AI workloads.',
        'Entra groups map to AI Search index ACLs; Monitor alerts on token spike anomalies.',
        'Validate disabled Entra user cannot invoke Azure OpenAI within minutes.',
    ),
    "entropy": (
        'Entropy measures uncertainty or information content in a distribution—high when outcomes are evenly spread, low when one dominates. It guides feature selection, decision trees, and regularization.',
        'A classifier with 95% softmax mass on one class is low-entropy and cheap to trust for routing; a flat distribution signals ambiguity worth escalating.',
        'Compute entropy for a sharp and a flat softmax vector and tie each to an operational action.',
    ),
    "episodic-memory": (
        'Episodic memory stores past run trajectories—what was tried, what failed—for future reference within or across sessions.',
        "Remembering last week's failed migration path prevents repeating the same broken sequence.",
        'Retrieve relevant episodes for similar goals and measure retry avoidance rate.',
    ),
    "eval-datasets": (
        'Eval datasets are labeled or rubric-scored cases representing production risks and happy paths. They must refresh as products and policies evolve.',
        '200 support queries with gold answers updated quarterly after product launches.',
        'Version eval dataset with changelog and rerun full suite monthly.',
    ),
    "evaluation-specs": (
        "Evaluation specs define datasets, metrics, slices, and release thresholds before shipping. They turn 'good enough' into numbers.",
        'Eval spec: 200 cases, faithfulness ≥ 0.9, P0 safety cases 100% pass.',
        'Block merge if eval spec checklist incomplete in release ticket.',
    ),
    "expected-cost": (
        'Expected cost combines probabilities of outcomes with their business costs to rank decisions. It makes asymmetric errors explicit instead of hiding them in accuracy.',
        'Approving a loan when P(default)=0.08 is cheap only if the expected loss is below the interest margin.',
        'Compute expected cost for three threshold settings and pick the minimum on a labeled validation set.',
    ),
    "experiment-tracking": (
        'Experiment tracking logs hyperparameters, data versions, metrics, and artifacts for every training run. Without it, teams cannot reproduce or compare results.',
        'Logging learning rate, seed, and dataset hash explains why run 47 beat run 46.',
        'Reproduce a logged run from its metadata and verify metric within 1% of the original.',
    ),
    "expert-systems": (
        'Expert systems capture domain heuristics in if-then rules curated by specialists, often with explanation traces. They trade flexibility for transparency and predictable behavior in narrow domains.',
        'A manufacturing diagnostic system asks sequential sensor questions and explains which rule fired when recommending a shutdown.',
        'Audit ten decisions and verify each cites the rule chain that produced the recommendation.',
    ),
    "fairness": (
        'Fairness examines disparate performance or harm across demographic or regional groups. Legal and ethical requirements vary by jurisdiction and use case.',
        'Loan model approval rate disparity across groups triggers review even if aggregate AUC is high.',
        'Evaluate primary metric and error rates per protected slice; document mitigation plan.',
    ),
    "faithfulness": (
        'Faithfulness checks that generated statements are entailed by retrieved evidence, not hallucinated additions. It is separate from fluency or user satisfaction.',
        'Correct tone but wrong deductible amount is unfaithful despite readable prose.',
        'Use NLI or human rubric on 100 answers; require faithfulness ≥ threshold for release.',
    ),
    "fallbacks": (
        'Fallbacks switch to alternate models, cached answers, or human handoff when primary path fails.',
        'If primary API 503, serve smaller local model with degraded-quality banner.',
        'Chaos-test primary failure; verify fallback activates within SLA with metric logged.',
    ),
    "feasibility": (
        'Feasibility assesses whether data, latency, risk, and model capability can meet requirements—not whether a demo works once.',
        'If no labeled data exists and mistakes cost $10k, feasibility may be low despite flashy prototype.',
        'List top three feasibility risks with mitigation or kill criteria.',
    ),
    "features-and-labels": (
        'Features are inputs; labels are supervised targets—both must be available at the decision time you actually deploy. Leaking future information creates impressive offline metrics and production disasters.',
        "Using 'time to resolution' as a feature to predict escalation leaks the outcome into the input.",
        'For each feature, document availability timestamp relative to prediction time and reject any post-outcome fields.',
    ),
    "feedback": (
        'Feedback closes the loop: outcomes from actions update beliefs, models, or policies for subsequent decisions. Without feedback channels, the same mistakes repeat indefinitely.',
        'Misrouted tickets returned by engineers should update routing features so the error rate on that category is trackable week over week.',
        'Identify one feedback signal, where it is stored, and measure how many days until it influences the next decision.',
    ),
    "few-shot-examples": (
        'Few-shot examples demonstrate desired input–output patterns inside the prompt. They help format and tone but consume tokens and can overfit demo patterns.',
        'Three invoice extraction examples teach field boundaries better than prose instructions alone.',
        'Compare accuracy with zero, three, and ten shots on held-out invoices.',
    ),
    "fine-tuning": (
        'Fine-tuning adapts pretrained weights with supervised or preference data when prompts and RAG cannot stabilize behavior. It trades generality and ops simplicity for targeted changes.',
        'Support tone and escalation policy may need SFT when prompts drift across thousands of ticket types.',
        'Compare fine-tuned and prompt-only models on held-out behavioral eval with rollback plan.',
    ),
    "finops": (
        'FinOps tracks and optimizes AI spend—tokens, GPU hours, API fees—against business value.',
        'Dashboard shows cost per successful ticket deflection by model route.',
        'Monthly review: top three cost drivers and optimization actions with owner.',
    ),
    "freshness": (
        'Freshness policies define acceptable document age, re-ingest cadence, and TTL for cached answers. Regulated domains often require sub-daily updates for policy corpora.',
        'Benefits enrollment answers must exclude documents marked superseded after open enrollment ends.',
        'Reject or downgrade chunks where ingest_timestamp exceeds freshness SLA for the topic.',
    ),
    "function-calling": (
        'Function calling lets models emit structured invocations with typed arguments that runtime code validates and executes.',
        'Searching internal docs via a read-only tool returns live titles instead of hallucinated links.',
        'Fuzz tool arguments and confirm unauthorized calls fail before side effects.',
    ),
    "functional-specifications": (
        'Functional specifications describe observable system behavior—inputs, outputs, errors—for builders and testers. They precede implementation and model choice.',
        'Spec states: given valid invoice PDF, return JSON with vendor, total, date or structured error code.',
        'Write acceptance examples as executable tests before coding.',
    ),
    "generalization": (
        'Generalization is performance on unseen data drawn from the deployment distribution, not memorization of training examples. The central engineering question is whether the system will work next month on real users.',
        'A memorizing model hits 100% on training tickets but fails on new product names never seen during training.',
        'Compare train and held-out slice metrics and require held-out performance above a release threshold.',
    ),
    "goal-decomposition": (
        "Goal decomposition maps a top-level objective into subgoals with success conditions and dependencies. It clarifies what 'done' means at each level.",
        "'Ship feature' decomposes into spec approved, code merged, eval passed, and canary clean.",
        'Validate dependency graph: no circular deps and every leaf goal is testable.',
    ),
    "goal-directed-behavior": (
        'Goal-directed behavior means selecting actions to reduce distance to an explicit objective rather than producing unconstrained text. Engineers care because fluent language can mask the absence of a measurable goal.',
        'An incident router should minimize misroutes and escalation time, not maximize eloquent ticket summaries.',
        'Define the goal metric and show one action that improves it versus one that sounds better but scores worse.',
    ),
    "gold-datasets": (
        'Gold datasets hold authoritative labels or reference outputs for evaluation. They require versioning, access control, and refresh cadence.',
        '200 lawyer-reviewed contract clauses with gold entity spans versioned quarterly.',
        'Hash dataset version in every eval report; reject runs on unversioned snapshots.',
    ),
    "gpus": (
        'GPUs accelerate matrix operations for training and inference; memory capacity limits model size and batch.',
        '80GB GPU runs 70B quantized; 24GB fits 7B fine-tune with QLoRA.',
        'Profile GPU utilization and memory headroom during peak inference load.',
    ),
    "gradient-descent": (
        'Gradient descent adjusts parameters in the direction that most reduces loss, using gradients computed from training examples. It is the workhorse optimizer behind most neural network training.',
        'One SGD step on linear regression moves weights toward the line minimizing squared error on the mini-batch.',
        'Hand-compute one update for noisy y = 2x + 1 data and confirm loss decreases on that batch.',
    ),
    "graph-rag": (
        'Graph RAG combines knowledge graphs with retrieval so multi-hop relations traverse explicit edges. It helps when answers require chained entity relationships.',
        "'Which vendor supplies part X used in product Y?' may need graph traversal, not one vector search.",
        'Compare multi-hop question accuracy versus flat chunk retrieval on ten linked-entity queries.',
    ),
    "grounded-generation": (
        'Grounded generation conditions answers strictly on provided evidence, refusing when support is insufficient. Prompts and validators enforce cite-or-abstain behavior.',
        'The model quotes section 4.2 for refund rules instead of inventing a 30-day window.',
        'Score faithfulness and abstention rate on cases with and without supporting passages.',
    ),
    "grounding": (
        'Grounding ties model statements to verifiable evidence—retrieved passages, database rows, tool outputs. Ungrounded generation is speculation presented as fact.',
        'Support answers should quote the ticket macro article that authorizes the refund step.',
        'Measure percent of claims with valid citations on a labeled answer set.',
    ),
    "hard-negatives": (
        'Hard negatives are plausible but incorrect passages that confuse retrievers—essential for training and evaluation realism. Easy negatives inflate metrics.',
        'A chunk about vacation policy is a hard negative for a sick-leave query sharing HR vocabulary.',
        'Include at least three hard negatives per query in eval sets and report recall drop versus easy-only sets.',
    ),
    "heuristics": (
        'Heuristics estimate remaining cost or promise of partial solutions to guide search toward promising branches. Good heuristics cut compute; bad ones waste it or break optimality guarantees.',
        'Manhattan distance guides grid navigation; an overestimated heuristic can make A* suboptimal or incomplete.',
        'Measure nodes expanded with and without the heuristic on ten random maps and report the speedup ratio.',
    ),
    "human-evaluation": (
        'Human evaluation labels outputs quality when automation cannot capture nuance or safety. Design for rater training, agreement, and throughput.',
        'Lawyers label contract summaries for legal accuracy on 50 cases monthly.',
        'Track inter-rater agreement and adjudicate disagreements with gold committee.',
    ),
    "human-oversight": (
        'Human oversight defines when and how people supervise agents—monitoring dashboards, escalation queues, kill switches. It scales only with clear triggers.',
        'Escalate to human when confidence < 0.7 or spend > $1 on a single task.',
        'Track escalation rate, human resolution time, and override frequency weekly.',
    ),
    "human-review": (
        'Human review inserts expert judgment for high-impact or low-confidence decisions. Designing the queue—what gets reviewed, SLA, feedback loop—determines ROI.',
        'Loan officers review only applications where the model score falls in the 0.4–0.6 band, covering 12% of volume at 3× higher fraud catch.',
        'Track review queue depth, override rate, and post-review error rate weekly.',
    ),
    "hybrid-search": (
        'Hybrid search combines lexical and dense signals—often via reciprocal rank fusion—when neither alone covers identifiers and paraphrases.',
        'Fusion surfaces policy IDs lexically while keeping semantic matches for informal phrasing.',
        'Show a query where lexical-only and dense-only each miss but fusion succeeds.',
    ),
    "idempotency": (
        'Idempotent tools produce the same effect when called repeatedly with the same idempotency key. Agents retry safely only when tools support this.',
        "create_ticket with idempotency key 'abc' must not spawn duplicate tickets on retry.",
        'Call the same tool twice with identical keys and verify single side effect.',
    ),
    "identity": (
        'Identity establishes who users and services are—SSO, service principals, workload identity—for AI data access.',
        'Employee SSO identity flows to retrieval filters and audit logs on every query.',
        'Verify deprovisioned user loses model and index access within one hour.',
    ),
    "impact-assessment": (
        'Impact assessment evaluates consequences of deploying AI on people, rights, and society before high-risk launch.',
        'Automated hiring tool requires assessment of bias, appeal process, and human override.',
        'Complete assessment template with sign-offs from legal, security, and product.',
    ),
    "incident-response": (
        'Incident response defines detect, triage, mitigate, communicate, and postmortem for AI failures—hallucination harm, data leak, outage.',
        'Kill switch disables feature flag within 5 minutes of P0 safety incident.',
        'Run tabletop exercise quarterly; measure time to mitigation in drill.',
    ),
    "inference": (
        'Inference applies a trained model to new inputs to produce predictions or generations. Serving latency, cost, and correctness are measured here—not during training.',
        'A production chatbot runs inference on every user message; batching ten requests changes throughput but not the trained weights.',
        'Measure p50 and p95 latency for single and batched requests at fixed concurrency.',
    ),
    "instruction-conflict": (
        'Instruction conflict occurs when system, developer, user, or retrieved text give incompatible directives. Resolution policy must be explicit and tested.',
        'User asks to bypass safety; system forbids it—the system policy must win consistently.',
        'Catalog ten conflict scenarios and measure compliance with documented precedence rules.',
    ),
    "instruction-hierarchy": (
        'Instruction hierarchy ranks system, developer, and user messages so lower-priority text cannot override safety or policy. It is essential when untrusted content appears in context.',
        'Retrieved web pages must not outrank the system prompt forbidding credential disclosure.',
        'Inject conflicting instructions at each level and verify system policy wins.',
    ),
    "instruction-tuning": (
        'Instruction tuning fine-tunes models on prompt–response pairs covering diverse tasks, improving zero-shot instruction following. It shapes helpfulness and format compliance.',
        "After instruction tuning, models follow 'respond in JSON' without task-specific fine-tuning.",
        'Compare instruction-following score on 50 held-out prompts before and after tuning.',
    ),
    "inter-rater-agreement": (
        "Inter-rater agreement measures how consistently multiple human graders apply rubrics—Cohen's kappa, Krippendorff's alpha.",
        'Low agreement on tone dimension means rubric needs refinement before scaling labeling.',
        'Compute kappa per rubric dimension; block scaling if below 0.6.',
    ),
    "jobs-to-be-done": (
        'Jobs-to-be-done frames what users hire a product to accomplish, not which technology it uses. AI fits when it improves the job outcome measurably.',
        "Users hire expense tool to 'get reimbursed fast', not to 'chat with AI'.",
        'Write job statement and success metric independent of model choice.',
    ),
    "json-schema": (
        'JSON Schema declares required fields, types, and constraints that validators enforce after model generation. It turns free-form text into typed data boundaries.',
        "Rejecting payloads where 'total' is a string prevents silent accounting errors from plausible JSON.",
        'Validate three intentionally invalid payloads and confirm distinct error reasons.',
    ),
    "keys": (
        'Keys are attention projections indexed for lookup—compatible queries receive high weights. Together with values they implement content-addressable memory over sequences.',
        "A pronoun's query should match keys at its antecedent position for correct coreference routing.",
        'Mask illegal keys and confirm attention mass stays on permitted positions only.',
    ),
    "knowledge-freshness": (
        'Knowledge freshness measures how current stored facts are relative to the real world. Stale indexes cause confident wrong answers until re-ingestion catches up.',
        'A travel policy updated yesterday is invisible if the index last synced last month.',
        'Track max document age in retrieved sets and alert when any source exceeds SLA staleness.',
    ),
    "knowledge-representation": (
        'Knowledge representation chooses how facts, relations, and uncertainty are stored—graphs, frames, schemas, or vectors. The representation determines what queries and updates are cheap or hard.',
        "Modeling product compatibility as a graph makes 'works-with' queries fast; flattening to text loses compositional structure.",
        'Run three query types on the same facts in two representations and compare answer latency and correctness.',
    ),
    "kv-cache": (
        'The KV cache stores key and value tensors for prior tokens during autoregressive decoding, avoiding recomputation of the prefix. Memory grows linearly with context length.',
        'Streaming chat reuses cached states for system prompt and prior turns, cutting latency after the first token.',
        'Compare tokens-per-second with and without KV cache on a 2k-token prefix.',
    ),
    "lambda-and-eks": (
        'AWS Lambda and EKS provide serverless functions and Kubernetes clusters for AI orchestration, agents, and custom servers.',
        'Lambda handles lightweight ingest triggers; EKS hosts vLLM GPU workloads with Karpenter scaling.',
        'Map workload to Lambda versus EKS based on duration, GPU need, and cold-start tolerance.',
    ),
    "latency": (
        'Latency is time from request to usable response—dominated by model, retrieval, tools, and serialization. User workflows break when p95 exceeds interaction tolerance.',
        'Adding reranking adds 200ms; measure whether task success gain justifies it.',
        'Track p50 and p95 end-to-end latency with breakdown by stage in traces.',
    ),
    "latent-space": (
        'Latent space in generative models compresses images to lower-dimensional representations for efficient editing and generation.',
        'Latent diffusion edits background without re-encoding full resolution each step.',
        'Measure edit consistency and artifact rate across ten latent manipulations.',
    ),
    "layout-models": (
        'Layout models detect reading order, tables, figures, and headings in documents beyond raw OCR boxes.',
        'Invoice layout model separates line items table from footer terms for field extraction.',
        'Evaluate field F1 with layout-aware parsing versus OCR-only on 50 document layouts.',
    ),
    "leases": (
        'Leases grant temporary exclusive ownership of a resource—document, ticket, shard—preventing duplicate processing. Expired leases must reclaim safely.',
        'Worker holds 60s lease on ticket; another worker picks up only after lease expiry.',
        'Simulate worker death before lease expiry and verify safe reassignment.',
    ),
    "llm-judges": (
        'LLM judges automate scoring using rubrics but must be calibrated against humans to avoid systematic bias.',
        'GPT-4 judge scores faithfulness correlated 0.85 with human labels after calibration.',
        'Sample 10% human audit of LLM judge scores each sprint; recalibrate if drift >5 points.',
    ),
    "logits": (
        'Logits are raw pre-softmax scores over the vocabulary for the next token. Decoding policies—temperature, top-k—operate on logits before sampling.',
        'Inspecting logits reveals whether the model hesitates between two equally likely tokens.',
        'Log top-5 logits for ten prompts and verify sampling changes when temperature increases.',
    ),
    "long-context": (
        'Long context models attend to hundred-thousand-plus tokens in one window—reducing need for retrieval but not eliminating cost or lost-in-middle effects.',
        'Pasting entire contract for QA works until cost and middle-section attention degrade answers.',
        'Compare long-context versus RAG on 50 questions requiring distant clause lookup.',
    ),
    "long-term-memory": (
        'Long-term memory stores durable facts—preferences, past resolutions—retrieved selectively for future sessions. It requires consent, expiry, and correction paths.',
        'Storing preferred language and timezone reduces friction but must be deletable on request.',
        'Test memory write, retrieval, update, and deletion with audit logs for GDPR requests.',
    ),
    "lora": (
        'LoRA fine-tunes low-rank adapter matrices in attention layers, reducing trainable parameters versus full fine-tuning.',
        '7B model with LoRA learns domain tone on one GPU while base weights stay frozen.',
        'Report eval uplift, training cost, and adapter version at inference.',
    ),
    "loss-functions": (
        'Loss functions score how wrong predictions are and drive optimization—cross-entropy for classes, MSE for regression, custom losses for ranking. The loss encodes what the system is punished for.',
        'Using focal loss down-weights easy negatives so a rare-defect detector trains on hard examples.',
        'Train with two losses on the same data and compare which aligns with the business metric.',
    ),
    "lstms": (
        'LSTMs add gating to RNNs to mitigate vanishing gradients and capture longer dependencies than plain RNNs. They dominated seq2seq before transformers but remain in some streaming pipelines.',
        'LSTM encoders for time-series logs capture hourly patterns over days of context.',
        'Compare validation loss at step 10k for LSTM versus transformer on identical data.',
    ),
    "matrix-transformations": (
        'Matrix transformations apply linear maps that rotate, scale, or project vector spaces—core to neural layers and attention projections. Understanding them clarifies why depth composes operations.',
        'An embedding layer is a matrix multiply that maps one-hot token indices into dense vectors.',
        'Multiply a 2×2 matrix by three vectors and confirm the output spans the expected subspace.',
    ),
    "mcp": (
        'Model Context Protocol standardizes how clients discover tools, resources, and prompts from servers. It reduces bespoke integration code but not trust decisions.',
        'An MCP server exposes filesystem read tools; the client still enforces path allowlists.',
        'Connect a hostile client and verify server rejects out-of-scope resource requests.',
    ),
    "memory": (
        'Memory in frontier systems spans working, episodic, and semantic stores beyond context windows—implementation varies widely.',
        'Agent stores user preferences in durable memory retrieved each session.',
        'Test memory CRUD and measure retrieval precision on continuation tasks.',
    ),
    "memory-retrieval": (
        'Memory retrieval selects relevant past facts given the current query—vector search, keyword, or structured lookup. Irrelevant memories pollute context and cause confabulation.',
        'Retrieving only memories tagged with the current project ID avoids cross-project contamination.',
        'Measure precision@5 of retrieved memories on labeled session continuations.',
    ),
    "metadata": (
        'Metadata tags documents with tenant, date, author, permissions, and type for filtering and ranking. Rich metadata enables policy enforcement beyond vector similarity.',
        'Filtering by effective_date prevents superseded policies from ranking above current ones.',
        'Verify every indexed chunk carries required metadata fields in ingest validation.',
    ),
    "metadata-filtering": (
        'Metadata filtering restricts vector or lexical search by tenant, date, permission, or document type before or after similarity scoring. It enforces policy and improves precision.',
        'Searching only documents where tenant_id matches and effective_date ≤ today prevents cross-customer leakage.',
        'Run ten queries with filters and confirm zero results violate authorization metadata.',
    ),
    "mixture-of-experts": (
        'Mixture-of-experts activates subsets of parameters per token, scaling capacity without proportional compute. Routing and load balancing add engineering complexity.',
        'An MoE layer may route math tokens to specialized experts while sharing common language experts.',
        'Monitor expert utilization histograms and penalize imbalance if any expert exceeds 40% load.',
    ),
    "mlp-blocks": (
        'MLP blocks apply position-wise feed-forward networks after attention, adding nonlinear capacity per token. They typically expand dimension 4× then project back.',
        'FFN layers store factual associations in some interpretability studies of LMs.',
        'Measure parameter count and FLOPs share of MLP versus attention in one block.',
    ),
    "model-cards": (
        'Model cards document intended use, training data, limitations, metrics, and ethical considerations for a model version.',
        'Card states model not for legal advice; lists languages supported and known failure modes.',
        'Publish model card link in registry for every production model version.',
    ),
    "model-catalog": (
        'Model catalog lists approved models with risk tier, eval status, and allowed use cases for developers.',
        'Catalog shows gpt-4o approved tier-2; llama-local approved tier-1 air-gapped only.',
        'Reject deployment requests for models not in catalog with approved version.',
    ),
    "model-registry": (
        'A model registry stores versioned models with stage labels—staging, production, archived—and metadata for audit. It is the handoff point between ML and serving teams.',
        'Promoting v3.2 to production requires passing eval gates linked in the registry entry.',
        'Trace one production prediction back to registry version, training data hash, and eval report.',
    ),
    "model-routing": (
        'Model routing directs requests to appropriate models by task, risk, cost, or latency policy.',
        'Regex on ticket category routes billing to fine-tuned small model, general to large.',
        'Log route decisions; compare blended cost and quality versus single-model baseline.',
    ),
    "model-selection": (
        'Model selection matches capabilities, cost, latency, license, and risk to task requirements—not brand prestige.',
        'Small model handles classification; large model only for complex reasoning slice.',
        'Benchmark three candidates on task eval with cost and latency columns in ADR.',
    ),
    "monitoring": (
        'Monitoring observes live inputs, outputs, latency, errors, and business metrics continuously. It connects production behavior to retraining and incident response.',
        'A spike in abstention rate may signal upstream data breakage before users complain.',
        'Dashboard p95 latency, error rate, and task success with alerts tied to runbooks.',
    ),
    "multi-head-attention": (
        'Multi-head attention runs several attention operations in parallel with separate projections, letting different heads capture diverse relations. Heads are often redundant but increase capacity.',
        'One head may track syntax; another tracks coreference in the same layer.',
        'Ablate heads individually and measure perplexity or task metric impact per head.',
    ),
    "multi-hop-retrieval": (
        'Multi-hop retrieval gathers evidence across sequential lookups when no single passage contains the answer. Orchestration must avoid error propagation from early hops.',
        'Finding budget owner requires hop one: project ID → department; hop two: department → approver.',
        'Measure end-to-end accuracy and per-hop recall on labeled multi-hop questions.',
    ),
    "multi-tenancy": (
        'Multi-tenancy isolates customer data, indexes, quotas, and configs in shared AI platforms.',
        'Tenant A embeddings never appear in Tenant B vector search results.',
        'Cross-tenant penetration tests must return zero data leaks.',
    ),
    "multilingual-models": (
        'Multilingual models share parameters across languages, enabling cross-lingual retrieval and generation. Performance varies by language pair and training data balance.',
        'A Spanish employee query can retrieve English policy text if the embedding space aligns concepts.',
        'Evaluate recall@5 separately per language on parallel query sets.',
    ),
    "multimodal-models": (
        'Multimodal models ingest text, images, audio, or video in shared architectures for joint understanding or generation. Modality alignment and tokenization differ per input type.',
        'A vision-language model answers questions about chart images in earnings reports.',
        'Evaluate field extraction accuracy on 50 document images with ground-truth labels.',
    ),
    "n-grams": (
        'N-gram models predict tokens from local history of n−1 prior tokens—simple, fast, and limited to short context. They remain baselines for compression and sanity checks.',
        "A trigram model captures 'New York' but not dependencies spanning whole paragraphs.",
        'Compare perplexity of n-gram versus small neural LM on the same held-out corpus.',
    ),
    "nearest-neighbors": (
        'Nearest-neighbor search returns the closest vectors to a query by a chosen metric. Exact search is fine for small indexes; production scales require approximate methods.',
        'Brute-force cosine over 10k chunks is fast; at 10M you need ANN indexes with recall trade-offs.',
        'Measure recall@10 of ANN versus exact search on a held-out query set.',
    ),
    "neurons-and-layers": (
        'Neurons apply activations to weighted sums; layers stack these transforms into composable functions. Depth lets networks build hierarchical abstractions.',
        'First layers in vision nets detect edges; deeper layers combine them into parts and objects.',
        'Inspect activation histograms per layer during training to catch dying ReLU or saturation.',
    ),
    "normalization": (
        'Text normalization lowercases, strips diacritics, standardizes whitespace, and canonicalizes equivalents before indexing or tokenization. Over-normalization destroys discriminative identifiers.',
        'Collapsing hyphens in SKUs merges distinct product codes; preserving case matters for camelCase APIs.',
        'Compare retrieval recall with and without aggressive normalization on identifier-heavy queries.',
    ),
    "ocr": (
        'OCR extracts text from scanned images and photos, introducing recognition errors that propagate to chunks and answers. Confidence scores help gate low-quality extractions.',
        'Scanned contracts with skewed pages need deskew preprocessing before OCR.',
        'Report word-error rate on ten scanned pages and abstain when mean confidence < threshold.',
    ),
    "one-hot-vectors": (
        'One-hot vectors encode categorical items as sparse binary indicators—simple but high-dimensional and semantically blind. They remain baselines for small categorical features.',
        'Encoding 10k product IDs as one-hot vectors is impractical; embeddings replace them at scale.',
        'Compare memory and lookup time for one-hot versus learned embedding on the same catalog size.',
    ),
    "open-weights": (
        'Open-weights models publish parameters for local deployment, fine-tuning, and inspection—versus API-only access. They shift control, compliance, and operational burden to your team.',
        'Self-hosting Llama enables air-gapped inference but requires GPU ops and security patching.',
        'Document license terms, hardware requirements, and eval parity versus API baseline before adoption.',
    ),
    "opensearch": (
        'Amazon OpenSearch supports lexical, vector, and hybrid search with k-NN indexes for RAG on AWS.',
        'OpenSearch k-NN index stores policy embeddings filtered by IAM-scoped document metadata.',
        'Benchmark recall@10 and p95 query latency on OpenSearch versus managed alternative.',
    ),
    "optimization": (
        'Optimization finds parameters that minimize loss—SGD, Adam, learning-rate schedules, and batch size interact with convergence speed and final quality.',
        'A too-high learning rate oscillates; too-low wastes GPU hours on a plateau.',
        'Log loss per step for three learning rates and pick the fastest stable convergence.',
    ),
    "optimizers": (
        'Optimizers like Adam, AdamW, and SGD with momentum adapt update rules beyond vanilla gradient descent. They affect convergence speed, final loss, and generalization.',
        'AdamW decouples weight decay from adaptive steps—common default for transformer fine-tuning.',
        'Compare final validation metric and training time for Adam versus SGD on the same task.',
    ),
    "parent-child-retrieval": (
        'Parent–child retrieval indexes small child chunks for precision but returns parent sections for generation context.',
        'A child bullet may lack the section title needed for a correct answer unless parent is joined.',
        'Demonstrate failure with child-only context and fix by returning parent at generation time.',
    ),
    "parsing": (
        'Parsing converts documents—PDF, HTML, DOCX—into clean text and structure for indexing. Bad parsing loses tables, headings, and lists that retrieval cannot recover.',
        'OCR garbling a table of limits makes correct retrieval impossible regardless of embedding quality.',
        'Measure character-error rate and table cell accuracy on 50 representative documents.',
    ),
    "permissions": (
        'Permissions bind tools and data access to authenticated identities and roles. Models must not bypass authorization by guessing URLs or parameters.',
        'delete_user tool requires admin role verified server-side, not in the prompt.',
        'Attempt privileged tool calls as low-privilege identity and expect denial.',
    ),
    "plan-act-observe": (
        'Plan–act–observe separates choosing the next action, executing it, and recording observations that update state.',
        "Agent plans 'create draft', executes, observes 'draft id=7', then plans verification instead of repeating creation.",
        'Log each cycle and show observations change subsequent plans, not identical repeats.',
    ),
    "plan-representation": (
        'Plan representation encodes steps, preconditions, effects, and dependencies in structures machines can validate—DAGs, STRIPS, or typed JSON plans.',
        'A migration plan lists DB schema change before app deploy as a hard dependency edge.',
        "Reject plans where any step's preconditions are unmet given simulated initial state.",
    ),
    "planner-executor": (
        'Planner–executor splits strategic planning from tactical execution, often with different models or prompts. Plans can be validated before expensive actions.',
        'Planner outputs step graph; executor calls tools one step at a time with verification.',
        'Measure plan validity rate and end-to-end success versus monolithic agent.',
    ),
    "planning": (
        'Planning sequences actions to reach a goal given a model of state transitions, costs, and constraints. It separates deliberation from execution so plans can be validated before side effects occur.',
        'A deployment planner orders database migration before code rollout because the transition model forbids incompatible schema states.',
        'Produce a plan, simulate it against the transition model, and flag any action that violates preconditions.',
    ),
    "platform-engineering": (
        'Platform engineering builds self-service AI infrastructure—gateways, eval harnesses, templates—so product teams ship faster safely.',
        'Platform provides RAG starter kit with auth, ingest, eval wired to corporate SSO.',
        'Track internal customer time-to-first-production-feature as platform KPI.',
    ),
    "portable-interfaces": (
        'Portable interfaces—OpenAI-compatible APIs, OTel traces, standard embedding dims—reduce lock-in across clouds.',
        'Gateway speaks OpenAI schema; backends swap Bedrock, Azure, or vLLM without client changes.',
        'Migrate one backend in staging with zero client SDK changes verified by integration tests.',
    ),
    "position": (
        'Position information tells transformers token order since self-attention is permutation-invariant without it. Methods include sinusoidal, learned, and rotary (RoPE) encodings.',
        'Rotary embeddings encode relative position in Q/K products for long-context models.',
        'Shuffle token order without position encodings and observe catastrophic perplexity increase.',
    ),
    "pragmatics": (
        'Pragmatics interprets meaning in context—speaker intent, implicature, and shared knowledge. Models lack shared world state unless you supply it explicitly.',
        "'Can you shut the door?' is a request, not a capability question—intent classification must capture this.",
        'Evaluate intent classification on indirect requests versus literal questions in the same domain.',
    ),
    "precision-and-recall": (
        'Precision is correctness among positive predictions; recall is coverage of actual positives. Trading them off reflects whether false positives or false negatives hurt more.',
        'High recall in safety alerts catches more incidents; high precision in auto-replies avoids annoying customers.',
        'Plot precision-recall curve and mark the operating point that meets your cost constraint.',
    ),
    "pretraining-objectives": (
        'Pretraining objectives define self-supervised targets—causal LM, masked LM, denoising—that shape what models learn from raw text. Objective choice affects bidirectionality and use cases.',
        'Causal LM suits generation; masked LM suits understanding tasks before fine-tuning.',
        'Compare downstream task scores after pretraining two small models with different objectives.',
    ),
    "primary-sources": (
        'Primary sources are original papers, specs, and official docs—not summaries or hype threads—for technical claims.',
        'Read Attention Is All You Need for architecture claims, not a blog recap.',
        'Every frontier assessment cites primary source DOI or spec version.',
    ),
    "privacy": (
        'Privacy limits collection, retention, and exposure of personal data in training, logs, and outputs. GDPR and similar laws define user rights.',
        'Support logs must redact credit card numbers; retention capped at 90 days.',
        'Run PII scanner on logs and outputs; zero high-severity findings before release.',
    ),
    "probability": (
        'Probability quantifies uncertainty over outcomes, enabling expectations, risk calculations, and principled decisions under incomplete information. ML outputs are almost always distributions, not certainties.',
        'A fraud scorer outputs P(fraud); finance uses that probability with loss asymmetries, not a raw boolean.',
        'Convert three model scores to expected cost given asymmetric false-positive and false-negative penalties.',
    ),
    "problem-framing": (
        'Problem framing defines the unit of prediction, target label, decision, population, and time boundary before choosing algorithms. Most ML failures are mis-specified problems, not wrong models.',
        "Predicting 'will this ticket reopen within 7 days' differs from 'summarize this ticket'—only the first is a measurable ML task.",
        'Write the prediction unit, label definition, and decision rule; verify each is observable in production logs.',
    ),
    "prompt-injection": (
        'Prompt injection embeds hostile instructions in untrusted content that models may follow instead of trusted policy.',
        "A retrieved page saying 'ignore previous instructions' can redirect a summarizer to exfiltrate secrets.",
        'Red-team with malicious retrieved text and verify external content is treated as data only.',
    ),
    "prompt-specs": (
        'Prompt specs version instructions, constraints, examples, and expected behaviors like API contracts. They enable review and regression unlike ad hoc prompts.',
        'Prompt spec defines abstention when confidence low and JSON schema for outputs.',
        'Diff prompt spec versions in CI and run regression eval on every change.',
    ),
    "prompt-versioning": (
        'Prompt versioning tracks template changes with IDs, authors, and diffs like code. Unversioned prompt edits cause silent regressions impossible to roll back.',
        'Prompt v2.3.1 changes abstention wording—eval must compare v2.3.0 versus v2.3.1 before deploy.',
        'Store prompt hash on every trace and correlate with quality metrics by version.',
    ),
    "prompting": (
        'Prompting steers model behavior at inference via instructions and examples without weight updates. It is the fastest iteration path when context fits.',
        "Adding 'cite sources' instruction improves citation rate without retraining.",
        'Compare prompt variants on behavioral eval with fixed model weights.',
    ),
    "provenance": (
        'Provenance for generated media records model, prompt, timestamp, and user for copyright and authenticity disputes.',
        'C2PA metadata embeds creation tool and prompt hash in exported campaign image.',
        'Verify provenance survives export format and is readable by audit tool.',
    ),
    "qlora": (
        'QLoRA combines quantization of base weights with LoRA adapters for fine-tuning on consumer GPUs.',
        'Fine-tune 13B on single 24GB card using 4-bit base plus LoRA adapters.',
        'Document quantization config and compare quality versus full-precision LoRA baseline.',
    ),
    "quantization": (
        'Quantization reduces weight precision—INT8, INT4—to cut memory and increase throughput with small quality trade-offs.',
        'AWQ 4-bit model runs 2× faster with <1 point eval drop on some tasks.',
        'Benchmark task metric and tokens/sec for FP16 versus INT4 on production hardware.',
    ),
    "queries": (
        'In attention, queries represent what information a position seeks from other positions. They are learned projections of hidden states, not user search queries.',
        'Each decoder token issues a query vector to attend over encoder keys during translation.',
        'Visualize query-key dot products and verify peak weights align with alignments.',
    ),
    "query-rewriting": (
        'Query rewriting transforms requests via expansion, decomposition, or HyDE before retrieval to close vocabulary gaps.',
        "Expanding 'PTO' to 'paid time off' helps lexical retrievers match handbook language.",
        'Compare recall@k with and without rewrite on acronym-heavy queries.',
    ),
    "queues": (
        'Queues decouple agent work submission from processing, smoothing load and enabling retries. Poison messages need dead-letter handling.',
        'Approval tasks queue while humans respond; workers poll with backoff.',
        'Measure queue depth p95 and time-to-drain under 2× normal submit rate.',
    ),
    "rag": (
        'Retrieval-augmented generation retrieves external evidence at query time and conditions generation on it.',
        'HR assistant retrieves current travel policy and refuses when no supporting document exists.',
        'Evaluate retrieval recall and answer faithfulness separately before end-to-end judgment.',
    ),
    "ranking": (
        'Ranking orders candidates—retrieved passages or context sections—by relevance, recency, or priority before the model sees them. Final order determines what fits in the token budget and what the model can cite.',
        'Reranking retrieved chunks by cross-encoder score beats vector order alone for policy QA.',
        'Compare nDCG@5 or answer faithfulness before and after reranking at equal token budget.',
    ),
    "rational-agents": (
        "Rational agents choose actions that maximize expected utility toward a goal given perceived state and known constraints. The design question is whether the system's action policy aligns with business utility, not model confidence.",
        'A lending assistant should prefer declining uncertain high-risk cases when false approvals cost more than false declines.',
        'Write the utility function and compare two candidate actions by expected cost, not by response fluency.',
    ),
    "re-indexing": (
        'Re-indexing rebuilds search indexes after embedding model or chunking changes. It is a data migration with downtime, cost, and quality validation requirements.',
        'Switching embedding models requires dual-running indexes until recall parity is proven.',
        'Compare recall@10 old versus new index on the same eval set before cutover.',
    ),
    "reasoning-models": (
        'Reasoning models allocate extra inference compute—long chains, self-checks—for math, code, and planning tasks. They trade latency and cost for accuracy on hard problems.',
        'A reasoning model may emit scratchpad steps before the final answer on a budget word problem.',
        'Measure accuracy and tokens used versus a base model on a reasoning benchmark.',
    ),
    "reciprocal-rank-fusion": (
        'Reciprocal rank fusion merges ranked lists by summing 1/(k + rank) per document across retrievers.',
        'A document ranked third lexically and second densely outscores a single-list winner.',
        'Fuse two hand-built rankings and verify the dual-high document gets top fused score.',
    ),
    "recovery": (
        'Recovery restores consistent state after crashes, tool failures, or partial commits. It requires durable checkpoints and compensating actions.',
        'After payment timeout, recovery verifies ledger state before retry or refund.',
        'Inject crash at each step and verify recovery reaches consistent terminal state.',
    ),
    "reflection": (
        'Reflection lets agents critique recent actions and adjust strategy—retry, replan, or escalate. Without reflection, loops repeat the same failing action.',
        'After tool 403, reflect and switch to read-only search instead of retrying delete.',
        'Count reflection-triggered strategy changes versus blind retries on failure injection suite.',
    ),
    "regression": (
        'Regression predicts continuous targets—latency, revenue, temperature—by minimizing loss over numeric outputs. Choice of loss (MSE, Huber) reflects outlier sensitivity in operations.',
        'Forecasting queue wait time uses regression; thresholds on predicted minutes trigger staffing alerts.',
        'Compare MAE and RMSE on a holdout set and inspect worst 5% errors for systematic bias.',
    ),
    "regression-evaluation": (
        'Regression evaluation re-runs fixed test suites after prompt or context changes to catch quality drops. It complements aggregate monitoring with known hard cases.',
        'A 30-case eval set includes injection attempts and acronym queries that must never regress.',
        'Block release if any P0 case fails or overall score drops more than two points.',
    ),
    "regularization": (
        'Regularization penalizes complexity—L2 weight decay, dropout, early stopping—to improve generalization. It trades training fit for deployment stability.',
        'Dropout on a small tabular network prevents memorizing 500 rows of customer data.',
        'Plot train versus validation loss with and without regularization and note the generalization gap.',
    ),
    "release-gates": (
        'Release gates block deployment until eval, security, and performance criteria pass. They encode organizational risk tolerance numerically.',
        'No deploy if faithfulness drops >2 points or p95 latency exceeds SLO.',
        'Automate gate checks in CI/CD with auditable pass/fail artifacts.',
    ),
    "repair": (
        'Repair loops attempt to fix invalid model outputs—re-prompting with errors, partial parsing, or constrained retries. They improve yield but add latency and cost.',
        'When JSON is malformed, a repair prompt includes the parse error and asks for correction.',
        'Track repair success rate and average extra tokens per successful repair.',
    ),
    "replanning": (
        'Replanning updates the action sequence when observations invalidate assumptions. Static plans fail in open environments with changing data.',
        "If inventory check shows zero stock, replan from 'ship item' to 'notify backorder'.",
        'Inject mid-run observation changes and measure replan latency and success rate.',
    ),
    "repo-instructions": (
        'Repo instructions—AGENTS.md, CONTRIBUTING—orient coding agents to build, test, and review conventions. They reduce wrong-file edits and skipped tests.',
        'Instructions specify pytest command, lint rules, and forbidden directories.',
        'Run agent on sample task and measure review comments tied to instruction violations.',
    ),
    "representation-learning": (
        'Representation learning discovers features automatically instead of hand-engineering them. Quality of representations determines retrieval, transfer, and sample efficiency.',
        'Sentence embeddings trained on internal docs outperform bag-of-words on paraphrase-heavy policy search.',
        'Evaluate embeddings on a retrieval benchmark with paraphrases and hard negatives.',
    ),
    "reproduction": (
        'Reproduction reruns experiments with disclosed details to verify claims before betting architecture on results.',
        "Reproduce reported recall gain within 2 points using authors' config or document differences.",
        'Publish internal reproduction note with confidence level and blocking gaps.',
    ),
    "rerankers": (
        'Rerankers rescore top-k candidates with cross-attention models more accurate than bi-encoders alone. They add latency proportional to candidates rescored.',
        'Cross-encoder reranking top-50 BM25 hits improves precision@5 for policy QA.',
        'Measure nDCG@5 and p95 latency with reranker on versus off at k=50.',
    ),
    "residual-connections": (
        'Residual connections add layer inputs to outputs, easing gradient flow through deep stacks. They let layers learn incremental refinements instead of full remappings.',
        'Transformer blocks compute attention(x) + x rather than attention(x) alone.',
        'Train depth-12 with and without residuals and compare convergence speed.',
    ),
    "resilience": (
        'Resilience designs for partial failure—retries, circuit breakers, multi-region—without total service loss.',
        'Circuit breaker stops calling failing embedding API after 50% errors, uses lexical only.',
        'Fault injection test: verify graceful degradation and recovery per runbook.',
    ),
    "resources": (
        'MCP resources expose readable data—files, records, configs—to clients with URI identifiers. Resource access must respect same authorization as APIs.',
        'resource://policy/2024 exposes the PDF bytes; listing must not leak unauthorized URIs.',
        'Enumerate resources as unprivileged user and confirm restricted URIs are absent.',
    ),
    "retries": (
        'Retries re-invoke models or tools after transient failures or validation misses, with backoff and limits. Unbounded retries cause runaway cost and duplicate side effects.',
        'Three retries with exponential backoff on 429 rate limits recover most requests without overload.',
        'Cap retries at N and measure success rate versus total token spend.',
    ),
    "retrieval": (
        'Retrieval selects candidate evidence from a corpus given a query before ranking and generation. It is candidate generation under relevance and policy constraints—not the final answer.',
        'Hybrid retrieval returns 20 chunks for reranking; generation never sees the full million-document index.',
        'Report recall@20 on a labeled query set before tuning downstream prompts.',
    ),
    "retrieval-metrics": (
        'Retrieval metrics—recall@k, MRR, nDCG—measure candidate set quality before generation sees it.',
        'High recall@20 with poor faithfulness suggests generation issue, not retrieval.',
        'Report recall@5, @10, @20 on fixed query set each index version.',
    ),
    "reviewer": (
        'Reviewer pattern inserts a critique pass before delivery or irreversible actions. Reviewers should use different prompts or models than generators.',
        'Draft email reviewed for PII leakage before send tool invocation.',
        'Measure defect catch rate with reviewer on versus off at equal total latency budget.',
    ),
    "risk-tiers": (
        'Risk tiers classify AI systems by potential harm—low, medium, high—driving eval depth, approval path, and monitoring.',
        'Internal summarization is tier 1; automated credit decision is tier 3 with full gate package.',
        'Assign tier per system; verify tier-3 systems have required controls before deploy.',
    ),
    "rnns": (
        'Recurrent neural networks process sequences step by step, maintaining hidden state across time. Serial computation limits parallel training and long-range credit assignment.',
        'Character-level RNN language models learn spelling but struggle with paragraph-level coherence.',
        'Measure training steps/sec versus transformer on the same sequence length.',
    ),
    "robotics-interfaces": (
        'Robotics interfaces connect AI planners to sensors and actuators with safety interlocks and real-time constraints.',
        'Warehouse robot API accepts move commands only within geofenced zones with E-stop.',
        'Simulate estop latency and command rejection outside safety envelope.',
    ),
    "roi": (
        'ROI compares value gained—time saved, revenue, deflected tickets—to total cost—build, inference, review, incidents.',
        'Saving 500 agent-hours/month at $40/hr must exceed inference plus maintenance cost.',
        'Document ROI calculation assumptions and revisit quarterly with actuals.',
    ),
    "role-isolation": (
        'Role isolation restricts each agent to tools and data matching its role, limiting blast radius of compromise or error.',
        'Billing agent cannot access HR records even if prompt requests it.',
        'Attempt cross-role tool access in tests and expect hard denial.',
    ),
    "roles": (
        'Roles—system, user, assistant, tool—label message provenance and expected behavior in chat APIs. Misassigned roles confuse models about who said what.',
        'Putting user text in the system role can unintentionally elevate it to trusted policy.',
        'Swap roles on ten prompts and measure compliance change on a fixed eval set.',
    ),
    "routing": (
        'Routing directs requests to models, tools, or strategies by task type, risk, or budget. Routers encode product policy about cheap versus capable paths.',
        'Simple FAQs route to small model; compliance questions route to audited large model.',
        'Log routing decisions and compare quality and cost versus always-large baseline.',
    ),
    "rubrics": (
        'Rubrics score qualitative outputs against anchored criteria with examples at each level. They enable consistent human and LLM judging.',
        'Support reply rubric scores correctness, completeness, tone, citations on 1–4 scale.',
        "Calibrate two raters on 20 cases; report Cohen's kappa ≥ target before solo grading.",
    ),
    "sagemaker": (
        'Amazon SageMaker covers ML training, tuning, hosting, and monitoring for custom and foundation models on AWS.',
        'Fine-tune and deploy custom classifier on SageMaker endpoint with autoscaling and Model Monitor.',
        'Document training job config hash linked to endpoint version in registry.',
    ),
    "sampling": (
        'Sampling draws next tokens from the predicted distribution rather than always taking the argmax. It enables diverse outputs but introduces nondeterminism unless seeded.',
        'Creative writing uses sampling; factual extraction often uses greedy or low-temperature decoding.',
        'Generate 20 completions at temperature 0 versus 1 and measure factual consistency.',
    ),
    "sandboxing": (
        'Sandboxing isolates code execution, browsing, or file access in restricted environments with network and filesystem limits.',
        'Python tool runs in container without egress except allowlisted APIs.',
        'Attempt filesystem and network escapes in sandbox test suite monthly.',
    ),
    "scaled-dot-product": (
        'Scaled dot-product attention computes softmax(QKᵀ/√d)V, scaling dot products to stable gradients. It is the core operation inside transformer blocks.',
        'Without scaling, large dimensions push softmax into near one-hot distributions and vanishing gradients.',
        'Implement attention and verify gradient norms remain stable with versus without √d scaling.',
    ),
    "scaling-laws": (
        'Scaling laws relate model size, data, and compute to predictable loss improvements—guiding budget allocation. They are approximate and domain-dependent.',
        'Doubling parameters may yield diminishing returns if data quality does not scale similarly.',
        'Fit a loss-versus-compute curve on three model sizes and extrapolate budget for target loss.',
    ),
    "search": (
        'Search explores a space of partial solutions—plans, code candidates, tool sequences—guided by heuristics and budgets. Inference-time search trades compute for accuracy.',
        'Tree-of-thought explores multiple math solution paths before committing to an answer.',
        'Plot accuracy versus number of nodes expanded with a fixed timeout.',
    ),
    "segmentation": (
        'Segmentation splits text into sentences, paragraphs, or utterances for processing pipelines. Wrong boundaries merge unrelated content or split entities across chunks.',
        'Legal documents need section-aware segmentation so clauses are not cut mid-sentence.',
        'Measure boundary error rate on 50 manually segmented pages including tables and lists.',
    ),
    "self-consistency": (
        'Self-consistency samples multiple reasoning paths and aggregates answers by majority vote. It improves reliability when individual samples are noisy.',
        "Five chain-of-thought samples that agree on '42' outweigh one outlier '41'.",
        'Compare accuracy of majority vote versus single sample at equal total token budget.',
    ),
    "self-supervision": (
        'Self-supervision creates training signal from the data itself—mask prediction, contrastive pairs—without manual labels. It scales representation learning to massive unlabeled corpora.',
        'BERT-style masked language modeling learns syntax and semantics from raw text before task fine-tuning.',
        'Pretrain on domain corpus and compare downstream task accuracy versus training from scratch.',
    ),
    "semantics": (
        'Semantics concerns meaning—entities, relations, entailment—not just form. Systems must map language to intended referents and propositions, especially under ambiguity.',
        "'Bank' as financial institution versus river edge changes retrieval targets entirely.",
        'Build ten minimal pairs differing by one word and verify the system assigns different meanings.',
    ),
    "sentence-embeddings": (
        'Sentence embeddings encode whole utterances into vectors for semantic search and clustering. Quality depends on training objective and domain match.',
        'Embedding employee questions matches handbook paraphrases even without shared keywords.',
        'Benchmark recall@5 on paraphrase pairs with hard negative passages in the index.',
    ),
    "sentencepiece": (
        'SentencePiece trains subword models directly on raw text without pre-tokenization, simplifying multilingual pipelines. It supports unigram and BPE objectives with shared vocabularies.',
        'One SentencePiece model covers Japanese and English in a single vocabulary for multilingual search.',
        'Compare segmentation consistency across languages on parallel sentences.',
    ),
    "seq2seq": (
        'Sequence-to-sequence models map input sequences to output sequences via encoder–decoder architectures. They underpin translation, summarization, and tool-output generation patterns.',
        'An encoder compresses ticket text; a decoder generates structured JSON fields.',
        'Evaluate BLEU or field-level F1 on a held-out seq2seq task with beam search.',
    ),
    "service-catalog": (
        'Service catalog lists internal AI products—approved models, RAG templates, tools—for self-service discovery.',
        'Developer portal shows tier-2 chatbot template with cost estimate and onboarding steps.',
        'Track catalog entry usage and time from discovery to first successful API call.',
    ),
    "session-memory": (
        'Session memory persists within a conversation—recent turns, pending clarifications—without long-term storage. TTL and summarization policies prevent unbounded growth.',
        "Remembering the user's chosen account ID this session avoids re-asking on every message.",
        'Measure token growth over 20-turn dialogues with and without rolling summarization.',
    ),
    "sft": (
        'Supervised fine-tuning trains on input–output pairs to imitate desired behaviors on similar tasks.',
        'SFT on 5k support replies teaches consistent empathy and escalation triggers.',
        'Compare SFT model to base plus prompt on held-out behavioral eval.',
    ),
    "shared-retrieval": (
        'Shared retrieval services provide governed indexes, embedding pipelines, and search APIs reused across products.',
        'Enterprise policy index serves HR bot and IT bot with tenant filters from one platform team.',
        'Measure index freshness SLA and per-tenant isolation in platform tests.',
    ),
    "shared-state": (
        'Shared state stores variables visible to multiple agents—task boards, evidence pools. Consistency requires versioning or transactional updates.',
        'Research evidence store accumulates URLs all workers cite; stale entries need TTL.',
        'Verify concurrent writes do not lose updates using version counters or locks.',
    ),
    "skills": (
        'Skills package reusable agent capabilities—prompts, scripts, checklists—for specific tasks in Cursor and similar tools. They encode institutional workflow knowledge.',
        "A 'create PR' skill runs tests, drafts description template, and calls gh CLI.",
        'Compare task success rate with skill versus generic agent on three repo tasks.',
    ),
    "slice-analysis": (
        'Slice analysis evaluates metrics on subpopulations—language, product, tenant—to catch aggregate illusions. A model can pass overall while failing high-value segments.',
        '95% accuracy overall can hide 60% on enterprise accounts or non-English queries.',
        'Define three production-representative slices and require each meets its release threshold.',
    ),
    "slices": (
        'Slices are subpopulations—language, tenant, risk tier—where aggregate metrics may hide failure.',
        '95% overall accuracy can mask 60% on enterprise accounts.',
        'Report metrics on three production slices with separate release thresholds.',
    ),
    "slos": (
        'SLOs define target reliability and latency—availability, p95 latency, eval faithfulness—for AI platform services.',
        'Gateway SLO: 99.9% availability, p95 <2s excluding model provider outages.',
        'Error budget policy triggers feature freeze when SLO burn exceeds threshold.',
    ),
    "speech-recognition": (
        'Speech recognition (ASR) transcribes audio to text with word error rate varying by accent, noise, and domain.',
        'Call center ASR feeds ticket summary pipeline with custom vocabulary for product names.',
        'Report WER on held-out audio including noisy and accented slices.',
    ),
    "state": (
        'State captures variables the system believes true at a point in execution—inventory, user intent, pending approvals. Explicit state enables recovery and verification.',
        'Agent state tracks current_step, artifacts_created, and budget_remaining across turns.',
        'Serialize and deserialize state; resume mid-run and verify identical next action.',
    ),
    "state-machines": (
        'State machines model allowed statuses and transitions explicitly, making illegal steps unrepresentable. They clarify where agents pause, resume, or terminate.',
        'Ticket automation states: open → pending_approval → resolved with defined transition triggers.',
        'Draw state diagram and verify code rejects all undefined transitions in tests.',
    ),
    "state-spaces": (
        'A state space enumerates all configurations a system can occupy plus the actions that move between them. Explicit state models make search, planning, and verification tractable.',
        'Warehouse robots represent position and load status as state; illegal moves (overweight pickup) are edges you never traverse.',
        'List states, actions, and goal conditions for one task and confirm every action has a defined transition.',
    ),
    "statistical-learning": (
        'Statistical learning infers patterns from data with explicit assumptions about noise, independence, and generalization. It replaced brittle hand rules where variability and scale made manual encoding impractical.',
        'Spam filtering learned from labeled inboxes outperforms keyword lists when attackers vary phrasing continuously.',
        'Report train versus validation error and show the simplest model that meets the decision threshold.',
    ),
    "streaming-audio": (
        'Streaming audio processes speech incrementally for real-time captions and voice agents.',
        'Live meeting captions display partial hypotheses updated as speaker continues.',
        'Measure caption delay from speech to stable text on streaming benchmark.',
    ),
    "structured-data": (
        'Structured data lives in tables, APIs, and graphs with typed fields—better for precise queries than prose retrieval. Hybrid systems route quantitative questions to SQL, not RAG alone.',
        "'How many open P1 incidents?' needs a database query, not semantic search over runbooks.",
        'Route ten numeric questions to structured tools and verify answers match ground truth.',
    ),
    "structured-output": (
        'Structured output forces models to emit machine-parseable formats—JSON, XML, tool calls—via prompting or constrained decoding. Parsers must still validate because models can violate schema.',
        'An invoice extractor returns JSON fields consumed directly by ERP ingestion.',
        'Measure schema pass rate on 200 adversarial and normal inputs post-generation.',
    ),
    "subwords": (
        'Subword units split rare words into frequent pieces so models handle morphology and typos without huge vocabularies. Splitting affects cost, semantics, and cross-lingual behavior.',
        "'unhappiness' may become ['un', 'happiness'] preserving morphemes better than character splits.",
        'Compare token counts for 100 product names under word versus BPE tokenizers.',
    ),
    "success-metrics": (
        'Success metrics tie releases to user-valued outcomes—task success, time saved, revenue—not model perplexity alone.',
        'Deflect 20% of L1 tickets without increasing reopen rate defines success for support bot.',
        'Pre-register primary and guardrail metrics before launch with target deltas.',
    ),
    "summarization": (
        'Summarization compresses dialogue or documents into shorter forms for memory or display. Summaries lose detail; critical constraints may need structured extraction instead.',
        'Rolling summaries of support chats preserve issue status but may drop exact error codes.',
        'Compare task success using full transcript versus summary after 30 turns.',
    ),
    "supervisor-worker": (
        'Supervisor–worker assigns subtasks to workers and integrates results, adding coordination overhead for parallelizable work.',
        'Supervisor delegates research subtopics to three workers, then merges citations.',
        'Compare wall time and error rate versus single agent with sequential tool calls.',
    ),
    "symbolic-ai": (
        'Symbolic AI represents knowledge as explicit rules, facts, and logical relations rather than learned weights. It remains valuable when constraints are crisp, auditable, and change infrequently.',
        'A tax-credit eligibility checker can encode statutory thresholds as rules that always produce the same answer for the same inputs.',
        'Compare rule coverage against a held-out set of edge cases and report precision on legally ambiguous scenarios.',
    ),
    "syntax": (
        'Syntax governs how words combine into grammatical structures—phrases, clauses, dependencies. Parsers and models exploit syntactic patterns but fluent text can violate syntax without humans noticing.',
        'Dependency parsing links verbs to subjects, helping extract who did what in contract clauses.',
        'Compare parser accuracy on ten hand-annotated sentences including passive voice and coordination.',
    ),
    "synthetic-data": (
        'Synthetic data generates training examples via models or rules—useful when real data is scarce but risks model collapse if overused.',
        'GPT generates varied phrasings of intent labels to augment small classifier set.',
        'Compare fine-tune with synthetic augmentation versus real-only on held-out real eval.',
    ),
    "task-definitions": (
        'Task definitions specify input, expected output, constraints, and graders for eval cases. Vague tasks produce noisy, incomparable metrics.',
        "'Summarize ticket' becomes 'Extract product, issue, sentiment JSON matching schema X'.",
        'Peer-review ten task definitions for ambiguity before adding to gold set.',
    ),
    "task-success": (
        'Task success measures whether users completed their intended job with acceptable quality—not click-through on AI features.',
        'User submitted correct expense report without support contact counts as success.',
        'Define success per job; sample sessions and label pass/fail weekly.',
    ),
    "team-topology": (
        'Team topology assigns platform, product, and enabling teams for AI delivery with clear interaction modes.',
        'Platform team owns gateway; product teams own prompts and evals within guardrails.',
        'RACI matrix covers model approve, incident on-call, and data ingest ownership.',
    ),
    "technology-forecasting": (
        'Technology forecasting estimates when emerging capabilities become production-ready using evidence tiers and uncertainty bounds.',
        'Estimate computer-use reliability for your UI stack as low/med/high with dated reassessment.',
        'Quarterly frontier review updates confidence levels with new reproductions, not headlines.',
    ),
    "temperature": (
        'Temperature scales logits before softmax—lower sharpens the distribution (more deterministic), higher flattens it (more random). It is a primary creativity-versus-consistency knob.',
        'Temperature 0.2 keeps support answers stable; 1.2 increases phrasing variety for marketing copy.',
        'Plot entropy of next-token distribution versus temperature on a fixed prompt set.',
    ),
    "termination": (
        'Termination criteria stop search, agent loops, or generation when goals are met, budgets exhausted, or progress stalls. Without them, systems loop indefinitely.',
        'Stop after five tool calls, success, or three consecutive no-progress iterations.',
        'Verify 100% of test runs halt within max_steps and document stop reason distribution.',
    ),
    "test-time-adaptation": (
        'Test-time adaptation updates model behavior during inference from recent inputs—risky for stability without guardrails.',
        "Adapter adjusts to user's jargon mid-session if enabled with rollback.",
        'Compare adaptation on versus off for target slice with regression suite unchanged.',
    ),
    "test-time-compute": (
        'Test-time compute spends extra inference—search, sampling, verification—at query time to improve accuracy. It trades latency and cost for quality on hard inputs.',
        'Spending 5× tokens on best-of-N may be worth it for $10k loan decisions only.',
        'Plot quality versus total tokens and mark Pareto-optimal operating points.',
    ),
    "tests": (
        'Tests provide executable specifications for tools, plans, and outputs in reasoning pipelines. They turn vague correctness into pass/fail signals.',
        'A migration plan test asserts rollback step exists before destructive changes.',
        'Run test suite on every candidate plan and require 100% pass before execution.',
    ),
    "text-to-speech": (
        'Text-to-speech synthesizes natural audio from text with voice, prosody, and latency trade-offs.',
        'IVR reads dynamic account balance with consistent brand voice under 500ms first byte.',
        'MOS evaluation and latency p95 on 50 test phrases monthly.',
    ),
    "tf-idf": (
        'TF–IDF weights terms by local frequency and inverse document frequency, highlighting discriminative words in sparse retrieval. It is a strong lexical baseline before dense methods.',
        "Searching 'PTO accrual cap' ranks handbook sections containing rare terms 'accrual' and 'cap' highly.",
        'Measure recall@10 on 30 keyword-heavy queries against a dense baseline.',
    ),
    "threat-modeling": (
        'Threat modeling systematically identifies assets, adversaries, and attack paths for AI systems—STRIDE, attack trees adapted for LLM risks.',
        'Diagram data flow from user → retrieval → model → tools noting untrusted inputs.',
        'Produce threat model doc with mitigations mapped to each high-severity threat.',
    ),
    "thresholds": (
        'Thresholds are minimum acceptable metric values for release or routing decisions. They encode risk appetite numerically.',
        'Faithfulness ≥ 0.92 and P0 safety 100% required for production promotion.',
        'Document threshold rationale and review quarterly with incident data.',
    ),
    "timeouts": (
        'Timeouts cap how long tools or model calls may run before cancellation. They prevent hung workflows from blocking resources indefinitely.',
        'A 30-second web search timeout returns partial results instead of freezing the agent.',
        'Inject slow tool responses and verify cancellation within configured timeout ± slack.',
    ),
    "token-budgeting": (
        'Token budgeting allocates fixed slices of the context window to system, history, evidence, and completion. Explicit budgets prevent silent truncation of critical sections.',
        'Reserving 500 tokens for output ensures answers are not cut mid-sentence when evidence fills the window.',
        'Log per-section token usage and alert when system prompt exceeds 10% of window.',
    ),
    "token-budgets": (
        'Token budgets cap how many tokens each prompt section—system, evidence, user—may consume. Hard budgets prevent silent truncation of safety instructions.',
        'Allocating 2k tokens to evidence and 500 to instructions ensures policy text survives long retrievals.',
        'Log token counts per section and alert when any section exceeds its budget before send.',
    ),
    "tool-abuse": (
        'Tool abuse exploits excessive permissions—delete, send email, SQL write—through manipulated agent behavior.',
        'Agent tricked into mass email via send_campaign tool with broad scope.',
        'Apply least privilege per tool; fuzz adversarial prompts expecting zero abusive executions.',
    ),
    "tool-contracts": (
        'Tool contracts specify schemas, auth, idempotency, errors, and SLAs for each agent tool. They are integration boundaries models depend on.',
        'search_docs contract promises p95 500ms, max 10 results, ReadScope auth.',
        'Contract tests mock failures and verify agent handles each error code.',
    ),
    "tool-discovery": (
        'Tool discovery lets clients list available tools and schemas at runtime instead of hardcoding integrations. Discovery responses must be filtered by permission.',
        'A client sees only search_docs, not admin_delete, when connected with read-only scope.',
        'Compare discovered tool list across role configurations in automated tests.',
    ),
    "tool-registry": (
        'Tool registry catalogs approved agent tools with schemas, owners, and security review status.',
        'Registry entry for create_jira_ticket includes schema v2 and pentest date.',
        'Agents may only bind tools present in registry with current approval.',
    ),
    "tool-schemas": (
        'Tool schemas define parameter names, types, required fields, and descriptions models use to construct calls. Ambiguous schemas cause systematic argument errors.',
        "date_iso string format in schema prevents models passing 'next Tuesday' unparseably.",
        'Measure argument validation failure rate per tool after schema revision.',
    ),
    "tool-success": (
        'Tool success rate tracks correct schema, auth, execution, and useful results from tool calls. It isolates integration failures from model reasoning.',
        '60% tool success with high answer quality still blocks reliable agents.',
        'Log tool error taxonomy—validation, timeout, 403—and set minimum success rate gate.',
    ),
    "tracing": (
        'Tracing records spans for retrieval, model calls, tools, and validation with correlation IDs across services.',
        'OpenTelemetry trace shows 400ms in reranker, 1.2s in LLM for slow request diagnosis.',
        'Sample traces link 100% of P0 incidents to span breakdown within five minutes.',
    ),
    "training": (
        'Training fits model parameters to data by minimizing a loss over many examples. It defines what behavior the model is rewarded for and must be separated from inference in operations.',
        'Fine-tuning a classifier on support tickets teaches phrasing patterns that inference-time prompts alone may not stabilize.',
        'Log training loss, validation loss, and one task metric per epoch and stop when validation degrades.',
    ),
    "transparency": (
        'Transparency discloses when users interact with AI, what data is used, and system limitations. It supports informed consent and trust.',
        'Chat banner states AI-generated; citations show source documents.',
        'Audit UX copy and logs for required disclosures per policy checklist.',
    ),
    "transports": (
        'MCP transports—stdio, SSE, HTTP—carry protocol messages between clients and servers. Choice affects latency, deployment, and security boundaries.',
        'Stdio suits local IDE agents; SSE suits remote servers behind auth proxies.',
        'Measure round-trip latency for tool call over each transport in your deployment.',
    ),
    "uncertainty-ux": (
        'Uncertainty UX communicates confidence, limits, and alternatives so users calibrate trust. Hiding uncertainty causes overreliance on wrong answers.',
        "Show 'I'm not sure—here are sources' instead of definitive tone on weak retrieval.",
        'User study: measure appropriate reliance rate with versus without confidence cues.',
    ),
    "undo": (
        'Undo reverses AI-initiated or AI-assisted actions within a safe window. It is essential when actions affect user data or send communications.',
        'Auto-drafted email can be undone for 30 seconds before SMTP send.',
        'Verify undo restores prior state exactly on ten action types.',
    ),
    "unicode": (
        'Unicode assigns code points to characters across scripts; mishandling causes mojibake, broken tokens, and security bypasses via homoglyphs.',
        'Normalizing NFC versus NFD changes string equality for accented characters in user names.',
        'Run ingestion on ten multilingual samples and verify round-trip display matches source glyphs.',
    ),
    "unit-tests": (
        'Unit tests verify deterministic functions and components in isolation with fast feedback. They anchor quality while model behavior stays statistical.',
        'Parser unit tests cover edge cases agents might not consider when editing.',
        'Require ≥80% coverage on changed deterministic modules per PR policy.',
    ),
    "user-research": (
        'User research observes real workflows, pain points, and workarounds before proposing AI features. It prevents building impressive demos nobody needs.',
        'Watching support agents copy-paste from three systems reveals integration beats summarization.',
        'Document five observed user sessions and map pains to non-AI and AI options.',
    ),
    "validation": (
        'Validation checks model outputs against schemas, business rules, and safety policies before downstream use. It belongs in application code, not trust in model compliance.',
        'A date field must parse as ISO-8601 and fall within contract term bounds.',
        'Define ten validation rules and report pass rate on production sample weekly.',
    ),
    "values": (
        "Values carry the content aggregated by attention weights—what actually flows between positions. Weighted sums of values update each position's representation.",
        "Attending to a verb's value brings predicate information into the subject's representation.",
        'Compare hidden states with and without value projection on a toy attention module.',
    ),
    "vector-governance": (
        'Vector governance covers access control, versioning, retention, and audit for embedding stores and indexes. Vectors can leak semantic content of restricted documents if misconfigured.',
        "Tenant-isolated namespaces prevent one customer's embeddings appearing in another's search results.",
        'Attempt cross-tenant retrieval in tests and verify zero unauthorized hits.',
    ),
    "vectors": (
        'Vectors represent objects as numeric arrays so similarity, direction, and composition become computable. They underpin embeddings, attention, and most modern ML pipelines.',
        'Representing users and items as vectors lets recommendation score candidates with a dot product in milliseconds.',
        'Compute dot products for three pairs and verify ordering matches your semantic expectations.',
    ),
    "vendor-management": (
        'Vendor management evaluates AI providers on security, compliance, cost, performance, and exit strategy.',
        'Annual review of OpenAI/Azure/Bedrock DPAs, data retention, and failover plan.',
        'Maintain vendor scorecard with exit migration test date documented.',
    ),
    "verifiers": (
        'Verifiers check candidate outputs with independent logic—unit tests, schemas, calculators—not the same model that generated them.',
        'A Python assert verifies JSON plan steps include all required migration phases.',
        'Report verifier catch rate on intentionally corrupted candidate outputs.',
    ),
    "versioning": (
        'Versioning tracks prompts, models, indexes, and eval suites so changes are attributable and reversible.',
        'Prod trace includes prompt v3.1, model llama-3-8b-q4, index 2024-06-01.',
        'Rollback drill: revert one version dimension and restore prior metric within one hour.',
    ),
    "vertex-ai": (
        'Google Vertex AI offers unified model training, tuning, deployment, and evaluation on GCP with Gemini and open models.',
        'Fine-tune Gemini on proprietary data and deploy to private endpoint with VPC-SC.',
        'Compare Vertex eval pipeline scores pre/post deploy on held-out set.',
    ),
    "vertex-ai-search": (
        'Vertex AI Search (Discovery Engine) provides enterprise search and grounding APIs with document ingest and ranking.',
        'Ingest GCS policy PDFs; grounding API returns answers with source references.',
        'Measure grounding citation accuracy versus self-built OpenSearch RAG baseline.',
    ),
    "video-generation": (
        'Video generation extends image models temporally—short clips from text with consistency and motion challenges.',
        'Generate 5s product demo clip from storyboard prompts for social ads.',
        'Evaluate temporal flicker, object consistency, and brand safety on rubric.',
    ),
    "vision-encoders": (
        'Vision encoders map images to embeddings or tokens for multimodal models—ViT, CLIP-style architectures.',
        'Chart screenshot encoded to tokens fused with text question about Q3 revenue trend.',
        'Compare OCR-plus-text baseline versus vision encoder on chart QA accuracy.',
    ),
    "visual-grounding": (
        'Visual grounding links language to regions or objects in images—pointing, bounding boxes, UI elements.',
        "Model clicks 'Submit' button coordinates in screenshot for computer-use agent.",
        'Measure grounding accuracy IoU on labeled UI element dataset.',
    ),
    "vllm": (
        'vLLM is a high-throughput inference server using PagedAttention for efficient KV cache memory management.',
        'vLLM serves Llama-8B at higher concurrent requests than naive HuggingFace pipeline.',
        'Load-test vLLM versus baseline server at equal hardware; report throughput and p95 latency.',
    ),
    "vocabulary": (
        'Vocabulary is the set of tokens a model or index recognizes; out-of-vocabulary items become unknown or split subwords. Size trades coverage against memory and sparsity.',
        'A 32k BPE vocabulary handles common English and code fragments but may fragment rare product SKUs.',
        'Measure OOV rate on production queries and track how subword splits affect identifier retrieval.',
    ),
    "voice-safety": (
        'Voice safety covers consent, voice cloning abuse, deepfake detection, and secure storage of biometric voice data.',
        'Require explicit opt-in before cloning executive voice for IVR.',
        'Red-team voice clone misuse scenarios; verify detection or block triggers.',
    ),
    "word-embeddings": (
        'Word embeddings map tokens to dense vectors where semantic similarity corresponds to geometric proximity. They enable arithmetic analogies and feed neural NLP stacks.',
        "'King' − 'man' + 'woman' ≈ 'queen' in classic Word2Vec demonstrations of linear structure.",
        'Evaluate nearest neighbors for 20 domain terms and have experts rate relevance.',
    ),
    "workflows": (
        'Workflows are deterministic orchestrations with predefined steps, branches, and error handlers. They excel when paths are known and compliance requires repeatability.',
        'Invoice approval always follows submit → manager → finance with explicit gates.',
        'Measure success rate and change failure rate versus agent on identical structured tasks.',
    ),
    "working-memory": (
        'Working memory holds transient state for the current turn—scratchpad notes, intermediate calculations—not durable across sessions. It clears when the task completes.',
        'A calculator agent keeps running totals in working memory while parsing a multi-step word problem.',
        'Verify working memory resets between unrelated tasks in the same session.',
    ),
    "world-models": (
        'World models learn predictive representations of environments for planning or simulation—active research area with engineering gaps.',
        'Game agent predicts next frame state to plan moves without full environment queries.',
        'Benchmark predicted versus actual state error on controlled simulation suite.',
    ),
}


def get_topic_entry(topic: str) -> tuple[str, str, str]:
    """Return (explanation, example, evidence) for a catalog topic.

    Each field is 2-4 sentences of substantive, topic-specific content.
    """
    key = normalize(topic)
    try:
        return TOPIC_FACTS[key]
    except KeyError as exc:
        raise KeyError(f"Unknown topic: {topic!r} (normalized: {key!r})") from exc

