# Ann Indexes

**Purpose:** Reference card for **ann indexes** used across AIEBOK books and knowledge areas.

## Core explanation

Approximate nearest neighbor indexes—HNSW, IVF, LSH—trade recall for speed at million-plus scale. Index parameters must be tuned on representative queries.

## Example

HNSW with efSearch=100 may hit 98% recall@10 at 5ms versus 50ms exact on 1M vectors.

## Evidence of understanding

Plot latency versus recall@k for three index configurations on production query sample.

## Trade-offs

No mechanism is universal. Compare ann indexes against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
