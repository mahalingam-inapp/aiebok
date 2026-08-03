# Scaling Laws for Neural Language Models

## Citation

Kaplan et al.. *Scaling Laws for Neural Language Models.* 2020. [https://arxiv.org/abs/2001.08361](https://arxiv.org/abs/2001.08361)

## One-sentence contribution

Loss scales predictably with compute, parameters, and data.

## Problem

Training large LMs is expensive; practitioners lacked principled guidance on how to allocate compute between model size, dataset size, and training duration to minimize loss.

## Prior art

Empirical scaling in vision (Hestness et al.) showed power-law learning curves. Prior LM work (Kaplan's team at OpenAI, earlier) had scattered results without a unified framework. Ad hoc decisions dominated pretraining budgets.

## Core idea

Kaplan et al. empirically measured language modeling loss across models spanning 7 orders of magnitude in compute, finding smooth power-law relationships: L(N) ∝ N^{-α} for parameters, L(D) ∝ D^{-β} for dataset size, L(C) ∝ C^{-γ} for total compute. The exponents α, β, γ were fit from hundreds of training runs. Optimal allocation under a fixed compute budget favors scaling model size over data more aggressively than later Chinchilla work would suggest.

## Evidence

- Loss curves were smooth power laws across 6+ orders of magnitude with no observed plateau—larger always helped within the tested range.
- Downstream task performance (e.g., HellaSwag) correlated with pretraining loss across scales.
- Optimal compute allocation formula predicted GPT-3 sizing reasonably well.
- Extrapolation from smaller runs predicted larger model loss within ~10% error.

## Limitations

- Chinchilla (2022) revised optimal token-to-parameter ratio—Kaplan favored larger models relative to data than is compute-optimal.
- Power laws are task-dependent; code and math may scale differently from general text.
- Does not account for data quality, architecture choices, or post-training effects.
- Extrapolation beyond measured range (to trillion-parameter models) is uncertain.

## Lasting impact

Scaling laws justified billion-dollar pretraining investments and shaped GPT-3/4, PaLM, and LLaMA sizing decisions. They remain the starting point for compute budgeting, even after Chinchilla refinements.

## Reproduction exercise

Train 5 small GPT-2 variants (varying params 10M–400M) on the same OpenWebText subset for fixed token counts. Plot validation loss vs. parameters on log-log axes. Fit a power law and predict the 800M model's loss. Compare predicted vs. actual.

## Related chapters

- [04 Training Foundation Models](../../books/04-transformers-and-foundation-models/04-training-foundation-models.md)
- [04 Inference Infrastructure](../../books/11-training-serving-and-ai-operations/04-inference-infrastructure.md)
- [05 Evaluation And Error Analysis](../../books/02-machine-learning-systems/05-evaluation-and-error-analysis.md)

## Related concepts

- [Scaling Laws](../../concepts/cards/scaling-laws.md)
- [Training](../../concepts/cards/training.md)
- [Loss Functions](../../concepts/cards/loss-functions.md)
