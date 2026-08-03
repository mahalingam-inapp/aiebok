# Qlora

**Purpose:** Reference card for **qlora** used across AIEBOK books and knowledge areas.

## Core explanation

QLoRA combines quantization of base weights with LoRA adapters for fine-tuning on consumer GPUs.

## Example

Fine-tune 13B on single 24GB card using 4-bit base plus LoRA adapters.

## When to use

Use when behavior must change systematically across many examples and prompts alone cannot reach quality or format targets.

## When not to use

Skip when RAG, better prompts, or routing fix the gap with less regression risk.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Document quantization config and compare quality versus full-precision LoRA baseline.

## Common failure modes

- Overfitting small curated sets
- Catastrophic forgetting of general capabilities
- Train-serve skew from preprocessing differences

## Trade-offs

No mechanism is universal. Compare qlora against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Distillation](../../concepts/cards/distillation.md)
- [Dpo](../../concepts/cards/dpo.md)
- [Lora](../../concepts/cards/lora.md)
- [Sft](../../concepts/cards/sft.md)

## Related chapters

- [02 Post Training Methods](../../books/11-training-serving-and-ai-operations/02-post-training-methods.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
