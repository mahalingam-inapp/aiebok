# LoRA: Low-Rank Adaptation of Large Language Models

## Citation

Hu et al.. *LoRA: Low-Rank Adaptation of Large Language Models.* 2021. [https://arxiv.org/abs/2106.09685](https://arxiv.org/abs/2106.09685)

## One-sentence contribution

Train low-rank adapters while freezing base weights.

## Problem

Full fine-tuning of multi-billion-parameter models requires storing optimizer states and gradients for every parameter—prohibitively expensive for most practitioners and deployment scenarios with many task-specific adapters.

## Prior art

Adapters (Houlsby et al.) inserted small modules between layers. Prefix tuning prepended trainable tokens. BitFit updated only bias terms. All reduced trainable params but adapters added inference latency; prefix tuning limited context window.

## Core idea

Hu et al. hypothesized that weight updates during fine-tuning have low intrinsic rank. Instead of updating the full weight matrix W, LoRA learns a low-rank decomposition ΔW = BA where B ∈ R^{d×r}, A ∈ R^{r×k}, with r << min(d,k). Only A and B are trained; base weights W stay frozen. At inference, ΔW can be merged into W (no latency overhead) or kept separate for hot-swapping adapters. Applied to attention projection matrices (W_q, W_k, W_v, W_o) in Transformer layers.

## Evidence

- RoBERTa, DeBERTa, GPT-2: LoRA with r=4–8 matched full fine-tuning on GLUE, WikiSQL, SAMSum with <1% trainable parameters.
- GPT-3 175B: LoRA reduced trainable params by 10,000× vs. full fine-tuning with comparable MNLI and WikiSQL performance.
- No inference latency when merged; adapter swapping enables multi-tenant serving.
- Higher rank r improves quality but with diminishing returns beyond r=16 for most tasks.

## Limitations

- Rank r is a hyperparameter—too low underfits, too high approaches full fine-tuning cost.
- Not all tasks benefit equally; some complex reasoning tasks may need full fine-tune or higher rank.
- Merging adapters from different tasks is non-trivial (interference between LoRA matrices).
- Quantization + LoRA (QLoRA) adds compatibility constraints.

## Lasting impact

LoRA became the default parameter-efficient fine-tuning method, enabling the open-source fine-tuning ecosystem (Alpaca, thousands of HuggingFace adapters). Cloud providers offer LoRA training as a managed service.

## Reproduction exercise

Fine-tune `mistral-7b` with LoRA (r=8, alpha=16) on 500 instruction pairs using PEFT library. Compare eval loss and task accuracy against full fine-tune on a 7B model if GPU memory allows, or against prompt-only baseline. Log trainable parameter count and peak GPU memory.

## Related chapters

- [01 Choosing Adaptation](../../books/11-training-serving-and-ai-operations/01-choosing-adaptation.md)
- [02 Post Training Methods](../../books/11-training-serving-and-ai-operations/02-post-training-methods.md)
- [05 Deployment And Routing](../../books/11-training-serving-and-ai-operations/05-deployment-and-routing.md)

## Related concepts

- [Lora](../../concepts/cards/lora.md)
- [Qlora](../../concepts/cards/qlora.md)
- [Fine Tuning](../../concepts/cards/fine-tuning.md)
