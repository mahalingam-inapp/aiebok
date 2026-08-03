# Canaries

**Purpose:** Reference card for **canaries** used across AIEBOK books and knowledge areas.

## Core explanation

Canaries route small traffic percentage to new versions before full rollout.

## Example

5% traffic to new embedding index for 24h comparing recall and latency.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Auto-rollback canary if error rate or primary metric degrades beyond bound.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare canaries against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Continuous Evaluation](../../concepts/cards/continuous-evaluation.md)
- [Finops](../../concepts/cards/finops.md)
- [Tracing](../../concepts/cards/tracing.md)
- [Versioning](../../concepts/cards/versioning.md)

## Related chapters

- [06 Llmops](../../books/11-training-serving-and-ai-operations/06-llmops.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
