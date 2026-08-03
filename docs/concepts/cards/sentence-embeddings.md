# Sentence Embeddings

**Purpose:** Reference card for **sentence embeddings** used across AIEBOK books and knowledge areas.

## Core explanation

Sentence embeddings encode whole utterances into vectors for semantic search and clustering. Quality depends on training objective and domain match.

## Example

Embedding employee questions matches handbook paraphrases even without shared keywords.

## Evidence of understanding

Benchmark recall@5 on paraphrase pairs with hard negative passages in the index.

## Trade-offs

No mechanism is universal. Compare sentence embeddings against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
