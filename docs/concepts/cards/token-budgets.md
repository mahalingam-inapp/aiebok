# Token Budgets

**Purpose:** Reference card for **token budgets** used across AIEBOK books and knowledge areas.

## Core explanation

Token budgets cap how many tokens each prompt section—system, evidence, user—may consume. Hard budgets prevent silent truncation of safety instructions.

## Example

Allocating 2k tokens to evidence and 500 to instructions ensures policy text survives long retrievals.

## When to use

Use when optimizing latency, cost, or throughput of generation and serving paths.

## When not to use

Skip micro-optimizations before measuring end-to-end SLOs and quality slices.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Log token counts per section and alert when any section exceeds its budget before send.

## Common failure modes

- KV cache bugs causing repetition or truncation
- Sampling settings that look fluent but fail eval slices
- Batching that violates latency SLOs

## Trade-offs

No mechanism is universal. Compare token budgets against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Bpe](../../concepts/cards/bpe.md)
- [Sentencepiece](../../concepts/cards/sentencepiece.md)
- [Subwords](../../concepts/cards/subwords.md)
- [Vocabulary](../../concepts/cards/vocabulary.md)

## Related chapters

- [03 Tokenization](../../books/03-language-and-representation/03-tokenization.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
