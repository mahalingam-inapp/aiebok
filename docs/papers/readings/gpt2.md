# Language Models are Unsupervised Multitask Learners

## Citation

Radford et al.. *Language Models are Unsupervised Multitask Learners.* 2019. [https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)

## One-sentence contribution

Decoder-only LM scales to strong zero-shot behavior.

## Problem

Demonstrating that a single left-to-right language model could perform diverse NLP tasks without task-specific architectures.

## Prior art

BERT-style masked modeling excelled at understanding tasks but generation required separate decoders.

## Core idea

Train a large decoder-only transformer to predict the next token on WebText; use prompts to steer behavior at inference time.

## Evidence

- Strong zero-shot performance on QA, summarization, and translation versus prior supervised systems on some benchmarks.
- Scaling model size improved zero-shot capabilities predictably.

## Limitations

- No bidirectional context
- Hallucination on factual QA without retrieval

## Lasting impact

Established the GPT line and in-context learning as a product paradigm.

## Reproduction exercise

Run gpt2-small on a few prompt templates and compare outputs with temperature 0 vs 0.8 on the same seed.

## Related chapters

- [05 Inference And Sampling](../../books/04-transformers-and-foundation-models/05-inference-and-sampling.md)
- [01 Instructions That Work](../../books/05-prompt-and-context-engineering/01-instructions-that-work.md)

## Related concepts

- [Sampling](../../concepts/cards/sampling.md)
- [Few Shot Examples](../../concepts/cards/few-shot-examples.md)
- [Logits](../../concepts/cards/logits.md)
