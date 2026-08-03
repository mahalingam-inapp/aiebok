# LLaMA: Open and Efficient Foundation Language Models

## Citation

Touvron et al.. *LLaMA: Open and Efficient Foundation Language Models.* 2023. [https://arxiv.org/abs/2302.13971](https://arxiv.org/abs/2302.13971)

## One-sentence contribution

High-quality open-weights models trained on public data mixtures.

## Problem

State-of-the-art LMs (GPT-3, PaLM, Chinchilla) were closed—weights unavailable, training data undisclosed. Researchers and engineers needed high-quality open models to reproduce, fine-tune, and deploy without API dependencies.

## Prior art

GPT-3 and PaLM were API-only. OPT (Meta) and BLOOM (BigScience) released open weights but lagged closed models on quality. GPT-Neo/GPT-J were open but significantly weaker than frontier models.

## Core idea

Touvron et al. trained decoder-only Transformers (7B–65B) on publicly available text only, using Chinchilla-optimal token counts and architectural choices tuned for inference efficiency (SwiGLU activations, rotary embeddings, pre-normalization). No proprietary data—training mixture curated from CommonCrawl, C4, GitHub, Wikipedia, Books, ArXiv, and Stack Exchange. Released weights under a research license, enabling the open fine-tuning ecosystem (Alpaca, Vicuna, thousands of derivatives).

## Evidence

- LLaMA-13B outperformed GPT-3 175B on most benchmarks despite 13× fewer parameters.
- LLaMA-65B competitive with Chinchilla 70B and PaLM 540B on MMLU, HellaSwag, BigBench.
- Inference efficiency: 7B model runnable on consumer hardware with quantization.
- Open release spawned 1000+ fine-tuned variants within months (Alpaca, Vicuna, WizardLM).

## Limitations

- Initial license restricted commercial use (relaxed in LLaMA 2).
- English-heavy training data; multilingual performance lags dedicated multilingual models.
- No alignment training in base LLaMA—requires SFT/RLHF for assistant use.
- Safety and toxicity not primary training objectives; base model can generate harmful content.

## Lasting impact

LLaMA catalyzed the open-weights revolution—local deployment, private fine-tuning, and research reproducibility at near-frontier quality. LLaMA 2/3 and derivatives (Mistral, Mixtral) continue this lineage.

## Reproduction exercise

Download `meta-llama/Llama-3.2-1B` (or smallest available), run perplexity on a 1MB text sample, and compare against GPT-2-xl. Fine-tune with LoRA on 200 instruction pairs and evaluate on 20 held-out prompts vs. base model.

## Related chapters

- [06 Model Families And Selection](../../books/04-transformers-and-foundation-models/06-model-families-and-selection.md)
- [05 Deployment And Routing](../../books/11-training-serving-and-ai-operations/05-deployment-and-routing.md)
- [01 Choosing Adaptation](../../books/11-training-serving-and-ai-operations/01-choosing-adaptation.md)

## Related concepts

- [Open Weights](../../concepts/cards/open-weights.md)
- [Quantization](../../concepts/cards/quantization.md)
- [Lora](../../concepts/cards/lora.md)
