# Decision Thresholds

**Purpose:** Reference card for **decision thresholds** used across AIEBOK books and knowledge areas.

## Core explanation

Decision thresholds turn continuous scores into actions—approve, escalate, or abstain. They encode business costs and should be tuned on validation data, not defaults.

## Example

Raising a fraud threshold reduces false positives but increases missed fraud; the optimum depends on chargeback cost.

## Evidence of understanding

Sweep thresholds on a validation set and plot precision-recall against expected dollar cost.

## Trade-offs

No mechanism is universal. Compare decision thresholds against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
