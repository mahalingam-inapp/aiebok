# Prompt Cache Key

## Context

Reuse prefix KV cache across similar requests.

## Solution

Hash stable system prefix; cache by tenant.

## Consequences

Lower latency/cost. Stale policy if prefix changes silently.

## Do not use when

Unique prompts every request.
