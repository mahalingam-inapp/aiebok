# Citations

**Purpose:** Reference card for **citations** used across AIEBOK books and knowledge areas.

## Core explanation

Citations link UI claims to source passages users can verify. They must be accurate, clickable, and adjacent to the supported statement.

## Example

Refund policy answer includes link jumping to handbook section 4.2.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Audit 50 UI citations for precision and broken links monthly.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare citations against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Accessibility](../../concepts/cards/accessibility.md)
- [Correction](../../concepts/cards/correction.md)
- [Uncertainty Ux](../../concepts/cards/uncertainty-ux.md)
- [Undo](../../concepts/cards/undo.md)

## Related chapters

- [05 Human Centered Ai Ux](../../books/09-ai-software-and-product-engineering/05-human-centered-ai-ux.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
