# Decision Thresholds

**Purpose:** Reference card for **decision thresholds** used across AIEBOK books and knowledge areas.

## Core explanation

Decision thresholds turn continuous scores into actions—approve, escalate, or abstain. They encode business costs and should be tuned on validation data, not defaults.

## Example

Raising a fraud threshold reduces false positives but increases missed fraud; the optimum depends on chargeback cost.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Sweep thresholds on a validation set and plot precision-recall against expected dollar cost.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare decision thresholds against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Abstention](../../concepts/cards/abstention.md)
- [Calibration](../../concepts/cards/calibration.md)
- [Expected Cost](../../concepts/cards/expected-cost.md)
- [Human Review](../../concepts/cards/human-review.md)

## Related chapters

- [06 Engineering With Uncertainty](../../books/01-foundations-of-intelligence/06-engineering-with-uncertainty.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
