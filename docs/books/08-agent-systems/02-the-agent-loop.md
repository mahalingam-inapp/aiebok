# 8.2 — The Agent Loop

*Book 8: Agent Systems · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- Books 5–7
- State machines
- Tools and evaluation

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Connect goal, state, planning, action, observation, reflection, and termination into a bounded state machine.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain why the agent loop matters using the chapter scenario, not abstract definitions alone.
- Trace how **plan-act-observe** and **state** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to budgets.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    An agent loop without explicit state and stopping rules is an unreliable retry loop.

## Mental model

```mermaid
flowchart LR
  N0["Goal and state"] --> N1["Plan"]
  N1["Plan"] --> N2["Act"]
  N2["Act"] --> N3["Checkpoint"]
  N3["Checkpoint"] --> N4["Stop or continue"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **the agent loop** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### Plan-Act-Observe

Plan–act–observe separates choosing the next action, executing it, and recording observations that update state. See the [Plan-Act-Observe concept card](../../concepts/cards/plan-act-observe.md).

**Example:** Agent plans 'create draft', executes, observes 'draft id=7', then plans verification instead of repeating creation.

**Evidence of understanding:** Log each cycle and show observations change subsequent plans, not identical repeats.

### State

State captures variables the system believes true at a point in execution—inventory, user intent, pending approvals. Explicit state enables recovery and verification. See the [State concept card](../../concepts/cards/state.md).

**Example:** Agent state tracks current_step, artifacts_created, and budget_remaining across turns.

**Evidence of understanding:** Serialize and deserialize state; resume mid-run and verify identical next action.

### Reflection

Reflection lets agents critique recent actions and adjust strategy—retry, replan, or escalate. Without reflection, loops repeat the same failing action. See the [Reflection concept card](../../concepts/cards/reflection.md).

**Example:** After tool 403, reflect and switch to read-only search instead of retrying delete.

**Evidence of understanding:** Count reflection-triggered strategy changes versus blind retries on failure injection suite.

### Termination

Termination criteria stop search, agent loops, or generation when goals are met, budgets exhausted, or progress stalls. Without them, systems loop indefinitely. See the [Termination concept card](../../concepts/cards/termination.md).

**Example:** Stop after five tool calls, success, or three consecutive no-progress iterations.

**Evidence of understanding:** Verify 100% of test runs halt within max_steps and document stop reason distribution.

### Budgets

Budgets cap tokens, tool calls, wall time, or dollars per task or session. Hard budgets prevent runaway agents and make economics predictable. See the [Budgets concept card](../../concepts/cards/budgets.md).

**Example:** A research agent stops after $0.50 API spend or ten tool calls, whichever comes first.

**Evidence of understanding:** Verify 100% of runs respect budget caps in stress tests with tempting infinite loops.

## Worked example

**Book scenario:** A multi-step task may pause for hours and must resume without repeating side effects.

**Situation:** The onboarding agent runs plan-act-observe cycles but previously spiraled on repeated failed API calls.

**Baseline:** while True loop calling model until success—no termination budget.

**Application:** Implement bounded state machine: goal, step counter, max attempts, reflection on failure, explicit termination states; log observations each cycle.

**Test cases:** (1) Normal: three-step plan completes. (2) Boundary: hits max attempts exactly. (3) Adversarial: tool returns success but wrong employee ID.

**Measurement:** Steps to completion, loop termination compliance, false-success detection rate.

**Design question:** Which state variable prevents an unreliable retry loop masquerading as an agent?

## Chapter hook

Run this short snippet first to anchor **the agent loop** before the book-level sample:

```python
CHAPTER = "8.2"
print("chapter hook:", CHAPTER)
state = {"step": 0, "observations": [], "done": False, "budget": 3}
while not state["done"] and state["step"] < state["budget"]:
    state["step"] += 1
    obs = f"obs-{state['step']}"
    state["observations"].append(obs)
    state["done"] = state["step"] == 3
print(state)
print("---")
print("change one input above, predict output, re-run")
```

Predict the printed values, then change one line tied to **plan-act-observe** or **state** and observe how the chapter mechanism moves.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/08-agent-state-machine.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/08-agent-state-machine.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    The state machine pauses at approval, resumes after approval, and terminates within the attempt budget.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **plan-act-observe** and **state**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Extend the included agent loop with failures and checkpointing.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without plan-act-observe and record quality, latency, and failure cases.
2. **Mechanism:** Add state while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when the agent loop earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Spec-driven habit

Every chapter lab pairs reading with **executable acceptance**. Before implementing book 8.2 — the agent loop:

1. Draft cases in `test_lab.py` or `specs/lab-0802.yaml`.
2. Use [Cursor Plan/Agent](https://cursor.com/) with "read spec first, then minimal diff".
3. Or use [OpenSpec](https://openspec.dev/) `/opsx:propose` so requirements live in `openspec/` next to code.

→ [Spec-driven workflow guide](../../getting-started/spec-driven-workflow.md) · [Lab 8.2](../../labs/0802-the-agent-loop.md)


## Architecture lens

For a production design in **Agent Systems**, make the following explicit for **the agent loop**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns plan-act-observe versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the reflection boundary expose? |
| **Evidence** | Which eval slices prove the agent loop meets requirements before and after each release? |
| **Security** | What untrusted data crosses the budgets boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover plan-act-observe or state | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | the agent loop is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in budgets without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream plan-act-observe behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Connect goal, state, planning, action, observation, reflection, and termination into a bounded state machine. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of the agent loop without explicit plan-act-observe.
- **Today:** Engineering teams implement the agent loop as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but budgets and governance constraints will still require explicit design.
- **What survives:** An agent loop without explicit state and stopping rules is an unreliable retry loop.

## Knowledge check

1. Why must agent loops have explicit termination rules?
2. How does reflection differ from blind retry?
3. What baseline lacks state tracking?

??? question "Answer guidance"
    Q1: Unbounded loops burn cost and duplicate effects. Q2: Reflection diagnoses failure cause before next action. Q3: Retry-until-success with no budget.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain plan-act-observe without jargon and give a counterexample.**
       *Proficient answer:* plan–act–observe separates choosing the next action, executing it, and recording observations that update state. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare state with budgets using quality, cost, latency, and risk.**
       *Proficient answer:* state captures variables the system believes true at a point in execution—inventory, user intent, pending approvals; budgets cap tokens, tool calls, wall time, or dollars per task or session. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after state; authorization before any side effect or retrieval of restricted data; observability at the transition the agent loop introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* An agent loop without explicit state and stopping rules is an unreliable retry loop.

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
