# Data Cards

**Purpose:** Reference card for **data cards** used across AIEBOK books and knowledge areas.

## Core explanation

Data cards document dataset sources, collection, demographics, limitations, and recommended uses—parallel to model cards.

## Example

Fine-tune data card lists languages, date range, PII handling, and opt-out process.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Publish data card with every dataset version in registry.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare data cards against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Contamination](../../concepts/cards/contamination.md)
- [Data Curation](../../concepts/cards/data-curation.md)
- [Deduplication](../../concepts/cards/deduplication.md)
- [Synthetic Data](../../concepts/cards/synthetic-data.md)

## Related chapters

- [03 Dataset Engineering](../../books/11-training-serving-and-ai-operations/03-dataset-engineering.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
