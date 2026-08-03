# Context Poisoning

**Purpose:** Reference card for **context poisoning** used across AIEBOK books and knowledge areas.

## Core explanation

Context poisoning inserts false or misleading evidence into retrieval or memory stores to manipulate outputs. Integrity controls on indexes and ingestion are defenses.

## Example

An attacker uploads a fake policy PDF to skew answers about refund eligibility.

## Evidence of understanding

Monitor ingest sources, sign documents, and detect anomalous embedding clusters post-ingest.

## Trade-offs

No mechanism is universal. Compare context poisoning against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
