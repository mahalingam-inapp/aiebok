# Thresholds

**Purpose:** Reference card for **thresholds** used across AIEBOK books and knowledge areas.

## Core explanation

Thresholds are minimum acceptable metric values for release or routing decisions. They encode risk appetite numerically.

## Example

Faithfulness ≥ 0.92 and P0 safety 100% required for production promotion.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Document threshold rationale and review quarterly with incident data.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare thresholds against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Gold Datasets](../../concepts/cards/gold-datasets.md)
- [Rubrics](../../concepts/cards/rubrics.md)
- [Slices](../../concepts/cards/slices.md)
- [Task Definitions](../../concepts/cards/task-definitions.md)

## Related chapters

- [01 Evaluation As Requirements](../../books/10-evaluation-safety-and-governance/01-evaluation-as-requirements.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
