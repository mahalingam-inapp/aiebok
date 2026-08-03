# Model Warm Pool

## Context

Keep minimum replicas warm.

## Solution

HPA with min replicas > 0.

## Consequences

Stable tail latency. Idle cost.

## Do not use when

Sporadic batch jobs.
