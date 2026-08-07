# Book 5 — Prompt and Context Engineering

## Purpose

Design the information, instructions, state, and output boundaries that make model behavior useful and testable.

## Chapter learning path

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } __Instructions That Work__

    Write clear tasks, roles, constraints, examples, delimiters, and success criteria while avoiding unnecessary…

    [Open chapter →](01-instructions-that-work.md)

-   :material-numeric-2-circle:{ .lg .middle } __Structured Generation__

    Use schemas, constrained decoding, validation, repair, retries, and typed application boundaries.

    [Open chapter →](02-structured-generation.md)

-   :material-numeric-3-circle:{ .lg .middle } __Context Construction__

    Assemble instructions, user input, state, evidence, tools, and examples under priority and token constraints.

    [Open chapter →](03-context-construction.md)

-   :material-numeric-4-circle:{ .lg .middle } __Conversation and Memory__

    Separate transcript, session state, summaries, semantic memory, episodic memory, user preferences, and source…

    [Open chapter →](04-conversation-and-memory.md)

-   :material-numeric-5-circle:{ .lg .middle } __Context Failure and Security__

    Recognize instruction conflict, prompt injection, context poisoning, stale memory, overflow, lost provenance,…

    [Open chapter →](05-context-failure-and-security.md)

-   :material-numeric-6-circle:{ .lg .middle } __Prompt and Context Operations__

    Version prompts, trace context, cache safely, run regressions, compare variants, and monitor cost and quality.

    [Open chapter →](06-prompt-and-context-operations.md)

</div>

## Entry prerequisites

- Book 4
- Model inference
- Tokens and context windows

## Book project

Build a context engine with structured output, memory policies, token budgets, and regression tests.

The project should include a short specification, runnable artifact or architecture, evaluation evidence, failure analysis, and at least one ADR. Prefer a small well-measured system over a large demo with unclear behavior.

## Suggested three-week schedule

- **Week 1:** Chapters 1–2, concept notes, and quick checks.
- **Week 2:** Chapters 3–4 and the runnable sample; begin the book project.
- **Week 3:** Chapters 5–6, failure analysis, project evaluation, and written reflection.

## Assessment

| Evidence | Weight |
|---|---:|
| Chapter knowledge checks | 20% |
| Runnable exercises and failure cases | 30% |
| Book project | 35% |
| Architecture defense and reflection | 15% |

## Anchor readings

- Provider documentation for structured output and tool calling
- Current prompt-injection guidance from authoritative security sources

## Completion standard

You can explain the key mechanisms, complete the practice in every chapter, pass your own mastery review, and defend the project design against simpler alternatives.
