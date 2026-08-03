# Grounded Generation

**Purpose:** Reference card for **grounded generation** used across AIEBOK books and knowledge areas.

## Core explanation

Grounded generation conditions answers strictly on provided evidence, refusing when support is insufficient. Prompts and validators enforce cite-or-abstain behavior.

## Example

The model quotes section 4.2 for refund rules instead of inventing a 30-day window.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Score faithfulness and abstention rate on cases with and without supporting passages.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare grounded generation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Abstention](../../concepts/cards/abstention.md)
- [Answer Validation](../../concepts/cards/answer-validation.md)
- [Citation Precision](../../concepts/cards/citation-precision.md)
- [Faithfulness](../../concepts/cards/faithfulness.md)

## Related chapters

- [05 Rag Generation And Citations](../../books/06-knowledge-and-retrieval-systems/05-rag-generation-and-citations.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
