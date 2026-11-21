# Machine Learning Systems

Technical course 02 · 3 sections · 6 lectures · 10–12 hours of lecture and practice time, plus the project

Learn how models are trained, validated, diagnosed, and integrated into reliable software systems.

[Start the first lecture](01-problems-data-and-baselines.md){ .md-button .md-button--primary }
[Download the course notebook](../../assets/notebooks/02-machine-learning-systems.ipynb){ .md-button download }

## Entry prerequisites

- Course 01 or equivalent experience
- Basic Python
- Graphs and averages

## Course outline

### Problem framing and supervised models

- [01 · Problems, Data, and Baselines](01-problems-data-and-baselines.md)
- [02 · Supervised Learning](02-supervised-learning.md)

**Checkpoint**

Define a prediction cutoff and a naive baseline. Identify a feature available only after the cutoff.

### Representations and neural networks

- [03 · Unsupervised and Representation Learning](03-unsupervised-and-representation-learning.md)
- [04 · Neural Networks](04-neural-networks.md)

**Checkpoint**

Compare fitting a line with learning an intermediate representation. Name an input for which a line would be inadequate.

### Evidence and lifecycle

- [05 · Evaluation and Error Analysis](05-evaluation-and-error-analysis.md)
- [06 · The ML Lifecycle](06-the-ml-lifecycle.md)

**Checkpoint**

Define a holdout slice and a rollback trigger. Explain which metric would detect the failure first.

## Notebook workshop

Add a held-out point and compare the trained line with the mean of the training labels. Keep the held-out point outside DATA.

The notebook includes each lecture's short demonstration and a checked exercise. For setup and execution, see [Course notebooks](../../labs/notebooks/index.md).

<span id="book-project"></span>

## Course project

Deliver a prediction service with a data card, baseline, evaluation report, error analysis, and monitoring plan.

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

- Hastie, Tibshirani & Friedman — The Elements of Statistical Learning
- Mitchell — Machine Learning

## Completion standard

Complete the lecture checks and section checkpoints, run the notebook workshop, and defend your project against a simpler alternative using the evidence you collected.

[All courses](../../courses/index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
