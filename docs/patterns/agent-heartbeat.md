# Agent Heartbeat

## Context

Detect stuck agents via heartbeat.

## Solution

Timeout if no progress events.

## Consequences

Ops visibility. False timeouts.

## Do not use when

Sub-second tasks.
