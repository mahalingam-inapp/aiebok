# Correction

**Purpose:** Reference card for **correction** used across AIEBOK books and knowledge areas.

## Core explanation

Correction flows let users fix wrong AI outputs and feed improvements—labels, prompts, or models. Without correction, errors repeat silently.

## Example

Thumbs-down on answer captures expected response for eval set addition.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Track correction rate and time-to-incorporate into eval or training.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare correction against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Accessibility](../../concepts/cards/accessibility.md)
- [Citations](../../concepts/cards/citations.md)
- [Uncertainty Ux](../../concepts/cards/uncertainty-ux.md)
- [Undo](../../concepts/cards/undo.md)

## Related chapters

- [05 Human Centered Ai Ux](../../books/09-ai-software-and-product-engineering/05-human-centered-ai-ux.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
