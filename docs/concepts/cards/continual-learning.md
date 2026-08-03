# Continual Learning

**Purpose:** Reference card for **continual learning** used across AIEBOK books and knowledge areas.

## Core explanation

Continual learning updates models on new data without catastrophic forgetting of prior tasks. Production systems often prefer explicit versioning and retraining over true continual learning today.

## Example

Adding new product SKUs to classifier without retraining on old SKUs should not collapse accuracy on legacy labels.

## Evidence of understanding

Measure accuracy on old and new task slices after incremental update versus full retrain baseline.

## Trade-offs

No mechanism is universal. Compare continual learning against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
