# Token Budget Forecast

## Context

Estimate tokens before calling model.

## Solution

Pre-count sections; drop lowest priority.

## Consequences

Fewer overflows. Estimation error.

## Do not use when

Tiny prompts.
