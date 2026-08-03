# KA 14 — Infrastructure & Deployment

## Purpose

Serve models efficiently.

## What you should be able to do

- Explain core mechanisms without vendor-specific jargon
- Build or inspect a minimal implementation for each mechanism in the lesson path
- Evaluate quality, latency, cost, safety, and operational trade-offs with evidence
- Defend architecture and product choices using measured results

## Lesson sequence (6 lessons)

1. **Inference Infrastructure** — read [chapter](../books/11-training-serving-and-ai-operations/04-inference-infrastructure.md), run [lab](../labs/1104-inference-infrastructure.md), lesson page [L-14-infrastructure-01](../lessons/14-infrastructure-01.md)
2. **Deployment and Routing** — read [chapter](../books/11-training-serving-and-ai-operations/05-deployment-and-routing.md), run [lab](../labs/1105-deployment-and-routing.md), lesson page [L-14-infrastructure-02](../lessons/14-infrastructure-02.md)
3. **LLMOps** — read [chapter](../books/11-training-serving-and-ai-operations/06-llmops.md), run [lab](../labs/1106-llmops.md), lesson page [L-14-infrastructure-03](../lessons/14-infrastructure-03.md)
4. **Choosing Adaptation** — read [chapter](../books/11-training-serving-and-ai-operations/01-choosing-adaptation.md), run [lab](../labs/1101-choosing-adaptation.md), lesson page [L-14-infrastructure-04](../lessons/14-infrastructure-04.md)
5. **Post-Training Methods** — read [chapter](../books/11-training-serving-and-ai-operations/02-post-training-methods.md), run [lab](../labs/1102-post-training-methods.md), lesson page [L-14-infrastructure-05](../lessons/14-infrastructure-05.md)
6. **Dataset Engineering** — read [chapter](../books/11-training-serving-and-ai-operations/03-dataset-engineering.md), run [lab](../labs/1103-dataset-engineering.md), lesson page [L-14-infrastructure-06](../lessons/14-infrastructure-06.md)

## Core mechanisms

| Mechanism | Engineering role | Common failure |
|---|---|---|
| Inference Infrastructure | Inference performance is a queueing and memory problem as much as a model problem. | Apply without baseline or slice eval |
| Deployment and Routing | Deployment choices allocate control, cost, latency, and operational burden. | Apply without baseline or slice eval |
| LLMOps | Every production change needs evidence, observability, and a reversible release path. | Apply without baseline or slice eval |
| Choosing Adaptation | Choose the smallest intervention at the correct system layer. | Apply without baseline or slice eval |

## Core topics

- [quantization](../concepts/cards/quantization.md)
- [batching](../concepts/cards/batching.md)
- [KV cache](../concepts/cards/kv-cache.md)

## Guided resources

- Primary book: [Training, Serving, and AI Operations](../books/11-training-serving-and-ai-operations/index.md)
- Concept cards: [index](../concepts/cards/index.md)
- Build guides: [index](../guides/index.md)
- Cloud capabilities: [index](../cloud/capabilities/index.md)

## Architecture studio

Apply reference architectures in [architectures/](../architectures/index.md). Threat-model authorization, failure modes, cost, and rollback.

## Practice project

Load-test inference configurations.

## Mastery checkpoint

You can teach the lesson path to a peer using one diagram, one baseline comparison, and one failure story from your own implementation.
