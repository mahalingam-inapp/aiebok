# KA 09 — Agents

## Content plan

Agent versus workflow; goals; state; plan–act–observe loops; memory; tools; recovery; termination; approval; delegation; planner–executor; supervisor–worker; reviewer; multi-agent communication; long-running execution; computer use; durable orchestration.

## Code practice

Start with the five-state loop in `labs/04-agent-loop`. Add tool errors, bounded retries, checkpointing, human approval, and a reviewer.

## Architecture rule

Prefer explicit workflows where the path is known. Use agentic choice only where uncertainty or open-ended search creates real value.
