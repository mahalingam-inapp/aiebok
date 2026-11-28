# Hybrid backbones and architecture selection

<p class="study-position" data-course="sparse-model-architectures" data-lecture="04-hybrid-backbones-and-architecture-selection.md">Size the system and workload · Lecture 4 of 4</p>

[← Expert parallelism and communication](03-expert-parallelism-and-communication.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions }

??? note "Jump to a lecture"

    **Route tokens through experts**

    - [Token routing and top-k experts](01-token-routing-and-top-k-experts.md)
    - [Expert capacity and load balancing](02-expert-capacity-and-load-balancing.md)

    **Size the system and workload**

    - [Expert parallelism and communication](03-expert-parallelism-and-communication.md)
    - **Hybrid backbones and architecture selection** (current)

## What you will learn

Compare conventional KV cache growth with a hybrid model that combines recurrent state and full attention.

## The workload has two kinds of long prompt

Support wants exact citations in a long policy. Maintenance wants a summary of recurring events across a log. Those requests can have the same number of input tokens.

Measure memory against input length and run each task separately. A lower cache estimate can be a useful reason to benchmark and says little about quality on an exact lookup.

## How it works

MoE changes the feed-forward path. Attention variants change how a layer represents or accesses sequence history. Grouped-query attention shares key and value heads across query heads. Multi-head latent attention stores a compressed latent representation with implementation-specific cache overhead. Hybrid models can mix gated linear or state-space layers with full-attention layers, so the remaining full-attention layers still grow a cache with context.

### Match architecture to a real request shape
Use one formula per attention or recurrent layer. Grouped-query attention reduces KV heads relative to multi-head attention, while some recurrent layers keep a fixed-size state for each active sequence. Compressed latent KV is a third approach and cache layout varies by runtime. Report actual device memory separately from arithmetic estimates. Measure long-context evidence use as well as memory, and fix the model and tokenizer when isolating a serving-engine change.

## Worked example

A 32-layer hybrid with eight full-attention layers can grow less token-dependent state than 32 equivalent full-attention layers. The recurrent layers still consume fixed per-sequence state, and the crossover changes with context length.

### Follow the example

**Given:** One 32-layer model uses full attention in every layer. The hybrid has eight full-attention layers and 24 fixed-state layers.

**Walkthrough:** Multiply token-dependent bytes by 32 and 8 respectively, then add the fixed hybrid state. Before selecting the hybrid, check exact recall on a long policy and compare with summarized logs.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
def estimate_state(tokens, layers, attention_layers, kv_heads=4, head_dim=128, scalar_bytes=2,
                   recurrent_state_bytes=65536):
    kv = tokens * attention_layers * 2 * kv_heads * head_dim * scalar_bytes
    return kv + (layers - attention_layers) * recurrent_state_bytes


for tokens in (128, 4096, 32768):
    print(tokens, {count: estimate_state(tokens, 32, count) for count in (32, 8)})
assert estimate_state(0, 32, 8) == 24 * 65536
assert estimate_state(4096, 32, 8) < estimate_state(4096, 32, 32)
```

## Try it yourself

Compare both formulas at short and long contexts. Add weight memory separately and explain what a real load test must hold constant.

[Download the workbook](../../assets/notebooks/sparse-model-architectures.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Compare quality on exact retrieval and long document tasks alongside throughput and memory. The simulation estimates state bytes under stated assumptions.

## Continue

[← Expert parallelism and communication](03-expert-parallelism-and-communication.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions .study-directions--footer }
