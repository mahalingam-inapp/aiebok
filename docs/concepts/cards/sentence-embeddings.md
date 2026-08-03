# Sentence Embeddings

**Purpose:** Reference card for **sentence embeddings** used across AIEBOK books and knowledge areas.

## Core explanation

Sentence embeddings encode whole utterances into vectors for semantic search and clustering. Quality depends on training objective and domain match.

## Example

Embedding employee questions matches handbook paraphrases even without shared keywords.

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

Benchmark recall@5 on paraphrase pairs with hard negative passages in the index.

## Common failure modes

- Recall failure on acronym-heavy or multi-hop questions
- Stale index after document or embedding model change
- Cross-tenant leakage when metadata filters are missing

## Trade-offs

No mechanism is universal. Compare sentence embeddings against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Bm25](../../concepts/cards/bm25.md)
- [One Hot Vectors](../../concepts/cards/one-hot-vectors.md)
- [Tf Idf](../../concepts/cards/tf-idf.md)
- [Word Embeddings](../../concepts/cards/word-embeddings.md)

## Related chapters

- [04 From Sparse Features To Embeddings](../../books/03-language-and-representation/04-from-sparse-features-to-embeddings.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
