# Unit Tests

**Purpose:** Reference card for **unit tests** used across AIEBOK books and knowledge areas.

## Core explanation

Unit tests verify deterministic functions and components in isolation with fast feedback. They anchor quality while model behavior stays statistical.

## Example

Parser unit tests cover edge cases agents might not consider when editing.

## Evidence of understanding

Require ≥80% coverage on changed deterministic modules per PR policy.

## Trade-offs

No mechanism is universal. Compare unit tests against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
