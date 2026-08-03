# Build Versus Buy

**Purpose:** Reference card for **build versus buy** used across AIEBOK books and knowledge areas.

## Core explanation

Build versus buy weighs custom AI development against vendor APIs and platforms on control, cost, and time-to-value.

## Example

Buy GPT-4 API for prototype; build fine-tuned model when volume makes unit economics favorable.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

ADR comparing three-year TCO and risk for build versus buy options.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare build versus buy against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [A B Testing](../../concepts/cards/a-b-testing.md)
- [Adoption](../../concepts/cards/adoption.md)
- [Roi](../../concepts/cards/roi.md)
- [Task Success](../../concepts/cards/task-success.md)

## Related chapters

- [06 Experiments Adoption And Value](../../books/09-ai-software-and-product-engineering/06-experiments-adoption-and-value.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
