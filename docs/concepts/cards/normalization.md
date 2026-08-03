# Normalization

**Purpose:** Reference card for **normalization** used across AIEBOK books and knowledge areas.

## Core explanation

Text normalization lowercases, strips diacritics, standardizes whitespace, and canonicalizes equivalents before indexing or tokenization. Over-normalization destroys discriminative identifiers.

## Example

Collapsing hyphens in SKUs merges distinct product codes; preserving case matters for camelCase APIs.

## Evidence of understanding

Compare retrieval recall with and without aggressive normalization on identifier-heavy queries.

## Trade-offs

No mechanism is universal. Compare normalization against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
