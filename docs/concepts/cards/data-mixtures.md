# Data Mixtures

**Purpose:** Reference card for **data mixtures** used across AIEBOK books and knowledge areas.

## Core explanation

Data mixtures blend corpora—web, code, books, dialog—at tuned ratios during pretraining. Mixture proportions strongly affect capabilities and biases.

## Example

Over-weighting code improves programming but may hurt conversational tone.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Ablate one corpus slice from the mixture and measure task-specific eval deltas.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare data mixtures against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Checkpoints](../../concepts/cards/checkpoints.md)
- [Mixture Of Experts](../../concepts/cards/mixture-of-experts.md)
- [Pretraining Objectives](../../concepts/cards/pretraining-objectives.md)
- [Scaling Laws](../../concepts/cards/scaling-laws.md)

## Related chapters

- [04 Training Foundation Models](../../books/04-transformers-and-foundation-models/04-training-foundation-models.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
