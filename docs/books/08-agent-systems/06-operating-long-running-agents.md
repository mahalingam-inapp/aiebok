# 8.6 — Operating Long-Running Agents

*Book 8: Agent Systems · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- Books 5–7
- State machines
- Tools and evaluation

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Design durable orchestration, queues, scheduling, leases, approvals, monitoring, incident response, and safe cancellation.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain why operating long-running agents matters using the chapter scenario, not abstract definitions alone.
- Trace how **durable execution** and **queues** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to cancellation.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    Long-running agents are distributed systems with probabilistic decision components.

## Mental model

```mermaid
flowchart LR
  N0["Goal and state"] --> N1["Plan"]
  N1["Plan"] --> N2["Act"]
  N2["Act"] --> N3["Checkpoint"]
  N3["Checkpoint"] --> N4["Stop or continue"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **operating long-running agents** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### Durable Execution

Durable execution persists workflow state across process restarts and deploys—Temporal, Step Functions patterns. Long agents need this, not in-memory loops alone. See the [Durable Execution concept card](../../concepts/cards/durable-execution.md).

**Example:** Day-long onboarding workflow survives server restart and resumes at last checkpoint.

**Evidence of understanding:** Kill worker mid-run twice and verify exactly-once side effects for non-idempotent steps.

### Queues

Queues decouple agent work submission from processing, smoothing load and enabling retries. Poison messages need dead-letter handling. See the [Queues concept card](../../concepts/cards/queues.md).

**Example:** Approval tasks queue while humans respond; workers poll with backoff.

**Evidence of understanding:** Measure queue depth p95 and time-to-drain under 2× normal submit rate.

### Leases

Leases grant temporary exclusive ownership of a resource—document, ticket, shard—preventing duplicate processing. Expired leases must reclaim safely. See the [Leases concept card](../../concepts/cards/leases.md).

**Example:** Worker holds 60s lease on ticket; another worker picks up only after lease expiry.

**Evidence of understanding:** Simulate worker death before lease expiry and verify safe reassignment.

### Human Oversight

Human oversight defines when and how people supervise agents—monitoring dashboards, escalation queues, kill switches. It scales only with clear triggers. See the [Human Oversight concept card](../../concepts/cards/human-oversight.md).

**Example:** Escalate to human when confidence < 0.7 or spend > $1 on a single task.

**Evidence of understanding:** Track escalation rate, human resolution time, and override frequency weekly.

### Cancellation

Cancellation stops in-flight agent work cleanly—revoke leases, abort tool calls, compensate partial effects. Users need cancel when plans change. See the [Cancellation concept card](../../concepts/cards/cancellation.md).

**Example:** User cancels long research job; system stops tools and marks run cancelled, not failed.

**Evidence of understanding:** Cancel at random steps and verify no orphaned side effects remain.

## Worked example

**Book scenario:** A multi-step task may pause for hours and must resume without repeating side effects.

**Situation:** Onboarding agent runs up to 24 hours with human approvals; SRE needs SLOs and safe cancellation.

**Baseline:** Fire-and-forget background job with no lease or monitoring.

**Application:** Design durable orchestration with queue, worker leases, approval webhooks, heartbeat monitoring, cancel propagates to in-flight tools, runbook for stuck runs.

**Test cases:** (1) Normal: completes within SLO. (2) Boundary: approval waits 12 hours. (3) Adversarial: worker crash mid-lease without release.

**Measurement:** SLO adherence, stuck-run detection time, clean cancel success rate.

**Design question:** What lease duration balances slow approvals against fast failure detection?

## Chapter hook

Run this short snippet first to anchor **operating long-running agents** before the book-level sample:

```python
CHAPTER = "8.6"
print("chapter hook:", CHAPTER)
SLO_HOURS = 24
lease_minutes = 30
elapsed = 12 * 60
renewals = elapsed // lease_minutes
print({"elapsed_min": elapsed, "lease_renewals": renewals, "within_slo": elapsed <= SLO_HOURS * 60})
print("---")
print("change one input above, predict output, re-run")
```

Predict the printed values, then change one line tied to **durable execution** or **queues** and observe how the chapter mechanism moves.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/08-agent-state-machine.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/08-agent-state-machine.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    The state machine pauses at approval, resumes after approval, and terminates within the attempt budget.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **durable execution** and **queues**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Create an SLO and runbook for a day-long agent workflow.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without durable execution and record quality, latency, and failure cases.
2. **Mechanism:** Add queues while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when operating long-running agents earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Spec-driven habit

Every chapter lab pairs reading with **executable acceptance**. Before implementing book 8.6 — operating long-running agents:

1. Draft cases in `test_lab.py` or `specs/lab-0806.yaml`.
2. Use [Cursor Plan/Agent](https://cursor.com/) with "read spec first, then minimal diff".
3. Or use [OpenSpec](https://openspec.dev/) `/opsx:propose` so requirements live in `openspec/` next to code.

→ [Spec-driven workflow guide](../../getting-started/spec-driven-workflow.md) · [Lab 8.6](../../labs/0806-operating-long-running-agents.md)


## Architecture lens

For a production design in **Agent Systems**, make the following explicit for **operating long-running agents**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns durable execution versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the leases boundary expose? |
| **Evidence** | Which eval slices prove operating long-running agents meets requirements before and after each release? |
| **Security** | What untrusted data crosses the cancellation boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover durable execution or queues | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | operating long-running agents is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in cancellation without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream durable execution behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Design durable orchestration, queues, scheduling, leases, approvals, monitoring, incident response, and safe cancellation. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of operating long-running agents without explicit durable execution.
- **Today:** Engineering teams implement operating long-running agents as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but cancellation and governance constraints will still require explicit design.
- **What survives:** Long-running agents are distributed systems with probabilistic decision components.

## Knowledge check

1. Why are long-running agents distributed systems problems?
2. How do leases prevent duplicate workers?
3. What operations baseline lacks cancellation?

??? question "Answer guidance"
    Q1: They need queues, timeouts, idempotency, human waits. Q2: Expired lease allows takeover; active lease blocks duplicate. Q3: Background thread with no orchestrator.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain durable execution without jargon and give a counterexample.**
       *Proficient answer:* durable execution persists workflow state across process restarts and deploys—temporal, step functions patterns. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare queues with cancellation using quality, cost, latency, and risk.**
       *Proficient answer:* queues decouple agent work submission from processing, smoothing load and enabling retries; cancellation stops in-flight agent work cleanly—revoke leases, abort tool calls, compensate partial effects. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after queues; authorization before any side effect or retrieval of restricted data; observability at the transition operating long-running agents introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Long-running agents are distributed systems with probabilistic decision components.

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
