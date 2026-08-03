# Confusion Matrix

**Purpose:** Reference card for **confusion matrix** used across AIEBOK books and knowledge areas.

## Core explanation

A confusion matrix counts predicted versus actual classes, exposing which errors dominate. It is essential when classes are imbalanced or costs asymmetric.

## Example

A router may confuse 'billing' with 'refund' while rarely missing 'outage'—the matrix shows where to invest labeling.

## Evidence of understanding

Compute per-class precision and recall from the matrix on a stratified test set.

## Trade-offs

No mechanism is universal. Compare confusion matrix against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
