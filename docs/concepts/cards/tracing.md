# Tracing

**Purpose:** Reference card for **tracing** used across AIEBOK books and knowledge areas.

## Core explanation

Tracing records spans for retrieval, model calls, tools, and validation with correlation IDs across services.

## Example

OpenTelemetry trace shows 400ms in reranker, 1.2s in LLM for slow request diagnosis.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Sample traces link 100% of P0 incidents to span breakdown within five minutes.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare tracing against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Canaries](../../concepts/cards/canaries.md)
- [Continuous Evaluation](../../concepts/cards/continuous-evaluation.md)
- [Finops](../../concepts/cards/finops.md)
- [Versioning](../../concepts/cards/versioning.md)

## Related chapters

- [06 Llmops](../../books/11-training-serving-and-ai-operations/06-llmops.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
