# Training Compute-Optimal Large Language Models

## Citation

Hoffmann et al.. *Training Compute-Optimal Large Language Models.* 2022. [https://arxiv.org/abs/2203.15556](https://arxiv.org/abs/2203.15556)

## One-sentence contribution

Optimal training balances model size and token count.

## Problem

Kaplan scaling laws suggested allocating most compute to model size, leading to undertrained large models (e.g., Gopher 280B). The field needed revised guidance on the optimal balance between parameters and training tokens.

## Prior art

Kaplan et al. (2020) scaling laws favored larger models. GPT-3, Gopher, and early LLaMA variants trained on fewer tokens per parameter than later models. Empirical evidence suggested some large models were compute-inefficient.

## Core idea

Hoffmann et al. re-derived scaling laws with a corrected compute budget formulation and found that model size and training tokens should scale equally—roughly 20 tokens per parameter for compute-optimal training. They trained Chinchilla (70B params, 1.4T tokens)—4× more data than Gopher (280B, 300B tokens)—and showed it outperformed Gopher on virtually every benchmark despite being 4× smaller. The key insight: most contemporary LMs were over-parameterized and under-trained.

## Evidence

- Chinchilla 70B beat Gopher 280B on MMLU, HellaSwag, BigBench, and 15+ other benchmarks.
- Compute-optimal frontier: ~20 tokens/parameter across model sizes from 400M to 70B.
- Training smaller models on more data matched larger undertrained models at equal compute.
- Revised scaling exponents differed from Kaplan—equal scaling of N and D, not favoring N.

## Limitations

- Assumes fixed compute budget; inference cost favors smaller models even if training cost is equal.
- Data quality and mixture not modeled—20 tokens/parameter is an average, not universal.
- Does not address post-training (SFT, RLHF) compute allocation.
- Chinchilla weights were not released—impact is primarily on training recipes.

## Lasting impact

Chinchilla-optimal training became the standard for open models: LLaMA 2, Mistral, OLMo, and most post-2022 models train on ~20 tokens/parameter. It corrected a systematic inefficiency in the field's scaling strategy.

## Reproduction exercise

Compare two training runs at equal FLOPs budget: (A) small model, many tokens vs. (B) large model, few tokens using nanoGPT or a similar framework. Evaluate perplexity on held-out text. Confirm that (A) matches or beats (B)—demonstrating the Chinchilla principle at small scale.

## Related chapters

- [04 Training Foundation Models](../../books/04-transformers-and-foundation-models/04-training-foundation-models.md)
- [03 Dataset Engineering](../../books/11-training-serving-and-ai-operations/03-dataset-engineering.md)
- [06 Model Families And Selection](../../books/04-transformers-and-foundation-models/06-model-families-and-selection.md)

## Related concepts

- [Scaling Laws](../../concepts/cards/scaling-laws.md)
- [Data Curation](../../concepts/cards/data-curation.md)
- [Data Mixtures](../../concepts/cards/data-mixtures.md)
