# Latency

**Purpose:** Reference card for **latency** used across AIEBOK books and knowledge areas.

## Core explanation

Latency is time from request to usable response—dominated by model, retrieval, tools, and serialization. User workflows break when p95 exceeds interaction tolerance.

## Example

Adding reranking adds 200ms; measure whether task success gain justifies it.

## Evidence of understanding

Track p50 and p95 end-to-end latency with breakdown by stage in traces.

## Trade-offs

No mechanism is universal. Compare latency against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
