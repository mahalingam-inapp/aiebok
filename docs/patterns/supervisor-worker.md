# Supervisor–Worker

## Context

Delegate subtasks from a coordinator to specialized workers.

## Solution

Supervisor plans; workers execute bounded tools; results aggregate.

## Consequences

Parallelism and separation of concerns. Coordination overhead and failure modes.

## Do not use when

Single-agent loop with parallel tool calls is enough.
