# Orca: Progressive Learning from Complex Explanation Traces

## Citation

Mukherjee et al.. *Orca: Progressive Learning from Complex Explanation Traces.* 2023. [https://arxiv.org/abs/2306.02707](https://arxiv.org/abs/2306.02707)

## One-sentence contribution

Distill reasoning traces from stronger teachers.

## Problem

Instruction-tuned models lagged proprietary assistants in reasoning and explanation quality.

## Prior art

SFT on human-written instructions alone was limited by dataset scale and diversity.

## Core idea

Orca distills reasoning traces from a stronger teacher model into a smaller open model using explanation-rich training signals.

## Evidence

- Reported gains on reasoning benchmarks versus standard instruction tuning on similar compute.
- Showed synthetic explanation data can improve smaller models.

## Limitations

- Teacher dependency
- Risk of inheriting teacher errors and style

## Lasting impact

Accelerated distillation and synthetic instruction dataset practices.

## Reproduction exercise

Compare base vs instruction-tuned 7B model on 20 math word problems; optionally add chain-of-thought exemplars.

## Related chapters

- [02 Post Training Methods](../../books/11-training-serving-and-ai-operations/02-post-training-methods.md)
- [01 Reasoning As Search](../../books/07-reasoning-and-tool-use/01-reasoning-as-search.md)

## Related concepts

- [Sft](../../concepts/cards/sft.md)
- [Instruction Tuning](../../concepts/cards/instruction-tuning.md)
- [Distillation](../../concepts/cards/distillation.md)
