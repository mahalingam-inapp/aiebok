# LLM Adaptation and Inference Lab

Project practicum · 2 sections · 4 lectures · 3–4 hours, plus the project

Adapt an autoregressive model, compare retrieval and tuning, and quantify serving trade-offs.

[Start the first lecture](01-autoregressive-evaluation-and-retrieval-baseline.md){ .md-button .md-button--primary }

## Entry prerequisites

Python, basic linear algebra, train and holdout splits, and equivalents of the ML and transformer cores.

## Course outline

### Establish and adapt baselines

- [01 · Autoregressive evaluation and retrieval baseline](01-autoregressive-evaluation-and-retrieval-baseline.md) — Establish frozen and retrieval-augmented baselines on a held-out task.
- [02 · Train and evaluate a low-rank adapter](02-train-and-evaluate-a-low-rank-adapter.md) — Train a small adapter over frozen parameters and evaluate held-out next-token predictions.

### Compress and transfer

- [03 · Quantization and inference measurement](03-quantization-and-inference-measurement.md) — Quantize a learned correction and compare held-out quality, payload bytes, and latency.
- [04 · Transfer to an open-weight checkpoint](04-transfer-to-an-open-weight-checkpoint.md) — Run the same train and holdout comparison against a compatible local transformer checkpoint.

## Workbook

[Download the workbook](../../assets/notebooks/llm-adaptation-inference.ipynb){ download }. Run the exercises in lecture order using the bundled sample data. Each lecture includes checks and a suggested variation.

## Course project

Compare a frozen baseline, a retrieval-augmented baseline, and an adapted model. Report held-out task results and quality after reducing precision. Use the optional local checkpoint lab for foundation-model transfer.

**How to check your project**

Keep train and held-out data separate. Measure inference quality, stored parameter memory, and repeated latency. Publish the model identity, hardware, precision, and a keep or revert decision.

## Further study

- [Donner’s LLM Engineering course and adaptation examples](https://github.com/ed-donner/llm_engineering)

[All courses](../index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
