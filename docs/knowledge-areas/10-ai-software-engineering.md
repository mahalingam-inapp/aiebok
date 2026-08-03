# KA 10 — AI Software Engineering

## Purpose

Apply SDLC rigor to AI features.

## What you should be able to do

- Explain core mechanisms without vendor-specific jargon
- Build or inspect a minimal implementation for each mechanism in the lesson path
- Evaluate quality, latency, cost, safety, and operational trade-offs with evidence
- Defend architecture and product choices using measured results

## Lesson sequence (6 lessons)

1. **Discovering the Right Problem** — read [chapter](../books/09-ai-software-and-product-engineering/01-discovering-the-right-problem.md), run [lab](../labs/0901-discovering-the-right-problem.md), lesson page [L-10-ai-software-engineering-01](../lessons/10-ai-software-engineering-01.md)
2. **Specification-Driven Development** — read [chapter](../books/09-ai-software-and-product-engineering/02-specification-driven-development.md), run [lab](../labs/0902-specification-driven-development.md), lesson page [L-10-ai-software-engineering-02](../lessons/10-ai-software-engineering-02.md)
3. **AI-Native Development Workflow** — read [chapter](../books/09-ai-software-and-product-engineering/03-ai-native-development-workflow.md), run [lab](../labs/0903-ai-native-development-workflow.md), lesson page [L-10-ai-software-engineering-03](../lessons/10-ai-software-engineering-03.md)
4. **Testing AI Systems** — read [chapter](../books/09-ai-software-and-product-engineering/04-testing-ai-systems.md), run [lab](../labs/0904-testing-ai-systems.md), lesson page [L-10-ai-software-engineering-04](../lessons/10-ai-software-engineering-04.md)
5. **Human-Centered AI UX** — read [chapter](../books/09-ai-software-and-product-engineering/05-human-centered-ai-ux.md), run [lab](../labs/0905-human-centered-ai-ux.md), lesson page [L-10-ai-software-engineering-05](../lessons/10-ai-software-engineering-05.md)
6. **Experiments, Adoption, and Value** — read [chapter](../books/09-ai-software-and-product-engineering/06-experiments-adoption-and-value.md), run [lab](../labs/0906-experiments-adoption-and-value.md), lesson page [L-10-ai-software-engineering-06](../lessons/10-ai-software-engineering-06.md)

## Core mechanisms

| Mechanism | Engineering role | Common failure |
|---|---|---|
| Discovering the Right Problem | Optimize the human outcome, not the amount of AI in the product. | Apply without baseline or slice eval |
| Specification-Driven Development | Specifications align humans and agents around observable outcomes and constraints. | Apply without baseline or slice eval |
| AI-Native Development Workflow | AI accelerates change production, making specification and verification more important. | Apply without baseline or slice eval |
| Testing AI Systems | Test deterministic properties deterministically and probabilistic behavior statistically. | Apply without baseline or slice eval |

## Core topics

- [functional specifications](../concepts/cards/functional-specifications.md)
- [contract tests](../concepts/cards/contract-tests.md)
- [evaluation specs](../concepts/cards/evaluation-specs.md)

## Guided resources

- Primary book: [AI Software and Product Engineering](../books/09-ai-software-and-product-engineering/index.md)
- Concept cards: [index](../concepts/cards/index.md)
- Build guides: [index](../guides/index.md)
- Cloud capabilities: [index](../cloud/capabilities/index.md)

## Architecture studio

Apply reference architectures in [architectures/](../architectures/index.md). Threat-model authorization, failure modes, cost, and rollback.

## Practice project

Deliver spec-to-test AI feature with release evidence.

## Mastery checkpoint

You can teach the lesson path to a peer using one diagram, one baseline comparison, and one failure story from your own implementation.
