# Slos

**Purpose:** Reference card for **slos** used across AIEBOK books and knowledge areas.

## Core explanation

SLOs define target reliability and latency—availability, p95 latency, eval faithfulness—for AI platform services.

## Example

Gateway SLO: 99.9% availability, p95 <2s excluding model provider outages.

## Evidence of understanding

Error budget policy triggers feature freeze when SLO burn exceeds threshold.

## Trade-offs

No mechanism is universal. Compare slos against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
