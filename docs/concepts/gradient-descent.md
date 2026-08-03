# Gradient Descent

**Purpose:** Gradient descent adjusts parameters in the direction that most reduces loss, using gradients computed from training examples.

**Prerequisites:** See related concepts and book chapters linked from the [concept card](cards/gradient-descent.md).

## Why this exists

Gradient descent adjusts parameters in the direction that most reduces loss, using gradients computed from training examples. It is the workhorse optimizer behind most neural network training.

## Core intuition

One SGD step on linear regression moves weights toward the line minimizing squared error on the mini-batch.

## Mechanics

1. Define the decision or system stage where gradient descent applies.
2. Implement the smallest version that beats an obvious baseline.
3. Measure on normal, boundary, and adversarial slices—not a single demo.
4. Document version, config, and rollback before production use.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Hand-compute one update for noisy y = 2x + 1 data and confirm loss decreases on that batch.

## Code practice

Run `python labs/0104-the-mathematics-engineers-need/main.py` from the repository root.

## When to use

Use when behavior must change systematically across many examples and prompts alone cannot reach quality or format targets.

## When not to use

Skip when RAG, better prompts, or routing fix the gap with less regression risk.

## Common failure modes

- Overfitting small curated sets
- Catastrophic forgetting of general capabilities
- Train-serve skew from preprocessing differences

## Common misconceptions

- Fine-tuning fixes bad retrieval or missing data.
- More training steps always help.
- Open weights eliminate governance responsibilities.

## Trade-offs

Gradient Descent improves some outcomes but adds complexity, latency, or operational burden. Compare against simpler alternatives on *your* workload before adopting by default.

## Evolution lens

Yesterday: task-specific training from scratch. Today: adapt foundation models with SFT, LoRA, and preferences. Tomorrow: continuous learning with governance. The durable principle is matching adaptation method to data and risk.
