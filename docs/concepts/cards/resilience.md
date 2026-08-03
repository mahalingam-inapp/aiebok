# Resilience

**Purpose:** Reference card for **resilience** used across AIEBOK books and knowledge areas.

## Core explanation

Resilience designs for partial failure—retries, circuit breakers, multi-region—without total service loss.

## Example

Circuit breaker stops calling failing embedding API after 50% errors, uses lexical only.

## Evidence of understanding

Fault injection test: verify graceful degradation and recovery per runbook.

## Trade-offs

No mechanism is universal. Compare resilience against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
