# Residual Connections

**Purpose:** Reference card for **residual connections** used across AIEBOK books and knowledge areas.

## Core explanation

Residual connections add layer inputs to outputs, easing gradient flow through deep stacks. They let layers learn incremental refinements instead of full remappings.

## Example

Transformer blocks compute attention(x) + x rather than attention(x) alone.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Train depth-12 with and without residuals and compare convergence speed.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare residual connections against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Mlp Blocks](../../concepts/cards/mlp-blocks.md)
- [Multi Head Attention](../../concepts/cards/multi-head-attention.md)
- [Normalization](../../concepts/cards/normalization.md)
- [Position](../../concepts/cards/position.md)

## Related chapters

- [03 The Transformer Block](../../books/04-transformers-and-foundation-models/03-the-transformer-block.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
