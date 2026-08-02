# AIEBOK Comprehensive Content Plan

This file is the editorial blueprint for turning the starter into a comprehensive, durable body of knowledge.

## Curriculum backbone

The 20 knowledge areas in `docs/knowledge-areas/` progress from first principles through models, context, knowledge, reasoning, tools, agents, software engineering, operations, enterprise delivery, multimodality, frontier research, and product engineering.

## Parallel threads

Every knowledge-area expansion should deliberately weave in these threads:

1. **Theory:** enduring concepts, vocabulary, mental models, and minimal mathematics.
2. **Engineering:** current implementation approaches, interfaces, and debugging practices.
3. **Code labs:** implement important mechanisms once; then adopt mature libraries.
4. **Architecture studios:** scale, reliability, security, governance, cost, and alternatives.
5. **Research reading:** primary papers, specifications, evidence quality, and reproduction.
6. **Evolution:** yesterday, today, tomorrow, and the principle that survives.
7. **Why it exists:** problem, prior art, innovation, limitations, and successors.
8. **Trade-offs:** benefits, costs, failure modes, when to use, and when not to use.
9. **Industry case studies:** infer and critique real system designs without presenting guesses as facts.
10. **Career/portfolio:** code, ADRs, benchmarks, diagrams, evaluation reports, and explanatory writing.
11. **Engineering skills:** specification writing, experimentation, debugging, evaluation, and communication.
12. **Mastery questions:** understanding, engineering, architecture, research, and leadership.
13. **Cloud implementation:** provider-neutral capability first; dated AWS, Azure, and Google Cloud mappings second.
14. **Security and responsible AI:** data, identity, threat boundaries, misuse, harm, audit, and governance.
15. **Product thinking:** human workflow, uncertainty UX, feedback, adoption, value, and organizational fit.

## Target inventory

| Artifact | Starter | Mature target |
|---|---:|---:|
| Knowledge-area overview pages | 20 | 20 |
| Guided lessons | 0 | 120–160 |
| Concept cards | 5 | 150–250 |
| Pattern cards | 2 | 50–100 |
| Architecture studios | 1 | 20–30 |
| Cloud/tool guides | 4 | 30–50 |
| Code labs | 5 | 50–70 |
| Research readings | 1 template | 30–50 |
| End-to-end build guides | 0 | 10–15 |

## Recommended lesson sequence by cluster

### Cluster A — First principles

Foundations → machine learning → language/representation → transformers. Projects: symbolic search, predictive model, semantic search, and tiny transformer.

### Cluster B — Model interaction

Models → prompt/context → structured outputs and memory. Project: a model-neutral context engine with regression tests.

### Cluster C — Grounded intelligence

Knowledge systems → reasoning → evaluation. Project: an enterprise RAG system with stage-specific evals and citations.

### Cluster D — Action

Tools/integration → agents → safety/security. Project: a bounded assistant with typed tools, approval, recovery, and audit traces.

### Cluster E — Delivery discipline

AI software engineering → coding ecosystem → product engineering. Project: a specification-driven AI feature from discovery through release evidence.

### Cluster F — Model and platform lifecycle

Training → infrastructure → AI operations → enterprise architecture. Project: deploy, observe, load-test, govern, and cost a model-backed service.

### Cluster G — Broader and future systems

Multimodal → frontier. Project: reproduce and critique one emerging capability using strong baselines.

## Page templates

- Use `templates/content-spec.yml` before substantial content work.
- Use the lesson anatomy in `docs/editorial/content-specification.md`.
- Use `templates/adr-template.md` for architecture decisions.
- Use `docs/papers/paper-reading-template.md` for research summaries.
- Use the pattern and architecture starter pages as structural examples.

## Expansion method

For each knowledge area:

1. Define its 6–12 lesson sequence and prerequisites.
2. Create concept cards for terms reused elsewhere.
3. Select 2–4 code labs and one architecture studio.
4. Add at least one primary-source reading seminar.
5. Add cloud/tool mappings only after the enduring capability is explained.
6. Define mastery outcomes and a portfolio artifact.
7. Classify stability and set a review cadence.
8. Run technical, editorial, accessibility, code, link, and mobile reviews.

## Question index seed

- How do models learn and generate language?
- What are weights, parameters, tokens, logits, and context windows?
- Why do embeddings capture useful similarity, and where do they fail?
- When should I use RAG, long context, fine-tuning, or deterministic queries?
- How do prompts, context, memory, skills, and harnesses differ?
- Why are reasoning models slower, and when is extra compute worthwhile?
- How do agents differ from workflows and ordinary tool calling?
- How do I evaluate a new model or architecture objectively?
- How do specification-driven development and eval-driven release work together?
- How do AWS, Azure, and Google Cloud map to the same logical architecture?
- How do I build, secure, operate, govern, and pay for an enterprise AI system?

Turn these into a navigable question index after enough concept cards exist to provide stable destinations.
