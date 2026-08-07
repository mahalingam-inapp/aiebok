# Book 8 — Agent Systems

## Purpose

Design agentic systems as bounded stateful architectures rather than treating autonomy as a model feature.

## Chapter learning path

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } __Agent or Workflow?__

    Define agents by goal-directed action selection in a loop and contrast them with deterministic workflows and…

    [Open chapter →](01-agent-or-workflow.md)

-   :material-numeric-2-circle:{ .lg .middle } __The Agent Loop__

    Connect goal, state, planning, action, observation, reflection, and termination into a bounded state machine.

    [Open chapter →](02-the-agent-loop.md)

-   :material-numeric-3-circle:{ .lg .middle } __Agent Memory and Recovery__

    Manage working state, episodic history, durable checkpoints, resumability, compensation, and idempotent tools.

    [Open chapter →](03-agent-memory-and-recovery.md)

-   :material-numeric-4-circle:{ .lg .middle } __Agent Patterns__

    Apply planner–executor, supervisor–worker, reviewer, evaluator–optimizer, routing, and human-approval pattern…

    [Open chapter →](04-agent-patterns.md)

-   :material-numeric-5-circle:{ .lg .middle } __Multi-Agent Systems__

    Study delegation, role boundaries, communication, shared state, consensus, conflict, security, and why many t…

    [Open chapter →](05-multi-agent-systems.md)

-   :material-numeric-6-circle:{ .lg .middle } __Operating Long-Running Agents__

    Design durable orchestration, queues, scheduling, leases, approvals, monitoring, incident response, and safe…

    [Open chapter →](06-operating-long-running-agents.md)

</div>

## Entry prerequisites

- Books 5–7
- State machines
- Tools and evaluation

## Book project

Build a durable multi-step agent with checkpoints, approval gates, evaluation, and observable termination.

The project should include a short specification, runnable artifact or architecture, evaluation evidence, failure analysis, and at least one ADR. Prefer a small well-measured system over a large demo with unclear behavior.

## Suggested three-week schedule

- **Week 1:** Chapters 1–2, concept notes, and quick checks.
- **Week 2:** Chapters 3–4 and the runnable sample; begin the book project.
- **Week 3:** Chapters 5–6, failure analysis, project evaluation, and written reflection.

## Assessment

| Evidence | Weight |
|---|---:|
| Chapter knowledge checks | 20% |
| Runnable exercises and failure cases | 30% |
| Book project | 35% |
| Architecture defense and reflection | 15% |

## Anchor readings

- Primary papers for the selected agent pattern
- Distributed-systems references for durable execution and idempotency

## Completion standard

You can explain the key mechanisms, complete the practice in every chapter, pass your own mastery review, and defend the project design against simpler alternatives.
