# Hybrid Attention Backbones

**Purpose:** Reference card for **hybrid attention backbones** used across AIEBOK books and knowledge areas.

## Core explanation

Hybrid backbones combine full attention with layers that use another mechanism, such as gated linear attention or a state-space model. Full-attention layers still allocate context-dependent KV cache during standard decoding.

## Example

A 32-layer hybrid with eight full-attention layers carries both growing KV state and per-sequence recurrent state.

## When to use

Use when long contexts make per-layer KV growth expensive.

## When not to use

Require separate evidence for tasks that depend on exact long-range recall.

## Engineering checklist

- Account for recurrent state and full-attention KV separately.

## Evidence of understanding

Measure state memory by sequence length and include long-context tasks that require exact evidence retrieval.

## Common failure modes

- Memory estimates overlook state that scales with the number of active sequences.

## Trade-offs

No mechanism is universal. Compare hybrid attention backbones against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- [Run the course practicum](../../courses/sparse-model-architectures/index.md)
- [Question index](../../reference/question-index.md)
- [Guided lessons](../../lessons/index.md)
- Run the matching chapter lab under `labs/` when available
