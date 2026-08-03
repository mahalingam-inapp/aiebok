# Contamination

**Purpose:** Reference card for **contamination** used across AIEBOK books and knowledge areas.

## Core explanation

Contamination occurs when eval examples leak into training data, inflating benchmark scores.

## Example

Near-duplicate test questions in fine-tune set invalidate held-out claims.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Run n-gram or embedding overlap check between train and eval; zero high overlap pairs.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare contamination against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Data Cards](../../concepts/cards/data-cards.md)
- [Data Curation](../../concepts/cards/data-curation.md)
- [Deduplication](../../concepts/cards/deduplication.md)
- [Synthetic Data](../../concepts/cards/synthetic-data.md)

## Related chapters

- [03 Dataset Engineering](../../books/11-training-serving-and-ai-operations/03-dataset-engineering.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
