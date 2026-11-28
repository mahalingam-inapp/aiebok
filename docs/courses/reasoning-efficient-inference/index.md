# Reasoning and Efficient Model Inference

Project practicum · 2 sections · 4 lectures · 3–4 hours, plus the project

Compare reasoning budgets, verifier-backed search, and speculative decoding under explicit quality and latency constraints.

[Start the first lecture](01-reasoning-budgets-and-model-cascades.md){ .md-button .md-button--primary .study-start data-course="reasoning-efficient-inference" }

## Practice case · Fast answers without a guess

Meera owns HarborLink's response-time budget. Some requests only need one current policy excerpt. Others require choosing a route across stations with exclusions. She can afford added model time when it changes what the desk can verify.

This fictional case continues through the lectures.

## Entry prerequisites

Basic language-model decoding, held-out evaluation, and Python.

## Course outline

### Allocate compute at inference time

- [01 · Reasoning budgets and model cascades](01-reasoning-budgets-and-model-cascades.md){ .study-lecture data-lecture="01-reasoning-budgets-and-model-cascades.md" } — Design a request-level escalation policy and compare it against always using one model configuration.
- [02 · Bounded search and independent verification](02-bounded-search-and-independent-verification.md){ .study-lecture data-lecture="02-bounded-search-and-independent-verification.md" } — Select a valid answer from candidate outputs under a bounded attempt budget.

### Improve throughput and measure honestly

- [03 · Prefill, decode and speculative decoding](03-prefill-decode-and-speculative-decoding.md){ .study-lecture data-lecture="03-prefill-decode-and-speculative-decoding.md" } — Model draft-token acceptance and explain when speculation can lower decode time.
- [04 · Serving workload and release gates](04-serving-workload-and-release-gates.md){ .study-lecture data-lecture="04-serving-workload-and-release-gates.md" } — Report time to first token, inter-token latency, and verified quality under a predeclared serving gate.

## Workbook

[Download the workbook](../../assets/notebooks/reasoning-efficient-inference.ipynb){ download }. Run the exercises in lecture order using the bundled sample data. Each lecture includes checks and a suggested variation.

## Course project

Deliver a paired inference evaluation with a default, an escalation policy, and a bounded fallback.

**How to check your project**

Report quality, p95 latency, cost per verified success, and the escalation rate separately. Keep model and serving configurations versioned.

## Further study

- [OpenAI reasoning model guide](https://developers.openai.com/api/docs/guides/reasoning)
- [Speculative decoding research](https://arxiv.org/abs/2211.17192)
- [vLLM serving benchmark reference](https://docs.vllm.ai/en/stable/cli/bench/serve/)
- [Continuous batching](../../concepts/cards/continuous-batching.md)

[All courses](../index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
