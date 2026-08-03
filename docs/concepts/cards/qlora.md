# Qlora

**Purpose:** Reference card for **qlora** used across AIEBOK books and knowledge areas.

## Core explanation

QLoRA combines quantization of base weights with LoRA adapters for fine-tuning on consumer GPUs.

## Example

Fine-tune 13B on single 24GB card using 4-bit base plus LoRA adapters.

## Evidence of understanding

Document quantization config and compare quality versus full-precision LoRA baseline.

## Trade-offs

No mechanism is universal. Compare qlora against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
