# Slice Analysis

**Purpose:** Reference card for **slice analysis** used across AIEBOK books and knowledge areas.

## Core explanation

Slice analysis evaluates metrics on subpopulations—language, product, tenant—to catch aggregate illusions. A model can pass overall while failing high-value segments.

## Example

95% accuracy overall can hide 60% on enterprise accounts or non-English queries.

## When to use

Use before every release, model swap, prompt change, or retrieval index migration.

## When not to use

Skip aggregate-only metrics when slices or safety cases can hide regressions.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.
- Report worst-slice performance, not aggregate alone.

## Evidence of understanding

Define three production-representative slices and require each meets its release threshold.

## Common failure modes

- Benchmark overfitting without production-like queries
- Stale eval sets that no longer match user behavior
- LLM judges drifting from human standards

## Trade-offs

No mechanism is universal. Compare slice analysis against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Calibration](../../concepts/cards/calibration.md)
- [Confusion Matrix](../../concepts/cards/confusion-matrix.md)
- [Cross Validation](../../concepts/cards/cross-validation.md)
- [Precision And Recall](../../concepts/cards/precision-and-recall.md)

## Related chapters

- [05 Evaluation And Error Analysis](../../books/02-machine-learning-systems/05-evaluation-and-error-analysis.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
