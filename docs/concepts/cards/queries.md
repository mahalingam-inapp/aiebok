# Queries

**Purpose:** Reference card for **queries** used across AIEBOK books and knowledge areas.

## Core explanation

In attention, queries represent what information a position seeks from other positions. They are learned projections of hidden states, not user search queries.

## Example

Each decoder token issues a query vector to attend over encoder keys during translation.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Visualize query-key dot products and verify peak weights align with alignments.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare queries against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Attention Masks](../../concepts/cards/attention-masks.md)
- [Keys](../../concepts/cards/keys.md)
- [Scaled Dot Product](../../concepts/cards/scaled-dot-product.md)
- [Values](../../concepts/cards/values.md)

## Related chapters

- [02 Attention](../../books/04-transformers-and-foundation-models/02-attention.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
