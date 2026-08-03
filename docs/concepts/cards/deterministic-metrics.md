# Deterministic Metrics

**Purpose:** Reference card for **deterministic metrics** used across AIEBOK books and knowledge areas.

## Core explanation

Deterministic metrics—exact match, F1 on spans, JSON validity—give reproducible scores without sampling variance.

## Example

Schema validation pass rate is deterministic; helpfulness often is not.

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

Prefer deterministic metrics for CI gates; use statistical metrics with confidence intervals for quality tracking.

## Common failure modes

- Benchmark overfitting without production-like queries
- Stale eval sets that no longer match user behavior
- LLM judges drifting from human standards

## Trade-offs

No mechanism is universal. Compare deterministic metrics against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Confidence Intervals](../../concepts/cards/confidence-intervals.md)
- [Human Evaluation](../../concepts/cards/human-evaluation.md)
- [Inter Rater Agreement](../../concepts/cards/inter-rater-agreement.md)
- [Llm Judges](../../concepts/cards/llm-judges.md)

## Related chapters

- [02 Metrics And Human Judgment](../../books/10-evaluation-safety-and-governance/02-metrics-and-human-judgment.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
