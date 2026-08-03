# Batching

**Purpose:** Reference card for **batching** used across AIEBOK books and knowledge areas.

## Core explanation

Batching groups requests to amortize GPU kernel overhead, improving throughput at possible latency cost. Continuous batching in servers interleaves sequences of different lengths.

## Example

Batch size 32 may double throughput versus batch 1 but increase p95 latency for short prompts.

## Evidence of understanding

Load-test at concurrency 1, 8, and 32; report throughput and p95 latency.

## Trade-offs

No mechanism is universal. Compare batching against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
