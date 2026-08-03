# Release Gates

**Purpose:** Reference card for **release gates** used across AIEBOK books and knowledge areas.

## Core explanation

Release gates block deployment until eval, security, and performance criteria pass. They encode organizational risk tolerance numerically.

## Example

No deploy if faithfulness drops >2 points or p95 latency exceeds SLO.

## Evidence of understanding

Automate gate checks in CI/CD with auditable pass/fail artifacts.

## Trade-offs

No mechanism is universal. Compare release gates against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
