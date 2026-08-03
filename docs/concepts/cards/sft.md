# Sft

**Purpose:** Reference card for **sft** used across AIEBOK books and knowledge areas.

## Core explanation

Supervised fine-tuning trains on input–output pairs to imitate desired behaviors on similar tasks.

## Example

SFT on 5k support replies teaches consistent empathy and escalation triggers.

## When to use

Use when behavior must change systematically across many examples and prompts alone cannot reach quality or format targets.

## When not to use

Skip when RAG, better prompts, or routing fix the gap with less regression risk.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Compare SFT model to base plus prompt on held-out behavioral eval.

## Common failure modes

- Overfitting small curated sets
- Catastrophic forgetting of general capabilities
- Train-serve skew from preprocessing differences

## Trade-offs

No mechanism is universal. Compare sft against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Distillation](../../concepts/cards/distillation.md)
- [Dpo](../../concepts/cards/dpo.md)
- [Lora](../../concepts/cards/lora.md)
- [Qlora](../../concepts/cards/qlora.md)

## Related chapters

- [02 Post Training Methods](../../books/11-training-serving-and-ai-operations/02-post-training-methods.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
