# KA 03 — Transformers

## Purpose

Understand attention, blocks, training, and inference.

## What you should be able to do

- Explain core mechanisms without vendor-specific jargon
- Build or inspect a minimal implementation for each mechanism in the lesson path
- Evaluate quality, latency, cost, safety, and operational trade-offs with evidence
- Defend architecture and product choices using measured results

## Lesson sequence (6 lessons)

1. **Sequence Models Before Transformers** — read [chapter](../books/04-transformers-and-foundation-models/01-sequence-models-before-transformers.md), run [lab](../labs/0401-sequence-models-before-transformers.md), lesson page [L-03-transformers-01](../lessons/03-transformers-01.md)
2. **Attention** — read [chapter](../books/04-transformers-and-foundation-models/02-attention.md), run [lab](../labs/0402-attention.md), lesson page [L-03-transformers-02](../lessons/03-transformers-02.md)
3. **The Transformer Block** — read [chapter](../books/04-transformers-and-foundation-models/03-the-transformer-block.md), run [lab](../labs/0403-the-transformer-block.md), lesson page [L-03-transformers-03](../lessons/03-transformers-03.md)
4. **Training Foundation Models** — read [chapter](../books/04-transformers-and-foundation-models/04-training-foundation-models.md), run [lab](../labs/0404-training-foundation-models.md), lesson page [L-03-transformers-04](../lessons/03-transformers-04.md)
5. **Inference and Sampling** — read [chapter](../books/04-transformers-and-foundation-models/05-inference-and-sampling.md), run [lab](../labs/0405-inference-and-sampling.md), lesson page [L-03-transformers-05](../lessons/03-transformers-05.md)
6. **Model Families and Selection** — read [chapter](../books/04-transformers-and-foundation-models/06-model-families-and-selection.md), run [lab](../labs/0406-model-families-and-selection.md), lesson page [L-03-transformers-06](../lessons/03-transformers-06.md)

## Core mechanisms

| Mechanism | Engineering role | Common failure |
|---|---|---|
| Sequence Models Before Transformers | Architectures evolve in response to information-flow and optimization bottlenecks. | Apply without baseline or slice eval |
| Attention | Attention is content-dependent routing of information. | Apply without baseline or slice eval |
| The Transformer Block | Depth repeatedly mixes information and transforms representations. | Apply without baseline or slice eval |
| Training Foundation Models | Pretraining compresses statistical regularities into parameters; it does not create a fact | Apply without baseline or slice eval |

## Core topics

- [multi-head attention](../concepts/cards/multi-head-attention.md)
- [KV cache](../concepts/cards/kv-cache.md)
- [scaling laws](../concepts/cards/scaling-laws.md)

## Guided resources

- Primary book: [Transformers and Foundation Models](../books/04-transformers-and-foundation-models/index.md)
- Concept cards: [index](../concepts/cards/index.md)
- Build guides: [index](../guides/index.md)
- Cloud capabilities: [index](../cloud/capabilities/index.md)

## Architecture studio

Apply reference architectures in [architectures/](../architectures/index.md). Threat-model authorization, failure modes, cost, and rollback.

## Practice project

Implement attention and compare decoder configurations.

## Mastery checkpoint

You can teach the lesson path to a peer using one diagram, one baseline comparison, and one failure story from your own implementation.
