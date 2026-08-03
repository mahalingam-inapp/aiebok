# Attention

**Purpose:** Route information between sequence positions based on content compatibility rather than fixed distance.

**Prerequisites:** Vectors, dot product, softmax, sequence models.

## Why attention exists

Recurrent models pass information through a fixed bottleneck and struggle with long-range dependencies. Attention lets each position directly gather context from any other position by comparing a query against keys and weighting values.

## Core intuition

Attention is content-dependent routing: positions with compatible queries and keys receive higher weight. Multi-head attention runs several such routes in parallel so the model can capture different relationship types.

## Mechanics

1. Project hidden states into queries (Q), keys (K), and values (V).
2. Compute compatibility scores, typically scaled dot products: \(QK^\top / \sqrt{d_k}\).
3. Apply masks to block illegal positions (e.g., future tokens during decoding).
4. Normalize scores with softmax to obtain attention weights.
5. Return the weighted sum of values.

## Engineering checklist

- Verify tensor shapes at each step when implementing from scratch.
- Use masking for causal decoding and padding; unmasked illegal positions leak information.
- Profile attention cost; it scales quadratically with sequence length in standard form.
- Compare attention patterns when debugging unexpected generation or translation behavior.

## Code practice

Run `python examples/04-attention-sampling/main.py` and inspect weight distributions for aligned versus misaligned token pairs.

## Trade-offs

Attention enables flexible long-range mixing but increases compute and memory versus local convolutions or recurrence. Sparse, linear, or sliding-window variants trade expressiveness for efficiency.

## Common misconceptions

- Attention weights are not guaranteed interpretable “explanations.”
- More heads are not automatically better; each head must earn its cost.
- Attention replaces neither data quality nor downstream evaluation.

## Evolution lens

Yesterday: fixed recurrence and local windows. Today: scaled dot-product attention in transformers. Tomorrow: more efficient approximations and modality-specific routing. The durable principle is selective information flow based on content similarity.
