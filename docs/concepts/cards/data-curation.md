# Data Curation

**Purpose:** Reference card for **data curation** used across AIEBOK books and knowledge areas.

## Core explanation

Data curation selects, cleans, and balances training examples for quality over quantity. Garbage data teaches garbage behavior.

## Example

Removing toxic and duplicate examples improves fine-tune safety more than doubling raw size.

## When to use

Use when behavior must change systematically across many examples and prompts alone cannot reach quality or format targets.

## When not to use

Skip when RAG, better prompts, or routing fix the gap with less regression risk.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Document inclusion rules and manual audit sample of 100 rows pre-training.

## Common failure modes

- Overfitting small curated sets
- Catastrophic forgetting of general capabilities
- Train-serve skew from preprocessing differences

## Trade-offs

No mechanism is universal. Compare data curation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Contamination](../../concepts/cards/contamination.md)
- [Data Cards](../../concepts/cards/data-cards.md)
- [Deduplication](../../concepts/cards/deduplication.md)
- [Synthetic Data](../../concepts/cards/synthetic-data.md)

## Related chapters

- [03 Dataset Engineering](../../books/11-training-serving-and-ai-operations/03-dataset-engineering.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
