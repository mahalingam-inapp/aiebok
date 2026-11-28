# Mixture Of Experts

**Purpose:** Reference card for **mixture of experts** used across AIEBOK books and knowledge areas.

## Core explanation

A sparse mixture-of-experts layer routes each token to a subset of expert feed-forward networks and combines their outputs. Resident weight memory, shared computation, and cross-device communication matter even when few experts are active.

## Example

A layer with eight equally sized routed experts and top-2 routing uses two experts per token. A shared expert, if present, adds work for every token.

## When to use

Use when a larger parameter budget is plausible at bounded token compute.

## When not to use

Favor a dense baseline for workloads that cannot accommodate resident experts or inter-device traffic.

## Engineering checklist

- Count active and resident weights, including shared layers.

## Evidence of understanding

Report active and resident parameters separately. Measure skew, overflow or queueing, and quality on realistic input bursts.

## Common failure modes

- A router concentrates a burst on a few experts.

## Trade-offs

No mechanism is universal. Compare mixture of experts against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Checkpoints](../../concepts/cards/checkpoints.md)
- [Data Mixtures](../../concepts/cards/data-mixtures.md)
- [Pretraining Objectives](../../concepts/cards/pretraining-objectives.md)
- [Scaling Laws](../../concepts/cards/scaling-laws.md)

## Related chapters

- [04 Training Foundation Models](../../books/04-transformers-and-foundation-models/04-training-foundation-models.md)

## Related study

- [Run the course practicum](../../courses/sparse-model-architectures/index.md)
- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
