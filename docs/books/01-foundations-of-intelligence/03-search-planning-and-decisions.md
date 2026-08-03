# 1.3 — Search, Planning, and Decisions

*Book 1: Foundations of Intelligence · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- No AI background required
- Comfort reading simple Python
- Basic algebra

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

See classical search as an explicit form of reasoning. Learn how state, actions, transition models, costs, heuristics, and stopping rules turn a vague goal into an algorithm.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain why search, planning, and decisions matters using the chapter scenario, not abstract definitions alone.
- Trace how **state spaces** and **breadth-first search** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to planning.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    Reasoning can be viewed as controlled search over possible states or candidate solutions.

## Mental model

```mermaid
flowchart LR
  N0["Goal"] --> N1["State model"]
  N1["State model"] --> N2["Search or learn"]
  N2["Search or learn"] --> N3["Decision"]
  N3["Decision"] --> N4["Feedback"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **search, planning, and decisions** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### State Spaces

A state space enumerates all configurations a system can occupy plus the actions that move between them. Explicit state models make search, planning, and verification tractable. See the [State Spaces concept card](../../concepts/cards/state-spaces.md).

**Example:** Warehouse robots represent position and load status as state; illegal moves (overweight pickup) are edges you never traverse.

**Evidence of understanding:** List states, actions, and goal conditions for one task and confirm every action has a defined transition.

### Breadth-First Search

Breadth-first search expands nodes level by level, guaranteeing shortest path in unweighted graphs. It is the baseline for optimal reachability before adding heuristics. See the [Breadth-First Search concept card](../../concepts/cards/breadth-first-search.md).

**Example:** In a grid maze, BFS finds the minimum-step route from start to exit by exploring all distance-1 cells before distance-2.

**Evidence of understanding:** Run BFS on a fixed maze and verify path length equals the known shortest distance.

### A*

A* expands the lowest estimated total-cost node first, combining path cost g(n) with heuristic h(n) toward the goal. With an admissible heuristic it finds optimal paths while often expanding fewer nodes than BFS. See the [A* concept card](../../concepts/cards/a.md).

**Example:** In a grid maze, A* with Manhattan distance typically expands fewer cells than BFS while returning the same shortest path.

**Evidence of understanding:** Compare expanded node counts for BFS and A* on identical inputs and verify equal path cost.

### Heuristics

Heuristics estimate remaining cost or promise of partial solutions to guide search toward promising branches. Good heuristics cut compute; bad ones waste it or break optimality guarantees. See the [Heuristics concept card](../../concepts/cards/heuristics.md).

**Example:** Manhattan distance guides grid navigation; an overestimated heuristic can make A* suboptimal or incomplete.

**Evidence of understanding:** Measure nodes expanded with and without the heuristic on ten random maps and report the speedup ratio.

### Planning

Planning sequences actions to reach a goal given a model of state transitions, costs, and constraints. It separates deliberation from execution so plans can be validated before side effects occur. See the [Planning concept card](../../concepts/cards/planning.md).

**Example:** A deployment planner orders database migration before code rollout because the transition model forbids incompatible schema states.

**Evidence of understanding:** Produce a plan, simulate it against the transition model, and flag any action that violates preconditions.

## Worked example

**Book scenario:** A support team must route incidents without mistaking fluent descriptions for reliable decisions.

**Situation:** Overnight, three dependent services fail in sequence; the router must find a valid escalation path under on-call availability constraints.

**Baseline:** Greedy "pick highest severity keyword" with no search over dependency order.

**Application:** Model on-call slots as a graph: states are (open_incidents, assigned_engineer), actions are assign/defer/escalate, costs are SLA minutes. Run BFS for shortest escalation chain, then A* with heuristic = estimated SLA breach time.

**Test cases:** (1) Normal: single P1 with one qualified on-call. (2) Boundary: P1 when primary on-call is busy but secondary exists. (3) Adversarial: circular dependency declarations causing infinite defer loops.

**Measurement:** Path length, expanded nodes (BFS vs A*), and SLA minutes saved vs greedy on synthetic graphs.

**Design question:** What stopping rule prevents the search from exploring defer loops while still finding a valid escalation?

## Chapter hook

Run this short snippet first to anchor **search, planning, and decisions** before the book-level sample:

```python
GRAPH = {"start": ["oncall_a", "oncall_b"], "oncall_a": ["lead"], "oncall_b": ["lead"], "lead": []}
GOAL = "lead"
def bfs(start, goal):
    queue = [(start, [start])]
    seen = {start}
    while queue:
        node, path = queue.pop(0)
        if node == goal:
            return path
        for nxt in GRAPH.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, path + [nxt]))
    return None
print("escalation path:", bfs("start", GOAL))
```

Predict the printed values, then change one line tied to **state spaces** or **breadth-first search** and observe how the chapter mechanism moves.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/01-search-planning.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/01-search-planning.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    A* should reach the same shortest path as breadth-first search while often expanding fewer states when the heuristic is informative.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **state spaces** and **breadth-first search**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Implement breadth-first search and A* on the same maze.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without state spaces and record quality, latency, and failure cases.
2. **Mechanism:** Add breadth-first search while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when search, planning, and decisions earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Architecture lens

For a production design in **Foundations of Intelligence**, make the following explicit for **search, planning, and decisions**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns state spaces versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the a* boundary expose? |
| **Evidence** | Which eval slices prove search, planning, and decisions meets requirements before and after each release? |
| **Security** | What untrusted data crosses the planning boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover state spaces or breadth-first search | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | search, planning, and decisions is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in planning without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream state spaces behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

See classical search as an explicit form of reasoning. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of search, planning, and decisions without explicit state spaces.
- **Today:** Engineering teams implement search, planning, and decisions as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but planning and governance constraints will still require explicit design.
- **What survives:** Reasoning can be viewed as controlled search over possible states or candidate solutions.

## Knowledge check

1. Why is explicit state representation necessary for incident escalation?
2. How would you detect a bad heuristic in A* for routing?
3. What non-search baseline should you beat before claiming planning adds value?

??? question "Answer guidance"
    Q1: Without state you cannot represent busy on-call or deferred tickets—greedy picks repeat failed assignments. Q2: A* expands as many nodes as BFS or returns suboptimal paths. Q3: Fixed playbook order regardless of availability graph.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain state spaces without jargon and give a counterexample.**
       *Proficient answer:* a state space enumerates all configurations a system can occupy plus the actions that move between them. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare breadth-first search with planning using quality, cost, latency, and risk.**
       *Proficient answer:* breadth-first search expands nodes level by level, guaranteeing shortest path in unweighted graphs; planning sequences actions to reach a goal given a model of state transitions, costs, and constraints. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after breadth-first search; authorization before any side effect or retrieval of restricted data; observability at the transition search, planning, and decisions introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Reasoning can be viewed as controlled search over possible states or candidate solutions.

## Self-assessment rubric

| Level | Evidence |
|---|---|
| Not yet | Can repeat terms but cannot trace the visual or predict the sample. |
| Developing | Can explain the mechanism and complete the normal case with help. |
| Proficient | Can implement the exercise, diagnose a failure, and compare a baseline. |
| Transfer | Can defend an architecture choice in a new domain with evaluation evidence. |

## Evidence and further study

- Russell & Norvig — Artificial Intelligence: A Modern Approach
- Sutton & Barto — Reinforcement Learning: An Introduction

Use primary sources for technical claims and official documentation for current product behavior. Record the version or access date for evolving material.

## Continue

Return to the [book index](index.md) or use site search to follow the chapter's concepts into the knowledge-area and reference pages.
