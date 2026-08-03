# Freshness

**Purpose:** Reference card for **freshness** used across AIEBOK books and knowledge areas.

## Core explanation

Freshness policies define acceptable document age, re-ingest cadence, and TTL for cached answers. Regulated domains often require sub-daily updates for policy corpora.

## Example

Benefits enrollment answers must exclude documents marked superseded after open enrollment ends.

## Evidence of understanding

Reject or downgrade chunks where ingest_timestamp exceeds freshness SLA for the topic.

## Trade-offs

No mechanism is universal. Compare freshness against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
