# Chunking

**Purpose:** Reference card for **chunking** used across AIEBOK books and knowledge areas.

## Core explanation

Chunking splits documents into index units sized for retrieval precision and generation context. Boundaries should respect sections, not arbitrary token counts alone.

## Example

Splitting mid-table separates headers from values, producing useless retrieval hits.

## Evidence of understanding

Compare recall@5 with fixed-size versus section-aware chunking on table-heavy docs.

## Trade-offs

No mechanism is universal. Compare chunking against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
