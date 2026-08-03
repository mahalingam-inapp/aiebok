# Data Leakage

**Purpose:** Reference card for **data leakage** used across AIEBOK books and knowledge areas.

## Core explanation

Data leakage lets information from the target or future timesteps into features or labels during training. It inflates offline metrics while production performance collapses.

## Example

Including the support agent's resolution note written after closure as a feature perfectly predicts reopen—uselessly.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Run a feature audit: remove each suspicious column and watch for unrealistic AUC drops that signal leakage.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare data leakage against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Baselines](../../concepts/cards/baselines.md)
- [Features And Labels](../../concepts/cards/features-and-labels.md)
- [Problem Framing](../../concepts/cards/problem-framing.md)
- [Sampling](../../concepts/cards/sampling.md)

## Related chapters

- [01 Problems Data And Baselines](../../books/02-machine-learning-systems/01-problems-data-and-baselines.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
