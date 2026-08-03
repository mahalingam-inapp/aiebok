# KA 16 — Enterprise Architecture

## Purpose

Design governed AI platforms.

## What you should be able to do

- Explain core mechanisms without vendor-specific jargon
- Build or inspect a minimal implementation for each mechanism in the lesson path
- Evaluate quality, latency, cost, safety, and operational trade-offs with evidence
- Defend architecture and product choices using measured results

## Lesson sequence (6 lessons)

1. **Enterprise AI Building Blocks** — read [chapter](../books/12-cloud-and-enterprise-ai-architecture/01-enterprise-ai-building-blocks.md), run [lab](../labs/1201-enterprise-ai-building-blocks.md), lesson page [L-16-enterprise-architecture-01](../lessons/16-enterprise-architecture-01.md)
2. **Identity, Data, and Trust Boundaries** — read [chapter](../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md), run [lab](../labs/1202-identity-data-and-trust-boundaries.md), lesson page [L-16-enterprise-architecture-02](../lessons/16-enterprise-architecture-02.md)
3. **AWS Managed AI** — read [chapter](../books/12-cloud-and-enterprise-ai-architecture/03-aws-managed-ai.md), run [lab](../labs/1203-aws-managed-ai.md), lesson page [L-16-enterprise-architecture-03](../lessons/16-enterprise-architecture-03.md)
4. **Azure Managed AI** — read [chapter](../books/12-cloud-and-enterprise-ai-architecture/04-azure-managed-ai.md), run [lab](../labs/1204-azure-managed-ai.md), lesson page [L-16-enterprise-architecture-04](../lessons/16-enterprise-architecture-04.md)
5. **Google Cloud and Portable Patterns** — read [chapter](../books/12-cloud-and-enterprise-ai-architecture/05-google-cloud-and-portable-patterns.md), run [lab](../labs/1205-google-cloud-and-portable-patterns.md), lesson page [L-16-enterprise-architecture-05](../lessons/16-enterprise-architecture-05.md)
6. **Enterprise Operating Model** — read [chapter](../books/12-cloud-and-enterprise-ai-architecture/06-enterprise-operating-model.md), run [lab](../labs/1206-enterprise-operating-model.md), lesson page [L-16-enterprise-architecture-06](../lessons/16-enterprise-architecture-06.md)

## Core mechanisms

| Mechanism | Engineering role | Common failure |
|---|---|---|
| Enterprise AI Building Blocks | Stable capability boundaries make vendor choices replaceable and governance consistent. | Apply without baseline or slice eval |
| Identity, Data, and Trust Boundaries | A model call does not suspend ordinary identity and data-security requirements. | Apply without baseline or slice eval |
| AWS Managed AI | Start with logical capabilities; use managed services where their constraints match the sy | Apply without baseline or slice eval |
| Azure Managed AI | Cloud-native integration can accelerate governance but increases platform coupling. | Apply without baseline or slice eval |

## Core topics

- [identity](../concepts/cards/identity.md)
- [multi-tenancy](../concepts/cards/multi-tenancy.md)
- [AI gateways](../concepts/cards/ai-gateways.md)

## Guided resources

- Primary book: [Cloud and Enterprise AI Architecture](../books/12-cloud-and-enterprise-ai-architecture/index.md)
- Concept cards: [index](../concepts/cards/index.md)
- Build guides: [index](../guides/index.md)
- Cloud capabilities: [index](../cloud/capabilities/index.md)

## Architecture studio

Apply reference architectures in [architectures/](../architectures/index.md). Threat-model authorization, failure modes, cost, and rollback.

## Practice project

Produce reference architecture and ADRs.

## Mastery checkpoint

You can teach the lesson path to a peer using one diagram, one baseline comparison, and one failure story from your own implementation.
