# Problem Framing

**Purpose:** Reference card for **problem framing** used across AIEBOK books and knowledge areas.

## Core explanation

Problem framing defines the unit of prediction, target label, decision, population, and time boundary before choosing algorithms. Most ML failures are mis-specified problems, not wrong models.

## Example

Predicting 'will this ticket reopen within 7 days' differs from 'summarize this ticket'—only the first is a measurable ML task.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Write the prediction unit, label definition, and decision rule; verify each is observable in production logs.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare problem framing against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Baselines](../../concepts/cards/baselines.md)
- [Data Leakage](../../concepts/cards/data-leakage.md)
- [Features And Labels](../../concepts/cards/features-and-labels.md)
- [Sampling](../../concepts/cards/sampling.md)

## Related chapters

- [01 Problems Data And Baselines](../../books/02-machine-learning-systems/01-problems-data-and-baselines.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
