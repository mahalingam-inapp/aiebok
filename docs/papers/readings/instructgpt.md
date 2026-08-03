# Training Language Models to Follow Instructions

## Citation

Ouyang et al.. *Training Language Models to Follow Instructions.* 2022. [https://arxiv.org/abs/2203.02155](https://arxiv.org/abs/2203.02155)

## One-sentence contribution

RLHF aligns models to human preferences on instruction following.

## Problem

Large LMs trained on internet text predict the next token, not what users actually want—they produce unhelpful, untruthful, or toxic outputs despite high fluency. Aligning model behavior to human intent required more than scale alone.

## Prior art

GPT-3 could be prompted but was unreliable on instructions. Supervised fine-tuning (SFT) on demonstration data helped but did not scale and did not optimize for human preferences over multiple valid outputs. Earlier RLHF work (Christiano et al.) existed but not at LM scale.

## Core idea

Ouyang et al. applied a three-stage pipeline: (1) SFT on human-written demonstrations for desired behavior; (2) train a reward model (RM) on human comparisons of model outputs—labelers rank which of several completions is better; (3) fine-tune the SFT model with PPO reinforcement learning, using the RM as the reward signal while constraining deviation from the SFT policy via a KL penalty. The RM captures preferences that are hard to specify as rules; PPO optimizes the policy toward higher reward.

## Evidence

- 1.3B InstructGPT preferred over 175B raw GPT-3 by human labelers on prompts—alignment beat scale.
- Truthfulness and harmlessness scores improved significantly vs. GPT-3 on held-out prompts.
- PPO + RM outperformed SFT alone and supervised fine-tuning on human-written completions.
- Labeler agreement with held-out researchers' preferences correlated with RM scores.

## Limitations

- Human labeling is expensive (~$600k+ for InstructGPT-scale data) and introduces labeler bias.
- PPO training is unstable—requires careful KL tuning, reward hacking monitoring.
- Reward model can be gamed (verbose, sycophantic outputs score well).
- Does not eliminate hallucination or jailbreaks—alignment is partial.

## Lasting impact

InstructGPT's RLHF pipeline became the template for ChatGPT, Claude, and virtually every aligned assistant. It shifted industry focus from raw LM benchmarks to human preference evaluation and safety metrics.

## Reproduction exercise

Using TRL or a similar library, run SFT on 500 instruction-response pairs (Alpaca subset), then train a reward model on 200 preference pairs (chosen/rejected). Compare PPO-tuned vs. SFT-only outputs on 20 held-out prompts with a simple LLM-as-judge or human rating. Budget: single A100 for a few hours on a 1–3B model.

## Related chapters

- [02 Post Training Methods](../../books/11-training-serving-and-ai-operations/02-post-training-methods.md)
- [02 Metrics And Human Judgment](../../books/10-evaluation-safety-and-governance/02-metrics-and-human-judgment.md)
- [01 Instructions That Work](../../books/05-prompt-and-context-engineering/01-instructions-that-work.md)

## Related concepts

- [Sft](../../concepts/cards/sft.md)
- [Instruction Tuning](../../concepts/cards/instruction-tuning.md)
- [Human Evaluation](../../concepts/cards/human-evaluation.md)
