# Attention Masks

**Purpose:** Reference card for **attention masks** used across AIEBOK books and knowledge areas.

## Core explanation

Attention masks zero out disallowed positions—future tokens in decoding, padding, or cross-segment boundaries. Masks enforce causality and ignore irrelevant tokens.

## Example

Causal masks prevent a language model from peeking at answer tokens during training.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Apply a causal mask and confirm no weight connects position i to j > i.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare attention masks against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Keys](../../concepts/cards/keys.md)
- [Queries](../../concepts/cards/queries.md)
- [Scaled Dot Product](../../concepts/cards/scaled-dot-product.md)
- [Values](../../concepts/cards/values.md)

## Related chapters

- [02 Attention](../../books/04-transformers-and-foundation-models/02-attention.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
