# Data Leakage

**Purpose:** Reference card for **data leakage** used across AIEBOK books and knowledge areas.

## Core explanation

Data leakage lets information from the target or future timesteps into features or labels during training. It inflates offline metrics while production performance collapses.

## Example

Including the support agent's resolution note written after closure as a feature perfectly predicts reopen—uselessly.

## Evidence of understanding

Run a feature audit: remove each suspicious column and watch for unrealistic AUC drops that signal leakage.

## Trade-offs

No mechanism is universal. Compare data leakage against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
