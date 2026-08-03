# Tool Calling

**Purpose:** Let models request typed, authorized actions through deterministic software boundaries instead of hallucinating facts or effects.

**Prerequisites:** APIs, JSON Schema, authentication, basic agent loops.

## Why tool calling exists

Models alone cannot reliably fetch live data, run calculations, or change systems. Tool calling translates natural-language intent into structured function invocations that services execute under explicit permissions and contracts.

## Core intuition

Tools are **capability boundaries**: the model proposes; typed code validates, authorizes, executes, and returns observations. Protocols like MCP standardize discovery and transport—they do not replace trust decisions.

## Mechanics

1. Declare tools with names, descriptions, JSON schemas, and error models.
2. Model emits a structured call with arguments matching the schema.
3. Runtime validates arguments, checks permissions, enforces timeouts and idempotency.
4. Execute and return observations to the model or orchestrator.
5. Audit every call with caller identity, inputs, outputs, and latency.

## Engineering checklist

- Fuzz argument validation; never trust model-produced IDs or SQL.
- Default to read-only tools; gate write/delete behind approval.
- Make timeouts and partial failures observable in traces.
- Evaluate tool selection accuracy separately from final answer quality.

## Code practice

Run `python examples/07-planner-verifier/main.py` and add a typed read-only search tool with schema validation.

## Trade-offs

Tools ground systems in real data but expand attack surface, latency, and integration work. More tools can confuse selection unless scoped and described clearly.

## Common misconceptions

- MCP or OpenAPI exposure does not imply authorization.
- Idempotency keys matter for retried agent loops.
- Tool descriptions are part of the interface—vague descriptions cause misuse.

## Evolution lens

Yesterday: hard-coded integrations per application. Today: schema-defined tools with agent orchestrators and protocol standards. Tomorrow: finer-grained policy and provenance on every effect. The durable principle is probabilistic intent crossing deterministic, authorized boundaries.
