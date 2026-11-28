# Expert Parallelism

**Purpose:** Reference card for **expert parallelism** used across AIEBOK books and knowledge areas.

## Core explanation

Expert parallelism places different feed-forward experts on different devices. Routed activations travel to the selected expert and back, so communication and the slowest rank can dominate a step.

## Example

A rank running rare experts has spare capacity while a remote rank serving a popular expert is saturated.

## When to use

Use when a device cannot efficiently host the entire expert bank.

## When not to use

Avoid increasing parallelism if small batches cannot amortize synchronization.

## Engineering checklist

- Measure local and remote assignments and record maximum rank load.

## Evidence of understanding

Compare traffic, per-rank load, queueing and p95 latency at fixed batch and sequence lengths.

## Common failure modes

- A straggler rank dominates latency despite low average utilization.

## Trade-offs

No mechanism is universal. Compare expert parallelism against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- [Run the course practicum](../../courses/sparse-model-architectures/index.md)
- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
