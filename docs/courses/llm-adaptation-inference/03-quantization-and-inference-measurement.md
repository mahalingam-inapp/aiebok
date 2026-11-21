# Quantization and inference measurement

[LLM Adaptation and Inference Lab](index.md) · Compress and transfer · Lecture 3 of 4 · 45–60 min · Project practicum

## What you will learn

Quantize a learned correction and compare held-out quality, payload bytes, and latency.

## How it works

Symmetric quantization maps floating-point values to an integer range using a scale. Keep model quality and numeric drift separate from performance. A smaller payload can reduce transfers, while dequantization can add work on hardware without suitable kernels.

## Worked example

An int8 correction uses fewer payload bytes. In a small Python implementation, unpacking can offset any latency benefit.

## Try it yourself

Run repeated measurements before and after quantizing. Record scale overhead and name the hardware.

[Download the workbook](../../assets/notebooks/llm-adaptation-inference.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Report actual bytes for the matrix payload and the measured timing distribution. Clarify which model components the demonstration compresses.

## Continue

[← Previous lecture](02-train-and-evaluate-a-low-rank-adapter.md) · [Course outline](index.md) · [Next lecture →](04-transfer-to-an-open-weight-checkpoint.md)
