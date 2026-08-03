# Context Windows

**Purpose:** Reference card for **context windows** used across AIEBOK books and knowledge areas.

## Core explanation

Context windows cap tokens the model attends to in one forward pass—prompt, evidence, tools, and output compete for this budget.

## Example

A 128k window still requires prioritization when ten long documents are retrieved.

## When to use

Use when optimizing latency, cost, or throughput of generation and serving paths.

## When not to use

Skip micro-optimizations before measuring end-to-end SLOs and quality slices.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Measure task quality versus tokens used and find the knee of the curve for your workload.

## Common failure modes

- KV cache bugs causing repetition or truncation
- Sampling settings that look fluent but fail eval slices
- Batching that violates latency SLOs

## Trade-offs

No mechanism is universal. Compare context windows against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Compression](../../concepts/cards/compression.md)
- [Context Assembly](../../concepts/cards/context-assembly.md)
- [Ranking](../../concepts/cards/ranking.md)
- [Token Budgeting](../../concepts/cards/token-budgeting.md)

## Related chapters

- [03 Context Construction](../../books/05-prompt-and-context-engineering/03-context-construction.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
