# Distribution Shift

**Purpose:** Reference card for **distribution shift** used across AIEBOK books and knowledge areas.

## Core explanation

Distribution shift occurs when deployment data differs from training data in language, demographics, seasonality, or product mix. Models degrade silently when shift is unmonitored.

## Example

A model trained pre-acquisition fails on the acquired company's ticket vocabulary until retrained or augmented.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Monitor slice metrics weekly and alert when any slice drops more than five points from its baseline.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare distribution shift against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Bias And Variance](../../concepts/cards/bias-and-variance.md)
- [Generalization](../../concepts/cards/generalization.md)
- [Inference](../../concepts/cards/inference.md)
- [Training](../../concepts/cards/training.md)

## Related chapters

- [05 Learning And Generalization](../../books/01-foundations-of-intelligence/05-learning-and-generalization.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
