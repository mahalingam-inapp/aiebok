# Sparse Models and Mixture of Experts

Project practicum · 2 sections · 4 lectures · 3–4 hours, plus the project

Build a token router, measure imbalance and communication, and compare sparse and hybrid architectures for a target workload.

[Start the first lecture](01-token-routing-and-top-k-experts.md){ .md-button .md-button--primary .study-start data-course="sparse-model-architectures" }

## Practice case · A Monday morning at HarborLink

HarborLink's engineering team wants to process rider questions and long equipment logs on the same fleet. Arun has a dense baseline, a candidate with sparse experts, and a limited device budget. The support desk only cares which choice still works during a noisy Monday queue.

This fictional case continues through the lectures.

## Entry prerequisites

Python, vector operations, and the transformer feed-forward and attention blocks.

## Course outline

### Route tokens through experts

- [01 · Token routing and top-k experts](01-token-routing-and-top-k-experts.md){ .study-lecture data-lecture="01-token-routing-and-top-k-experts.md" } — Implement top-k expert routing and distinguish it from routing entire requests to different models.
- [02 · Expert capacity and load balancing](02-expert-capacity-and-load-balancing.md){ .study-lecture data-lecture="02-expert-capacity-and-load-balancing.md" } — Measure routing skew, simulate a capacity limit, and compare overflow against a balancing policy.

### Size the system and workload

- [03 · Expert parallelism and communication](03-expert-parallelism-and-communication.md){ .study-lecture data-lecture="03-expert-parallelism-and-communication.md" } — Account for expert dispatch and return traffic alongside local computation and queueing.
- [04 · Hybrid backbones and architecture selection](04-hybrid-backbones-and-architecture-selection.md){ .study-lecture data-lecture="04-hybrid-backbones-and-architecture-selection.md" } — Compare conventional KV cache growth with a hybrid model that combines recurrent state and full attention.

## Workbook

[Download the workbook](../../assets/notebooks/sparse-model-architectures.ipynb){ download }. Run the exercises in lecture order using the bundled sample data. Each lecture includes checks and a suggested variation.

## Course project

Submit a sparse-routing simulator and an architecture decision for a fixed interactive and batch workload.

**How to check your project**

Count active and resident parameters separately. Include a load-skew slice and an overflow policy. Identify which bottleneck needs a real multi-device benchmark.

## Further study

- [DeepSeek-V3 technical report](https://arxiv.org/abs/2412.19437)
- [Qwen3.5 MoE architecture](https://huggingface.co/docs/transformers/model_doc/qwen3_5_moe)
- [vLLM expert parallel deployment](https://docs.vllm.ai/en/stable/serving/expert_parallel_deployment/)
- [Expert load balancing](../../concepts/cards/expert-load-balancing.md)
- [Hybrid attention backbones](../../concepts/cards/hybrid-attention-backbones.md)

[All courses](../index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
