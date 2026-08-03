# Recovery

**Purpose:** Reference card for **recovery** used across AIEBOK books and knowledge areas.

## Core explanation

Recovery restores consistent state after crashes, tool failures, or partial commits. It requires durable checkpoints and compensating actions.

## Example

After payment timeout, recovery verifies ledger state before retry or refund.

## Evidence of understanding

Inject crash at each step and verify recovery reaches consistent terminal state.

## Trade-offs

No mechanism is universal. Compare recovery against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
