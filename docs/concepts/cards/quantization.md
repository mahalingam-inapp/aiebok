# Quantization

**Purpose:** Reference card for **quantization** used across AIEBOK books and knowledge areas.

## Core explanation

Quantization reduces weight precision—INT8, INT4—to cut memory and increase throughput with small quality trade-offs.

## Example

AWQ 4-bit model runs 2× faster with <1 point eval drop on some tasks.

## Evidence of understanding

Benchmark task metric and tokens/sec for FP16 versus INT4 on production hardware.

## Trade-offs

No mechanism is universal. Compare quantization against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
