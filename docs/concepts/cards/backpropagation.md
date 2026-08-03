# Backpropagation

**Purpose:** Reference card for **backpropagation** used across AIEBOK books and knowledge areas.

## Core explanation

Backpropagation applies the chain rule to compute gradients through layered computations efficiently. It enables training deep networks but requires careful initialization and normalization.

## Example

One backward pass from loss to weights updates every layer in a classifier simultaneously.

## Evidence of understanding

Verify gradients with finite differences on a tiny network for one batch.

## Trade-offs

No mechanism is universal. Compare backpropagation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
