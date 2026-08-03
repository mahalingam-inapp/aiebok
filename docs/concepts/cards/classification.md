# Classification

**Purpose:** Reference card for **classification** used across AIEBOK books and knowledge areas.

## Core explanation

Classification assigns inputs to discrete categories via scores converted to labels. Thresholds, class imbalance, and cost asymmetry matter as much as raw accuracy.

## Example

Binary fraud classification at 0.5 default threshold wastes money when false positives cost $2 and false negatives cost $200.

## Evidence of understanding

Publish confusion matrix and per-class recall on a stratified validation set.

## Trade-offs

No mechanism is universal. Compare classification against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
