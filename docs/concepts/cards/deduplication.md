# Deduplication

**Purpose:** Reference card for **deduplication** used across AIEBOK books and knowledge areas.

## Core explanation

Deduplication removes near-duplicate training examples that inflate metrics and memorization.

## Example

Duplicate FAQ pairs in SFT data cause verbatim regurgitation in deployment.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Report duplicate rate before/after MinHash dedup on training corpus.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare deduplication against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Contamination](../../concepts/cards/contamination.md)
- [Context Packing](../../concepts/cards/context-packing.md)
- [Data Cards](../../concepts/cards/data-cards.md)
- [Data Curation](../../concepts/cards/data-curation.md)

## Related chapters

- [04 Ranking And Context Selection](../../books/06-knowledge-and-retrieval-systems/04-ranking-and-context-selection.md)
- [03 Dataset Engineering](../../books/11-training-serving-and-ai-operations/03-dataset-engineering.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
