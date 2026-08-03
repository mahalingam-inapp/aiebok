# Fine-Tuning

**Purpose:** Adapt a pretrained model's behavior or style with supervised or preference data when prompting and retrieval are insufficient.

**Prerequisites:** Training versus inference, datasets, evaluation, model serving basics.

## Why fine-tuning exists

Some requirements need consistent tone, format, domain phrasing, or task-specific decisions that are expensive or unreliable to enforce purely through prompts. Fine-tuning bakes patterns into weights—at the cost of flexibility and operational complexity.

## Core intuition

Choose the **smallest intervention at the correct layer**: prompt first, then retrieval and tools, then fine-tuning when behavior—not just knowledge—must change reproducibly. Adaptation trades generality for targeted performance.

## Mechanics

1. **Diagnose the gap:** missing knowledge (often RAG) versus missing behavior (often SFT/DPO).
2. **Curate data:** representative, labeled, deduplicated, with held-out eval unaffected by contamination.
3. **Select method:** full fine-tune, LoRA/QLoRA for efficiency, DPO/RLHF for preferences.
4. **Train with tracked hyperparameters, seeds, and data versions.**
5. **Evaluate** on task metrics and regression suites before replacing the base model in production.

## Engineering checklist

- Publish a data card: sources, filters, label process, known biases, and eval splits.
- Check eval contamination from training duplicates.
- Compare adapted model against strong prompt+RAG baselines on cost and quality.
- Plan rollback to base or prior adapter versions.

## Trade-offs

Fine-tuning can improve consistency but adds training pipelines, drift risk, and version management. Small adapters (LoRA) reduce cost but still require eval discipline.

## Common misconceptions

- Fine-tuning is not a substitute for authorization, retrieval freshness, or eval.
- More training data does not fix misdefined tasks or leaky splits.
- Open-weight access does not remove governance obligations.

## Evolution lens

Yesterday: train models from scratch per task. Today: adapt foundation models with parameter-efficient methods. Tomorrow: continuous adaptation with stronger guardrails. The durable principle is targeted adaptation with evidence and rollback paths.
