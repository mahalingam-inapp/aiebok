# Token Budgets

**Purpose:** Reference card for **token budgets** used across AIEBOK books and knowledge areas.

## Core explanation

Token budgets cap how many tokens each prompt section—system, evidence, user—may consume. Hard budgets prevent silent truncation of safety instructions.

## Example

Allocating 2k tokens to evidence and 500 to instructions ensures policy text survives long retrievals.

## Evidence of understanding

Log token counts per section and alert when any section exceeds its budget before send.

## Trade-offs

No mechanism is universal. Compare token budgets against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
