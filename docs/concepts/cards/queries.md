# Queries

**Purpose:** Reference card for **queries** used across AIEBOK books and knowledge areas.

## Core explanation

In attention, queries represent what information a position seeks from other positions. They are learned projections of hidden states, not user search queries.

## Example

Each decoder token issues a query vector to attend over encoder keys during translation.

## Evidence of understanding

Visualize query-key dot products and verify peak weights align with alignments.

## Trade-offs

No mechanism is universal. Compare queries against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
