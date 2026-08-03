"""Generate the guided AIEBOK books from a reviewed curriculum catalog.

The generated Markdown is committed to the repository so deployment never
depends on this script. Edit the catalog, rerun, review the diff, then build.
"""
from pathlib import Path
import re

from chapter_enrichments import (
    architecture_lens,
    engineering_practice,
    evolution_lens,
    failure_clinic,
    learning_objectives,
    mastery_exemplars,
    render_chapter_hook,
    render_knowledge_check,
    render_worked_example,
)
from concept_library import render_core_concepts

ROOT = Path(__file__).resolve().parents[1]
BOOKS_DIR = ROOT / "docs" / "books"


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


BOOKS = [
    {
        "title": "Foundations of Intelligence",
        "goal": "Understand intelligence as search, learning, representation, decision-making, and feedback before studying language models.",
        "project": "Build and compare a rule-based solver, a search-based solver, and a learned predictor for one bounded problem.",
        "chapters": [
            ("What Intelligence Means", "Treat intelligence as a collection of capabilities rather than a mystical substance. Separate perception, representation, memory, learning, reasoning, planning, action, and adaptation.", ["goal-directed behavior", "rational agents", "bounded rationality", "capability decomposition", "feedback"], "Create a capability map for a familiar human task.", "Intelligence is system behavior under goals and constraints, not a property inferred from fluent language."),
            ("From Symbols to Statistics", "Trace the path from symbolic rules and expert systems to statistical learning, deep learning, foundation models, and agents. Each era solved different problems and retained useful ideas.", ["symbolic AI", "expert systems", "knowledge representation", "statistical learning", "deep learning"], "Implement a tiny rule engine and document where it becomes brittle.", "New paradigms usually absorb rather than erase earlier engineering techniques."),
            ("Search, Planning, and Decisions", "See classical search as an explicit form of reasoning. Learn how state, actions, transition models, costs, heuristics, and stopping rules turn a vague goal into an algorithm.", ["state spaces", "breadth-first search", "A*", "heuristics", "planning"], "Implement breadth-first search and A* on the same maze.", "Reasoning can be viewed as controlled search over possible states or candidate solutions."),
            ("The Mathematics Engineers Need", "Develop intuition for vectors, matrices, probability, distributions, statistics, entropy, gradients, and optimization without turning the book into a mathematics degree.", ["vectors", "matrix transformations", "probability", "entropy", "gradient descent"], "Compute dot products, cosine similarity, softmax, and one gradient update by hand.", "Mathematics is a compact language for relationships, uncertainty, and change."),
            ("Learning and Generalization", "Distinguish memorization from generalization and training from inference. Understand data-generating processes, inductive bias, overfitting, underfitting, and distribution shift.", ["training", "inference", "generalization", "bias and variance", "distribution shift"], "Fit increasingly flexible models to a small noisy dataset and plot errors.", "A system is useful when it performs under future conditions, not merely on its training examples."),
            ("Engineering with Uncertainty", "Translate uncertain predictions into decisions with thresholds, costs, calibration, fallback behavior, and human oversight.", ["calibration", "decision thresholds", "expected cost", "abstention", "human review"], "Design a decision policy for a high-cost false-positive scenario.", "Prediction and decision are separate layers; consequences belong in the decision layer."),
        ],
    },
    {
        "title": "Machine Learning Systems",
        "goal": "Learn how models are trained, validated, diagnosed, and integrated into reliable software systems.",
        "project": "Deliver a prediction service with a data card, baseline, evaluation report, error analysis, and monitoring plan.",
        "chapters": [
            ("Problems, Data, and Baselines", "Frame an ML task before choosing an algorithm. Define the unit of prediction, target, decision, population, time boundary, data availability, and a simple baseline.", ["problem framing", "features and labels", "sampling", "data leakage", "baselines"], "Create a dataset split that respects time and entity boundaries.", "Most model failures begin as problem or data-definition failures."),
            ("Supervised Learning", "Understand regression and classification as function approximation under a chosen loss. Connect linear models, trees, and neural networks through their assumptions.", ["regression", "classification", "loss functions", "regularization", "optimization"], "Implement linear and logistic regression before using a library.", "The best model is the simplest one that meets the real decision requirement."),
            ("Unsupervised and Representation Learning", "Use unlabeled data to discover structure, compress observations, and learn reusable representations.", ["clustering", "dimensionality reduction", "autoencoders", "self-supervision", "representation learning"], "Cluster a dataset, visualize it, and explain why clusters are not automatically meaningful categories.", "Structure found by an algorithm is a hypothesis to validate, not a fact."),
            ("Neural Networks", "Build the mental model of layers, activations, losses, backpropagation, initialization, normalization, and optimization.", ["neurons and layers", "activations", "backpropagation", "normalization", "optimizers"], "Train a small network and inspect gradients and learning curves.", "Neural networks learn compositions of transformations; training adjusts those transformations to reduce loss."),
            ("Evaluation and Error Analysis", "Choose metrics from the decision context, estimate uncertainty, inspect slices, and turn mistakes into the next experiment.", ["confusion matrix", "precision and recall", "calibration", "cross-validation", "slice analysis"], "Write an error taxonomy and compare two models with confidence intervals.", "An aggregate metric can hide the exact population where a system is unsafe or useless."),
            ("The ML Lifecycle", "Connect data, experiments, models, releases, monitoring, drift, retraining, and retirement into an accountable lifecycle.", ["experiment tracking", "model registry", "data validation", "drift", "monitoring"], "Write a release checklist and a rollback plan for a prediction service.", "A trained model is an artifact; value and risk emerge from its full operating system."),
        ],
    },
    {
        "title": "Language and Representation",
        "goal": "Understand how language becomes computable representations and why embeddings enable semantic systems.",
        "project": "Build and evaluate a multilingual semantic search engine with lexical and vector baselines.",
        "chapters": [
            ("Why Language Is Hard", "Explore ambiguity, reference, syntax, semantics, pragmatics, intent, and the dependence of meaning on context and shared knowledge.", ["syntax", "semantics", "pragmatics", "ambiguity", "discourse"], "Annotate ten ambiguous requests with possible interpretations and missing context.", "Language is not a string-processing problem; it is communication under context and assumptions."),
            ("Corpora and Text Pipelines", "Learn how collection, encoding, normalization, language detection, segmentation, privacy, and provenance shape every downstream model.", ["Unicode", "normalization", "corpora", "segmentation", "data provenance"], "Build a normalization pipeline and test it on multilingual and adversarial text.", "Representation quality cannot recover information destroyed during ingestion."),
            ("Tokenization", "Understand character, word, and subword tokenization; BPE, WordPiece, and SentencePiece; and the impact on cost, latency, languages, and code.", ["vocabulary", "subwords", "BPE", "SentencePiece", "token budgets"], "Write a toy byte-pair tokenizer and compare segmentations.", "Tokenization is an engineering boundary that determines what units the model can efficiently process."),
            ("From Sparse Features to Embeddings", "Move from one-hot vectors, n-grams, TF–IDF, and BM25 to learned dense representations.", ["one-hot vectors", "TF–IDF", "BM25", "word embeddings", "sentence embeddings"], "Implement TF–IDF and compare it with the included vector lab.", "Different representations preserve different relationships; no representation is universally best."),
            ("Similarity and Vector Search", "Connect distance metrics, normalization, nearest neighbors, approximate indexes, clustering, filtering, and ranking.", ["dot product", "cosine similarity", "nearest neighbors", "ANN indexes", "metadata filtering"], "Run the cosine and semantic-search labs, then add hybrid scoring.", "Retrieval quality depends on representation, metric, index, filters, and query—not the database brand."),
            ("Embedding Systems in Production", "Select and evaluate embedding models, manage versions and re-indexing, protect tenant boundaries, and monitor drift.", ["embedding evaluation", "multilingual models", "hard negatives", "re-indexing", "vector governance"], "Create a retrieval evaluation set with realistic queries and hard negatives.", "Embedding changes are data migrations with quality, compatibility, and operational consequences."),
        ],
    },
    {
        "title": "Transformers and Foundation Models",
        "goal": "Understand the architecture, training, inference, and model families behind modern generative AI.",
        "project": "Implement a tiny transformer and create a vendor-neutral model selection report.",
        "chapters": [
            ("Sequence Models Before Transformers", "Understand n-grams, recurrent networks, LSTMs, encoder–decoder models, bottlenecks, and why long-range dependencies and serial computation were difficult.", ["n-grams", "RNNs", "LSTMs", "seq2seq", "bottlenecks"], "Train an n-gram model and inspect where local context fails.", "Architectures evolve in response to information-flow and optimization bottlenecks."),
            ("Attention", "Build attention from queries, keys, values, similarity scores, normalization, and weighted aggregation.", ["queries", "keys", "values", "scaled dot product", "attention masks"], "Implement scaled dot-product attention and visualize weights.", "Attention is content-dependent routing of information."),
            ("The Transformer Block", "Compose multi-head attention, feed-forward layers, residual paths, normalization, positional information, and masking.", ["multi-head attention", "residual connections", "normalization", "MLP blocks", "position"], "Assemble one transformer block and test tensor shapes.", "Depth repeatedly mixes information and transforms representations."),
            ("Training Foundation Models", "Study autoregressive, masked, and sequence-to-sequence objectives; data mixtures; scaling; checkpoints; and mixture-of-experts.", ["pretraining objectives", "data mixtures", "scaling laws", "checkpoints", "mixture of experts"], "Estimate compute and data requirements for a tiny language model.", "Pretraining compresses statistical regularities into parameters; it does not create a fact database."),
            ("Inference and Sampling", "Trace logits, softmax, temperature, top-k, top-p, streaming, batching, KV cache, prefix cache, and speculative decoding.", ["logits", "sampling", "temperature", "KV cache", "batching"], "Build a sampling playground and compare decoding strategies.", "Generation is repeated conditional prediction shaped by decoding and system context."),
            ("Model Families and Selection", "Compare base, instruction, reasoning, code, embedding, reranking, reward, safety, speech, vision, and diffusion models.", ["instruction tuning", "reasoning models", "multimodal models", "open weights", "model routing"], "Benchmark candidate models on a task-specific dataset.", "Select models as replaceable components against requirements, not by reputation."),
        ],
    },
    {
        "title": "Prompt and Context Engineering",
        "goal": "Design the information, instructions, state, and output boundaries that make model behavior useful and testable.",
        "project": "Build a context engine with structured output, memory policies, token budgets, and regression tests.",
        "chapters": [
            ("Instructions That Work", "Write clear tasks, roles, constraints, examples, delimiters, and success criteria while avoiding unnecessary prompt folklore.", ["instruction hierarchy", "roles", "few-shot examples", "delimiters", "constraints"], "Solve one task with weak and strong prompts and compare failures.", "A prompt is an interface specification for probabilistic behavior."),
            ("Structured Generation", "Use schemas, constrained decoding, validation, repair, retries, and typed application boundaries.", ["JSON Schema", "structured output", "validation", "repair", "retries"], "Build an invoice extractor with schema validation and adversarial inputs.", "Free-form model output must become validated data before software trusts it."),
            ("Context Construction", "Assemble instructions, user input, state, evidence, tools, and examples under priority and token constraints.", ["context windows", "token budgeting", "ranking", "compression", "context assembly"], "Implement a context builder with explicit section budgets.", "Context is a scarce, ordered working set—not a dumping ground."),
            ("Conversation and Memory", "Separate transcript, session state, summaries, semantic memory, episodic memory, user preferences, and source-of-truth data.", ["working memory", "session memory", "long-term memory", "summarization", "memory retrieval"], "Implement a conversation summarizer and memory scoring policy.", "Memory is selected state reconstructed for the next decision."),
            ("Context Failure and Security", "Recognize instruction conflict, prompt injection, context poisoning, stale memory, overflow, lost provenance, and authorization mistakes.", ["prompt injection", "instruction conflict", "provenance", "authorization", "context poisoning"], "Attack a context pipeline with malicious retrieved text and test defenses.", "Treat external content as data, never as authority to override trusted instructions."),
            ("Prompt and Context Operations", "Version prompts, trace context, cache safely, run regressions, compare variants, and monitor cost and quality.", ["prompt versioning", "context traces", "caching", "A/B tests", "regression evaluation"], "Create a prompt change report with before/after evals.", "Context changes are software changes and require evidence, review, and rollback."),
        ],
    },
    {
        "title": "Knowledge and Retrieval Systems",
        "goal": "Build grounded knowledge systems whose ingestion, retrieval, generation, and citations can be evaluated separately.",
        "project": "Deliver an enterprise RAG system with authorization, hybrid retrieval, reranking, citations, and stage-specific evaluation.",
        "chapters": [
            ("Knowledge Outside the Model", "Decide among direct context, search, databases, knowledge graphs, RAG, fine-tuning, and deterministic rules.", ["knowledge freshness", "grounding", "structured data", "retrieval", "fine-tuning"], "Classify ten requirements by the correct knowledge mechanism.", "Put knowledge in the component best suited to update, govern, query, and verify it."),
            ("Document Ingestion", "Preserve provenance while parsing documents, OCR, tables, images, metadata, permissions, versions, and deletions.", ["parsing", "OCR", "chunking", "metadata", "provenance"], "Create an ingestion manifest and measure parse fidelity.", "Retrieval cannot recover content or permissions lost during ingestion."),
            ("Retrieval", "Compare lexical, dense, sparse, hybrid, filtered, multi-query, parent-child, and late-interaction retrieval.", ["BM25", "dense retrieval", "hybrid search", "query rewriting", "parent-child retrieval"], "Implement lexical and vector baselines and calculate recall@k.", "Retrieval is candidate selection under relevance and policy constraints."),
            ("Ranking and Context Selection", "Use fusion, reranking, diversity, deduplication, compression, and token-aware packing.", ["reciprocal rank fusion", "rerankers", "diversity", "deduplication", "context packing"], "Add reranking and measure quality versus latency.", "Every selected passage competes for limited attention; more context can reduce quality."),
            ("RAG Generation and Citations", "Construct grounded prompts, handle missing evidence, attribute claims, validate citations, and avoid unsupported synthesis.", ["grounded generation", "abstention", "citation precision", "faithfulness", "answer validation"], "Build a citation validator that checks claim-to-source alignment.", "A citation is useful only when it supports the nearby claim and resolves to source evidence."),
            ("Advanced and Enterprise RAG", "Study graph, multi-hop, adaptive, and agentic retrieval together with tenancy, freshness, security, resilience, and cost.", ["Graph RAG", "multi-hop retrieval", "adaptive RAG", "authorization", "freshness"], "Complete the enterprise RAG architecture studio and threat model.", "Advanced orchestration cannot compensate for weak data, retrieval, authorization, or evaluation."),
        ],
    },
    {
        "title": "Reasoning and Tool Use",
        "goal": "Understand when inference-time search, planning, verification, and external tools improve task outcomes.",
        "project": "Build a research workflow with a planner, typed tools, evidence store, verifier, and bounded recovery.",
        "chapters": [
            ("Reasoning as Search", "Separate recall from deliberate search and study decomposition, candidate generation, backtracking, and stopping.", ["decomposition", "search", "backtracking", "heuristics", "termination"], "Solve a constraint problem with explicit state search.", "Additional inference helps when the task benefits from exploring and rejecting alternatives."),
            ("Planning", "Represent goals, prerequisites, steps, dependencies, state, uncertainty, and replanning without confusing a plausible plan with execution.", ["goal decomposition", "plan representation", "dependencies", "replanning", "state"], "Build a planner that outputs a validated dependency graph.", "Plans are hypotheses about action sequences and must be updated by observations."),
            ("Verification and Critique", "Use deterministic checks, tests, rubrics, critics, self-consistency, best-of-N, and external evidence.", ["verifiers", "critique", "self-consistency", "best-of-N", "tests"], "Generate several candidates and select with an independent verifier.", "Verification should exploit signals different from those used to generate the answer."),
            ("Tools as Capability Boundaries", "Design typed tools, schemas, descriptions, errors, timeouts, idempotency, permissions, and audit records.", ["function calling", "tool schemas", "idempotency", "timeouts", "permissions"], "Wrap a read-only API as a typed tool and fuzz its arguments.", "Probabilistic intent must cross a deterministic, authorized boundary before effects occur."),
            ("MCP and Integration Protocols", "Understand clients, servers, tools, resources, prompts, discovery, transport, authentication, and protocol security.", ["MCP", "resources", "tool discovery", "transports", "authentication"], "Implement a small local MCP server and test a hostile client request.", "Protocols standardize capability exchange; they do not remove authorization or trust decisions."),
            ("Reasoning-System Economics", "Balance accuracy, latency, token use, parallel candidates, tool calls, caches, failure rates, and task value.", ["test-time compute", "latency", "cost-quality curves", "routing", "budgets"], "Plot quality and cost for single-pass, best-of-N, and verifier loops.", "Spend additional computation only where expected outcome improvement justifies it."),
        ],
    },
    {
        "title": "Agent Systems",
        "goal": "Design agentic systems as bounded stateful architectures rather than treating autonomy as a model feature.",
        "project": "Build a durable multi-step agent with checkpoints, approval gates, evaluation, and observable termination.",
        "chapters": [
            ("Agent or Workflow?", "Define agents by goal-directed action selection in a loop and contrast them with deterministic workflows and single tool calls.", ["agency", "workflows", "state machines", "autonomy", "control"], "Model the same task as a workflow and as an agent, then compare.", "Use the least autonomy that handles the uncertainty in the task."),
            ("The Agent Loop", "Connect goal, state, planning, action, observation, reflection, and termination into a bounded state machine.", ["plan-act-observe", "state", "reflection", "termination", "budgets"], "Extend the included agent loop with failures and checkpointing.", "An agent loop without explicit state and stopping rules is an unreliable retry loop."),
            ("Agent Memory and Recovery", "Manage working state, episodic history, durable checkpoints, resumability, compensation, and idempotent tools.", ["checkpoints", "episodic memory", "recovery", "compensation", "idempotency"], "Persist and resume an interrupted multi-step run.", "Continuity requires durable state and recoverable effects, not merely longer context."),
            ("Agent Patterns", "Apply planner–executor, supervisor–worker, reviewer, evaluator–optimizer, routing, and human-approval patterns.", ["planner-executor", "supervisor-worker", "reviewer", "routing", "approval gates"], "Implement two patterns and measure coordination overhead.", "Patterns trade flexibility for additional state, calls, latency, and failure surfaces."),
            ("Multi-Agent Systems", "Study delegation, role boundaries, communication, shared state, consensus, conflict, security, and why many tasks do not need multiple agents.", ["delegation", "coordination", "shared state", "consensus", "role isolation"], "Split a research task across workers and compare with one-agent parallel tools.", "More agents increase organizational complexity faster than raw capability."),
            ("Operating Long-Running Agents", "Design durable orchestration, queues, scheduling, leases, approvals, monitoring, incident response, and safe cancellation.", ["durable execution", "queues", "leases", "human oversight", "cancellation"], "Create an SLO and runbook for a day-long agent workflow.", "Long-running agents are distributed systems with probabilistic decision components."),
        ],
    },
    {
        "title": "AI Software and Product Engineering",
        "goal": "Use specifications, evaluations, secure development practices, and product discovery to deliver useful AI features.",
        "project": "Take one AI feature from problem discovery through a specification-driven implementation and evidence-based release.",
        "chapters": [
            ("Discovering the Right Problem", "Identify user jobs, workflow constraints, baseline performance, capability fit, failure cost, and measurable value before building.", ["user research", "jobs-to-be-done", "baseline workflow", "feasibility", "success metrics"], "Write a problem brief with a non-AI alternative.", "Optimize the human outcome, not the amount of AI in the product."),
            ("Specification-Driven Development", "Translate intent into functional, prompt, tool, agent, data, safety, and evaluation specifications with acceptance criteria.", ["functional specifications", "acceptance criteria", "prompt specs", "tool contracts", "evaluation specs"], "Write executable examples before implementation.", "Specifications align humans and agents around observable outcomes and constraints."),
            ("AI-Native Development Workflow", "Organize repositories, instructions, skills, context files, branches, reviews, tests, and coding-agent collaboration.", ["repo instructions", "skills", "context files", "AI coding agents", "code review"], "Run a bounded repository task with two assistants and compare review burden.", "AI accelerates change production, making specification and verification more important."),
            ("Testing AI Systems", "Combine unit, contract, integration, scenario, regression, adversarial, and human tests across deterministic and probabilistic components.", ["unit tests", "contract tests", "eval datasets", "adversarial tests", "release gates"], "Derive a test pyramid from an AI system architecture.", "Test deterministic properties deterministically and probabilistic behavior statistically."),
            ("Human-Centered AI UX", "Design uncertainty, citations, previews, correction, undo, approval, feedback, accessibility, and graceful failure.", ["uncertainty UX", "citations", "correction", "undo", "accessibility"], "Prototype a high-risk action flow with preview and approval.", "Trust grows from control, evidence, and recoverability—not from confident prose."),
            ("Experiments, Adoption, and Value", "Measure task success, time, correction effort, retention, adoption, cost, risk, and ROI through staged experiments.", ["A/B testing", "task success", "adoption", "ROI", "build versus buy"], "Design a rollout with guardrails and decision thresholds.", "A technically impressive feature is not successful until it improves a valued workflow."),
        ],
    },
    {
        "title": "Evaluation, Safety, and Governance",
        "goal": "Build evidence that AI systems meet task, safety, security, compliance, and business requirements.",
        "project": "Create an evaluation and assurance package with datasets, rubrics, adversarial tests, release gates, and governance evidence.",
        "chapters": [
            ("Evaluation as Requirements", "Turn desired behavior into tasks, cases, metrics, rubrics, slices, thresholds, and explicit failure tolerances.", ["task definitions", "gold datasets", "rubrics", "slices", "thresholds"], "Write a 30-case evaluation set from real workflow risks.", "Evaluation is executable requirements for uncertain behavior."),
            ("Metrics and Human Judgment", "Combine exact metrics, semantic similarity, pairwise comparison, human review, LLM judges, calibration, and uncertainty.", ["deterministic metrics", "human evaluation", "LLM judges", "confidence intervals", "inter-rater agreement"], "Calibrate an automated judge against two human reviewers.", "Every metric encodes a theory of quality; validate that theory against real decisions."),
            ("Evaluation by System Stage", "Evaluate ingestion, retrieval, generation, tools, agents, UX, latency, cost, and business outcomes separately and together.", ["component evals", "retrieval metrics", "faithfulness", "tool success", "end-to-end evals"], "Build a failure attribution matrix for a RAG system.", "Stage-specific evaluation makes failures diagnosable and improvements attributable."),
            ("Security of AI Systems", "Threat-model prompt injection, data exfiltration, tool abuse, identity confusion, insecure output handling, supply chain, and denial of service.", ["prompt injection", "data exfiltration", "tool abuse", "sandboxing", "threat modeling"], "Red-team a tool-enabled assistant and document mitigations.", "Treat models and retrieved content as untrusted components inside ordinary security boundaries."),
            ("Responsible AI and Risk", "Assess bias, privacy, transparency, human impact, misuse, accessibility, high-impact decisions, and safe failure.", ["fairness", "privacy", "transparency", "human oversight", "impact assessment"], "Write an impact assessment for a consequential use case.", "Responsible AI is a lifecycle of decisions and evidence, not a one-time checklist."),
            ("Governance and Assurance", "Define ownership, inventory, risk tiers, policies, approvals, audit evidence, incidents, exceptions, vendor review, and retirement.", ["AI inventory", "risk tiers", "model cards", "audit evidence", "incident response"], "Create a lightweight governance operating model for a mid-size company.", "Governance should make safe delivery easier by clarifying authority, evidence, and escalation."),
        ],
    },
    {
        "title": "Training, Serving, and AI Operations",
        "goal": "Understand model adaptation, efficient inference, deployment, observability, release, and lifecycle operations.",
        "project": "Adapt and serve a small model, benchmark it, instrument it, and release it with rollback evidence.",
        "chapters": [
            ("Choosing Adaptation", "Diagnose whether a requirement needs prompting, retrieval, tools, fine-tuning, continued pretraining, or a different model.", ["behavior versus knowledge", "prompting", "RAG", "fine-tuning", "model selection"], "Create a decision table for ten adaptation scenarios.", "Choose the smallest intervention at the correct system layer."),
            ("Post-Training Methods", "Understand supervised fine-tuning, LoRA, QLoRA, preference data, RLHF, DPO, distillation, and model merging.", ["SFT", "LoRA", "QLoRA", "DPO", "distillation"], "Fine-tune a small model and evaluate held-out behavior.", "Adaptation trades generality and operational simplicity for targeted behavior."),
            ("Dataset Engineering", "Curate, label, deduplicate, filter, balance, version, document, and protect training and evaluation data.", ["data curation", "synthetic data", "deduplication", "contamination", "data cards"], "Create a data card and contamination check for a small dataset.", "Data design is model behavior design."),
            ("Inference Infrastructure", "Connect accelerators, memory, quantization, model formats, servers, batching, streaming, caches, and speculative decoding.", ["GPUs", "quantization", "vLLM", "batching", "KV cache"], "Load-test a local model at several concurrency levels.", "Inference performance is a queueing and memory problem as much as a model problem."),
            ("Deployment and Routing", "Design containers, serverless endpoints, Kubernetes, autoscaling, routing, fallbacks, regional placement, and disaster recovery.", ["containers", "autoscaling", "model routing", "fallbacks", "resilience"], "Write a deployment ADR comparing hosted and self-hosted inference.", "Deployment choices allocate control, cost, latency, and operational burden."),
            ("LLMOps", "Version prompts, models, data, and evals; trace requests; monitor quality and cost; canary, roll back, and respond to incidents.", ["tracing", "versioning", "continuous evaluation", "canaries", "FinOps"], "Instrument a request and inject provider, retrieval, and validation failures.", "Every production change needs evidence, observability, and a reversible release path."),
        ],
    },
    {
        "title": "Cloud and Enterprise AI Architecture",
        "goal": "Design secure, governed, resilient AI platforms and map them to managed services without losing vendor-neutral reasoning.",
        "project": "Produce a multi-cloud-capable enterprise AI reference architecture and five architecture decision records.",
        "chapters": [
            ("Enterprise AI Building Blocks", "Decompose platforms into gateways, model access, retrieval, tool integration, identity, policy, observability, evaluation, and developer experience.", ["AI gateways", "model catalog", "shared retrieval", "tool registry", "platform engineering"], "Draw a logical platform architecture before naming products.", "Stable capability boundaries make vendor choices replaceable and governance consistent."),
            ("Identity, Data, and Trust Boundaries", "Apply authentication, authorization, tenancy, secrets, encryption, residency, lineage, and audit to AI data flows.", ["identity", "authorization", "multi-tenancy", "data residency", "audit"], "Threat-model an enterprise assistant across trust boundaries.", "A model call does not suspend ordinary identity and data-security requirements."),
            ("AWS Managed AI", "Map foundation models, ML lifecycle, retrieval, serverless compute, containers, workflow, identity, storage, and monitoring to AWS services.", ["Amazon Bedrock", "SageMaker", "OpenSearch", "Lambda and EKS", "CloudWatch and IAM"], "Map the enterprise RAG design to AWS and estimate managed-service trade-offs.", "Start with logical capabilities; use managed services where their constraints match the system."),
            ("Azure Managed AI", "Map models, ML, search, functions, containers, integration, identity, data, security, and operations to Azure.", ["Azure AI Foundry", "Azure OpenAI", "Azure AI Search", "AKS and Functions", "Entra ID and Monitor"], "Map the same RAG design to Azure and compare identity integration.", "Cloud-native integration can accelerate governance but increases platform coupling."),
            ("Google Cloud and Portable Patterns", "Map Vertex AI, search, Cloud Run, GKE, data, events, identity, and operations while identifying portable seams.", ["Vertex AI", "Vertex AI Search", "Cloud Run and GKE", "Cloud IAM", "portable interfaces"], "Map the design to Google Cloud and identify the migration boundary.", "Portability is achieved through deliberate contracts and data ownership, not lowest-common-denominator design."),
            ("Enterprise Operating Model", "Define platform teams, product teams, centers of enablement, governance, service catalogs, SLOs, chargeback, vendor management, and adoption.", ["team topology", "service catalog", "SLOs", "FinOps", "vendor management"], "Create a responsibility matrix and platform roadmap.", "Architecture succeeds only when ownership, incentives, operations, and delivery practices align."),
        ],
    },
    {
        "title": "Multimodal and Frontier Systems",
        "goal": "Understand multimodal pipelines and evaluate emerging AI capabilities through enduring principles and evidence.",
        "project": "Build a multimodal document system and reproduce one frontier claim against a strong baseline.",
        "chapters": [
            ("Vision and Document Intelligence", "Understand image representations, vision-language models, OCR, layout, tables, charts, spatial relationships, and provenance.", ["vision encoders", "OCR", "layout models", "document AI", "visual grounding"], "Extract fields from documents and evaluate field and page-level accuracy.", "Preserve spatial structure and provenance when converting visual documents into model context."),
            ("Speech and Audio", "Connect ASR, diarization, audio understanding, TTS, streaming, latency, consent, and voice safety.", ["speech recognition", "diarization", "text-to-speech", "streaming audio", "voice safety"], "Build a transcript pipeline with timestamps and confidence handling.", "Audio systems are temporal, identity-sensitive, and latency-constrained."),
            ("Image and Video Generation", "Study diffusion, conditioning, latent representations, control, evaluation, provenance, copyright, and content safety.", ["diffusion", "conditioning", "latent space", "video generation", "provenance"], "Design an evaluation rubric for generated campaign assets.", "Generative quality includes controllability, consistency, provenance, safety, and workflow fit."),
            ("Computer Use and Embodied Action", "Model perception–action loops, UI grounding, coordinate and semantic actions, recovery, permissions, and physical-world constraints.", ["computer use", "visual grounding", "action spaces", "recovery", "robotics interfaces"], "Design a safe browser task with confirmation and recovery.", "Acting through interfaces adds uncertainty and irreversible side effects to ordinary agent loops."),
            ("Long Context, World Models, and Continual Learning", "Examine active directions without mistaking larger demonstrations for solved engineering problems.", ["long context", "world models", "continual learning", "memory", "test-time adaptation"], "Compare a frontier method with retrieval, explicit state, or fine-tuning baselines.", "Frontier techniques should be decomposed into representation, memory, search, learning, and control claims."),
            ("How to Track the Frontier", "Develop research literacy, evidence hierarchies, reproduction habits, forecasting, and a review cadence for a fast-moving field.", ["primary sources", "benchmarks", "ablations", "reproduction", "technology forecasting"], "Write a one-page frontier assessment with confidence levels.", "The durable skill is evaluating claims and mapping new mechanisms to established principles."),
        ],
    },
]

SAMPLE_FILES = [
    "01-search-planning.py", "02-gradient-descent.py", "03-tokenization-vectors.py",
    "04-attention-sampling.py", "05-context-builder.py", "06-hybrid-rag.py",
    "07-planner-verifier.py", "08-agent-state-machine.py",
    "09-spec-driven-development.py", "10-evaluation-slices.py", "11-model-router.py",
    "12-cloud-capability-map.py", "13-multimodal-provenance.py",
]

VISUAL_STAGES = [
    ["Goal", "State model", "Search or learn", "Decision", "Feedback"],
    ["Problem frame", "Dataset", "Train", "Evaluate slices", "Operate"],
    ["Raw language", "Tokens", "Representation", "Similarity", "Retrieved meaning"],
    ["Tokens", "Attention", "Transformer layers", "Logits", "Sampled token"],
    ["Trusted instructions", "Selected state", "Evidence", "Model", "Validated output"],
    ["Sources", "Ingest", "Retrieve and rerank", "Generate", "Cite and evaluate"],
    ["Goal", "Candidate plans", "Tools", "Observations", "Verifier"],
    ["Goal and state", "Plan", "Act", "Checkpoint", "Stop or continue"],
    ["User problem", "Specification", "Implementation", "Evaluation", "Release evidence"],
    ["Requirements", "Cases and threats", "Measures", "Risk gate", "Assurance record"],
    ["Data", "Adapt", "Serve", "Trace", "Canary or rollback"],
    ["Logical capability", "Trust boundary", "Managed service", "SLO", "Governance"],
    ["Multimodal input", "Representation", "Fusion or action", "Provenance", "Evaluation"],
]

WORKED_SCENARIOS = [
    "A support team must route incidents without mistaking fluent descriptions for reliable decisions.",
    "A lender needs a prediction service whose errors can be explained across customer groups.",
    "Employees search for policies using vocabulary different from the source documents.",
    "A team must explain why decoding settings change model output and latency.",
    "A long-running assistant must fit policy, evidence, memory, and user input into a bounded context.",
    "An enterprise assistant must answer from authorized policies and cite the exact passages used.",
    "A research workflow must plan, call tools, and reject unsupported conclusions.",
    "A multi-step task may pause for hours and must resume without repeating side effects.",
    "A product team must convert a vague AI feature request into testable release evidence.",
    "A high-impact assistant may pass average quality while failing a safety-critical user slice.",
    "A service must route requests across models while controlling cost and retaining rollback.",
    "An architect must implement the same governed AI capability on different cloud providers.",
    "A document system must combine tables, charts, and text without losing source provenance.",
]

PREREQUISITES = [
    ["No AI background required", "Comfort reading simple Python", "Basic algebra"],
    ["Book 1 or equivalent", "Basic Python", "Graphs and averages"],
    ["Books 1–2", "Vectors and dot products", "Basic text processing"],
    ["Books 1–3", "Matrix multiplication intuition", "Neural-network basics"],
    ["Book 4", "Model inference", "Tokens and context windows"],
    ["Books 3–5", "Embeddings and search", "Structured model output"],
    ["Books 1 and 4–6", "Search and planning", "Typed software interfaces"],
    ["Books 5–7", "State machines", "Tools and evaluation"],
    ["Books 5–8", "Software testing", "Product discovery basics"],
    ["Books 5–9", "Statistics intuition", "Threat-model basics"],
    ["Books 2, 4, and 10", "Containers and APIs", "Performance measurement"],
    ["Books 5–11", "Cloud and identity fundamentals", "Architecture documentation"],
    ["Books 3–12 as relevant", "Evidence-oriented research reading", "Risk awareness"],
]

READINGS = [
    ["Russell & Norvig — Artificial Intelligence: A Modern Approach", "Sutton & Barto — Reinforcement Learning: An Introduction"],
    ["Hastie, Tibshirani & Friedman — The Elements of Statistical Learning", "Mitchell — Machine Learning"],
    ["Manning, Raghavan & Schütze — Introduction to Information Retrieval", "Mikolov et al. — Efficient Estimation of Word Representations in Vector Space"],
    ["Vaswani et al. — Attention Is All You Need", "Devlin et al. — BERT", "Brown et al. — Language Models are Few-Shot Learners"],
    ["Provider documentation for structured output and tool calling", "Current prompt-injection guidance from authoritative security sources"],
    ["Lewis et al. — Retrieval-Augmented Generation", "Karpukhin et al. — Dense Passage Retrieval"],
    ["Yao et al. — ReAct", "Primary protocol specifications for the tool interfaces studied"],
    ["Primary papers for the selected agent pattern", "Distributed-systems references for durable execution and idempotency"],
    ["Repository contribution and test documentation", "Architecture Decision Record guidance and product experiment literature"],
    ["NIST AI Risk Management Framework", "OWASP guidance for LLM applications", "Task-specific evaluation research"],
    ["Hu et al. — LoRA", "Ouyang et al. — InstructGPT", "Official inference-server documentation"],
    ["Official AWS, Azure, and Google Cloud architecture and service documentation", "Organization security and data-governance standards"],
    ["Primary papers for the selected modality or frontier claim", "Model and dataset cards for every reproduced system"],
]

EXPECTED_OBSERVATIONS = [
    "A* should reach the same shortest path as breadth-first search while often expanding fewer states when the heuristic is informative.",
    "Loss should decline while the learned line approaches the data-generating relationship y = 2x + 1.",
    "The outage document should rank highest because it shares the query's weighted terms; the example also exposes the limits of lexical features.",
    "The query-aligned value receives more attention, and lower temperature concentrates the sampling distribution.",
    "Trusted high-priority sections consume the budget first; untrusted evidence remains explicitly marked as data.",
    "Documents appearing high in both rankings receive the strongest reciprocal-rank-fusion scores.",
    "Only the plan containing every required step in dependency order should pass verification.",
    "The state machine pauses at approval, resumes after approval, and terminates within the attempt budget.",
    "Both executable acceptance examples pass; changing the abstention behavior should fail the second case.",
    "The release gate depends on both overall performance and perfect performance in the high-risk slice.",
    "Low-risk simple work routes to the cheaper model; high-risk work routes to the higher-quality model.",
    "The logical architecture remains stable while provider-specific service names change.",
    "Only evidence above the confidence threshold is emitted, and every output retains source, page, and modality." ,
]


def render_chapter(book_no: int, chapter_no: int, book: dict, chapter: tuple) -> str:
    title, summary, topics, practice, principle = chapter
    core = render_core_concepts(topics, summary)
    objectives = learning_objectives(title, topics, summary)
    practice_block = engineering_practice(practice, topics, title)
    failures = failure_clinic(title, topics, summary)
    architecture = architecture_lens(title, topics, book["title"])
    evolution = evolution_lens(title, topics, principle)
    scenario = WORKED_SCENARIOS[book_no - 1]
    hook = render_chapter_hook(title, topics, book_no, chapter_no)
    mastery = mastery_exemplars(title, topics, principle)
    worked = render_worked_example(book_no, chapter_no, title, summary, topics, scenario)
    knowledge = render_knowledge_check(book_no, chapter_no, topics)
    stages = VISUAL_STAGES[book_no - 1]
    diagram = "\n".join(
        f"  N{i}[\"{stage}\"] --> N{i+1}[\"{stages[i+1]}\"]"
        for i, stage in enumerate(stages[:-1])
    )
    sample_file = SAMPLE_FILES[book_no - 1]
    prerequisite_lines = "\n".join(f"- {item}" for item in PREREQUISITES[book_no - 1])
    reading_lines = "\n".join(f"- {item}" for item in READINGS[book_no - 1])
    expected = EXPECTED_OBSERVATIONS[book_no - 1]
    return f"""# {book_no}.{chapter_no} — {title}

*Book {book_no}: {book['title']} · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

{prerequisite_lines}

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

{summary}

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

{objectives}

!!! note "Enduring principle"
    {principle}

## Mental model

```mermaid
flowchart LR
{diagram}
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **{title.lower()}** changes one or more transitions.

## Core concepts

{core}

## Worked example

{worked}

{hook}

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/{sample_file}) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/{sample_file}"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    {expected}

This is a **book-level sample**. Its relevance to this chapter is the boundary between **{topics[0]}** and **{topics[1]}**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

{practice_block}

## Architecture lens

{architecture}

## Failure clinic

{failures}

## Evolution lens

{evolution}

## Knowledge check

{knowledge}

## Mastery questions

??? tip "Model answers (proficient level)"
    {mastery}

## Self-assessment rubric

| Level | Evidence |
|---|---|
| Not yet | Can repeat terms but cannot trace the visual or predict the sample. |
| Developing | Can explain the mechanism and complete the normal case with help. |
| Proficient | Can implement the exercise, diagnose a failure, and compare a baseline. |
| Transfer | Can defend an architecture choice in a new domain with evaluation evidence. |

## Evidence and further study

{reading_lines}

Use primary sources for technical claims and official documentation for current product behavior. Record the version or access date for evolving material.

## Continue

Return to the [book index](index.md) or use site search to follow the chapter's concepts into the knowledge-area and reference pages.
"""


def render_book_index(book_no: int, book: dict, chapter_files: list[tuple[str, str]]) -> str:
    links = "\n".join(f"{i}. [{title}]({filename})" for i, (title, filename) in enumerate(chapter_files, 1))
    prerequisite_lines = "\n".join(f"- {item}" for item in PREREQUISITES[book_no - 1])
    reading_lines = "\n".join(f"- {item}" for item in READINGS[book_no - 1])
    return f"""# Book {book_no} — {book['title']}

## Purpose

{book['goal']}

## Entry prerequisites

{prerequisite_lines}

## Chapters

{links}

## Book project

{book['project']}

The project should include a short specification, runnable artifact or architecture, evaluation evidence, failure analysis, and at least one ADR. Prefer a small well-measured system over a large demo with unclear behavior.

## Suggested three-week schedule

- **Week 1:** Chapters 1–2, concept notes, and quick checks.
- **Week 2:** Chapters 3–4 and the runnable sample; begin the book project.
- **Week 3:** Chapters 5–6, failure analysis, project evaluation, and written reflection.

## Assessment

| Evidence | Weight |
|---|---:|
| Chapter knowledge checks | 20% |
| Runnable exercises and failure cases | 30% |
| Book project | 35% |
| Architecture defense and reflection | 15% |

## Anchor readings

{reading_lines}

## Completion standard

You can explain the key mechanisms, complete the practice in every chapter, pass your own mastery review, and defend the project design against simpler alternatives.
"""


def main() -> None:
    BOOKS_DIR.mkdir(parents=True, exist_ok=True)
    catalog = ["# Guided Books", "", "The thirteen books are the primary reading path through AIEBOK. Knowledge-area and concept pages remain the reusable reference layer.", ""]
    for book_no, book in enumerate(BOOKS, 1):
        directory = BOOKS_DIR / f"{book_no:02d}-{slug(book['title'])}"
        directory.mkdir(parents=True, exist_ok=True)
        chapter_files = []
        for chapter_no, chapter in enumerate(book["chapters"], 1):
            filename = f"{chapter_no:02d}-{slug(chapter[0])}.md"
            (directory / filename).write_text(
                render_chapter(book_no, chapter_no, book, chapter), encoding="utf-8"
            )
            chapter_files.append((chapter[0], filename))
        (directory / "index.md").write_text(
            render_book_index(book_no, book, chapter_files), encoding="utf-8"
        )
        rel = directory.relative_to(BOOKS_DIR).as_posix()
        catalog.append(f"{book_no}. [**{book['title']}**]({rel}/index.md) — {book['goal']}")
    (BOOKS_DIR / "index.md").write_text("\n".join(catalog) + "\n", encoding="utf-8")
    print(f"Generated {len(BOOKS)} books and {sum(len(b['chapters']) for b in BOOKS)} chapters.")


if __name__ == "__main__":
    main()
