# Query Rewriting

**Purpose:** Reference card for **query rewriting** used across AIEBOK books and knowledge areas.

## Core explanation

Query rewriting transforms requests via expansion, decomposition, or HyDE before retrieval to close vocabulary gaps.

## Example

Expanding 'PTO' to 'paid time off' helps lexical retrievers match handbook language.

## Evidence of understanding

Compare recall@k with and without rewrite on acronym-heavy queries.

## Trade-offs

No mechanism is universal. Compare query rewriting against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
