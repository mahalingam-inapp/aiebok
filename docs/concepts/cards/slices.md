# Slices

**Purpose:** Reference card for **slices** used across AIEBOK books and knowledge areas.

## Core explanation

Slices are subpopulations—language, tenant, risk tier—where aggregate metrics may hide failure.

## Example

95% overall accuracy can mask 60% on enterprise accounts.

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

Report metrics on three production slices with separate release thresholds.

## Common failure modes

- Benchmark overfitting without production-like queries
- Stale eval sets that no longer match user behavior
- LLM judges drifting from human standards

## Trade-offs

No mechanism is universal. Compare slices against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Gold Datasets](../../concepts/cards/gold-datasets.md)
- [Rubrics](../../concepts/cards/rubrics.md)
- [Task Definitions](../../concepts/cards/task-definitions.md)
- [Thresholds](../../concepts/cards/thresholds.md)

## Related chapters

- [01 Evaluation As Requirements](../../books/10-evaluation-safety-and-governance/01-evaluation-as-requirements.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
