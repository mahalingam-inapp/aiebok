# Structured Output

**Purpose:** Convert probabilistic model text into validated, typed data that software can trust.

**Prerequisites:** JSON Schema or equivalent, API design, prompt engineering, error handling.

## Why structured output exists

Applications need invoices, configs, tool arguments, and database rows—not prose paragraphs. Free-form generation must cross a validation boundary before triggering business logic, payments, or infrastructure changes.

## Core intuition

Structured output is a **contract** between the model and the system. Schemas define allowed shapes; validators reject or repair non-conforming payloads; retries and fallbacks handle residual uncertainty.

## Mechanics

1. Define a schema for required fields, types, enums, and constraints.
2. Prompt or configure the model to emit schema-conformant structures.
3. Parse and validate; reject ambiguous or partial results when safety requires it.
4. Repair with constrained follow-up calls only when the domain allows it.
5. Log raw and validated outputs for regression testing.

## Engineering checklist

- Test adversarial inputs: extra fields, wrong types, missing required keys, unicode edge cases.
- Never execute tools or SQL from unvalidated model strings.
- Version schemas alongside prompts and evaluate parse/validation failure rates.
- Prefer deterministic post-processing for fields with strict formats (dates, IDs).

## Trade-offs

Constrained decoding and schema enforcement improve reliability but can reduce flexibility or increase latency. Overly rigid schemas fail on legitimately ambiguous extractions.

## Common misconceptions

- “JSON mode” without validation is not structured output.
- Repair loops can amplify hallucinations if not bounded.
- Schema success rate on demos ≠ production reliability under drift.

## Evolution lens

Yesterday: regex extraction from free text. Today: schema-guided generation with validation and repair. Tomorrow: tighter integration with type systems and compilers. The durable principle is validated data at the boundary.
