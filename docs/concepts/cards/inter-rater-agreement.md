# Inter Rater Agreement

**Purpose:** Reference card for **inter rater agreement** used across AIEBOK books and knowledge areas.

## Core explanation

Inter-rater agreement measures how consistently multiple human graders apply rubrics—Cohen's kappa, Krippendorff's alpha.

## Example

Low agreement on tone dimension means rubric needs refinement before scaling labeling.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compute kappa per rubric dimension; block scaling if below 0.6.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare inter rater agreement against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Confidence Intervals](../../concepts/cards/confidence-intervals.md)
- [Deterministic Metrics](../../concepts/cards/deterministic-metrics.md)
- [Human Evaluation](../../concepts/cards/human-evaluation.md)
- [Llm Judges](../../concepts/cards/llm-judges.md)

## Related chapters

- [02 Metrics And Human Judgment](../../books/10-evaluation-safety-and-governance/02-metrics-and-human-judgment.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
