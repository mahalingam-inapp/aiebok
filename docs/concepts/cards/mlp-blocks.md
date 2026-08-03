# Mlp Blocks

**Purpose:** Reference card for **mlp blocks** used across AIEBOK books and knowledge areas.

## Core explanation

MLP blocks apply position-wise feed-forward networks after attention, adding nonlinear capacity per token. They typically expand dimension 4× then project back.

## Example

FFN layers store factual associations in some interpretability studies of LMs.

## Evidence of understanding

Measure parameter count and FLOPs share of MLP versus attention in one block.

## Trade-offs

No mechanism is universal. Compare mlp blocks against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
