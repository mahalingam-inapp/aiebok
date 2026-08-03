# Tool Discovery

**Purpose:** Reference card for **tool discovery** used across AIEBOK books and knowledge areas.

## Core explanation

Tool discovery lets clients list available tools and schemas at runtime instead of hardcoding integrations. Discovery responses must be filtered by permission.

## Example

A client sees only search_docs, not admin_delete, when connected with read-only scope.

## Evidence of understanding

Compare discovered tool list across role configurations in automated tests.

## Trade-offs

No mechanism is universal. Compare tool discovery against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
