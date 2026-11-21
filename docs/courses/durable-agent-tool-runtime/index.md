# Durable Agent Runtime and MCP

Project practicum · 2 sections · 4 lectures · 3–4 hours, plus the project

Build a local review workflow with typed tool access, approvals, durable state, and replay-safe execution.

[Start the first lecture](01-discover-and-call-a-local-mcp-tool.md){ .md-button .md-button--primary }

## Entry prerequisites

Python, JSON, and the foundations of tool calling and agent state.

## Course outline

### Connect and constrain

- [01 · Discover and call a local MCP tool](01-discover-and-call-a-local-mcp-tool.md) — Trace the MCP initialization, tool discovery, and tool invocation over stdio.
- [02 · Tool authorization and argument validation](02-tool-authorization-and-argument-validation.md) — Validate caller scope and arguments before dispatching a tool.

### Pause, recover and replay

- [03 · Persistent approval and checkpoint recovery](03-persistent-approval-and-checkpoint-recovery.md) — Persist a proposal and its approval against a payload fingerprint, then reopen the runtime.
- [04 · Idempotent execution and decision traces](04-idempotent-execution-and-decision-traces.md) — Commit a local effect exactly once across retries and distinguish external effects.

## Workbook

[Download the workbook](../../assets/notebooks/durable-agent-tool-runtime.ipynb){ download }. Run the exercises in lecture order using the bundled sample data. Each lecture includes checks and a suggested variation.

## Course project

Build a supervised agenda-review workflow using an MCP-compatible local tool. Show validated calls, approval, a process restart, and no duplicate effect.

**How to check your project**

Capture a tool discovery transcript, a denied tool call, a human approval, and a replay from reopened state. Document which guarantees depend on the local transaction.

## Further study

- [Donner’s Agents course repositories and framework labs](https://github.com/ed-donner/agents)
- [Donner’s UnderCover durable workflow examples](https://github.com/ed-donner/undercover)

[All courses](../index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
