# Constraints

**Purpose:** Reference card for **constraints** used across AIEBOK books and knowledge areas.

## Core explanation

Constraints specify forbidden actions, length limits, formats, and scope boundaries in prompts. They reduce search space but must be testable.

## Example

'Do not mention competitors' and 'max 100 words' are enforceable constraints for eval.

## When to use

Use when behavior must change systematically across many examples and prompts alone cannot reach quality or format targets.

## When not to use

Skip when RAG, better prompts, or routing fix the gap with less regression risk.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Run constraint-violation checks on 100 outputs and track violation rate per release.

## Common failure modes

- Overfitting small curated sets
- Catastrophic forgetting of general capabilities
- Train-serve skew from preprocessing differences

## Trade-offs

No mechanism is universal. Compare constraints against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Delimiters](../../concepts/cards/delimiters.md)
- [Few Shot Examples](../../concepts/cards/few-shot-examples.md)
- [Instruction Hierarchy](../../concepts/cards/instruction-hierarchy.md)
- [Roles](../../concepts/cards/roles.md)

## Related chapters

- [01 Instructions That Work](../../books/05-prompt-and-context-engineering/01-instructions-that-work.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
