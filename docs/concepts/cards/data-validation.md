# Data Validation

**Purpose:** Reference card for **data validation** used across AIEBOK books and knowledge areas.

## Core explanation

Data validation checks schema, ranges, distributions, and freshness of incoming data before training or inference. Silent schema drift breaks pipelines quietly.

## Example

A new optional field arriving as null for 40% of rows should block training until investigated.

## Evidence of understanding

Run validation rules on daily ingest and alert when any column exceeds drift thresholds.

## Trade-offs

No mechanism is universal. Compare data validation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
