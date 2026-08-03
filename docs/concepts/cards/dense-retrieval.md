# Dense Retrieval

**Purpose:** Reference card for **dense retrieval** used across AIEBOK books and knowledge areas.

## Core explanation

Dense retrieval embeds queries and documents into the same vector space and returns nearest neighbors by similarity.

## Example

A query about 'application unavailable' retrieves 'service is down' without lexical overlap.

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

Build a 30-query eval with paraphrases and hard negatives; report recall@5 and MRR.

## Common failure modes

- Recall failure on acronym-heavy or multi-hop questions
- Stale index after document or embedding model change
- Cross-tenant leakage when metadata filters are missing

## Trade-offs

No mechanism is universal. Compare dense retrieval against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Bm25](../../concepts/cards/bm25.md)
- [Hybrid Search](../../concepts/cards/hybrid-search.md)
- [Parent Child Retrieval](../../concepts/cards/parent-child-retrieval.md)
- [Query Rewriting](../../concepts/cards/query-rewriting.md)

## Related chapters

- [03 Retrieval](../../books/06-knowledge-and-retrieval-systems/03-retrieval.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
