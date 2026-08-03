# Citation Precision

**Purpose:** Reference card for **citation precision** used across AIEBOK books and knowledge areas.

## Core explanation

Citation precision measures whether cited sources actually support the adjacent claims. Wrong citations destroy trust faster than no citations.

## Example

Linking a harassment policy to answer a parking question is high-recall citation but zero precision.

## When to use

Use before every release, model swap, prompt change, or retrieval index migration.

## When not to use

Skip aggregate-only metrics when slices or safety cases can hide regressions.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.
- Report worst-slice performance, not aggregate alone.

## Evidence of understanding

Manually audit 50 claim–citation pairs and report precision and unsupported-claim rate.

## Common failure modes

- Benchmark overfitting without production-like queries
- Stale eval sets that no longer match user behavior
- LLM judges drifting from human standards

## Trade-offs

No mechanism is universal. Compare citation precision against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Abstention](../../concepts/cards/abstention.md)
- [Answer Validation](../../concepts/cards/answer-validation.md)
- [Faithfulness](../../concepts/cards/faithfulness.md)
- [Grounded Generation](../../concepts/cards/grounded-generation.md)

## Related chapters

- [05 Rag Generation And Citations](../../books/06-knowledge-and-retrieval-systems/05-rag-generation-and-citations.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
