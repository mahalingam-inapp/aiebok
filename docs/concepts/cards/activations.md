# Activations

**Purpose:** Reference card for **activations** used across AIEBOK books and knowledge areas.

## Core explanation

Activation functions introduce nonlinearity—ReLU, GELU, sigmoid—without which deep networks collapse to linear maps. Choice affects gradient flow and training stability.

## Example

GELU in transformers smooths gradients compared to ReLU for language modeling at scale.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare training convergence with ReLU versus GELU on the same architecture and seed.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare activations against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Backpropagation](../../concepts/cards/backpropagation.md)
- [Neurons And Layers](../../concepts/cards/neurons-and-layers.md)
- [Normalization](../../concepts/cards/normalization.md)
- [Optimizers](../../concepts/cards/optimizers.md)

## Related chapters

- [04 Neural Networks](../../books/02-machine-learning-systems/04-neural-networks.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
