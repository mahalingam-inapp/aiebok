# Shared State

**Purpose:** Reference card for **shared state** used across AIEBOK books and knowledge areas.

## Core explanation

Shared state stores variables visible to multiple agents—task boards, evidence pools. Consistency requires versioning or transactional updates.

## Example

Research evidence store accumulates URLs all workers cite; stale entries need TTL.

## Evidence of understanding

Verify concurrent writes do not lose updates using version counters or locks.

## Trade-offs

No mechanism is universal. Compare shared state against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
