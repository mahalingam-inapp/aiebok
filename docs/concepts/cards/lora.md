# Lora

**Purpose:** Reference card for **lora** used across AIEBOK books and knowledge areas.

## Core explanation

LoRA fine-tunes low-rank adapter matrices in attention layers, reducing trainable parameters versus full fine-tuning.

## Example

7B model with LoRA learns domain tone on one GPU while base weights stay frozen.

## When to use

Use when behavior must change systematically across many examples and prompts alone cannot reach quality or format targets.

## When not to use

Skip when RAG, better prompts, or routing fix the gap with less regression risk.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Report eval uplift, training cost, and adapter version at inference.

## Common failure modes

- Overfitting small curated sets
- Catastrophic forgetting of general capabilities
- Train-serve skew from preprocessing differences

## Trade-offs

No mechanism is universal. Compare lora against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Distillation](../../concepts/cards/distillation.md)
- [Dpo](../../concepts/cards/dpo.md)
- [Qlora](../../concepts/cards/qlora.md)
- [Sft](../../concepts/cards/sft.md)

## Related chapters

- [02 Post Training Methods](../../books/11-training-serving-and-ai-operations/02-post-training-methods.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
