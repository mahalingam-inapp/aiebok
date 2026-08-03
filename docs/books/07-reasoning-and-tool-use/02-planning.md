# 7.2 — Planning

*Book 7: Reasoning and Tool Use · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- Books 1 and 4–6
- Search and planning
- Typed software interfaces

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Represent goals, prerequisites, steps, dependencies, state, uncertainty, and replanning without confusing a plausible plan with execution.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain why planning matters using the chapter scenario, not abstract definitions alone.
- Trace how **goal decomposition** and **plan representation** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to state.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    Plans are hypotheses about action sequences and must be updated by observations.

## Mental model

```mermaid
flowchart LR
  N0["Goal"] --> N1["Candidate plans"]
  N1["Candidate plans"] --> N2["Tools"]
  N2["Tools"] --> N3["Observations"]
  N3["Observations"] --> N4["Verifier"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **planning** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### Goal Decomposition

Goal decomposition maps a top-level objective into subgoals with success conditions and dependencies. It clarifies what 'done' means at each level. See the [Goal Decomposition concept card](../../concepts/cards/goal-decomposition.md).

**Example:** 'Ship feature' decomposes into spec approved, code merged, eval passed, and canary clean.

**Evidence of understanding:** Validate dependency graph: no circular deps and every leaf goal is testable.

### Plan Representation

Plan representation encodes steps, preconditions, effects, and dependencies in structures machines can validate—DAGs, STRIPS, or typed JSON plans. See the [Plan Representation concept card](../../concepts/cards/plan-representation.md).

**Example:** A migration plan lists DB schema change before app deploy as a hard dependency edge.

**Evidence of understanding:** Reject plans where any step's preconditions are unmet given simulated initial state.

### Dependencies

Dependencies constrain execution order—step B requires output or state from step A. Violating them causes flaky failures or data corruption. See the [Dependencies concept card](../../concepts/cards/dependencies.md).

**Example:** Sending customer emails before database migration commits references wrong product IDs.

**Evidence of understanding:** Topological sort the plan and simulate; flag any out-of-order execution.

### Replanning

Replanning updates the action sequence when observations invalidate assumptions. Static plans fail in open environments with changing data. See the [Replanning concept card](../../concepts/cards/replanning.md).

**Example:** If inventory check shows zero stock, replan from 'ship item' to 'notify backorder'.

**Evidence of understanding:** Inject mid-run observation changes and measure replan latency and success rate.

### State

State captures variables the system believes true at a point in execution—inventory, user intent, pending approvals. Explicit state enables recovery and verification. See the [State concept card](../../concepts/cards/state.md).

**Example:** Agent state tracks current_step, artifacts_created, and budget_remaining across turns.

**Evidence of understanding:** Serialize and deserialize state; resume mid-run and verify identical next action.

## Worked example

**Book scenario:** A research workflow must plan, call tools, and reject unsupported conclusions.

**Situation:** The research workflow must produce a validated plan: gather sources, compare jurisdictions, draft summary—steps have dependencies and prerequisites.

**Baseline:** Model outputs numbered list with hidden dependency violations.

**Application:** Build planner emitting DAG of steps with prerequisites; validate acyclicity and required tools; replan when observation shows missing document.

**Test cases:** (1) Normal: linear plan with clear deps. (2) Boundary: parallelizable searches. (3) Adversarial: circular dependency "approve before fetch."

**Measurement:** Plan validity rate, replans per task, wall-clock vs ad-hoc prompting.

**Design question:** What observation should trigger replanning rather than continuing the current branch?

## Chapter hook

Run this short snippet first to anchor **planning** before the book-level sample:

```python
steps = {"fetch_US": [], "fetch_CA": [], "compare": ["fetch_US", "fetch_CA"], "draft": ["compare"]}
def valid_plan(completed):
    for step, prereqs in steps.items():
        if step in completed and not all(p in completed for p in prereqs):
            return False, step
    return True, "ok"
completed = {"fetch_US", "compare"}
print(valid_plan(completed))
```

Predict the printed values, then change one line tied to **goal decomposition** or **plan representation** and observe how the chapter mechanism moves.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/07-planner-verifier.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/07-planner-verifier.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    Only the plan containing every required step in dependency order should pass verification.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **goal decomposition** and **plan representation**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Build a planner that outputs a validated dependency graph.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without goal decomposition and record quality, latency, and failure cases.
2. **Mechanism:** Add plan representation while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when planning earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Architecture lens

For a production design in **Reasoning and Tool Use**, make the following explicit for **planning**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns goal decomposition versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the dependencies boundary expose? |
| **Evidence** | Which eval slices prove planning meets requirements before and after each release? |
| **Security** | What untrusted data crosses the state boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover goal decomposition or plan representation | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | planning is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in state without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream goal decomposition behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Represent goals, prerequisites, steps, dependencies, state, uncertainty, and replanning without confusing a plausible plan with execution. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of planning without explicit goal decomposition.
- **Today:** Engineering teams implement planning as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but state and governance constraints will still require explicit design.
- **What survives:** Plans are hypotheses about action sequences and must be updated by observations.

## Knowledge check

1. Why are plans hypotheses rather than guarantees?
2. How do dependency graphs prevent impossible tool order?
3. What baseline lists steps without validation?

??? question "Answer guidance"
    Q1: Execution reveals missing tools, data, or permissions. Q2: Validator blocks compare before both fetches complete. Q3: Free-form bullet plan from single prompt.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain goal decomposition without jargon and give a counterexample.**
       *Proficient answer:* goal decomposition maps a top-level objective into subgoals with success conditions and dependencies. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare plan representation with state using quality, cost, latency, and risk.**
       *Proficient answer:* plan representation encodes steps, preconditions, effects, and dependencies in structures machines can validate—dags, strips, or typed json plans; state captures variables the system believes true at a point in execution—inventory, user intent, pending approvals. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after plan representation; authorization before any side effect or retrieval of restricted data; observability at the transition planning introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Plans are hypotheses about action sequences and must be updated by observations.

## Self-assessment rubric

| Level | Evidence |
|---|---|
| Not yet | Can repeat terms but cannot trace the visual or predict the sample. |
| Developing | Can explain the mechanism and complete the normal case with help. |
| Proficient | Can implement the exercise, diagnose a failure, and compare a baseline. |
| Transfer | Can defend an architecture choice in a new domain with evaluation evidence. |

## Evidence and further study

- Yao et al. — ReAct
- Primary protocol specifications for the tool interfaces studied

Use primary sources for technical claims and official documentation for current product behavior. Record the version or access date for evolving material.

## Continue

Return to the [book index](index.md) or use site search to follow the chapter's concepts into the knowledge-area and reference pages.
