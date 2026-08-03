# Lora

**Purpose:** LoRA fine-tunes low-rank adapter matrices in attention layers, reducing trainable parameters versus full fine-tuning.

**Prerequisites:** See related concepts and book chapters linked from the [concept card](cards/lora.md).

## Why this exists

LoRA fine-tunes low-rank adapter matrices in attention layers, reducing trainable parameters versus full fine-tuning.

## Core intuition

7B model with LoRA learns domain tone on one GPU while base weights stay frozen.

## Mechanics

1. Define the decision or system stage where lora applies.
2. Implement the smallest version that beats an obvious baseline.
3. Measure on normal, boundary, and adversarial slices—not a single demo.
4. Document version, config, and rollback before production use.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.

## Evidence of understanding

Report eval uplift, training cost, and adapter version at inference.

## Code practice

Run `python labs/1102-post-training-methods/main.py` from the repository root.

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

Lora improves some outcomes but adds complexity, latency, or operational burden. Compare against simpler alternatives on *your* workload before adopting by default.

## Evolution lens

Yesterday: task-specific training from scratch. Today: adapt foundation models with SFT, LoRA, and preferences. Tomorrow: continuous learning with governance. The durable principle is matching adaptation method to data and risk.
