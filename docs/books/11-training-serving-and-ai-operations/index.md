# Book 11 — Training, Serving, and AI Operations

## Purpose

Understand model adaptation, efficient inference, deployment, observability, release, and lifecycle operations.

## Entry prerequisites

- Books 2, 4, and 10
- Containers and APIs
- Performance measurement

## Chapters

1. [Choosing Adaptation](01-choosing-adaptation.md)
2. [Post-Training Methods](02-post-training-methods.md)
3. [Dataset Engineering](03-dataset-engineering.md)
4. [Inference Infrastructure](04-inference-infrastructure.md)
5. [Deployment and Routing](05-deployment-and-routing.md)
6. [LLMOps](06-llmops.md)

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
