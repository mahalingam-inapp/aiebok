# Quantization

**Purpose:** Reference card for **quantization** used across AIEBOK books and knowledge areas.

## Core explanation

Quantization reduces weight precision—INT8, INT4—to cut memory and increase throughput with small quality trade-offs.

## Example

AWQ 4-bit model runs 2× faster with <1 point eval drop on some tasks.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Benchmark task metric and tokens/sec for FP16 versus INT4 on production hardware.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare quantization against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Batching](../../concepts/cards/batching.md)
- [Gpus](../../concepts/cards/gpus.md)
- [Kv Cache](../../concepts/cards/kv-cache.md)
- [Vllm](../../concepts/cards/vllm.md)

## Related chapters

- [04 Inference Infrastructure](../../books/11-training-serving-and-ai-operations/04-inference-infrastructure.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
