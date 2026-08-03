# Structured Data

**Purpose:** Reference card for **structured data** used across AIEBOK books and knowledge areas.

## Core explanation

Structured data lives in tables, APIs, and graphs with typed fields—better for precise queries than prose retrieval. Hybrid systems route quantitative questions to SQL, not RAG alone.

## Example

'How many open P1 incidents?' needs a database query, not semantic search over runbooks.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Route ten numeric questions to structured tools and verify answers match ground truth.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare structured data against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Fine Tuning](../../concepts/cards/fine-tuning.md)
- [Grounding](../../concepts/cards/grounding.md)
- [Knowledge Freshness](../../concepts/cards/knowledge-freshness.md)
- [Retrieval](../../concepts/cards/retrieval.md)

## Related chapters

- [01 Knowledge Outside The Model](../../books/06-knowledge-and-retrieval-systems/01-knowledge-outside-the-model.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
