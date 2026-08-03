# Calibration

**Purpose:** Reference card for **calibration** used across AIEBOK books and knowledge areas.

## Core explanation

Calibration means predicted probabilities align with observed frequencies—70% confidence should be right about 70% of the time. Uncalibrated scores mislead threshold and cost decisions.

## Example

A medical triage model with miscalibrated probabilities causes undertriage when 0.9 confidence actually means 0.6 accuracy.

## Evidence of understanding

Plot a reliability diagram and report expected calibration error before setting production thresholds.

## Trade-offs

No mechanism is universal. Compare calibration against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
