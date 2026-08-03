# 8.4 — Agent Patterns

*Book 8: Agent Systems · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- Books 5–7
- State machines
- Tools and evaluation

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Apply planner–executor, supervisor–worker, reviewer, evaluator–optimizer, routing, and human-approval patterns.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain why agent patterns matters using the chapter scenario, not abstract definitions alone.
- Trace how **planner-executor** and **supervisor-worker** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to approval gates.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    Patterns trade flexibility for additional state, calls, latency, and failure surfaces.

## Mental model

```mermaid
flowchart LR
  N0["Goal and state"] --> N1["Plan"]
  N1["Plan"] --> N2["Act"]
  N2["Act"] --> N3["Checkpoint"]
  N3["Checkpoint"] --> N4["Stop or continue"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **agent patterns** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### Planner-Executor

Planner–executor splits strategic planning from tactical execution, often with different models or prompts. Plans can be validated before expensive actions. See the [Planner-Executor concept card](../../concepts/cards/planner-executor.md).

**Example:** Planner outputs step graph; executor calls tools one step at a time with verification.

**Evidence of understanding:** Measure plan validity rate and end-to-end success versus monolithic agent.

### Supervisor-Worker

Supervisor–worker assigns subtasks to workers and integrates results, adding coordination overhead for parallelizable work. See the [Supervisor-Worker concept card](../../concepts/cards/supervisor-worker.md).

**Example:** Supervisor delegates research subtopics to three workers, then merges citations.

**Evidence of understanding:** Compare wall time and error rate versus single agent with sequential tool calls.

### Reviewer

Reviewer pattern inserts a critique pass before delivery or irreversible actions. Reviewers should use different prompts or models than generators. See the [Reviewer concept card](../../concepts/cards/reviewer.md).

**Example:** Draft email reviewed for PII leakage before send tool invocation.

**Evidence of understanding:** Measure defect catch rate with reviewer on versus off at equal total latency budget.

### Routing

Routing directs requests to models, tools, or strategies by task type, risk, or budget. Routers encode product policy about cheap versus capable paths. See the [Routing concept card](../../concepts/cards/routing.md).

**Example:** Simple FAQs route to small model; compliance questions route to audited large model.

**Evidence of understanding:** Log routing decisions and compare quality and cost versus always-large baseline.

### Approval Gates

Approval gates pause execution until authorized humans confirm high-impact actions. They convert autonomy into supervised autonomy. See the [Approval Gates concept card](../../concepts/cards/approval-gates.md).

**Example:** Production deploy agent waits for manager click before kubectl apply.

**Evidence of understanding:** Verify gate cannot be bypassed via prompt injection or direct tool URL.

## Worked example

**Book scenario:** A multi-step task may pause for hours and must resume without repeating side effects.

**Situation:** Team debates planner–executor vs supervisor–worker patterns for onboarding with compliance review.

**Baseline:** Single monolithic agent prompt handling planning and execution.

**Application:** Implement two patterns: planner–executor with separate plans, and supervisor routing subtasks; measure coordination overhead, latency, and failure isolation.

**Test cases:** (1) Normal: linear subtasks. (2) Boundary: reviewer rejects one subtask. (3) Adversarial: worker agent returns plausible but unauthorized action.

**Measurement:** End-to-end latency, inter-agent messages, defect rate vs monolithic agent.

**Design question:** When does supervisor overhead exceed its fault-isolation benefit?

## Chapter hook

Run this short snippet first to anchor **agent patterns** before the book-level sample:

```python
patterns = {
    "monolith": {"calls": 1, "latency": 1.0},
    "planner_executor": {"calls": 3, "latency": 1.6},
    "supervisor_worker": {"calls": 5, "latency": 2.1},
}
task_risk = "high"
choice = "supervisor_worker" if task_risk == "high" else "planner_executor"
print({"pattern": choice, **patterns[choice]})
```

Predict the printed values, then change one line tied to **planner-executor** or **supervisor-worker** and observe how the chapter mechanism moves.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/08-agent-state-machine.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/08-agent-state-machine.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    The state machine pauses at approval, resumes after approval, and terminates within the attempt budget.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **planner-executor** and **supervisor-worker**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Implement two patterns and measure coordination overhead.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without planner-executor and record quality, latency, and failure cases.
2. **Mechanism:** Add supervisor-worker while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when agent patterns earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Architecture lens

For a production design in **Agent Systems**, make the following explicit for **agent patterns**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns planner-executor versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the reviewer boundary expose? |
| **Evidence** | Which eval slices prove agent patterns meets requirements before and after each release? |
| **Security** | What untrusted data crosses the approval gates boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover planner-executor or supervisor-worker | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | agent patterns is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in approval gates without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream planner-executor behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Apply planner–executor, supervisor–worker, reviewer, evaluator–optimizer, routing, and human-approval patterns. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of agent patterns without explicit planner-executor.
- **Today:** Engineering teams implement agent patterns as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but approval gates and governance constraints will still require explicit design.
- **What survives:** Patterns trade flexibility for additional state, calls, latency, and failure surfaces.

## Knowledge check

1. What do agent patterns trade for flexibility?
2. When is a reviewer agent worth the extra call?
3. What baseline uses one prompt for everything?

??? question "Answer guidance"
    Q1: Extra state, calls, latency, failure surfaces. Q2: High-risk actions needing independent gate. Q3: Single agent with combined plan+act instructions.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain planner-executor without jargon and give a counterexample.**
       *Proficient answer:* planner–executor splits strategic planning from tactical execution, often with different models or prompts. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare supervisor-worker with approval gates using quality, cost, latency, and risk.**
       *Proficient answer:* supervisor–worker assigns subtasks to workers and integrates results, adding coordination overhead for parallelizable work; approval gates pause execution until authorized humans confirm high-impact actions. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after supervisor-worker; authorization before any side effect or retrieval of restricted data; observability at the transition agent patterns introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Patterns trade flexibility for additional state, calls, latency, and failure surfaces.

## Self-assessment rubric

| Level | Evidence |
|---|---|
| Not yet | Can repeat terms but cannot trace the visual or predict the sample. |
| Developing | Can explain the mechanism and complete the normal case with help. |
| Proficient | Can implement the exercise, diagnose a failure, and compare a baseline. |
| Transfer | Can defend an architecture choice in a new domain with evaluation evidence. |

## Evidence and further study

- Primary papers for the selected agent pattern
- Distributed-systems references for durable execution and idempotency

Use primary sources for technical claims and official documentation for current product behavior. Record the version or access date for evolving material.

## Continue

Return to the [book index](index.md) or use site search to follow the chapter's concepts into the knowledge-area and reference pages.
