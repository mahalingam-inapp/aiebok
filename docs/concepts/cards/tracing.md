# Tracing

**Purpose:** Reference card for **tracing** used across AIEBOK books and knowledge areas.

## Core explanation

Tracing records spans for retrieval, model calls, tools, and validation with correlation IDs across services.

## Example

OpenTelemetry trace shows 400ms in reranker, 1.2s in LLM for slow request diagnosis.

## Evidence of understanding

Sample traces link 100% of P0 incidents to span breakdown within five minutes.

## Trade-offs

No mechanism is universal. Compare tracing against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
