# Dpo

**Purpose:** Reference card for **dpo** used across AIEBOK books and knowledge areas.

## Core explanation

Direct Preference Optimization aligns models from pairwise preferences without explicit reward model training.

## Example

Prefer concise accurate answers over verbose wrong ones via DPO preference pairs.

## Evidence of understanding

Win-rate versus base model on preference eval set ≥ target before deploy.

## Trade-offs

No mechanism is universal. Compare dpo against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
