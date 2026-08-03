# KA 13 — Model Training

## Purpose

Adapt models with curated data.

## What you should be able to do

- Explain core mechanisms without vendor-specific jargon
- Build or inspect a minimal implementation for each mechanism in the lesson path
- Evaluate quality, latency, cost, safety, and operational trade-offs with evidence
- Defend architecture and product choices using measured results

## Lesson sequence (6 lessons)

1. **Choosing Adaptation** — read [chapter](../books/11-training-serving-and-ai-operations/01-choosing-adaptation.md), run [lab](../labs/1101-choosing-adaptation.md), lesson page [L-13-model-training-01](../lessons/13-model-training-01.md)
2. **Post-Training Methods** — read [chapter](../books/11-training-serving-and-ai-operations/02-post-training-methods.md), run [lab](../labs/1102-post-training-methods.md), lesson page [L-13-model-training-02](../lessons/13-model-training-02.md)
3. **Dataset Engineering** — read [chapter](../books/11-training-serving-and-ai-operations/03-dataset-engineering.md), run [lab](../labs/1103-dataset-engineering.md), lesson page [L-13-model-training-03](../lessons/13-model-training-03.md)
4. **Inference Infrastructure** — read [chapter](../books/11-training-serving-and-ai-operations/04-inference-infrastructure.md), run [lab](../labs/1104-inference-infrastructure.md), lesson page [L-13-model-training-04](../lessons/13-model-training-04.md)
5. **Deployment and Routing** — read [chapter](../books/11-training-serving-and-ai-operations/05-deployment-and-routing.md), run [lab](../labs/1105-deployment-and-routing.md), lesson page [L-13-model-training-05](../lessons/13-model-training-05.md)
6. **LLMOps** — read [chapter](../books/11-training-serving-and-ai-operations/06-llmops.md), run [lab](../labs/1106-llmops.md), lesson page [L-13-model-training-06](../lessons/13-model-training-06.md)

## Core mechanisms

| Mechanism | Engineering role | Common failure |
|---|---|---|
| Choosing Adaptation | Choose the smallest intervention at the correct system layer. | Apply without baseline or slice eval |
| Post-Training Methods | Adaptation trades generality and operational simplicity for targeted behavior. | Apply without baseline or slice eval |
| Dataset Engineering | Data design is model behavior design. | Apply without baseline or slice eval |
| Inference Infrastructure | Inference performance is a queueing and memory problem as much as a model problem. | Apply without baseline or slice eval |

## Core topics

- [LoRA](../concepts/cards/lora.md)
- [SFT](../concepts/cards/sft.md)
- [data curation](../concepts/cards/data-curation.md)

## Guided resources

- Primary book: [Training, Serving, and AI Operations](../books/11-training-serving-and-ai-operations/index.md)
- Concept cards: [index](../concepts/cards/index.md)
- Build guides: [index](../guides/index.md)
- Cloud capabilities: [index](../cloud/capabilities/index.md)

## Architecture studio

Apply reference architectures in [architectures/](../architectures/index.md). Threat-model authorization, failure modes, cost, and rollback.

## Practice project

Fine-tune and evaluate a small model.

## Mastery checkpoint

You can teach the lesson path to a peer using one diagram, one baseline comparison, and one failure story from your own implementation.
