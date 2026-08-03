# Deduplication

**Purpose:** Reference card for **deduplication** used across AIEBOK books and knowledge areas.

## Core explanation

Deduplication removes near-duplicate training examples that inflate metrics and memorization.

## Example

Duplicate FAQ pairs in SFT data cause verbatim regurgitation in deployment.

## Evidence of understanding

Report duplicate rate before/after MinHash dedup on training corpus.

## Trade-offs

No mechanism is universal. Compare deduplication against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
