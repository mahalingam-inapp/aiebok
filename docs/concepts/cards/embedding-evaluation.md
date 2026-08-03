# Embedding Evaluation

**Purpose:** Reference card for **embedding evaluation** used across AIEBOK books and knowledge areas.

## Core explanation

Embedding evaluation measures retrieval quality—recall, MRR, nDCG—on realistic queries with hard negatives. Benchmarks must mirror production language and domains.

## Example

Evaluating only easy paraphrases overstates performance versus queries with acronyms and typos.

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

Build 50 queries with annotated gold passages and hard negatives; report recall@5 and MRR.

## Common failure modes

- Recall failure on acronym-heavy or multi-hop questions
- Stale index after document or embedding model change
- Cross-tenant leakage when metadata filters are missing

## Trade-offs

No mechanism is universal. Compare embedding evaluation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Hard Negatives](../../concepts/cards/hard-negatives.md)
- [Multilingual Models](../../concepts/cards/multilingual-models.md)
- [Re Indexing](../../concepts/cards/re-indexing.md)
- [Vector Governance](../../concepts/cards/vector-governance.md)

## Related chapters

- [06 Embedding Systems In Production](../../books/03-language-and-representation/06-embedding-systems-in-production.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
