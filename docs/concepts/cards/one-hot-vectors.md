# One Hot Vectors

**Purpose:** Reference card for **one hot vectors** used across AIEBOK books and knowledge areas.

## Core explanation

One-hot vectors encode categorical items as sparse binary indicators—simple but high-dimensional and semantically blind. They remain baselines for small categorical features.

## Example

Encoding 10k product IDs as one-hot vectors is impractical; embeddings replace them at scale.

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

Compare memory and lookup time for one-hot versus learned embedding on the same catalog size.

## Common failure modes

- Recall failure on acronym-heavy or multi-hop questions
- Stale index after document or embedding model change
- Cross-tenant leakage when metadata filters are missing

## Trade-offs

No mechanism is universal. Compare one hot vectors against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Bm25](../../concepts/cards/bm25.md)
- [Sentence Embeddings](../../concepts/cards/sentence-embeddings.md)
- [Tf Idf](../../concepts/cards/tf-idf.md)
- [Word Embeddings](../../concepts/cards/word-embeddings.md)

## Related chapters

- [04 From Sparse Features To Embeddings](../../books/03-language-and-representation/04-from-sparse-features-to-embeddings.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
