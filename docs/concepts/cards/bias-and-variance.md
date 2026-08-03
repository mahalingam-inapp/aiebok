# Bias And Variance

**Purpose:** Reference card for **bias and variance** used across AIEBOK books and knowledge areas.

## Core explanation

Bias is systematic underfitting from overly simple models; variance is sensitivity to training noise from overly complex ones. Tuning trades these errors against compute and data volume.

## Example

A linear model underfits nonlinear fraud patterns (high bias); a huge tree overfits small samples (high variance).

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Plot error versus model capacity and identify the knee where validation error stops improving.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare bias and variance against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Distribution Shift](../../concepts/cards/distribution-shift.md)
- [Generalization](../../concepts/cards/generalization.md)
- [Inference](../../concepts/cards/inference.md)
- [Training](../../concepts/cards/training.md)

## Related chapters

- [05 Learning And Generalization](../../books/01-foundations-of-intelligence/05-learning-and-generalization.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
