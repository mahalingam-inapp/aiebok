# 8.2 — The Agent Loop

<p class="study-position" data-course="08-agent-systems" data-lecture="02-the-agent-loop.md">Workflows and agent loops · Lecture 2 of 6</p>

[← Agent or Workflow?](01-agent-or-workflow.md) · [Course outline](index.md#course-outline){ .study-overview } · [Agent Memory and Recovery →](03-agent-memory-and-recovery.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Workflows and agent loops**

    - [Agent or Workflow?](01-agent-or-workflow.md)
    - **The Agent Loop** (current)

    **Recovery and patterns**

    - [Agent Memory and Recovery](03-agent-memory-and-recovery.md)
    - [Agent Patterns](04-agent-patterns.md)

    **Coordination and operations**

    - [Multi-Agent Systems](05-multi-agent-systems.md)
    - [Operating Long-Running Agents](06-operating-long-running-agents.md)

*Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

[Download the course notebook](../../assets/notebooks/08-agent-systems.ipynb){ download } · Use the exercise under **Lecture 02**.

## Before you begin

- Courses 05–07 or equivalent experience
- State machines
- Tools and evaluation

## Why this chapter exists

Connect goal, state, planning, action, observation, reflection, and termination into a bounded state machine.

## A loop that stops early is often the right result

The scheduler has exhausted its candidate slots and considers asking a calendar tool again despite unchanged inputs.

Make progress observable and set a stopping condition tied to budget and evidence. A stop with an explanation and a next action gives Lena something to work with. Repetition without new state gives her a delay.

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

## Follow the code

Run this short Python demonstration of **the agent loop**. Identify the input, the decision or calculation, and the printed result.

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

Predict the result before you run it. Change one input, then explain the resulting difference using the mechanism from the worked example.

For a longer implementation, run the [course code sample](../../code-samples/08-agent-state-machine.py). The state machine pauses at approval, resumes after approval, and terminates within the attempt budget.

## Engineering practice

**Build:** Extend the included agent loop with failures and checkpointing.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without plan-act-observe and record quality, latency, and failure cases.
2. **Mechanism:** Add state while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when the agent loop earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

**Section checkpoint**

Identify where a fixed workflow is sufficient. Write an invariant for a bounded loop.

Compare your prediction with the chapter demonstration and explain which input changed the result. The [course notebook](../../assets/notebooks/08-agent-systems.ipynb){ download } contains the runnable examples and a checked experiment. See [notebook setup](../../labs/notebooks/index.md) if you are new to Jupyter.

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

## Continue

[← Agent or Workflow?](01-agent-or-workflow.md) · [Course outline](index.md#course-outline){ .study-overview } · [Agent Memory and Recovery →](03-agent-memory-and-recovery.md)
{: .study-directions .study-directions--footer }
