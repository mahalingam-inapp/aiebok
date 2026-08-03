# Baselines

**Purpose:** Reference card for **baselines** used across AIEBOK books and knowledge areas.

## Core explanation

Baselines are simple reference methods—majority class, linear model, keyword rules—that quantify what complexity must beat. Without them, teams cannot justify neural networks or LLMs.

## Example

A TF–IDF logistic regression baseline on ticket routing sets the bar before trying embeddings.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Report baseline and candidate metrics on identical splits; require statistically meaningful uplift for release.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare baselines against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Data Leakage](../../concepts/cards/data-leakage.md)
- [Features And Labels](../../concepts/cards/features-and-labels.md)
- [Problem Framing](../../concepts/cards/problem-framing.md)
- [Sampling](../../concepts/cards/sampling.md)

## Related chapters

- [01 Problems Data And Baselines](../../books/02-machine-learning-systems/01-problems-data-and-baselines.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
