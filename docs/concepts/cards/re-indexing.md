# Re Indexing

**Purpose:** Reference card for **re indexing** used across AIEBOK books and knowledge areas.

## Core explanation

Re-indexing rebuilds search indexes after embedding model or chunking changes. It is a data migration with downtime, cost, and quality validation requirements.

## Example

Switching embedding models requires dual-running indexes until recall parity is proven.

## When to use

Use when answers must cite private or changing documents, identifiers and paraphrases both appear in queries, or model parametric knowledge is insufficient.

## When not to use

Skip when a deterministic query, small fixed FAQ, or fine-tuned behavior already meets requirements with lower ops cost.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.
- Version embedding model, index, and preprocessing together.

## Evidence of understanding

Compare recall@10 old versus new index on the same eval set before cutover.

## Common failure modes

- Recall failure on acronym-heavy or multi-hop questions
- Stale index after document or embedding model change
- Cross-tenant leakage when metadata filters are missing

## Trade-offs

No mechanism is universal. Compare re indexing against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Embedding Evaluation](../../concepts/cards/embedding-evaluation.md)
- [Hard Negatives](../../concepts/cards/hard-negatives.md)
- [Multilingual Models](../../concepts/cards/multilingual-models.md)
- [Vector Governance](../../concepts/cards/vector-governance.md)

## Related chapters

- [06 Embedding Systems In Production](../../books/03-language-and-representation/06-embedding-systems-in-production.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
