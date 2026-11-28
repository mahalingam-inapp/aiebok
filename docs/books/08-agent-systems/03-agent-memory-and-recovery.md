# 8.3 — Agent Memory and Recovery

<p class="study-position" data-course="08-agent-systems" data-lecture="03-agent-memory-and-recovery.md">Recovery and patterns · Lecture 3 of 6</p>

[← The Agent Loop](02-the-agent-loop.md) · [Course outline](index.md#course-outline){ .study-overview } · [Agent Patterns →](04-agent-patterns.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Workflows and agent loops**

    - [Agent or Workflow?](01-agent-or-workflow.md)
    - [The Agent Loop](02-the-agent-loop.md)

    **Recovery and patterns**

    - **Agent Memory and Recovery** (current)
    - [Agent Patterns](04-agent-patterns.md)

    **Coordination and operations**

    - [Multi-Agent Systems](05-multi-agent-systems.md)
    - [Operating Long-Running Agents](06-operating-long-running-agents.md)

*Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

[Download the course notebook](../../assets/notebooks/08-agent-systems.ipynb){ download } · Use the exercise under **Lecture 03**.

## Before you begin

- Courses 05–07 or equivalent experience
- State machines
- Tools and evaluation

## Why this chapter exists

Manage working state, episodic history, durable checkpoints, resumability, compensation, and idempotent tools.

## The service is back after midnight

An approval arrived before the worker restarted. The schedule proposal and its approval must stay paired after recovery.

Persist the reviewed proposal, the decision, and the next valid transition. Exercise restart separately from replay so the team can check both continuity and duplicate prevention.

## Learning objectives

- Explain why agent memory and recovery matters using the chapter scenario, not abstract definitions alone.
- Trace how **checkpoints** and **episodic memory** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to idempotency.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    Continuity requires durable state and recoverable effects, not merely longer context.

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

### Checkpoints

Checkpoints persist durable agent state so interrupted runs resume without repeating side effects. See the [Checkpoints concept card](../../concepts/cards/checkpoints.md).

**Example:** After approval gate, checkpoint stores pending payment until human approves, then continues.

**Evidence of understanding:** Kill run mid-loop, restore checkpoint, verify idempotent tools are not duplicated.

### Episodic Memory

Episodic memory stores past run trajectories—what was tried, what failed—for future reference within or across sessions. See the [Episodic Memory concept card](../../concepts/cards/episodic-memory.md).

**Example:** Remembering last week's failed migration path prevents repeating the same broken sequence.

**Evidence of understanding:** Retrieve relevant episodes for similar goals and measure retry avoidance rate.

### Recovery

Recovery restores consistent state after crashes, tool failures, or partial commits. It requires durable checkpoints and compensating actions. See the [Recovery concept card](../../concepts/cards/recovery.md).

**Example:** After payment timeout, recovery verifies ledger state before retry or refund.

**Evidence of understanding:** Inject crash at each step and verify recovery reaches consistent terminal state.

### Compensation

Compensation undo or offsets partial effects when later steps fail—Saga pattern for agents. Without it, retries duplicate charges or records. See the [Compensation concept card](../../concepts/cards/compensation.md).

**Example:** Failed booking after charge triggers automatic refund compensation transaction.

**Evidence of understanding:** Simulate mid-saga failure and verify compensation returns system to pre-transaction state.

### Idempotency

Idempotent tools produce the same effect when called repeatedly with the same idempotency key. Agents retry safely only when tools support this. See the [Idempotency concept card](../../concepts/cards/idempotency.md).

**Example:** create_ticket with idempotency key 'abc' must not spawn duplicate tickets on retry.

**Evidence of understanding:** Call the same tool twice with identical keys and verify single side effect.

## Worked example

**Book scenario:** A multi-step task may pause for hours and must resume without repeating side effects.

**Situation:** Onboarding pauses overnight for manager approval; the agent must resume without recreating accounts or double-charging hardware orders.

**Baseline:** Store only chat transcript—restart loses progress and repeats writes.

**Application:** Persist checkpoints after each idempotent-safe step, durable episodic log, compensation actions for partial failures, resume from last committed checkpoint.

**Test cases:** (1) Normal: resume after clean pause. (2) Boundary: crash after non-idempotent step before checkpoint. (3) Adversarial: duplicate resume messages from two workers.

**Measurement:** Duplicate side-effect count, time-to-resume, checkpoint integrity checks.

**Design question:** Which steps require idempotency keys before they can be checkpointed safely?

## Follow the code

Run this short Python demonstration of **agent memory and recovery**. Identify the input, the decision or calculation, and the printed result.

```python
checkpoints = []
state = {"step": "assign_laptop", "order_id": None}
def save(state):
    checkpoints.append(dict(state))
def resume():
    return checkpoints[-1] if checkpoints else None
save({"step": "create_account", "done": True})
state = resume()
print("resume_at:", state)
```

Predict the result before you run it. Change one input, then explain the resulting difference using the mechanism from the worked example.

For a longer implementation, run the [course code sample](../../code-samples/08-agent-state-machine.py). The state machine pauses at approval, resumes after approval, and terminates within the attempt budget.

## Engineering practice

**Build:** Persist and resume an interrupted multi-step run.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without checkpoints and record quality, latency, and failure cases.
2. **Mechanism:** Add episodic memory while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when agent memory and recovery earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

**Section checkpoint**

Record what must survive a restart so an approved action is handled once.

Compare your prediction with the chapter demonstration and explain which input changed the result. The [course notebook](../../assets/notebooks/08-agent-systems.ipynb){ download } contains the runnable examples and a checked experiment. See [notebook setup](../../labs/notebooks/index.md) if you are new to Jupyter.

## Spec-driven habit

Every chapter lab pairs reading with **executable acceptance**. Before implementing book 8.3 — agent memory and recovery:

1. Draft cases in `test_lab.py` or `specs/lab-0803.yaml`.
2. Use [Cursor Plan/Agent](https://cursor.com/) with "read spec first, then minimal diff".
3. Or use [OpenSpec](https://openspec.dev/) `/opsx:propose` so requirements live in `openspec/` next to code.

→ [Spec-driven workflow guide](../../getting-started/spec-driven-workflow.md) · [Lab 8.3](../../labs/0803-agent-memory-and-recovery.md)


## Architecture lens

For a production design in **Agent Systems**, make the following explicit for **agent memory and recovery**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns checkpoints versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the recovery boundary expose? |
| **Evidence** | Which eval slices prove agent memory and recovery meets requirements before and after each release? |
| **Security** | What untrusted data crosses the idempotency boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover checkpoints or episodic memory | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | agent memory and recovery is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in idempotency without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream checkpoints behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Manage working state, episodic history, durable checkpoints, resumability, compensation, and idempotent tools. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of agent memory and recovery without explicit checkpoints.
- **Today:** Engineering teams implement agent memory and recovery as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but idempotency and governance constraints will still require explicit design.
- **What survives:** Continuity requires durable state and recoverable effects, not merely longer context.

## Knowledge check

1. Why is continuity more than longer context?
2. How does compensation differ from retry?
3. What recovery baseline relies on transcript only?

??? question "Answer guidance"
    Q1: Durable state survives restarts; context windows do not. Q2: Compensation undoes partial effects; retry may duplicate them. Q3: Re-prompt model with chat history only.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain checkpoints without jargon and give a counterexample.**
       *Proficient answer:* checkpoints persist durable agent state so interrupted runs resume without repeating side effects. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare episodic memory with idempotency using quality, cost, latency, and risk.**
       *Proficient answer:* episodic memory stores past run trajectories—what was tried, what failed—for future reference within or across sessions; idempotent tools produce the same effect when called repeatedly with the same idempotency key. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after episodic memory; authorization before any side effect or retrieval of restricted data; observability at the transition agent memory and recovery introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Continuity requires durable state and recoverable effects, not merely longer context.

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

[← The Agent Loop](02-the-agent-loop.md) · [Course outline](index.md#course-outline){ .study-overview } · [Agent Patterns →](04-agent-patterns.md)
{: .study-directions .study-directions--footer }
