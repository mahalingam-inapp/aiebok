# Logits

**Purpose:** Reference card for **logits** used across AIEBOK books and knowledge areas.

## Core explanation

Logits are raw pre-softmax scores over the vocabulary for the next token. Decoding policies—temperature, top-k—operate on logits before sampling.

## Example

Inspecting logits reveals whether the model hesitates between two equally likely tokens.

## When to use

Use when optimizing latency, cost, or throughput of generation and serving paths.

## When not to use

Skip micro-optimizations before measuring end-to-end SLOs and quality slices.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Log top-5 logits for ten prompts and verify sampling changes when temperature increases.

## Common failure modes

- KV cache bugs causing repetition or truncation
- Sampling settings that look fluent but fail eval slices
- Batching that violates latency SLOs

## Trade-offs

No mechanism is universal. Compare logits against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Batching](../../concepts/cards/batching.md)
- [Kv Cache](../../concepts/cards/kv-cache.md)
- [Sampling](../../concepts/cards/sampling.md)
- [Temperature](../../concepts/cards/temperature.md)

## Related chapters

- [05 Inference And Sampling](../../books/04-transformers-and-foundation-models/05-inference-and-sampling.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
