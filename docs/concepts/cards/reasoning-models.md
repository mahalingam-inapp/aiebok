# Reasoning Models

**Purpose:** Reference card for **reasoning models** used across AIEBOK books and knowledge areas.

## Core explanation

Reasoning models allocate extra inference compute—long chains, self-checks—for math, code, and planning tasks. They trade latency and cost for accuracy on hard problems.

## Example

A reasoning model may emit scratchpad steps before the final answer on a budget word problem.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Measure accuracy and tokens used versus a base model on a reasoning benchmark.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare reasoning models against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Instruction Tuning](../../concepts/cards/instruction-tuning.md)
- [Model Routing](../../concepts/cards/model-routing.md)
- [Multimodal Models](../../concepts/cards/multimodal-models.md)
- [Open Weights](../../concepts/cards/open-weights.md)

## Related chapters

- [06 Model Families And Selection](../../books/04-transformers-and-foundation-models/06-model-families-and-selection.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
