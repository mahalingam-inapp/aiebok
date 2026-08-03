# Role Isolation

**Purpose:** Reference card for **role isolation** used across AIEBOK books and knowledge areas.

## Core explanation

Role isolation restricts each agent to tools and data matching its role, limiting blast radius of compromise or error.

## Example

Billing agent cannot access HR records even if prompt requests it.

## Evidence of understanding

Attempt cross-role tool access in tests and expect hard denial.

## Trade-offs

No mechanism is universal. Compare role isolation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
