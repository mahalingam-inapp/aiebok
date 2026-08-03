# Latency

**Purpose:** Reference card for **latency** used across AIEBOK books and knowledge areas.

## Core explanation

Latency is time from request to usable response—dominated by model, retrieval, tools, and serialization. User workflows break when p95 exceeds interaction tolerance.

## Example

Adding reranking adds 200ms; measure whether task success gain justifies it.

## When to use

Use when optimizing latency, cost, or throughput of generation and serving paths.

## When not to use

Skip micro-optimizations before measuring end-to-end SLOs and quality slices.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Track p50 and p95 end-to-end latency with breakdown by stage in traces.

## Common failure modes

- KV cache bugs causing repetition or truncation
- Sampling settings that look fluent but fail eval slices
- Batching that violates latency SLOs

## Trade-offs

No mechanism is universal. Compare latency against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Budgets](../../concepts/cards/budgets.md)
- [Cost Quality Curves](../../concepts/cards/cost-quality-curves.md)
- [Routing](../../concepts/cards/routing.md)
- [Test Time Compute](../../concepts/cards/test-time-compute.md)

## Related chapters

- [06 Reasoning System Economics](../../books/07-reasoning-and-tool-use/06-reasoning-system-economics.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
