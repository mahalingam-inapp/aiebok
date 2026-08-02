# 12.6 — Enterprise Operating Model

*Book 12: Cloud and Enterprise AI Architecture · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- Books 5–11
- Cloud and identity fundamentals
- Architecture documentation

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Define platform teams, product teams, centers of enablement, governance, service catalogs, SLOs, chargeback, vendor management, and adoption.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain the problem that motivated enterprise operating model.
- Connect the chapter's concepts into one causal mental model.
- Implement or design the bounded practice exercise.
- Evaluate quality, latency, cost, safety, and operational consequences.
- Distinguish enduring principles from current products and APIs.

!!! note "Enduring principle"
    Architecture succeeds only when ownership, incentives, operations, and delivery practices align.

## Mental model

```mermaid
flowchart LR
  N0["Logical capability"] --> N1["Trust boundary"]
  N1["Trust boundary"] --> N2["Managed service"]
  N2["Managed service"] --> N3["SLO"]
  N3["SLO"] --> N4["Governance"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **enterprise operating model** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read across the table before studying any row in isolation.

| Concept | Role in this chapter | Evidence of understanding |
|---|---|---|
| **Team Topology** | establishes the first representation or decision boundary | Define inputs and outputs; construct a minimal example; identify one invalid assumption. |
| **Service Catalog** | adds the main transformation or comparison | Define inputs and outputs; construct a minimal example; identify one invalid assumption. |
| **Slos** | connects the mechanism to the surrounding system | Define inputs and outputs; construct a minimal example; identify one invalid assumption. |
| **Finops** | controls quality, efficiency, or behavior | Define inputs and outputs; construct a minimal example; identify one invalid assumption. |
| **Vendor Management** | exposes an important operating constraint or failure mode | Define inputs and outputs; construct a minimal example; identify one invalid assumption. |
## Worked example

**Book scenario:** An architect must implement the same governed AI capability on different cloud providers.

**Chapter focus:** Define platform teams, product teams, centers of enablement, governance, service catalogs, SLOs, chargeback, vendor management, and adoption.

Apply this chapter in four moves:

1. Write the observable task and the simplest baseline before selecting a model or framework.
2. Locate where team topology and service catalog enter the book-level visual above.
3. Create one normal case, one boundary case, and one adversarial or failure case.
4. Compare the result using a task-quality measure plus latency, cost, and risk notes.

The design question is: **What evidence would show that enterprise operating model addresses this chapter's problem better than the baseline?** Answer with measured observations rather than intuition alone.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/12-cloud-capability-map.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/12-cloud-capability-map.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    The logical architecture remains stable while provider-specific service names change.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **team topology** and **service catalog**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Create a responsibility matrix and platform roadmap.

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
- **What survives:** Architecture succeeds only when ownership, incentives, operations, and delivery practices align.

## Knowledge check

1. What problem would remain if team topology were removed from the system?
2. Which observation would distinguish a failure in service catalog from a failure in vendor management?
3. What simpler alternative should be the baseline?

??? question "Answer guidance"
    A strong answer names an observable failure, traces it to a specific boundary in the chapter visual, and proposes a test that could disconfirm the explanation. The baseline should remove the chapter mechanism while holding the task and evaluation cases fixed.

## Mastery questions

1. Explain team topology without jargon and give a counterexample.
2. Compare service catalog with vendor management using quality, cost, latency, and risk.
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

- Official AWS, Azure, and Google Cloud architecture and service documentation
- Organization security and data-governance standards

Use primary sources for technical claims and official documentation for current product behavior. Record the version or access date for evolving material.

## Continue

Return to the [book index](index.md) or use site search to follow the chapter's concepts into the knowledge-area and reference pages.
