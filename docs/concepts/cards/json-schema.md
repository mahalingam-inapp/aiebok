# Json Schema

**Purpose:** Reference card for **json schema** used across AIEBOK books and knowledge areas.

## Core explanation

JSON Schema declares required fields, types, and constraints that validators enforce after model generation. It turns free-form text into typed data boundaries.

## Example

Rejecting payloads where 'total' is a string prevents silent accounting errors from plausible JSON.

## Evidence of understanding

Validate three intentionally invalid payloads and confirm distinct error reasons.

## Trade-offs

No mechanism is universal. Compare json schema against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
