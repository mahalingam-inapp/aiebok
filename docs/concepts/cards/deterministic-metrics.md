# Deterministic Metrics

**Purpose:** Reference card for **deterministic metrics** used across AIEBOK books and knowledge areas.

## Core explanation

Deterministic metrics—exact match, F1 on spans, JSON validity—give reproducible scores without sampling variance.

## Example

Schema validation pass rate is deterministic; helpfulness often is not.

## Evidence of understanding

Prefer deterministic metrics for CI gates; use statistical metrics with confidence intervals for quality tracking.

## Trade-offs

No mechanism is universal. Compare deterministic metrics against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
