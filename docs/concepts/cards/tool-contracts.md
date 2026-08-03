# Tool Contracts

**Purpose:** Reference card for **tool contracts** used across AIEBOK books and knowledge areas.

## Core explanation

Tool contracts specify schemas, auth, idempotency, errors, and SLAs for each agent tool. They are integration boundaries models depend on.

## Example

search_docs contract promises p95 500ms, max 10 results, ReadScope auth.

## Evidence of understanding

Contract tests mock failures and verify agent handles each error code.

## Trade-offs

No mechanism is universal. Compare tool contracts against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
