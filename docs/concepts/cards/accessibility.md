# Accessibility

**Purpose:** Reference card for **accessibility** used across AIEBOK books and knowledge areas.

## Core explanation

Accessibility ensures AI features work with screen readers, keyboard navigation, and assistive tech—not only visual chat UIs.

## Example

Streaming tokens must announce sensibly; citation links need accessible labels.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Run WCAG-oriented audit on primary AI flows and fix P1 issues before launch.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare accessibility against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Citations](../../concepts/cards/citations.md)
- [Correction](../../concepts/cards/correction.md)
- [Uncertainty Ux](../../concepts/cards/uncertainty-ux.md)
- [Undo](../../concepts/cards/undo.md)

## Related chapters

- [05 Human Centered Ai Ux](../../books/09-ai-software-and-product-engineering/05-human-centered-ai-ux.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
