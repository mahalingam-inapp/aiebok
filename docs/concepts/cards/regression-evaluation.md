# Regression Evaluation

**Purpose:** Reference card for **regression evaluation** used across AIEBOK books and knowledge areas.

## Core explanation

Regression evaluation re-runs fixed test suites after prompt or context changes to catch quality drops. It complements aggregate monitoring with known hard cases.

## Example

A 30-case eval set includes injection attempts and acronym queries that must never regress.

## Evidence of understanding

Block release if any P0 case fails or overall score drops more than two points.

## Trade-offs

No mechanism is universal. Compare regression evaluation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
