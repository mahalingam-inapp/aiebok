# Residual Connections

**Purpose:** Reference card for **residual connections** used across AIEBOK books and knowledge areas.

## Core explanation

Residual connections add layer inputs to outputs, easing gradient flow through deep stacks. They let layers learn incremental refinements instead of full remappings.

## Example

Transformer blocks compute attention(x) + x rather than attention(x) alone.

## Evidence of understanding

Train depth-12 with and without residuals and compare convergence speed.

## Trade-offs

No mechanism is universal. Compare residual connections against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
