# Context Budget Packing

## Context

Allocate fixed token budgets per context section by priority.

## Solution

Rank sections; truncate or summarize low-priority blocks.

## Consequences

Predictable cost and fewer overflow failures. Lost nuance from truncation.

## Do not use when

Short contexts where everything fits.
