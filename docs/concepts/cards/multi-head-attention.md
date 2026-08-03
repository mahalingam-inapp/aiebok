# Multi Head Attention

**Purpose:** Reference card for **multi head attention** used across AIEBOK books and knowledge areas.

## Core explanation

Multi-head attention runs several attention operations in parallel with separate projections, letting different heads capture diverse relations. Heads are often redundant but increase capacity.

## Example

One head may track syntax; another tracks coreference in the same layer.

## Evidence of understanding

Ablate heads individually and measure perplexity or task metric impact per head.

## Trade-offs

No mechanism is universal. Compare multi head attention against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
