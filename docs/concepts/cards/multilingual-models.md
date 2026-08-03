# Multilingual Models

**Purpose:** Reference card for **multilingual models** used across AIEBOK books and knowledge areas.

## Core explanation

Multilingual models share parameters across languages, enabling cross-lingual retrieval and generation. Performance varies by language pair and training data balance.

## Example

A Spanish employee query can retrieve English policy text if the embedding space aligns concepts.

## Evidence of understanding

Evaluate recall@5 separately per language on parallel query sets.

## Trade-offs

No mechanism is universal. Compare multilingual models against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
