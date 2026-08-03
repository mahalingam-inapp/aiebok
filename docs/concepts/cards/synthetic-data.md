# Synthetic Data

**Purpose:** Reference card for **synthetic data** used across AIEBOK books and knowledge areas.

## Core explanation

Synthetic data generates training examples via models or rules—useful when real data is scarce but risks model collapse if overused.

## Example

GPT generates varied phrasings of intent labels to augment small classifier set.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare fine-tune with synthetic augmentation versus real-only on held-out real eval.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare synthetic data against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Contamination](../../concepts/cards/contamination.md)
- [Data Cards](../../concepts/cards/data-cards.md)
- [Data Curation](../../concepts/cards/data-curation.md)
- [Deduplication](../../concepts/cards/deduplication.md)

## Related chapters

- [03 Dataset Engineering](../../books/11-training-serving-and-ai-operations/03-dataset-engineering.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
