# Entropy

**Purpose:** Reference card for **entropy** used across AIEBOK books and knowledge areas.

## Core explanation

Entropy measures uncertainty or information content in a distribution—high when outcomes are evenly spread, low when one dominates. It guides feature selection, decision trees, and regularization.

## Example

A classifier with 95% softmax mass on one class is low-entropy and cheap to trust for routing; a flat distribution signals ambiguity worth escalating.

## Evidence of understanding

Compute entropy for a sharp and a flat softmax vector and tie each to an operational action.

## Trade-offs

No mechanism is universal. Compare entropy against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
