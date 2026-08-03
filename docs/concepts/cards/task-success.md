# Task Success

**Purpose:** Reference card for **task success** used across AIEBOK books and knowledge areas.

## Core explanation

Task success measures whether users completed their intended job with acceptable quality—not click-through on AI features.

## Example

User submitted correct expense report without support contact counts as success.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Define success per job; sample sessions and label pass/fail weekly.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare task success against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [A B Testing](../../concepts/cards/a-b-testing.md)
- [Adoption](../../concepts/cards/adoption.md)
- [Build Versus Buy](../../concepts/cards/build-versus-buy.md)
- [Roi](../../concepts/cards/roi.md)

## Related chapters

- [06 Experiments Adoption And Value](../../books/09-ai-software-and-product-engineering/06-experiments-adoption-and-value.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
