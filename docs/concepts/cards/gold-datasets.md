# Gold Datasets

**Purpose:** Reference card for **gold datasets** used across AIEBOK books and knowledge areas.

## Core explanation

Gold datasets hold authoritative labels or reference outputs for evaluation. They require versioning, access control, and refresh cadence.

## Example

200 lawyer-reviewed contract clauses with gold entity spans versioned quarterly.

## When to use

Use when behavior must change systematically across many examples and prompts alone cannot reach quality or format targets.

## When not to use

Skip when RAG, better prompts, or routing fix the gap with less regression risk.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Hash dataset version in every eval report; reject runs on unversioned snapshots.

## Common failure modes

- Overfitting small curated sets
- Catastrophic forgetting of general capabilities
- Train-serve skew from preprocessing differences

## Trade-offs

No mechanism is universal. Compare gold datasets against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Rubrics](../../concepts/cards/rubrics.md)
- [Slices](../../concepts/cards/slices.md)
- [Task Definitions](../../concepts/cards/task-definitions.md)
- [Thresholds](../../concepts/cards/thresholds.md)

## Related chapters

- [01 Evaluation As Requirements](../../books/10-evaluation-safety-and-governance/01-evaluation-as-requirements.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
