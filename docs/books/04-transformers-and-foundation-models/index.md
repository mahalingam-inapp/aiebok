# Transformers and Foundation Models

Technical course 04 · 3 sections · 6 lectures · 10–12 hours of lecture and practice time, plus the project

Understand the architecture, training, inference, and model families behind modern generative AI.

[Start the first lecture](01-sequence-models-before-transformers.md){ .md-button .md-button--primary .study-start data-course="04-transformers-and-foundation-models" }
[Download the course notebook](../../assets/notebooks/04-transformers-and-foundation-models.ipynb){ .md-button download }

## Practice case · The meeting notes with the wrong owner

Asha reviews action items extracted from messy project transcripts. A teammate named twice is incorrectly assigned ownership for a different task. She needs a way to explain the failure to the project lead and compare a small local model with a hosted candidate without asking the team to trust the larger model by default.

This fictional case continues through the lectures.

For a documented comparison, read [When a better-liked model got harder to trust](../../casebook/model-behavior-rollback.md).

## Entry prerequisites

- Courses 01–03 or equivalent experience
- Matrix multiplication intuition
- Neural-network basics

## Course outline

### Sequence models and attention

- [01 · Sequence Models Before Transformers](01-sequence-models-before-transformers.md){ .study-lecture data-lecture="01-sequence-models-before-transformers.md" }
- [02 · Attention](02-attention.md){ .study-lecture data-lecture="02-attention.md" }

**Checkpoint**

Trace one attention query and identify which key contributes most to the weighted result.

### Transformer blocks and training

- [03 · The Transformer Block](03-the-transformer-block.md){ .study-lecture data-lecture="03-the-transformer-block.md" }
- [04 · Training Foundation Models](04-training-foundation-models.md){ .study-lecture data-lecture="04-training-foundation-models.md" }

**Checkpoint**

Draw the path through attention and the feed-forward block. Mark where training computes a loss.

### Decoding and model selection

- [05 · Inference and Sampling](05-inference-and-sampling.md){ .study-lecture data-lecture="05-inference-and-sampling.md" }
- [06 · Model Families and Selection](06-model-families-and-selection.md){ .study-lecture data-lecture="06-model-families-and-selection.md" }

**Checkpoint**

Compare decoding distributions at two temperatures. Pick a model selection metric for repeatability.

## Notebook workshop

Keep logits fixed, vary temperature, and compare the probability of the leading token. Explain why selection still needs a task-level evaluation.

The notebook includes each lecture's short demonstration and a checked exercise. For setup and execution, see [Course notebooks](../../labs/notebooks/index.md).

<span id="book-project"></span>

## Course project

Implement a tiny transformer and create a vendor-neutral model selection report.

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

- Vaswani et al. — Attention Is All You Need
- Devlin et al. — BERT
- Brown et al. — Language Models are Few-Shot Learners

## Completion standard

Complete the lecture checks and section checkpoints, run the notebook workshop, and defend your project against a simpler alternative using the evidence you collected.

[All courses](../../courses/index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
