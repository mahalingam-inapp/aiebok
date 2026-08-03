# Slice Analysis

**Purpose:** Reference card for **slice analysis** used across AIEBOK books and knowledge areas.

## Core explanation

Slice analysis evaluates metrics on subpopulations—language, product, tenant—to catch aggregate illusions. A model can pass overall while failing high-value segments.

## Example

95% accuracy overall can hide 60% on enterprise accounts or non-English queries.

## Evidence of understanding

Define three production-representative slices and require each meets its release threshold.

## Trade-offs

No mechanism is universal. Compare slice analysis against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
