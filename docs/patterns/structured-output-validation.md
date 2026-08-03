# Structured Output Validation

## Context

Parse and validate model JSON against schemas before use.

## Solution

Schema validate; repair or reject; never trust raw strings.

## Consequences

Safer integration with business logic. Parse failures on ambiguous extractions.

## Do not use when

Fully free-form chat UX.
