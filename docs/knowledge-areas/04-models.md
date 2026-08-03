# KA 04 — Models

## Purpose

Select and benchmark model families for tasks.

## What you should be able to do

- Explain core mechanisms without vendor-specific jargon
- Build or inspect a minimal implementation for each mechanism in the lesson path
- Evaluate quality, latency, cost, safety, and operational trade-offs with evidence
- Defend architecture and product choices using measured results

## Lesson sequence (6 lessons)

1. **Training Foundation Models** — read [chapter](../books/04-transformers-and-foundation-models/04-training-foundation-models.md), run [lab](../labs/0404-training-foundation-models.md), lesson page [L-04-models-01](../lessons/04-models-01.md)
2. **Inference and Sampling** — read [chapter](../books/04-transformers-and-foundation-models/05-inference-and-sampling.md), run [lab](../labs/0405-inference-and-sampling.md), lesson page [L-04-models-02](../lessons/04-models-02.md)
3. **Model Families and Selection** — read [chapter](../books/04-transformers-and-foundation-models/06-model-families-and-selection.md), run [lab](../labs/0406-model-families-and-selection.md), lesson page [L-04-models-03](../lessons/04-models-03.md)
4. **Sequence Models Before Transformers** — read [chapter](../books/04-transformers-and-foundation-models/01-sequence-models-before-transformers.md), run [lab](../labs/0401-sequence-models-before-transformers.md), lesson page [L-04-models-04](../lessons/04-models-04.md)
5. **Attention** — read [chapter](../books/04-transformers-and-foundation-models/02-attention.md), run [lab](../labs/0402-attention.md), lesson page [L-04-models-05](../lessons/04-models-05.md)
6. **The Transformer Block** — read [chapter](../books/04-transformers-and-foundation-models/03-the-transformer-block.md), run [lab](../labs/0403-the-transformer-block.md), lesson page [L-04-models-06](../lessons/04-models-06.md)

## Core mechanisms

| Mechanism | Engineering role | Common failure |
|---|---|---|
| Training Foundation Models | Pretraining compresses statistical regularities into parameters; it does not create a fact | Apply without baseline or slice eval |
| Inference and Sampling | Generation is repeated conditional prediction shaped by decoding and system context. | Apply without baseline or slice eval |
| Model Families and Selection | Select models as replaceable components against requirements, not by reputation. | Apply without baseline or slice eval |
| Sequence Models Before Transformers | Architectures evolve in response to information-flow and optimization bottlenecks. | Apply without baseline or slice eval |

## Core topics

- [model routing](../concepts/cards/model-routing.md)
- [instruction tuning](../concepts/cards/instruction-tuning.md)
- [open weights](../concepts/cards/open-weights.md)

## Guided resources

- Primary book: [Transformers and Foundation Models](../books/04-transformers-and-foundation-models/index.md)
- Concept cards: [index](../concepts/cards/index.md)
- Build guides: [index](../guides/index.md)
- Cloud capabilities: [index](../cloud/capabilities/index.md)

## Architecture studio

Apply reference architectures in [architectures/](../architectures/index.md). Threat-model authorization, failure modes, cost, and rollback.

## Practice project

Write a vendor-neutral model selection report.

## Mastery checkpoint

You can teach the lesson path to a peer using one diagram, one baseline comparison, and one failure story from your own implementation.
