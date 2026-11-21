# Training, Serving, and AI Operations

Technical course 11 · 3 sections · 6 lectures · 10–12 hours of lecture and practice time, plus the project

Understand model adaptation, efficient inference, deployment, observability, release, and lifecycle operations.

[Start the first lecture](01-choosing-adaptation.md){ .md-button .md-button--primary }
[Download the course notebook](../../assets/notebooks/11-training-serving-and-ai-operations.ipynb){ .md-button download }

## Entry prerequisites

- Courses 02, 04, and 10 or equivalent experience
- Containers and APIs
- Performance measurement

## Course outline

### Model adaptation and post-training

- [01 · Choosing Adaptation](01-choosing-adaptation.md)
- [02 · Post-Training Methods](02-post-training-methods.md)

**Checkpoint**

Specify a behavior where prompt changes are a reasonable baseline before considering an adapter.

### Datasets and inference infrastructure

- [03 · Dataset Engineering](03-dataset-engineering.md)
- [04 · Inference Infrastructure](04-inference-infrastructure.md)

**Checkpoint**

Describe a held-out slice and a serving constraint. Explain which one affects training versus deployment.

### Deployment and operations

- [05 · Deployment and Routing](05-deployment-and-routing.md)
- [06 · LLMOps](06-llmops.md)

**Checkpoint**

Compare routing choices and write a rollback trigger in terms of latency and quality.

## Notebook workshop

Compare the router's decisions for a simple task and a high-risk task. Draft a separate held-out evaluation for any future fine-tune.

In the applied exercise for Lecture 02, you will train a rank-one adapter and evaluate held-out inputs.

The notebook includes each lecture's short demonstration and a checked exercise. For setup and execution, see [Course notebooks](../../labs/notebooks/index.md).

<span id="book-project"></span>

## Course project

Adapt and serve a small model, benchmark it, instrument it, and release it with rollback evidence.

Submit a short specification, an implementation or architecture, evidence from a baseline comparison, and one architecture decision record. Include one example that fails and explain how you would handle it.

## Suggested three-week schedule

- **Week 1:** Complete the first section and its checkpoint.
- **Week 2:** Complete the second section and start the project.
- **Week 3:** Complete the final section and the notebook workshop. Evaluate and review the project.

## Assessment

| Evidence | Weight |
|---|---:|
| Lecture knowledge checks | 20% |
| Runnable exercises and failure cases | 30% |
| Course project | 35% |
| Architecture defense and reflection | 15% |

## Anchor readings

- Hu et al. — LoRA
- Ouyang et al. — InstructGPT
- Official inference-server documentation

## Completion standard

Complete the lecture checks and section checkpoints, run the notebook workshop, and defend your project against a simpler alternative using the evidence you collected.

[All courses](../../courses/index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
