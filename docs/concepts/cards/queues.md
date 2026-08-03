# Queues

**Purpose:** Reference card for **queues** used across AIEBOK books and knowledge areas.

## Core explanation

Queues decouple agent work submission from processing, smoothing load and enabling retries. Poison messages need dead-letter handling.

## Example

Approval tasks queue while humans respond; workers poll with backoff.

## Evidence of understanding

Measure queue depth p95 and time-to-drain under 2× normal submit rate.

## Trade-offs

No mechanism is universal. Compare queues against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
