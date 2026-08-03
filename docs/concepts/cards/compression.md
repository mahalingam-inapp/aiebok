# Compression

**Purpose:** Reference card for **compression** used across AIEBOK books and knowledge areas.

## Core explanation

Context compression summarizes, extracts, or prunes evidence to fit token limits while preserving decision-critical facts. Lossy compression can drop citations or qualifiers.

## Example

Summarizing ten pages into bullet points may omit exception clauses unless extraction is structured.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Measure citation recall and answer correctness before and after compression at fixed budget.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare compression against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Context Assembly](../../concepts/cards/context-assembly.md)
- [Context Windows](../../concepts/cards/context-windows.md)
- [Ranking](../../concepts/cards/ranking.md)
- [Token Budgeting](../../concepts/cards/token-budgeting.md)

## Related chapters

- [03 Context Construction](../../books/05-prompt-and-context-engineering/03-context-construction.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
