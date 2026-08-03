# Learning to Summarize from Human Feedback

## Citation

Stiennon et al.. *Learning to Summarize from Human Feedback.* 2020. [https://arxiv.org/abs/2009.01325](https://arxiv.org/abs/2009.01325)

## One-sentence contribution

Early large-scale RLHF for summarization quality.

## Problem

Automatic metrics (ROUGE, BLEU) poorly correlate with human judgment on summarization quality—optimizing ROUGE produces verbose, repetitive summaries. Human preferences needed to be incorporated into training objectives directly.

## Prior art

Supervised fine-tuning on reference summaries. ROUGE/BLEU optimization produced metric-gaming artifacts. RL from human feedback (Christiano et al., 2017) existed for simple tasks but not at summarization scale.

## Core idea

Stiennon et al. collected human comparisons of summary pairs (which is better?) for Reddit TL;DR posts. Trained a reward model (6B Transformer) to predict human preferences from comparison data. Fine-tuned a policy (GPT-3 1.3B) with PPO using the reward model as the objective, with a KL penalty to stay close to the SFT initialization. The key insight: preference comparisons are easier and more reliable for humans to provide than absolute quality scores or writing reference summaries.

## Evidence

- Human eval: RLHF summaries preferred over SFT and ROUGE-optimized baselines.
- ROUGE scores did not predict human preference—ROUGE-optimized summaries were dispreferred.
- Reward model accuracy on held-out comparisons: ~70%—sufficient for PPO training signal.
- KL penalty was critical—without it, PPO collapsed to high-reward but low-quality outputs.

## Limitations

- Reward hacking: models learn to exploit RM weaknesses (length bias, format preferences).
- Human comparison data is expensive (~64k comparisons for this paper).
- RM accuracy ceiling (~70%) limits alignment quality.
- Summarization-specific—generalizing to dialogue, coding, etc. required follow-up work (InstructGPT).

## Lasting impact

This paper established the RM + PPO pipeline that InstructGPT and ChatGPT scaled to general instruction following. Preference learning over pointwise metrics became the standard alignment approach.

## Reproduction exercise

Collect 50 pairwise summary preferences on news articles. Train a small reward model (BERT-base classifier) on chosen/rejected pairs. Compare RM-predicted rankings against held-out human judgments. Optionally run 100 steps of PPO on a 1B model and compare summaries before/after.

## Related chapters

- [02 Post Training Methods](../../books/11-training-serving-and-ai-operations/02-post-training-methods.md)
- [02 Metrics And Human Judgment](../../books/10-evaluation-safety-and-governance/02-metrics-and-human-judgment.md)
- [01 Evaluation As Requirements](../../books/10-evaluation-safety-and-governance/01-evaluation-as-requirements.md)

## Related concepts

- [Human Evaluation](../../concepts/cards/human-evaluation.md)
- [Sft](../../concepts/cards/sft.md)
- [Rubrics](../../concepts/cards/rubrics.md)
