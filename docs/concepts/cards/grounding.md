# Grounding

**Purpose:** Reference card for **grounding** used across AIEBOK books and knowledge areas.

## Core explanation

Grounding ties model statements to verifiable evidence—retrieved passages, database rows, tool outputs. Ungrounded generation is speculation presented as fact.

## Example

Support answers should quote the ticket macro article that authorizes the refund step.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Measure percent of claims with valid citations on a labeled answer set.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare grounding against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Fine Tuning](../../concepts/cards/fine-tuning.md)
- [Knowledge Freshness](../../concepts/cards/knowledge-freshness.md)
- [Retrieval](../../concepts/cards/retrieval.md)
- [Structured Data](../../concepts/cards/structured-data.md)

## Related chapters

- [01 Knowledge Outside The Model](../../books/06-knowledge-and-retrieval-systems/01-knowledge-outside-the-model.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
