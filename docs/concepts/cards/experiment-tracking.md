# Experiment Tracking

**Purpose:** Reference card for **experiment tracking** used across AIEBOK books and knowledge areas.

## Core explanation

Experiment tracking logs hyperparameters, data versions, metrics, and artifacts for every training run. Without it, teams cannot reproduce or compare results.

## Example

Logging learning rate, seed, and dataset hash explains why run 47 beat run 46.

## Evidence of understanding

Reproduce a logged run from its metadata and verify metric within 1% of the original.

## Trade-offs

No mechanism is universal. Compare experiment tracking against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
