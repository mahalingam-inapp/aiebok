# Constitutional AI: Harmlessness from AI Feedback

## Citation

Bai et al.. *Constitutional AI: Harmlessness from AI Feedback.* 2022. [https://arxiv.org/abs/2212.08073](https://arxiv.org/abs/2212.08073)

## One-sentence contribution

Principle-guided critique and revision for safer assistants.

## Problem

RLHF for harmlessness requires humans to label toxic/harmful outputs—a slow, expensive, and psychologically taxing process. Scaling safety alignment needed alternatives to human harm labels.

## Prior art

InstructGPT/RLHF used human preference labels for helpfulness and harmlessness. Red-teaming collected adversarial prompts but reactively. Rule-based filters were brittle and over-blocked legitimate queries.

## Core idea

Bai et al. introduced Constitutional AI (CAI): define a set of written principles (a 'constitution') and have the model self-critique its outputs against these principles, then revise to comply. The revised outputs become training data for RLAIF (RL from AI Feedback)—replacing human harm labels with AI-generated preference labels. Two phases: (1) supervised revision using critique→revision chains; (2) RLAIF preference training where AI compares revised vs. original outputs.

## Evidence

- Helpful and harmless: CAI models matched RLHF on human eval with fewer human harm labels.
- RLAIF preferences correlated with human preferences on held-out harmlessness comparisons.
- Chain-of-thought critique improved revision quality over direct revision.
- Principle specificity mattered—vague principles produced inconsistent revisions.

## Limitations

- Principles can conflict (helpful vs. harmless tradeoffs require priority ordering).
- Models can game principles (sycophantic agreement, excessive hedging).
- AI feedback inherits model biases—errors in critique propagate to training.
- Does not address jailbreaks or adversarial inputs at inference time.

## Lasting impact

CAI/RLAIF became Anthropic's alignment methodology for Claude and influenced industry thinking on scalable safety. Principle-based alignment is now a standard alternative to pure human-label RLHF.

## Reproduction exercise

Write 5 harmlessness principles. Prompt an LLM to critique 20 assistant responses against them, then revise. Compare original vs. revised on a toxicity classifier (e.g., Perspective API or a simple LLM judge). Measure revision rate and false-positive over-refusal on benign prompts.

## Related chapters

- [05 Responsible Ai And Risk](../../books/10-evaluation-safety-and-governance/05-responsible-ai-and-risk.md)
- [04 Security Of Ai Systems](../../books/10-evaluation-safety-and-governance/04-security-of-ai-systems.md)
- [02 Post Training Methods](../../books/11-training-serving-and-ai-operations/02-post-training-methods.md)

## Related concepts

- [Instruction Tuning](../../concepts/cards/instruction-tuning.md)
- [Human Evaluation](../../concepts/cards/human-evaluation.md)
- [Values](../../concepts/cards/values.md)
