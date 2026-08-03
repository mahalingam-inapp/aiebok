# Uncertainty Ux

**Purpose:** Reference card for **uncertainty ux** used across AIEBOK books and knowledge areas.

## Core explanation

Uncertainty UX communicates confidence, limits, and alternatives so users calibrate trust. Hiding uncertainty causes overreliance on wrong answers.

## Example

Show 'I'm not sure—here are sources' instead of definitive tone on weak retrieval.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

User study: measure appropriate reliance rate with versus without confidence cues.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare uncertainty ux against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Accessibility](../../concepts/cards/accessibility.md)
- [Citations](../../concepts/cards/citations.md)
- [Correction](../../concepts/cards/correction.md)
- [Undo](../../concepts/cards/undo.md)

## Related chapters

- [05 Human Centered Ai Ux](../../books/09-ai-software-and-product-engineering/05-human-centered-ai-ux.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
