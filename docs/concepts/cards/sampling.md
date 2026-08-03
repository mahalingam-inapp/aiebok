# Sampling

**Purpose:** Reference card for **sampling** used across AIEBOK books and knowledge areas.

## Core explanation

Sampling draws next tokens from the predicted distribution rather than always taking the argmax. It enables diverse outputs but introduces nondeterminism unless seeded.

## Example

Creative writing uses sampling; factual extraction often uses greedy or low-temperature decoding.

## When to use

Use when optimizing latency, cost, or throughput of generation and serving paths.

## When not to use

Skip micro-optimizations before measuring end-to-end SLOs and quality slices.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Generate 20 completions at temperature 0 versus 1 and measure factual consistency.

## Common failure modes

- KV cache bugs causing repetition or truncation
- Sampling settings that look fluent but fail eval slices
- Batching that violates latency SLOs

## Trade-offs

No mechanism is universal. Compare sampling against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Baselines](../../concepts/cards/baselines.md)
- [Batching](../../concepts/cards/batching.md)
- [Data Leakage](../../concepts/cards/data-leakage.md)
- [Features And Labels](../../concepts/cards/features-and-labels.md)

## Related chapters

- [01 Problems Data And Baselines](../../books/02-machine-learning-systems/01-problems-data-and-baselines.md)
- [05 Inference And Sampling](../../books/04-transformers-and-foundation-models/05-inference-and-sampling.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
