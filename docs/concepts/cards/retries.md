# Retries

**Purpose:** Reference card for **retries** used across AIEBOK books and knowledge areas.

## Core explanation

Retries re-invoke models or tools after transient failures or validation misses, with backoff and limits. Unbounded retries cause runaway cost and duplicate side effects.

## Example

Three retries with exponential backoff on 429 rate limits recover most requests without overload.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Cap retries at N and measure success rate versus total token spend.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare retries against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Json Schema](../../concepts/cards/json-schema.md)
- [Repair](../../concepts/cards/repair.md)
- [Structured Output](../../concepts/cards/structured-output.md)
- [Validation](../../concepts/cards/validation.md)

## Related chapters

- [02 Structured Generation](../../books/05-prompt-and-context-engineering/02-structured-generation.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
