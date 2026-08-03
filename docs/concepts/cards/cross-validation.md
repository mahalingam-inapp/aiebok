# Cross Validation

**Purpose:** Reference card for **cross validation** used across AIEBOK books and knowledge areas.

## Core explanation

Cross-validation rotates train and validation folds to estimate performance variance with limited data. It reduces luck from a single split but must respect temporal or group structure when required.

## Example

K-fold on i.i.d. tabular data estimates variance; time-series tasks need forward-chaining instead.

## Evidence of understanding

Report mean and standard deviation of the metric across folds, not just the best fold.

## Trade-offs

No mechanism is universal. Compare cross validation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
