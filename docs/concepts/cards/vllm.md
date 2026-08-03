# Vllm

**Purpose:** Reference card for **vllm** used across AIEBOK books and knowledge areas.

## Core explanation

vLLM is a high-throughput inference server using PagedAttention for efficient KV cache memory management.

## Example

vLLM serves Llama-8B at higher concurrent requests than naive HuggingFace pipeline.

## Evidence of understanding

Load-test vLLM versus baseline server at equal hardware; report throughput and p95 latency.

## Trade-offs

No mechanism is universal. Compare vllm against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
