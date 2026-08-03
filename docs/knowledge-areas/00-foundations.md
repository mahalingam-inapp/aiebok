# KA 00 — Foundations

## Purpose

Build a vocabulary for intelligence, learning, reasoning, memory, feedback, and optimization before treating language models as magic.

## What you should be able to do

- Decompose a task into perception, representation, memory, learning, planning, action, and feedback
- Implement search and planning on a bounded state space
- Explain why fluent language is not evidence of reliable decision-making
- Connect classical AI ideas to modern ML and agent systems

## Core mechanisms

| Mechanism | Engineering role | Common failure |
|---|---|---|
| Goal-directed behavior | Defines success criteria | Optimizing prose instead of outcomes |
| Search & planning | Explores action sequences | Missing stopping rules and costs |
| Learning | Generalizes from data | Overfitting and distribution shift |
| Feedback | Closes control loops | No channel from production errors to updates |

## Guided path

1. [Book 1 — Foundations of Intelligence](../books/01-foundations-of-intelligence/index.md)
2. Labs: `labs/01-*` through `labs/06-*`
3. Concepts: [goal-directed behavior](../concepts/cards/goal-directed-behavior.md), [A*](../concepts/cards/a.md), [feedback](../concepts/cards/feedback.md)

## Architecture studio

Given a decision problem, separate what should be deterministic, learned, retrieved, or reviewed by a human. Document the boundary in an ADR with eval evidence.

## Practice project

Build and compare a rule-based solver, search-based solver, and learned predictor for one bounded routing or classification problem. Report where each approach wins and fails.
