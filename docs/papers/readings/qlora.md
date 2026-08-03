# QLoRA: Efficient Finetuning of Quantized LLMs

## Citation

Dettmers et al.. *QLoRA: Efficient Finetuning of Quantized LLMs.* 2023. [https://arxiv.org/abs/2305.14314](https://arxiv.org/abs/2305.14314)

## One-sentence contribution

4-bit base model plus LoRA enables accessible fine-tuning.

## Problem

Full fine-tuning of large models is inaccessible on consumer GPUs.

## Prior art

LoRA reduced trainable parameters but activations still dominated memory.

## Core idea

QLoRA quantizes the frozen base model to 4-bit NormalFloat while training LoRA adapters, enabling fine-tuning large models on one GPU.

## Evidence

- Reported near full fine-tune quality on several benchmarks with 4-bit base + LoRA.
- Enabled widespread community fine-tuning experiments.

## Limitations

- Quantization can hurt sensitive tasks
- Still requires careful eval before production

## Lasting impact

Standard technique for accessible adaptation of open models.

## Reproduction exercise

Fine-tune a 7B model with QLoRA on 500 examples; compare to prompt-only baseline on held-out slice.

## Related chapters

- [02 Post Training Methods](../../books/11-training-serving-and-ai-operations/02-post-training-methods.md)
- [01 Choosing Adaptation](../../books/11-training-serving-and-ai-operations/01-choosing-adaptation.md)

## Related concepts

- [Lora](../../concepts/cards/lora.md)
- [Quantization](../../concepts/cards/quantization.md)
- [Sft](../../concepts/cards/sft.md)
