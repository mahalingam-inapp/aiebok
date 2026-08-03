# Secrets Scopes

## Context

Scope API keys per tool and environment.

## Solution

Separate keys; rotate; deny cross-env.

## Consequences

Limits blast radius. Key sprawl.

## Do not use when

Single shared key internal only.
