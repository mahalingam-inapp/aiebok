# Book 11 — Training, Serving, and AI Operations

## Purpose

Understand model adaptation, efficient inference, deployment, observability, release, and lifecycle operations.

## Chapter learning path

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } __Choosing Adaptation__

    Diagnose whether a requirement needs prompting, retrieval, tools, fine-tuning, continued pretraining, or a di…

    [Open chapter →](01-choosing-adaptation.md)

-   :material-numeric-2-circle:{ .lg .middle } __Post-Training Methods__

    Understand supervised fine-tuning, LoRA, QLoRA, preference data, RLHF, DPO, distillation, and model merging.

    [Open chapter →](02-post-training-methods.md)

-   :material-numeric-3-circle:{ .lg .middle } __Dataset Engineering__

    Curate, label, deduplicate, filter, balance, version, document, and protect training and evaluation data.

    [Open chapter →](03-dataset-engineering.md)

-   :material-numeric-4-circle:{ .lg .middle } __Inference Infrastructure__

    Connect accelerators, memory, quantization, model formats, servers, batching, streaming, caches, and speculat…

    [Open chapter →](04-inference-infrastructure.md)

-   :material-numeric-5-circle:{ .lg .middle } __Deployment and Routing__

    Design containers, serverless endpoints, Kubernetes, autoscaling, routing, fallbacks, regional placement, and…

    [Open chapter →](05-deployment-and-routing.md)

-   :material-numeric-6-circle:{ .lg .middle } __LLMOps__

    Version prompts, models, data, and evals; trace requests; monitor quality and cost; canary, roll back, and re…

    [Open chapter →](06-llmops.md)

</div>

## Entry prerequisites

- Books 2, 4, and 10
- Containers and APIs
- Performance measurement

## Book project

Adapt and serve a small model, benchmark it, instrument it, and release it with rollback evidence.

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

- Hu et al. — LoRA
- Ouyang et al. — InstructGPT
- Official inference-server documentation

## Completion standard

You can explain the key mechanisms, complete the practice in every chapter, pass your own mastery review, and defend the project design against simpler alternatives.
