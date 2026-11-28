# Continuous Batching

**Purpose:** Reference card for **continuous batching** used across AIEBOK books and knowledge areas.

## Core explanation

Continuous batching schedules active and newly arriving requests together at generation-step boundaries. It changes utilization and queueing, especially when inputs and outputs vary in length.

## Example

When a short request finishes, a new request can occupy its capacity while other requests continue decoding.

## When to use

Use when request lengths vary and generation steps leave reusable capacity.

## When not to use

Single-request latency benchmarks cannot justify changing a shared scheduler.

## Engineering checklist

- Benchmark short and long requests at several arrival rates.

## Evidence of understanding

Report time to first token, inter-token latency and throughput by concurrency and prompt-length cohort.

## Common failure modes

- Higher throughput conceals increased time to first token for cold requests.

## Trade-offs

No mechanism is universal. Compare continuous batching against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- [Run the course practicum](../../courses/reasoning-efficient-inference/index.md)
- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
