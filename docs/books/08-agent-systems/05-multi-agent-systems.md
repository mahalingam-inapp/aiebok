# 8.5 — Multi-Agent Systems

*Book 8: Agent Systems · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- Books 5–7
- State machines
- Tools and evaluation

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Study delegation, role boundaries, communication, shared state, consensus, conflict, security, and why many tasks do not need multiple agents.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain why multi-agent systems matters using the chapter scenario, not abstract definitions alone.
- Trace how **delegation** and **coordination** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to role isolation.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    More agents increase organizational complexity faster than raw capability.

## Mental model

```mermaid
flowchart LR
  N0["Goal and state"] --> N1["Plan"]
  N1["Plan"] --> N2["Act"]
  N2["Act"] --> N3["Checkpoint"]
  N3["Checkpoint"] --> N4["Stop or continue"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **multi-agent systems** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### Delegation

Delegation assigns subtasks to specialized agents or tools with scoped permissions. Poor delegation boundaries cause duplicated work or authority gaps. See the [Delegation concept card](../../concepts/cards/delegation.md).

**Example:** Legal sub-agent handles contract clauses; main agent cannot invoke legal tools directly.

**Evidence of understanding:** Audit delegation graph for cycles and privilege escalation paths.

### Coordination

Coordination synchronizes multiple agents—shared queues, locks, message passing—to avoid conflicting actions. It adds latency and failure modes. See the [Coordination concept card](../../concepts/cards/coordination.md).

**Example:** Two workers must not edit the same document; lease coordinates exclusive access.

**Evidence of understanding:** Stress test concurrent agents and measure conflict rate with and without coordination.

### Shared State

Shared state stores variables visible to multiple agents—task boards, evidence pools. Consistency requires versioning or transactional updates. See the [Shared State concept card](../../concepts/cards/shared-state.md).

**Example:** Research evidence store accumulates URLs all workers cite; stale entries need TTL.

**Evidence of understanding:** Verify concurrent writes do not lose updates using version counters or locks.

### Consensus

Consensus protocols align multiple agents on a decision before action—voting, debate, or judge model. Useful when single-agent judgment is unreliable. See the [Consensus concept card](../../concepts/cards/consensus.md).

**Example:** Three agents vote on classification before automated ticket routing proceeds.

**Evidence of understanding:** Compare accuracy of consensus versus single agent on ambiguous case set.

### Role Isolation

Role isolation restricts each agent to tools and data matching its role, limiting blast radius of compromise or error. See the [Role Isolation concept card](../../concepts/cards/role-isolation.md).

**Example:** Billing agent cannot access HR records even if prompt requests it.

**Evidence of understanding:** Attempt cross-role tool access in tests and expect hard denial.

## Worked example

**Book scenario:** A multi-step task may pause for hours and must resume without repeating side effects.

**Situation:** Engineering proposes five specialized agents for onboarding; operations struggles with coordination failures.

**Baseline:** Five agents with shared scratchpad and no role isolation—conflicting writes.

**Application:** Split research-only subtask across workers with role boundaries, shared read-only evidence store, supervisor merge; compare to single agent with parallel tool calls.

**Test cases:** (1) Normal: parallel document fetches. (2) Boundary: two workers propose conflicting access levels. (3) Adversarial: compromised worker poisons shared state.

**Measurement:** Conflict incidents, total tokens, task success vs single-agent parallel tools.

**Design question:** When do parallel tools inside one agent suffice instead of multiple agents?

## Chapter hook

Run this short snippet first to anchor **multi-agent systems** before the book-level sample:

```python
CHAPTER = "8.5"
print("chapter hook:", CHAPTER)
workers = {"A": "fetch HR policy", "B": "fetch IT policy"}
shared = []
for w, task in workers.items():
    shared.append({"worker": w, "result": f"evidence from {task}"})
conflicts = len({r["result"][:10] for r in shared}) < len(shared)
print({"evidence": shared, "conflict": conflicts})
print("---")
print("change one input above, predict output, re-run")
```

Predict the printed values, then change one line tied to **delegation** or **coordination** and observe how the chapter mechanism moves.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/08-agent-state-machine.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/08-agent-state-machine.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    The state machine pauses at approval, resumes after approval, and terminates within the attempt budget.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **delegation** and **coordination**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Split a research task across workers and compare with one-agent parallel tools.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without delegation and record quality, latency, and failure cases.
2. **Mechanism:** Add coordination while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when multi-agent systems earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Spec-driven habit

Every chapter lab pairs reading with **executable acceptance**. Before implementing book 8.5 — multi-agent systems:

1. Draft cases in `test_lab.py` or `specs/lab-0805.yaml`.
2. Use [Cursor Plan/Agent](https://cursor.com/) with "read spec first, then minimal diff".
3. Or use [OpenSpec](https://openspec.dev/) `/opsx:propose` so requirements live in `openspec/` next to code.

→ [Spec-driven workflow guide](../../getting-started/spec-driven-workflow.md) · [Lab 8.5](../../labs/0805-multi-agent-systems.md)


## Architecture lens

For a production design in **Agent Systems**, make the following explicit for **multi-agent systems**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns delegation versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the shared state boundary expose? |
| **Evidence** | Which eval slices prove multi-agent systems meets requirements before and after each release? |
| **Security** | What untrusted data crosses the role isolation boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover delegation or coordination | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | multi-agent systems is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in role isolation without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream delegation behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Study delegation, role boundaries, communication, shared state, consensus, conflict, security, and why many tasks do not need multiple agents. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of multi-agent systems without explicit delegation.
- **Today:** Engineering teams implement multi-agent systems as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but role isolation and governance constraints will still require explicit design.
- **What survives:** More agents increase organizational complexity faster than raw capability.

## Knowledge check

1. Why do more agents increase organizational complexity?
2. How does shared mutable state create security risk?
3. What simpler baseline parallelizes tool calls?

??? question "Answer guidance"
    Q1: Delegation, consensus, and messaging multiply failure modes. Q2: One agent can overwrite another's conclusions. Q3: Single agent issuing parallel read-only tool calls.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain delegation without jargon and give a counterexample.**
       *Proficient answer:* delegation assigns subtasks to specialized agents or tools with scoped permissions. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare coordination with role isolation using quality, cost, latency, and risk.**
       *Proficient answer:* coordination synchronizes multiple agents—shared queues, locks, message passing—to avoid conflicting actions; role isolation restricts each agent to tools and data matching its role, limiting blast radius of compromise or error. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after coordination; authorization before any side effect or retrieval of restricted data; observability at the transition multi-agent systems introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* More agents increase organizational complexity faster than raw capability.

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
