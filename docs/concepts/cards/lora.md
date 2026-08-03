# Lora

**Purpose:** Reference card for **lora** used across AIEBOK books and knowledge areas.

## Core explanation

LoRA fine-tunes low-rank adapter matrices in attention layers, reducing trainable parameters versus full fine-tuning.

## Example

7B model with LoRA learns domain tone on one GPU while base weights stay frozen.

## Evidence of understanding

Report eval uplift, training cost, and adapter version at inference.

## Trade-offs

No mechanism is universal. Compare lora against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
