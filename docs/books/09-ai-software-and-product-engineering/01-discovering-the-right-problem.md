# 9.1 — Discovering the Right Problem

*Book 9: AI Software and Product Engineering · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- Books 5–8
- Software testing
- Product discovery basics

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Identify user jobs, workflow constraints, baseline performance, capability fit, failure cost, and measurable value before building.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain the problem that motivated discovering the right problem.
- Connect the chapter's concepts into one causal mental model.
- Implement or design the bounded practice exercise.
- Evaluate quality, latency, cost, safety, and operational consequences.
- Distinguish enduring principles from current products and APIs.

!!! note "Enduring principle"
    Optimize the human outcome, not the amount of AI in the product.

## Mental model

```mermaid
flowchart LR
  N0["User problem"] --> N1["Specification"]
  N1["Specification"] --> N2["Implementation"]
  N2["Implementation"] --> N3["Evaluation"]
  N3["Evaluation"] --> N4["Release evidence"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **discovering the right problem** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read across the table before studying any row in isolation.

| Concept | Role in this chapter | Evidence of understanding |
|---|---|---|
| **User Research** | establishes the first representation or decision boundary | Define inputs and outputs; construct a minimal example; identify one invalid assumption. |
| **Jobs-To-Be-Done** | adds the main transformation or comparison | Define inputs and outputs; construct a minimal example; identify one invalid assumption. |
| **Baseline Workflow** | connects the mechanism to the surrounding system | Define inputs and outputs; construct a minimal example; identify one invalid assumption. |
| **Feasibility** | controls quality, efficiency, or behavior | Define inputs and outputs; construct a minimal example; identify one invalid assumption. |
| **Success Metrics** | exposes an important operating constraint or failure mode | Define inputs and outputs; construct a minimal example; identify one invalid assumption. |
## Worked example

**Book scenario:** A product team must convert a vague AI feature request into testable release evidence.

**Chapter focus:** Identify user jobs, workflow constraints, baseline performance, capability fit, failure cost, and measurable value before building.

Apply this chapter in four moves:

1. Write the observable task and the simplest baseline before selecting a model or framework.
2. Locate where user research and jobs-to-be-done enter the book-level visual above.
3. Create one normal case, one boundary case, and one adversarial or failure case.
4. Compare the result using a task-quality measure plus latency, cost, and risk notes.

The design question is: **What evidence would show that discovering the right problem addresses this chapter's problem better than the baseline?** Answer with measured observations rather than intuition alone.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/09-spec-driven-development.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/09-spec-driven-development.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    Both executable acceptance examples pass; changing the abstention behavior should fail the second case.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **user research** and **jobs-to-be-done**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Write a problem brief with a non-AI alternative.

Work in three passes:

1. Establish the simplest deterministic or naive baseline.
2. Add the chapter mechanism while keeping inputs and evaluation fixed.
3. Compare outcomes, inspect failures, and document when the extra complexity is justified.

Capture the code or diagram, assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Architecture lens

For a production design, make the following explicit:

| Concern | Question to answer |
|---|---|
| Boundary | Which component owns this capability? |
| Contract | What are its inputs, outputs, errors, and version? |
| Evidence | How will quality be measured before and after release? |
| Security | What data, identity, permission, or misuse risk crosses the boundary? |
| Operations | What is traced, monitored, cached, retried, and rolled back? |
| Economics | Which resource drives latency and cost, and what is the budget? |

## Failure clinic

Do not debug only the final output. Reproduce the failure, preserve the full input and versioned configuration, inspect intermediate state, compare a baseline, and classify the cause. Typical categories are missing or biased data, representation loss, incorrect assumptions, weak retrieval or planning, ambiguous contracts, invalid output, excessive autonomy, authorization gaps, and evaluation mismatch.

## Evolution lens

- **Yesterday:** identify the earlier manual, symbolic, statistical, or single-model approach.
- **Today:** describe the current engineering pattern without tying the principle to one vendor.
- **Tomorrow:** look for better representations, automatic optimization, stronger verification, lower cost, and clearer control.
- **What survives:** Optimize the human outcome, not the amount of AI in the product.

## Knowledge check

1. What problem would remain if user research were removed from the system?
2. Which observation would distinguish a failure in jobs-to-be-done from a failure in success metrics?
3. What simpler alternative should be the baseline?

??? question "Answer guidance"
    A strong answer names an observable failure, traces it to a specific boundary in the chapter visual, and proposes a test that could disconfirm the explanation. The baseline should remove the chapter mechanism while holding the task and evaluation cases fixed.

## Mastery questions

1. Explain user research without jargon and give a counterexample.
2. Compare jobs-to-be-done with success metrics using quality, cost, latency, and risk.
3. Design a minimal experiment that tests the chapter's central claim.
4. Identify which component should own validation, authorization, and observability.
5. State what would remain true if today's leading libraries and vendors disappeared.

## Self-assessment rubric

| Level | Evidence |
|---|---|
| Not yet | Can repeat terms but cannot trace the visual or predict the sample. |
| Developing | Can explain the mechanism and complete the normal case with help. |
| Proficient | Can implement the exercise, diagnose a failure, and compare a baseline. |
| Transfer | Can defend an architecture choice in a new domain with evaluation evidence. |

## Evidence and further study

- Repository contribution and test documentation
- Architecture Decision Record guidance and product experiment literature

Use primary sources for technical claims and official documentation for current product behavior. Record the version or access date for evolving material.

## Continue

Return to the [book index](index.md) or use site search to follow the chapter's concepts into the knowledge-area and reference pages.
