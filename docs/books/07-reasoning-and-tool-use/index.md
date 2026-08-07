# Book 7 — Reasoning and Tool Use

## Purpose

Understand when inference-time search, planning, verification, and external tools improve task outcomes.

## Chapter learning path

<div class="grid cards" markdown>

-   :material-numeric-1-circle:{ .lg .middle } __Reasoning as Search__

    Separate recall from deliberate search and study decomposition, candidate generation, backtracking, and stopp…

    [Open chapter →](01-reasoning-as-search.md)

-   :material-numeric-2-circle:{ .lg .middle } __Planning__

    Represent goals, prerequisites, steps, dependencies, state, uncertainty, and replanning without confusing a p…

    [Open chapter →](02-planning.md)

-   :material-numeric-3-circle:{ .lg .middle } __Verification and Critique__

    Use deterministic checks, tests, rubrics, critics, self-consistency, best-of-N, and external evidence.

    [Open chapter →](03-verification-and-critique.md)

-   :material-numeric-4-circle:{ .lg .middle } __Tools as Capability Boundaries__

    Design typed tools, schemas, descriptions, errors, timeouts, idempotency, permissions, and audit records.

    [Open chapter →](04-tools-as-capability-boundaries.md)

-   :material-numeric-5-circle:{ .lg .middle } __MCP and Integration Protocols__

    Understand clients, servers, tools, resources, prompts, discovery, transport, authentication, and protocol se…

    [Open chapter →](05-mcp-and-integration-protocols.md)

-   :material-numeric-6-circle:{ .lg .middle } __Reasoning-System Economics__

    Balance accuracy, latency, token use, parallel candidates, tool calls, caches, failure rates, and task value.

    [Open chapter →](06-reasoning-system-economics.md)

</div>

## Entry prerequisites

- Books 1 and 4–6
- Search and planning
- Typed software interfaces

## Book project

Build a research workflow with a planner, typed tools, evidence store, verifier, and bounded recovery.

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

- Yao et al. — ReAct
- Primary protocol specifications for the tool interfaces studied

## Completion standard

You can explain the key mechanisms, complete the practice in every chapter, pass your own mastery review, and defend the project design against simpler alternatives.
