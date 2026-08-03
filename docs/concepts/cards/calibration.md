# Calibration

**Purpose:** Reference card for **calibration** used across AIEBOK books and knowledge areas.

## Core explanation

Calibration means predicted probabilities align with observed frequencies—70% confidence should be right about 70% of the time. Uncalibrated scores mislead threshold and cost decisions.

## Example

A medical triage model with miscalibrated probabilities causes undertriage when 0.9 confidence actually means 0.6 accuracy.

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

Plot a reliability diagram and report expected calibration error before setting production thresholds.

## Common failure modes

- Benchmark overfitting without production-like queries
- Stale eval sets that no longer match user behavior
- LLM judges drifting from human standards

## Trade-offs

No mechanism is universal. Compare calibration against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Abstention](../../concepts/cards/abstention.md)
- [Confusion Matrix](../../concepts/cards/confusion-matrix.md)
- [Cross Validation](../../concepts/cards/cross-validation.md)
- [Decision Thresholds](../../concepts/cards/decision-thresholds.md)

## Related chapters

- [06 Engineering With Uncertainty](../../books/01-foundations-of-intelligence/06-engineering-with-uncertainty.md)
- [05 Evaluation And Error Analysis](../../books/02-machine-learning-systems/05-evaluation-and-error-analysis.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
