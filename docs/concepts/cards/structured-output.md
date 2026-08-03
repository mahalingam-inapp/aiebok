# Structured Output

**Purpose:** Reference card for **structured output** used across AIEBOK books and knowledge areas.

## Core explanation

Structured output forces models to emit machine-parseable formats—JSON, XML, tool calls—via prompting or constrained decoding. Parsers must still validate because models can violate schema.

## Example

An invoice extractor returns JSON fields consumed directly by ERP ingestion.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Measure schema pass rate on 200 adversarial and normal inputs post-generation.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare structured output against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Json Schema](../../concepts/cards/json-schema.md)
- [Repair](../../concepts/cards/repair.md)
- [Retries](../../concepts/cards/retries.md)
- [Validation](../../concepts/cards/validation.md)

## Related chapters

- [02 Structured Generation](../../books/05-prompt-and-context-engineering/02-structured-generation.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
