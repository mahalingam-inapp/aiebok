# Open Weights

**Purpose:** Reference card for **open weights** used across AIEBOK books and knowledge areas.

## Core explanation

Open-weights models publish parameters for local deployment, fine-tuning, and inspection—versus API-only access. They shift control, compliance, and operational burden to your team.

## Example

Self-hosting Llama enables air-gapped inference but requires GPU ops and security patching.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Document license terms, hardware requirements, and eval parity versus API baseline before adoption.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare open weights against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Instruction Tuning](../../concepts/cards/instruction-tuning.md)
- [Model Routing](../../concepts/cards/model-routing.md)
- [Multimodal Models](../../concepts/cards/multimodal-models.md)
- [Reasoning Models](../../concepts/cards/reasoning-models.md)

## Related chapters

- [06 Model Families And Selection](../../books/04-transformers-and-foundation-models/06-model-families-and-selection.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
