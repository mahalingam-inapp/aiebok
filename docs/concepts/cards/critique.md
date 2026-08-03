# Critique

**Purpose:** Reference card for **critique** used across AIEBOK books and knowledge areas.

## Core explanation

Critique models or rubrics evaluate drafts and suggest fixes before finalization. Separating generation from critique reduces shared blind spots.

## Example

A critic flags unsupported claims in a research draft before user delivery.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Measure error reduction with generate-then-critique versus single-pass on 50 tasks.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare critique against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Best Of N](../../concepts/cards/best-of-n.md)
- [Self Consistency](../../concepts/cards/self-consistency.md)
- [Tests](../../concepts/cards/tests.md)
- [Verifiers](../../concepts/cards/verifiers.md)

## Related chapters

- [03 Verification And Critique](../../books/07-reasoning-and-tool-use/03-verification-and-critique.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
