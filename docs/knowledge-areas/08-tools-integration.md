# KA 08 — Tools & Integration

## Purpose

Connect models to software safely.

## What you should be able to do

- Explain core mechanisms without vendor-specific jargon
- Build or inspect a minimal implementation for each mechanism in the lesson path
- Evaluate quality, latency, cost, safety, and operational trade-offs with evidence
- Defend architecture and product choices using measured results

## Lesson sequence (6 lessons)

1. **Tools as Capability Boundaries** — read [chapter](../books/07-reasoning-and-tool-use/04-tools-as-capability-boundaries.md), run [lab](../labs/0704-tools-as-capability-boundaries.md), lesson page [L-08-tools-integration-01](../lessons/08-tools-integration-01.md)
2. **MCP and Integration Protocols** — read [chapter](../books/07-reasoning-and-tool-use/05-mcp-and-integration-protocols.md), run [lab](../labs/0705-mcp-and-integration-protocols.md), lesson page [L-08-tools-integration-02](../lessons/08-tools-integration-02.md)
3. **Reasoning-System Economics** — read [chapter](../books/07-reasoning-and-tool-use/06-reasoning-system-economics.md), run [lab](../labs/0706-reasoning-system-economics.md), lesson page [L-08-tools-integration-03](../lessons/08-tools-integration-03.md)
4. **Reasoning as Search** — read [chapter](../books/07-reasoning-and-tool-use/01-reasoning-as-search.md), run [lab](../labs/0701-reasoning-as-search.md), lesson page [L-08-tools-integration-04](../lessons/08-tools-integration-04.md)
5. **Planning** — read [chapter](../books/07-reasoning-and-tool-use/02-planning.md), run [lab](../labs/0702-planning.md), lesson page [L-08-tools-integration-05](../lessons/08-tools-integration-05.md)
6. **Verification and Critique** — read [chapter](../books/07-reasoning-and-tool-use/03-verification-and-critique.md), run [lab](../labs/0703-verification-and-critique.md), lesson page [L-08-tools-integration-06](../lessons/08-tools-integration-06.md)

## Core mechanisms

| Mechanism | Engineering role | Common failure |
|---|---|---|
| Tools as Capability Boundaries | Probabilistic intent must cross a deterministic, authorized boundary before effects occur. | Apply without baseline or slice eval |
| MCP and Integration Protocols | Protocols standardize capability exchange; they do not remove authorization or trust decis | Apply without baseline or slice eval |
| Reasoning-System Economics | Spend additional computation only where expected outcome improvement justifies it. | Apply without baseline or slice eval |
| Reasoning as Search | Additional inference helps when the task benefits from exploring and rejecting alternative | Apply without baseline or slice eval |

## Core topics

- [function calling](../concepts/cards/function-calling.md)
- [tool schemas](../concepts/cards/tool-schemas.md)
- [MCP](../concepts/cards/mcp.md)

## Guided resources

- Primary book: [Reasoning and Tool Use](../books/07-reasoning-and-tool-use/index.md)
- Concept cards: [index](../concepts/cards/index.md)
- Build guides: [index](../guides/index.md)
- Cloud capabilities: [index](../cloud/capabilities/index.md)

## Architecture studio

Apply reference architectures in [architectures/](../architectures/index.md). Threat-model authorization, failure modes, cost, and rollback.

## Practice project

Wrap APIs as typed tools with auth and audit.

## Mastery checkpoint

You can teach the lesson path to a peer using one diagram, one baseline comparison, and one failure story from your own implementation.
