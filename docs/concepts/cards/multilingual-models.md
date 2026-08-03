# Multilingual Models

**Purpose:** Reference card for **multilingual models** used across AIEBOK books and knowledge areas.

## Core explanation

Multilingual models share parameters across languages, enabling cross-lingual retrieval and generation. Performance varies by language pair and training data balance.

## Example

A Spanish employee query can retrieve English policy text if the embedding space aligns concepts.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Evaluate recall@5 separately per language on parallel query sets.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare multilingual models against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Embedding Evaluation](../../concepts/cards/embedding-evaluation.md)
- [Hard Negatives](../../concepts/cards/hard-negatives.md)
- [Re Indexing](../../concepts/cards/re-indexing.md)
- [Vector Governance](../../concepts/cards/vector-governance.md)

## Related chapters

- [06 Embedding Systems In Production](../../books/03-language-and-representation/06-embedding-systems-in-production.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
