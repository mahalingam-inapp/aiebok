# Language Models are Few-Shot Learners

## Citation

Brown et al.. *Language Models are Few-Shot Learners.* 2020. [https://arxiv.org/abs/2005.14165](https://arxiv.org/abs/2005.14165)

## One-sentence contribution

Scale and in-context examples enable task behavior without fine-tuning.

## Problem

Task-specific fine-tuning required labeled datasets and separate model copies per task. Could a single large autoregressive model perform diverse tasks from natural language instructions and a few examples alone?

## Prior art

GPT-2 (1.5B) showed unsupervised LM pre-training produces some zero-shot ability. BERT required fine-tuning per task. T5 unified tasks as text-to-text but still needed fine-tuning. Prompt engineering on GPT-2 was anecdotal, not systematically evaluated.

## Core idea

Brown et al. scaled the GPT architecture to 175B parameters trained on ~300B tokens and evaluated three regimes: zero-shot (task description only), one-shot (one example), and few-shot (several in-context examples prepended to the prompt). No gradient updates  occur at inference—the model reads the prompt and continues generating. Scaling laws predicted that larger models would show sharper in-context learning curves, and the paper demonstrated this empirically across 10+ benchmarks.

## Evidence

- Few-shot GPT-3 175B matched or exceeded fine-tuned BERT-Large on TriviaQA, COPA, and LAMBADA in some settings.
- Scaling from 125M to 175B showed smooth improvement in in-context learning ability—smaller models gained little from few-shot prompts.
- Human eval on news article generation: 175B rated more coherent than 13B.
- One-shot and few-shot consistently outperformed zero-shot, confirming examples matter.

## Limitations

- 175B training cost (~$4.6M estimated) is not reproducible for most labs.
- In-context learning is inconsistent—prompt formatting, example order, and calibration swing results significantly.
- No built-in grounding, citation, or tool use; hallucination on factual queries.
- Few-shot performance still below dedicated fine-tuned models on many structured tasks.

## Lasting impact

GPT-3 shifted the field from fine-tuning to prompting and scaling, directly leading to ChatGPT, instruction tuning, and the current API-first AI product model. The in-context learning phenomenon remains an active research area.

## Reproduction exercise

Using an API model (e.g., GPT-4o-mini), evaluate GSM8K with 0-shot vs. 5-shot CoT prompts. Fix the random seed for example selection and run 50 problems. Compare accuracy and token cost. Repeat with permuted example order to measure prompt sensitivity.

## Related chapters

- [05 Inference And Sampling](../../books/04-transformers-and-foundation-models/05-inference-and-sampling.md)
- [01 Instructions That Work](../../books/05-prompt-and-context-engineering/01-instructions-that-work.md)
- [06 Model Families And Selection](../../books/04-transformers-and-foundation-models/06-model-families-and-selection.md)

## Related concepts

- [Few Shot Examples](../../concepts/cards/few-shot-examples.md)
- [Prompting](../../concepts/cards/prompting.md)
- [Scaling Laws](../../concepts/cards/scaling-laws.md)
