# KV Cache

**Purpose:** Reuse previously computed key and value tensors during autoregressive decoding to avoid reprocessing the full prefix on every new token.

**Prerequisites:** Transformer inference, autoregressive generation, attention.

## Why KV cache exists

Each generated token attends to all prior tokens. Without caching, the model recomputes keys and values for the entire prefix at every step, wasting compute and increasing latency—especially for long system prompts and multi-turn chats.

## Core intuition

After processing a prefix once, store its K and V tensors. When generating the next token, compute Q, K, and V only for the new position and append the new K/V to the cache. Attention then uses the cached prefix plus the current token.

## Mechanics

1. Prefill: process the prompt in one or more forward passes and populate the cache.
2. Decode: for each new token, extend cache with that token's K and V.
3. Memory grows with sequence length × layers × head dimension × batch size.
4. Batching requires padding or paged cache strategies when sequences differ in length.

## Engineering checklist

- Measure time-to-first-token separately from tokens-per-second after prefill.
- Budget GPU memory for maximum context plus concurrent sessions.
- Invalidate or rebuild cache when the prefix changes (prompt edit, tool result injection).
- Compare latency with and without cache on identical workloads before optimizing elsewhere.

## Trade-offs

KV caching dramatically improves decode throughput but increases memory footprint and complicates dynamic prefix updates. Very long contexts may require quantization, offloading, or prefix compression.

## Common misconceptions

- Caching does not remove the context window limit.
- Changing any cached prefix requires recomputation from the edit point forward.
- Cache hit rate in serving is a product of session design, not an automatic property.

## Evolution lens

Yesterday: full recompute per token. Today: standard in production inference servers. Tomorrow: smarter cache sharing, speculative decoding, and hierarchical memory. The durable principle is amortizing prefix computation across many decode steps.
