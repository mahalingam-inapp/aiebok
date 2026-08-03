# Precision And Recall

**Purpose:** Reference card for **precision and recall** used across AIEBOK books and knowledge areas.

## Core explanation

Precision is correctness among positive predictions; recall is coverage of actual positives. Trading them off reflects whether false positives or false negatives hurt more.

## Example

High recall in safety alerts catches more incidents; high precision in auto-replies avoids annoying customers.

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

Plot precision-recall curve and mark the operating point that meets your cost constraint.

## Common failure modes

- Benchmark overfitting without production-like queries
- Stale eval sets that no longer match user behavior
- LLM judges drifting from human standards

## Trade-offs

No mechanism is universal. Compare precision and recall against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Calibration](../../concepts/cards/calibration.md)
- [Confusion Matrix](../../concepts/cards/confusion-matrix.md)
- [Cross Validation](../../concepts/cards/cross-validation.md)
- [Slice Analysis](../../concepts/cards/slice-analysis.md)

## Related chapters

- [05 Evaluation And Error Analysis](../../books/02-machine-learning-systems/05-evaluation-and-error-analysis.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
