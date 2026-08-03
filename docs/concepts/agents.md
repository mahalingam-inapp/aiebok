# Agents

**Purpose:** Describe systems that select actions in a loop toward a goal, with explicit state, tools, budgets, and termination—distinct from single-shot prompts or fixed workflows.

**Prerequisites:** Tool calling, state machines, evaluation, basic planning concepts.

## Why agents exist

Many tasks require multiple dependent steps, external data, and recovery from failure. An agent wraps a model in a bounded loop: observe state, plan or choose an action, execute through typed tools, update state, and stop when done or budget exhausted.

## Core intuition

Agency is an **architecture property**, not a model brand feature. Without explicit state, stopping rules, and authorization at tool boundaries, an “agent” devolves into an unreliable retry loop with invisible side effects.

## Mechanics

1. Maintain durable state: goal, step count, observations, pending approvals.
2. Choose the next action from a constrained set of tools or sub-steps.
3. Execute through deterministic, authorized interfaces with timeouts and idempotency.
4. Reflect on observations; replan when assumptions fail.
5. Terminate on success, unrecoverable error, or budget limit.

## Engineering checklist

- Model the same task as a workflow and as an agent; keep the simpler design if it meets requirements.
- Require human approval before irreversible or high-cost actions.
- Persist checkpoints so long-running runs can resume without duplicating side effects.
- Evaluate task success, tool correctness, recovery, and cost—not fluent narration alone.

## Code practice

Run `python labs/04-agent-loop/main.py` and extend it with failure injection and checkpoint resume.

## Trade-offs

Agents handle uncertainty and multi-step work but add latency, coordination complexity, and failure surfaces. Workflows remain preferable when the path is known and stable.

## Common misconceptions

- More autonomy is not always better; use the least autonomy that fits task uncertainty.
- Multi-agent setups often increase organizational complexity faster than capability.
- Memory without provenance and expiry recreates stale or unsafe context.

## Evolution lens

Yesterday: scripted bots and rigid if-then automation. Today: bounded agent loops with tools, checkpoints, and observability. Tomorrow: more durable orchestration with stronger verification. The durable principle is goal-directed action under explicit constraints.
