# Self Consistency

**Purpose:** Reference card for **self consistency** used across AIEBOK books and knowledge areas.

## Core explanation

Self-consistency samples multiple reasoning paths and aggregates answers by majority vote. It improves reliability when individual samples are noisy.

## Example

Five chain-of-thought samples that agree on '42' outweigh one outlier '41'.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare accuracy of majority vote versus single sample at equal total token budget.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare self consistency against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Best Of N](../../concepts/cards/best-of-n.md)
- [Critique](../../concepts/cards/critique.md)
- [Tests](../../concepts/cards/tests.md)
- [Verifiers](../../concepts/cards/verifiers.md)

## Related chapters

- [03 Verification And Critique](../../books/07-reasoning-and-tool-use/03-verification-and-critique.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
