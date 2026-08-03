# Roles

**Purpose:** Reference card for **roles** used across AIEBOK books and knowledge areas.

## Core explanation

Roles—system, user, assistant, tool—label message provenance and expected behavior in chat APIs. Misassigned roles confuse models about who said what.

## Example

Putting user text in the system role can unintentionally elevate it to trusted policy.

## Evidence of understanding

Swap roles on ten prompts and measure compliance change on a fixed eval set.

## Trade-offs

No mechanism is universal. Compare roles against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
