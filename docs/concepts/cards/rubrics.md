# Rubrics

**Purpose:** Reference card for **rubrics** used across AIEBOK books and knowledge areas.

## Core explanation

Rubrics score qualitative outputs against anchored criteria with examples at each level. They enable consistent human and LLM judging.

## Example

Support reply rubric scores correctness, completeness, tone, citations on 1–4 scale.

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

Calibrate two raters on 20 cases; report Cohen's kappa ≥ target before solo grading.

## Common failure modes

- Benchmark overfitting without production-like queries
- Stale eval sets that no longer match user behavior
- LLM judges drifting from human standards

## Trade-offs

No mechanism is universal. Compare rubrics against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Gold Datasets](../../concepts/cards/gold-datasets.md)
- [Slices](../../concepts/cards/slices.md)
- [Task Definitions](../../concepts/cards/task-definitions.md)
- [Thresholds](../../concepts/cards/thresholds.md)

## Related chapters

- [01 Evaluation As Requirements](../../books/10-evaluation-safety-and-governance/01-evaluation-as-requirements.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
