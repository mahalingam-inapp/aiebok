# KA 01 — Machine Learning

## Purpose

Train, validate, and operate predictive systems.

## What you should be able to do

- Explain core mechanisms without vendor-specific jargon
- Build or inspect a minimal implementation for each mechanism in the lesson path
- Evaluate quality, latency, cost, safety, and operational trade-offs with evidence
- Defend architecture and product choices using measured results

## Lesson sequence (6 lessons)

1. **Problems, Data, and Baselines** — read [chapter](../books/02-machine-learning-systems/01-problems-data-and-baselines.md), run [lab](../labs/0201-problems-data-and-baselines.md), lesson page [L-01-machine-learning-01](../lessons/01-machine-learning-01.md)
2. **Supervised Learning** — read [chapter](../books/02-machine-learning-systems/02-supervised-learning.md), run [lab](../labs/0202-supervised-learning.md), lesson page [L-01-machine-learning-02](../lessons/01-machine-learning-02.md)
3. **Unsupervised and Representation Learning** — read [chapter](../books/02-machine-learning-systems/03-unsupervised-and-representation-learning.md), run [lab](../labs/0203-unsupervised-and-representation-learning.md), lesson page [L-01-machine-learning-03](../lessons/01-machine-learning-03.md)
4. **Neural Networks** — read [chapter](../books/02-machine-learning-systems/04-neural-networks.md), run [lab](../labs/0204-neural-networks.md), lesson page [L-01-machine-learning-04](../lessons/01-machine-learning-04.md)
5. **Evaluation and Error Analysis** — read [chapter](../books/02-machine-learning-systems/05-evaluation-and-error-analysis.md), run [lab](../labs/0205-evaluation-and-error-analysis.md), lesson page [L-01-machine-learning-05](../lessons/01-machine-learning-05.md)
6. **The ML Lifecycle** — read [chapter](../books/02-machine-learning-systems/06-the-ml-lifecycle.md), run [lab](../labs/0206-the-ml-lifecycle.md), lesson page [L-01-machine-learning-06](../lessons/01-machine-learning-06.md)

## Core mechanisms

| Mechanism | Engineering role | Common failure |
|---|---|---|
| Problems, Data, and Baselines | Most model failures begin as problem or data-definition failures. | Apply without baseline or slice eval |
| Supervised Learning | The best model is the simplest one that meets the real decision requirement. | Apply without baseline or slice eval |
| Unsupervised and Representation Learning | Structure found by an algorithm is a hypothesis to validate, not a fact. | Apply without baseline or slice eval |
| Neural Networks | Neural networks learn compositions of transformations; training adjusts those transformati | Apply without baseline or slice eval |

## Core topics

- [baselines](../concepts/cards/baselines.md)
- [cross-validation](../concepts/cards/cross-validation.md)
- [drift](../concepts/cards/drift.md)

## Guided resources

- Primary book: [Machine Learning Systems](../books/02-machine-learning-systems/index.md)
- Concept cards: [index](../concepts/cards/index.md)
- Build guides: [index](../guides/index.md)
- Cloud capabilities: [index](../cloud/capabilities/index.md)

## Architecture studio

Apply reference architectures in [architectures/](../architectures/index.md). Threat-model authorization, failure modes, cost, and rollback.

## Practice project

Ship a prediction service with error analysis and monitoring.

## Mastery checkpoint

You can teach the lesson path to a peer using one diagram, one baseline comparison, and one failure story from your own implementation.
