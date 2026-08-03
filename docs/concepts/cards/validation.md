# Validation

**Purpose:** Reference card for **validation** used across AIEBOK books and knowledge areas.

## Core explanation

Validation checks model outputs against schemas, business rules, and safety policies before downstream use. It belongs in application code, not trust in model compliance.

## Example

A date field must parse as ISO-8601 and fall within contract term bounds.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Define ten validation rules and report pass rate on production sample weekly.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare validation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Json Schema](../../concepts/cards/json-schema.md)
- [Repair](../../concepts/cards/repair.md)
- [Retries](../../concepts/cards/retries.md)
- [Structured Output](../../concepts/cards/structured-output.md)

## Related chapters

- [02 Structured Generation](../../books/05-prompt-and-context-engineering/02-structured-generation.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
