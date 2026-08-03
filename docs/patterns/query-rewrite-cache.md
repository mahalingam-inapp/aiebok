# Query Rewrite Cache

## Context

Cache rewritten queries for repeat intents.

## Solution

Store rewrite+results for session.

## Consequences

Latency. Wrong rewrite stuck.

## Do not use when

Highly diverse queries.
