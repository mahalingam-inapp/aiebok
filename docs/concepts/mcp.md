# Mcp

**Purpose:** Model Context Protocol standardizes how clients discover tools, resources, and prompts from servers.

**Prerequisites:** See related concepts and book chapters linked from the [concept card](cards/mcp.md).

## Why this exists

Model Context Protocol standardizes how clients discover tools, resources, and prompts from servers. It reduces bespoke integration code but not trust decisions.

## Core intuition

An MCP server exposes filesystem read tools; the client still enforces path allowlists.

## Mechanics

1. Define the decision or system stage where mcp applies.
2. Implement the smallest version that beats an obvious baseline.
3. Measure on normal, boundary, and adversarial slices—not a single demo.
4. Document version, config, and rollback before production use.

## Engineering checklist

- State the decision this mechanism supports before implementation.
- Compare against a simpler baseline on normal, boundary, and adversarial cases.
- Define metrics, slices, and rollback before production rollout.
- Bound steps, cost, tools, and human approval for side effects.

## Evidence of understanding

Connect a hostile client and verify server rejects out-of-scope resource requests.

## Code practice

Run `python labs/0705-mcp-and-integration-protocols/main.py` from the repository root.

## When to use

Use when tasks require multi-step decisions, tool use, or recovery across variable inputs.

## When not to use

Skip when a deterministic workflow with fixed steps is clearer and safer.

## Common failure modes

- Runaway loops without step or cost limits
- Tool calls with excessive privilege
- Lost state after partial failures

## Common misconceptions

- More autonomy always improves outcomes.
- Tool access equals capability without risk.
- Agents replace the need for specifications and tests.

## Trade-offs

Mcp improves some outcomes but adds complexity, latency, or operational burden. Compare against simpler alternatives on *your* workload before adopting by default.

## Evolution lens

Yesterday: scripted workflows. Today: bounded loops with tools and checkpoints. Tomorrow: supervised multi-agent platforms. The durable principle is goal-directed action under explicit policy limits.
