# Distribution Shift

**Purpose:** Reference card for **distribution shift** used across AIEBOK books and knowledge areas.

## Core explanation

Distribution shift occurs when deployment data differs from training data in language, demographics, seasonality, or product mix. Models degrade silently when shift is unmonitored.

## Example

A model trained pre-acquisition fails on the acquired company's ticket vocabulary until retrained or augmented.

## Evidence of understanding

Monitor slice metrics weekly and alert when any slice drops more than five points from its baseline.

## Trade-offs

No mechanism is universal. Compare distribution shift against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
