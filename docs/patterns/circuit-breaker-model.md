# Circuit Breaker

## Context

Stop calling failing model or tool temporarily.

## Solution

Open circuit on error rate threshold.

## Consequences

Protects downstream systems. Delayed recovery detection.

## Do not use when

Batch offline jobs.
