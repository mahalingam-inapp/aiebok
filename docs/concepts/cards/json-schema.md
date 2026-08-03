# Json Schema

**Purpose:** Reference card for **json schema** used across AIEBOK books and knowledge areas.

## Core explanation

JSON Schema declares required fields, types, and constraints that validators enforce after model generation. It turns free-form text into typed data boundaries.

## Example

Rejecting payloads where 'total' is a string prevents silent accounting errors from plausible JSON.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Validate three intentionally invalid payloads and confirm distinct error reasons.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare json schema against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Repair](../../concepts/cards/repair.md)
- [Retries](../../concepts/cards/retries.md)
- [Structured Output](../../concepts/cards/structured-output.md)
- [Validation](../../concepts/cards/validation.md)

## Related chapters

- [02 Structured Generation](../../books/05-prompt-and-context-engineering/02-structured-generation.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
