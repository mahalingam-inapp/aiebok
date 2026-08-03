# Training a Helpful and Harmless Assistant

## Citation

Bai et al.. *Training a Helpful and Harmless Assistant.* 2022. [https://arxiv.org/abs/2212.08073](https://arxiv.org/abs/2212.08073)

## One-sentence contribution

Preference modeling balances helpfulness and harmlessness.

## Problem

Assistant models optimized for helpfulness alone can produce harmful or unsafe outputs.

## Prior art

RLHF work focused primarily on task quality without explicit harm constraints.

## Core idea

Train preference models that trade off helpfulness and harmlessness, using human comparisons to steer responses away from unsafe compliance.

## Evidence

- Demonstrated reduction in harmful outputs on red-team prompts versus helpfulness-only models.
- Showed multi-objective preference modeling is feasible at scale.

## Limitations

- Over-refusal on benign tasks
- Preference data encodes annotator values

## Lasting impact

Established harmlessness as a first-class alignment objective alongside helpfulness.

## Reproduction exercise

Evaluate a base instruct model on 20 harmless vs sensitive prompts; tag over-refusal vs under-refusal.

## Related chapters

- [05 Responsible Ai And Risk](../../books/10-evaluation-safety-and-governance/05-responsible-ai-and-risk.md)
- [02 Post Training Methods](../../books/11-training-serving-and-ai-operations/02-post-training-methods.md)

## Related concepts

- [Human Evaluation](../../concepts/cards/human-evaluation.md)
- [Values](../../concepts/cards/values.md)
