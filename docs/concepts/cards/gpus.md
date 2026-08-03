# Gpus

**Purpose:** Reference card for **gpus** used across AIEBOK books and knowledge areas.

## Core explanation

GPUs accelerate matrix operations for training and inference; memory capacity limits model size and batch.

## Example

80GB GPU runs 70B quantized; 24GB fits 7B fine-tune with QLoRA.

## When to use

Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.

## When not to use

Skip when complexity, latency, or ops burden exceeds demonstrated benefit.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Profile GPU utilization and memory headroom during peak inference load.

## Common failure modes

- Applying the technique without a baseline comparison
- Ignoring boundary and adversarial inputs
- Optimizing demo cases instead of production slices

## Trade-offs

No mechanism is universal. Compare gpus against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related concepts

- [Batching](../../concepts/cards/batching.md)
- [Kv Cache](../../concepts/cards/kv-cache.md)
- [Quantization](../../concepts/cards/quantization.md)
- [Vllm](../../concepts/cards/vllm.md)

## Related chapters

- [04 Inference Infrastructure](../../books/11-training-serving-and-ai-operations/04-inference-infrastructure.md)

## Related study

- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
