# Versioning

**Purpose:** Reference card for **versioning** used across AIEBOK books and knowledge areas.

## Core explanation

Versioning tracks prompts, models, indexes, and eval suites so changes are attributable and reversible.

## Example

Prod trace includes prompt v3.1, model llama-3-8b-q4, index 2024-06-01.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Rollback drill: revert one version dimension and restore prior metric within one hour.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare versioning against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Canaries](../../concepts/cards/canaries.md)
- [Continuous Evaluation](../../concepts/cards/continuous-evaluation.md)
- [Finops](../../concepts/cards/finops.md)
- [Tracing](../../concepts/cards/tracing.md)

## Related chapters

- [06 Llmops](../../books/11-training-serving-and-ai-operations/06-llmops.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
