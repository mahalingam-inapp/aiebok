# Drift

**Purpose:** Reference card for **drift** used across AIEBOK books and knowledge areas.

## Core explanation

Drift is change in input or label distributions over time—covariate, prior, or concept drift. Unmonitored drift erodes model value without code changes.

## Example

New product vocabulary after a launch shifts ticket text while labels stay stable—covariate drift.

## Evidence of understanding

Monitor population stability index or embedding centroid shift weekly with alert thresholds.

## Trade-offs

No mechanism is universal. Compare drift against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
