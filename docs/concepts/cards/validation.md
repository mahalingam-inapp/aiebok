# Validation

**Purpose:** Reference card for **validation** used across AIEBOK books and knowledge areas.

## Core explanation

Validation checks model outputs against schemas, business rules, and safety policies before downstream use. It belongs in application code, not trust in model compliance.

## Example

A date field must parse as ISO-8601 and fall within contract term bounds.

## Evidence of understanding

Define ten validation rules and report pass rate on production sample weekly.

## Trade-offs

No mechanism is universal. Compare validation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
