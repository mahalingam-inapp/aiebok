# Position

**Purpose:** Reference card for **position** used across AIEBOK books and knowledge areas.

## Core explanation

Position information tells transformers token order since self-attention is permutation-invariant without it. Methods include sinusoidal, learned, and rotary (RoPE) encodings.

## Example

Rotary embeddings encode relative position in Q/K products for long-context models.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Shuffle token order without position encodings and observe catastrophic perplexity increase.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare position against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Mlp Blocks](../../concepts/cards/mlp-blocks.md)
- [Multi Head Attention](../../concepts/cards/multi-head-attention.md)
- [Normalization](../../concepts/cards/normalization.md)
- [Residual Connections](../../concepts/cards/residual-connections.md)

## Related chapters

- [03 The Transformer Block](../../books/04-transformers-and-foundation-models/03-the-transformer-block.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
