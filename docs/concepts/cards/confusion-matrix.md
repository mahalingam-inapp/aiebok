# Confusion Matrix

**Purpose:** Reference card for **confusion matrix** used across AIEBOK books and knowledge areas.

## Core explanation

A confusion matrix counts predicted versus actual classes, exposing which errors dominate. It is essential when classes are imbalanced or costs asymmetric.

## Example

A router may confuse 'billing' with 'refund' while rarely missing 'outage'—the matrix shows where to invest labeling.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compute per-class precision and recall from the matrix on a stratified test set.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare confusion matrix against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Calibration](../../concepts/cards/calibration.md)
- [Cross Validation](../../concepts/cards/cross-validation.md)
- [Precision And Recall](../../concepts/cards/precision-and-recall.md)
- [Slice Analysis](../../concepts/cards/slice-analysis.md)

## Related chapters

- [05 Evaluation And Error Analysis](../../books/02-machine-learning-systems/05-evaluation-and-error-analysis.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
