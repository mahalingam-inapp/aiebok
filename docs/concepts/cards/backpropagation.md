# Backpropagation

**Purpose:** Reference card for **backpropagation** used across AIEBOK books and knowledge areas.

## Core explanation

Backpropagation applies the chain rule to compute gradients through layered computations efficiently. It enables training deep networks but requires careful initialization and normalization.

## Example

One backward pass from loss to weights updates every layer in a classifier simultaneously.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Verify gradients with finite differences on a tiny network for one batch.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare backpropagation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Activations](../../concepts/cards/activations.md)
- [Neurons And Layers](../../concepts/cards/neurons-and-layers.md)
- [Normalization](../../concepts/cards/normalization.md)
- [Optimizers](../../concepts/cards/optimizers.md)

## Related chapters

- [04 Neural Networks](../../books/02-machine-learning-systems/04-neural-networks.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
