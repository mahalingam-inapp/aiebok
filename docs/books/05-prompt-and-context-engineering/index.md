# Book 5 — Prompt and Context Engineering

## Purpose

Design the information, instructions, state, and output boundaries that make model behavior useful and testable.

## Entry prerequisites

- Book 4
- Model inference
- Tokens and context windows

## Chapters

1. [Instructions That Work](01-instructions-that-work.md)
2. [Structured Generation](02-structured-generation.md)
3. [Context Construction](03-context-construction.md)
4. [Conversation and Memory](04-conversation-and-memory.md)
5. [Context Failure and Security](05-context-failure-and-security.md)
6. [Prompt and Context Operations](06-prompt-and-context-operations.md)

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
