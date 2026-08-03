# Confidence Intervals

**Purpose:** Reference card for **confidence intervals** used across AIEBOK books and knowledge areas.

## Core explanation

Confidence intervals quantify uncertainty in metric estimates from finite eval sets. Comparing models requires overlapping intervals or formal tests.

## Example

Model A at 82% ± 3% versus Model B at 85% ± 4% may not be significantly different.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Report 95% CI for primary metrics; require non-overlap for major release claims.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare confidence intervals against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Deterministic Metrics](../../concepts/cards/deterministic-metrics.md)
- [Human Evaluation](../../concepts/cards/human-evaluation.md)
- [Inter Rater Agreement](../../concepts/cards/inter-rater-agreement.md)
- [Llm Judges](../../concepts/cards/llm-judges.md)

## Related chapters

- [02 Metrics And Human Judgment](../../books/10-evaluation-safety-and-governance/02-metrics-and-human-judgment.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
