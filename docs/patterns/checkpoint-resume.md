# Checkpoint Resume

## Context

Persist agent state to survive interruptions.

## Solution

Save state after each step; resume idempotently.

## Consequences

Reliable long-running workflows. Storage and consistency complexity.

## Do not use when

Sub-minute synchronous tasks.
