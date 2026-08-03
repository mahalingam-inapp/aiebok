# Hybrid Search

**Purpose:** Reference card for **hybrid search** used across AIEBOK books and knowledge areas.

## Core explanation

Hybrid search combines lexical and dense signals—often via reciprocal rank fusion—when neither alone covers identifiers and paraphrases.

## Example

Fusion surfaces policy IDs lexically while keeping semantic matches for informal phrasing.

## Evidence of understanding

Show a query where lexical-only and dense-only each miss but fusion succeeds.

## Trade-offs

No mechanism is universal. Compare hybrid search against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
