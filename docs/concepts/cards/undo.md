# Undo

**Purpose:** Reference card for **undo** used across AIEBOK books and knowledge areas.

## Core explanation

Undo reverses AI-initiated or AI-assisted actions within a safe window. It is essential when actions affect user data or send communications.

## Example

Auto-drafted email can be undone for 30 seconds before SMTP send.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Verify undo restores prior state exactly on ten action types.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare undo against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Accessibility](../../concepts/cards/accessibility.md)
- [Citations](../../concepts/cards/citations.md)
- [Correction](../../concepts/cards/correction.md)
- [Uncertainty Ux](../../concepts/cards/uncertainty-ux.md)

## Related chapters

- [05 Human Centered Ai Ux](../../books/09-ai-software-and-product-engineering/05-human-centered-ai-ux.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
