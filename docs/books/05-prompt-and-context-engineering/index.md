# Prompt and Context Engineering

Technical course 05 · 3 sections · 6 lectures · 10–12 hours of lecture and practice time, plus the project

Design the information, instructions, state, and output boundaries that make model behavior useful and testable.

[Start the first lecture](01-instructions-that-work.md){ .md-button .md-button--primary .study-start data-course="05-prompt-and-context-engineering" }
[Download the course notebook](../../assets/notebooks/05-prompt-and-context-engineering.ipynb){ .md-button download }

## Practice case · The shift handoff that changed a date

Noah runs scheduling for a community center. A writing assistant helps staff hand off room changes between shifts. When it turns ‘date pending’ into ‘next Thursday’, volunteers receive an incorrect message. Noah wants brief drafts while giving the next shift enough evidence to verify and approve them.

This fictional case continues through the lectures.

For a documented comparison, read [A chatbot answer that changed a travel decision](../../casebook/bereavement-fares.md).

## Entry prerequisites

- Course 04 or equivalent experience
- Model inference
- Tokens and context windows

## Course outline

### Instructions and output contracts

- [01 · Instructions That Work](01-instructions-that-work.md){ .study-lecture data-lecture="01-instructions-that-work.md" }
- [02 · Structured Generation](02-structured-generation.md){ .study-lecture data-lecture="02-structured-generation.md" }

**Checkpoint**

Write a prompt requirement and one schema check that can be evaluated independently of the model.

### Context and memory

- [03 · Context Construction](03-context-construction.md){ .study-lecture data-lecture="03-context-construction.md" }
- [04 · Conversation and Memory](04-conversation-and-memory.md){ .study-lecture data-lecture="04-conversation-and-memory.md" }

**Checkpoint**

Rebuild the context for a smaller budget. Record which memory or evidence you would summarize first.

### Trust and prompt operations

- [05 · Context Failure and Security](05-context-failure-and-security.md){ .study-lecture data-lecture="05-context-failure-and-security.md" }
- [06 · Prompt and Context Operations](06-prompt-and-context-operations.md){ .study-lecture data-lecture="06-prompt-and-context-operations.md" }

**Checkpoint**

Identify which text originated outside the trusted boundary and propose one regression case.

## Notebook workshop

Give a trusted instruction and a retrieved passage competing budgets. Inspect which survives a tight budget and how source trust is represented.

The notebook includes each lecture's short demonstration and a checked exercise. For setup and execution, see [Course notebooks](../../labs/notebooks/index.md).

<span id="book-project"></span>

## Course project

Build a context engine with structured output, memory policies, token budgets, and regression tests.

Submit a short specification, an implementation or architecture, evidence from a baseline comparison, and one architecture decision record. Include one example that fails and explain how you would handle it.

## Suggested three-week schedule

- **Week 1:** Complete the first section and its checkpoint.
- **Week 2:** Complete the second section and start the project.
- **Week 3:** Complete the final section and the notebook workshop. Evaluate and review the project.

## Assessment

| Evidence | Weight |
|---|---:|
| Lecture knowledge checks | 20% |
| Runnable exercises and failure cases | 30% |
| Course project | 35% |
| Architecture defense and reflection | 15% |

## Anchor readings

- Provider documentation for structured output and tool calling
- Current prompt-injection guidance from authoritative security sources

## Completion standard

Complete the lecture checks and section checkpoints, run the notebook workshop, and defend your project against a simpler alternative using the evidence you collected.

[All courses](../../courses/index.md) · [Learning paths](../../getting-started/learning-paths/index.md)
