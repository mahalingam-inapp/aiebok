# Compensation

**Purpose:** Reference card for **compensation** used across AIEBOK books and knowledge areas.

## Core explanation

Compensation undo or offsets partial effects when later steps fail—Saga pattern for agents. Without it, retries duplicate charges or records.

## Example

Failed booking after charge triggers automatic refund compensation transaction.

## Evidence of understanding

Simulate mid-saga failure and verify compensation returns system to pre-transaction state.

## Trade-offs

No mechanism is universal. Compare compensation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
