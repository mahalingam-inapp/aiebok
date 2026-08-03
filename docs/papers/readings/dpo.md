# Direct Preference Optimization

## Citation

Rafailov et al.. *Direct Preference Optimization.* 2023. [https://arxiv.org/abs/2305.18290](https://arxiv.org/abs/2305.18290)

## One-sentence contribution

Optimize preferences without explicit reward modeling.

## Problem

RLHF requires training a separate reward model and running PPO—a complex, unstable pipeline with many hyperparameters. Simpler alignment methods that directly optimize preferences were needed for research reproducibility and production reliability.

## Prior art

InstructGPT used SFT + RM + PPO. Earlier work optimized ranking losses but not at LM scale. SLiC and similar methods used contrastive losses but without the closed-form preference likelihood derivation.

## Core idea

Rafailov et al. showed that the RLHF optimal policy has a closed-form solution under the Bradley-Terry preference model, yielding a simple classification loss: maximize log σ(β(log π_θ(y_w|x) - log π_θ(y_l|x))) where y_w and y_l are chosen/rejected responses and π_ref is the reference (SFT) policy implicit in the loss. DPO skips the reward model entirely—directly fine-tune the LM on preference pairs. β controls deviation from the reference policy (analogous to KL penalty in PPO).

## Evidence

- Sentiment control (IMDb): DPO matched PPO on human eval with simpler training.
- Summarization (Reddit TL;DR): DPO preferred over PPO and best-of-n baselines.
- Anthropic HH dialogue: DPO competitive with PPO on helpfulness/harmlessness.
- Training stability: DPO converged without PPO's reward hacking or KL collapse issues.

## Limitations

- Offline preferences only—cannot explore new responses during training like online RL.
- Distribution shift: policy moves away from reference, preferences may not generalize.
- β tuning is critical; wrong β causes overfitting to preferences or no learning.
- Does not handle multi-objective preferences or constraints as naturally as constrained RL.

## Lasting impact

DPO became the default alignment method for open-source models (Zephyr, Tulu, many HuggingFace models) due to simplicity and reproducibility. It largely replaced PPO in research settings.

## Reproduction exercise

Run DPO on 200 preference pairs (Anthropic HH subset) with `mistral-7b-sft` using TRL. Compare win-rate against the SFT baseline on 30 held-out prompts using an LLM judge. Sweep β ∈ {0.1, 0.5, 1.0} and plot preference accuracy on a validation set.

## Related chapters

- [02 Post Training Methods](../../books/11-training-serving-and-ai-operations/02-post-training-methods.md)
- [05 Responsible Ai And Risk](../../books/10-evaluation-safety-and-governance/05-responsible-ai-and-risk.md)
- [02 Metrics And Human Judgment](../../books/10-evaluation-safety-and-governance/02-metrics-and-human-judgment.md)

## Related concepts

- [Dpo](../../concepts/cards/dpo.md)
- [Sft](../../concepts/cards/sft.md)
- [Instruction Tuning](../../concepts/cards/instruction-tuning.md)
