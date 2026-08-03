# Context Assembly

**Purpose:** Reference card for **context assembly** used across AIEBOK books and knowledge areas.

## Core explanation

Context assembly is the pipeline that gathers instructions, state, evidence, tools, and examples into the final prompt. Order and separation affect model behavior.

## Example

Placing evidence after instructions but before the user question reduces instruction drift in long contexts.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Trace one request's assembly stages and verify each section matches the spec template.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare context assembly against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Compression](../../concepts/cards/compression.md)
- [Context Windows](../../concepts/cards/context-windows.md)
- [Ranking](../../concepts/cards/ranking.md)
- [Token Budgeting](../../concepts/cards/token-budgeting.md)

## Related chapters

- [03 Context Construction](../../books/05-prompt-and-context-engineering/03-context-construction.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
