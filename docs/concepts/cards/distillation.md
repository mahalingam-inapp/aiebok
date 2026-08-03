# Distillation

**Purpose:** Reference card for **distillation** used across AIEBOK books and knowledge areas.

## Core explanation

Distillation trains smaller student models to mimic larger teachers, trading capability for cost and speed.

## Example

Student classifier matches teacher on 95% of eval at 5× lower latency.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Measure student versus teacher gap on full eval and acceptable degradation threshold.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare distillation against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Dpo](../../concepts/cards/dpo.md)
- [Lora](../../concepts/cards/lora.md)
- [Qlora](../../concepts/cards/qlora.md)
- [Sft](../../concepts/cards/sft.md)

## Related chapters

- [02 Post Training Methods](../../books/11-training-serving-and-ai-operations/02-post-training-methods.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
