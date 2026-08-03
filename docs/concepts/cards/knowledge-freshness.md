# Knowledge Freshness

**Purpose:** Reference card for **knowledge freshness** used across AIEBOK books and knowledge areas.

## Core explanation

Knowledge freshness measures how current stored facts are relative to the real world. Stale indexes cause confident wrong answers until re-ingestion catches up.

## Example

A travel policy updated yesterday is invisible if the index last synced last month.

## Evidence of understanding

Track max document age in retrieved sets and alert when any source exceeds SLA staleness.

## Trade-offs

No mechanism is universal. Compare knowledge freshness against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
