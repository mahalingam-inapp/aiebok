# Gpus

**Purpose:** Reference card for **gpus** used across AIEBOK books and knowledge areas.

## Core explanation

GPUs accelerate matrix operations for training and inference; memory capacity limits model size and batch.

## Example

80GB GPU runs 70B quantized; 24GB fits 7B fine-tune with QLoRA.

## Evidence of understanding

Profile GPU utilization and memory headroom during peak inference load.

## Trade-offs

No mechanism is universal. Compare gpus against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
