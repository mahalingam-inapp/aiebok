# Self-Instruct: Aligning Language Models with Self-Generated Instructions

## Citation

Wang et al.. *Self-Instruct: Aligning Language Models with Self-Generated Instructions.* 2023. [https://arxiv.org/abs/2212.10560](https://arxiv.org/abs/2212.10560)

## One-sentence contribution

Bootstrap instruction data from a seed set.

## Problem

Instruction tuning requires large datasets of (instruction, response) pairs, typically written by humans. Scaling instruction data to improve zero-shot generalization was bottlenecked by annotation cost.

## Prior art

Manual datasets: Super-NaturalInstructions (600+ tasks), P3, FLAN collection—all human-curated. Data augmentation existed but not for instruction generation specifically.

## Core idea

Wang et al. bootstrap instruction data from a seed set of 175 human-written tasks: (1) prompt the LM to generate new instruction descriptions; (2) determine if each instruction is valid (classification); (3) generate input instances for the instruction; (4) filter low-quality instances; (5) generate responses. Iterate to expand the pool. The resulting 52k instruction dataset (Self-Instruct) fine-tunes the base LM, improving zero-shot performance on unseen tasks from Super-NaturalInstructions.

## Evidence

- 52k self-generated instructions improved zero-shot on 119 held-out tasks vs. base LM.
- Outperformed training on human-written instruction datasets of similar size.
- Alpaca (built on Self-Instruct methodology with GPT-3.5 as generator) went viral—demonstrating practical utility.
- Quality filtering was essential—unfiltered self-generated data hurt performance.

## Limitations

- Quality ceiling bounded by the generating model's capabilities.
- Repetitive or trivial instructions accumulate without diversity controls.
- Instruction complexity does not exceed the generator—no novel hard tasks emerge.
- Seed task selection biases the generated distribution.

## Lasting impact

Self-Instruct enabled Alpaca, Vicuna, and the open instruction-tuning ecosystem. Synthetic data generation for alignment is now standard practice in model training pipelines.

## Reproduction exercise

Start with 10 seed instruction templates. Use GPT-4o-mini to generate 100 new instructions, filter for validity, generate instances and responses. Fine-tune a 1B model on the result and evaluate on 20 held-out tasks vs. base model zero-shot.

## Related chapters

- [03 Dataset Engineering](../../books/11-training-serving-and-ai-operations/03-dataset-engineering.md)
- [02 Post Training Methods](../../books/11-training-serving-and-ai-operations/02-post-training-methods.md)
- [01 Instructions That Work](../../books/05-prompt-and-context-engineering/01-instructions-that-work.md)

## Related concepts

- [Synthetic Data](../../concepts/cards/synthetic-data.md)
- [Instruction Tuning](../../concepts/cards/instruction-tuning.md)
- [Sft](../../concepts/cards/sft.md)
