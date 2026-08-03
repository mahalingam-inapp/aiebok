# Delimiters

**Purpose:** Reference card for **delimiters** used across AIEBOK books and knowledge areas.

## Core explanation

Delimiters—XML tags, markdown fences, triple quotes—separate instructions from data so models parse structure reliably. Consistent delimiters reduce instruction–content bleed.

## Example

Wrapping user HTML in <document> tags prevents tags from being interpreted as instructions.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Test ten adversarial documents with and without delimiters and count instruction-following errors.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare delimiters against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Constraints](../../concepts/cards/constraints.md)
- [Few Shot Examples](../../concepts/cards/few-shot-examples.md)
- [Instruction Hierarchy](../../concepts/cards/instruction-hierarchy.md)
- [Roles](../../concepts/cards/roles.md)

## Related chapters

- [01 Instructions That Work](../../books/05-prompt-and-context-engineering/01-instructions-that-work.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
