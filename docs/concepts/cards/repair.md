# Repair

**Purpose:** Reference card for **repair** used across AIEBOK books and knowledge areas.

## Core explanation

Repair loops attempt to fix invalid model outputs—re-prompting with errors, partial parsing, or constrained retries. They improve yield but add latency and cost.

## Example

When JSON is malformed, a repair prompt includes the parse error and asks for correction.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Track repair success rate and average extra tokens per successful repair.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare repair against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Json Schema](../../concepts/cards/json-schema.md)
- [Retries](../../concepts/cards/retries.md)
- [Structured Output](../../concepts/cards/structured-output.md)
- [Validation](../../concepts/cards/validation.md)

## Related chapters

- [02 Structured Generation](../../books/05-prompt-and-context-engineering/02-structured-generation.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
