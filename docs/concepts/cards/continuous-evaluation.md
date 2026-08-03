# Continuous Evaluation

**Purpose:** Reference card for **continuous evaluation** used across AIEBOK books and knowledge areas.

## Core explanation

Continuous evaluation runs production or shadow traffic against eval suites to detect drift post-release.

## Example

Nightly job scores 500 sampled prod queries with LLM judge against rubric.

## Evidence of understanding

Alert when rolling 7-day faithfulness drops below threshold versus launch baseline.

## Trade-offs

No mechanism is universal. Compare continuous evaluation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
