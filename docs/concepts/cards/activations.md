# Activations

**Purpose:** Reference card for **activations** used across AIEBOK books and knowledge areas.

## Core explanation

Activation functions introduce nonlinearity—ReLU, GELU, sigmoid—without which deep networks collapse to linear maps. Choice affects gradient flow and training stability.

## Example

GELU in transformers smooths gradients compared to ReLU for language modeling at scale.

## Evidence of understanding

Compare training convergence with ReLU versus GELU on the same architecture and seed.

## Trade-offs

No mechanism is universal. Compare activations against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
