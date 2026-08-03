# Few Shot Examples

**Purpose:** Reference card for **few shot examples** used across AIEBOK books and knowledge areas.

## Core explanation

Few-shot examples demonstrate desired input–output patterns inside the prompt. They help format and tone but consume tokens and can overfit demo patterns.

## Example

Three invoice extraction examples teach field boundaries better than prose instructions alone.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare accuracy with zero, three, and ten shots on held-out invoices.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare few shot examples against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Constraints](../../concepts/cards/constraints.md)
- [Delimiters](../../concepts/cards/delimiters.md)
- [Instruction Hierarchy](../../concepts/cards/instruction-hierarchy.md)
- [Roles](../../concepts/cards/roles.md)

## Related chapters

- [01 Instructions That Work](../../books/05-prompt-and-context-engineering/01-instructions-that-work.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
