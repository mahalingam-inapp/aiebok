# Agent Systems

Technical course 08 · 3 sections · 6 lectures · 10–12 hours of lecture and practice time, plus the project

Design agentic systems as bounded stateful architectures rather than treating autonomy as a model feature.

[Start the first lecture](01-agent-or-workflow.md){ .md-button .md-button--primary }
[Download the course notebook](../../assets/notebooks/08-agent-systems.ipynb){ .md-button download }

## Entry prerequisites

- Courses 05–07 or equivalent experience
- State machines
- Tools and evaluation

## Course outline

### Workflows and agent loops

- [01 · Agent or Workflow?](01-agent-or-workflow.md)
- [02 · The Agent Loop](02-the-agent-loop.md)

**Checkpoint**

Identify where a fixed workflow is sufficient. Write an invariant for a bounded loop.

### Recovery and patterns

- [03 · Agent Memory and Recovery](03-agent-memory-and-recovery.md)
- [04 · Agent Patterns](04-agent-patterns.md)

**Checkpoint**

Record what must survive a restart so an approved action is handled once.

### Coordination and operations

- [05 · Multi-Agent Systems](05-multi-agent-systems.md)
- [06 · Operating Long-Running Agents](06-operating-long-running-agents.md)

**Checkpoint**

Choose a stopping rule and specify what evidence an operator receives on failure.

## Notebook workshop

Trace the example from planning to its approval pause, then resume after approval and verify that it reaches completion.

The notebook includes each lecture's short demonstration and a checked exercise. For setup and execution, see [Course notebooks](../../labs/notebooks/index.md).

<span id="book-project"></span>

## Course project

Build a durable multi-step agent with checkpoints, approval gates, evaluation, and observable termination.

Submit a short specification, an implementation or architecture, evidence from a baseline comparison, and one architecture decision record. Include one example that fails and explain how you would handle it.

## Suggested three-week schedule

- **Week 1:** Complete the first section and its checkpoint.
- **Week 2:** Complete the second section and start the project.
- **Week 3:** Complete the final section and the notebook workshop. Evaluate and review the project.

## Assessment

| Evidence | Weight |
|---|---:|
| Lecture knowledge checks | 20% |
| Runnable exercises and failure cases | 30% |
| Course project | 35% |
| Architecture defense and reflection | 15% |

## Anchor readings

- Primary papers for the selected agent pattern
- Distributed-systems references for durable execution and idempotency

## Completion standard

Complete the lecture checks and section checkpoints, run the notebook workshop, and defend your project against a simpler alternative using the evidence you collected.

[All courses](../../courses/index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
