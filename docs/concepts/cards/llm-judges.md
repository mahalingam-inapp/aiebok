# Llm Judges

**Purpose:** Reference card for **llm judges** used across AIEBOK books and knowledge areas.

## Core explanation

LLM judges automate scoring using rubrics but must be calibrated against humans to avoid systematic bias.

## Example

GPT-4 judge scores faithfulness correlated 0.85 with human labels after calibration.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Sample 10% human audit of LLM judge scores each sprint; recalibrate if drift >5 points.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare llm judges against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Confidence Intervals](../../concepts/cards/confidence-intervals.md)
- [Deterministic Metrics](../../concepts/cards/deterministic-metrics.md)
- [Human Evaluation](../../concepts/cards/human-evaluation.md)
- [Inter Rater Agreement](../../concepts/cards/inter-rater-agreement.md)

## Related chapters

- [02 Metrics And Human Judgment](../../books/10-evaluation-safety-and-governance/02-metrics-and-human-judgment.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
