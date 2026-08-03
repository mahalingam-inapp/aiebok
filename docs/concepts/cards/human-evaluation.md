# Human Evaluation

**Purpose:** Reference card for **human evaluation** used across AIEBOK books and knowledge areas.

## Core explanation

Human evaluation labels outputs quality when automation cannot capture nuance or safety. Design for rater training, agreement, and throughput.

## Example

Lawyers label contract summaries for legal accuracy on 50 cases monthly.

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

Track inter-rater agreement and adjudicate disagreements with gold committee.

## Common failure modes

- Benchmark overfitting without production-like queries
- Stale eval sets that no longer match user behavior
- LLM judges drifting from human standards

## Trade-offs

No mechanism is universal. Compare human evaluation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Confidence Intervals](../../concepts/cards/confidence-intervals.md)
- [Deterministic Metrics](../../concepts/cards/deterministic-metrics.md)
- [Inter Rater Agreement](../../concepts/cards/inter-rater-agreement.md)
- [Llm Judges](../../concepts/cards/llm-judges.md)

## Related chapters

- [02 Metrics And Human Judgment](../../books/10-evaluation-safety-and-governance/02-metrics-and-human-judgment.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
