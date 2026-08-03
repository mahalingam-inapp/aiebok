# KA 09 — Agents

## Purpose

Design bounded autonomous loops.

## What you should be able to do

- Explain core mechanisms without vendor-specific jargon
- Build or inspect a minimal implementation for each mechanism in the lesson path
- Evaluate quality, latency, cost, safety, and operational trade-offs with evidence
- Defend architecture and product choices using measured results

## Lesson sequence (6 lessons)

1. **Agent or Workflow?** — read [chapter](../books/08-agent-systems/01-agent-or-workflow.md), run [lab](../labs/0801-agent-or-workflow.md), lesson page [L-09-agents-01](../lessons/09-agents-01.md)
2. **The Agent Loop** — read [chapter](../books/08-agent-systems/02-the-agent-loop.md), run [lab](../labs/0802-the-agent-loop.md), lesson page [L-09-agents-02](../lessons/09-agents-02.md)
3. **Agent Memory and Recovery** — read [chapter](../books/08-agent-systems/03-agent-memory-and-recovery.md), run [lab](../labs/0803-agent-memory-and-recovery.md), lesson page [L-09-agents-03](../lessons/09-agents-03.md)
4. **Agent Patterns** — read [chapter](../books/08-agent-systems/04-agent-patterns.md), run [lab](../labs/0804-agent-patterns.md), lesson page [L-09-agents-04](../lessons/09-agents-04.md)
5. **Multi-Agent Systems** — read [chapter](../books/08-agent-systems/05-multi-agent-systems.md), run [lab](../labs/0805-multi-agent-systems.md), lesson page [L-09-agents-05](../lessons/09-agents-05.md)
6. **Operating Long-Running Agents** — read [chapter](../books/08-agent-systems/06-operating-long-running-agents.md), run [lab](../labs/0806-operating-long-running-agents.md), lesson page [L-09-agents-06](../lessons/09-agents-06.md)

## Core mechanisms

| Mechanism | Engineering role | Common failure |
|---|---|---|
| Agent or Workflow? | Use the least autonomy that handles the uncertainty in the task. | Apply without baseline or slice eval |
| The Agent Loop | An agent loop without explicit state and stopping rules is an unreliable retry loop. | Apply without baseline or slice eval |
| Agent Memory and Recovery | Continuity requires durable state and recoverable effects, not merely longer context. | Apply without baseline or slice eval |
| Agent Patterns | Patterns trade flexibility for additional state, calls, latency, and failure surfaces. | Apply without baseline or slice eval |

## Core topics

- [plan-act-observe](../concepts/cards/plan-act-observe.md)
- [checkpoints](../concepts/cards/checkpoints.md)
- [approval gates](../concepts/cards/approval-gates.md)

## Guided resources

- Primary book: [Agent Systems](../books/08-agent-systems/index.md)
- Concept cards: [index](../concepts/cards/index.md)
- Build guides: [index](../guides/index.md)
- Cloud capabilities: [index](../cloud/capabilities/index.md)

## Architecture studio

Apply reference architectures in [architectures/](../architectures/index.md). Threat-model authorization, failure modes, cost, and rollback.

## Practice project

Ship a checkpointed agent with eval traces.

## Mastery checkpoint

You can teach the lesson path to a peer using one diagram, one baseline comparison, and one failure story from your own implementation.
