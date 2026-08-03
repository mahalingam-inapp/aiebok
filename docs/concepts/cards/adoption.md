# Adoption

**Purpose:** Reference card for **adoption** used across AIEBOK books and knowledge areas.

## Core explanation

Adoption tracks who uses the feature, how often, and whether usage persists after novelty fades.

## Example

80% weekly active support agents using suggest-reply after 60 days indicates adoption.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Plot cohort retention curve at 7, 30, and 90 days post-launch.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare adoption against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [A B Testing](../../concepts/cards/a-b-testing.md)
- [Build Versus Buy](../../concepts/cards/build-versus-buy.md)
- [Roi](../../concepts/cards/roi.md)
- [Task Success](../../concepts/cards/task-success.md)

## Related chapters

- [06 Experiments Adoption And Value](../../books/09-ai-software-and-product-engineering/06-experiments-adoption-and-value.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
