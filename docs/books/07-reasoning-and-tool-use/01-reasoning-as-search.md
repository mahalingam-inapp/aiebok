# 7.1 — Reasoning as Search

*Book 7: Reasoning and Tool Use · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- Books 1 and 4–6
- Search and planning
- Typed software interfaces

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Separate recall from deliberate search and study decomposition, candidate generation, backtracking, and stopping.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain why reasoning as search matters using the chapter scenario, not abstract definitions alone.
- Trace how **decomposition** and **search** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to termination.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    Additional inference helps when the task benefits from exploring and rejecting alternatives.

## Mental model

```mermaid
flowchart LR
  N0["Goal"] --> N1["Candidate plans"]
  N1["Candidate plans"] --> N2["Tools"]
  N2["Tools"] --> N3["Observations"]
  N3["Observations"] --> N4["Verifier"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **reasoning as search** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### Decomposition

Decomposition breaks complex tasks into subtasks with clearer stopping criteria and verifiable intermediate results. It enables parallel work and localized retries. See the [Decomposition concept card](../../concepts/cards/decomposition.md).

**Example:** Research splits into search, read, synthesize, and cite—each subtask has its own eval.

**Evidence of understanding:** Compare success rate on compound tasks with monolithic prompts versus explicit decomposition.

### Search

Search explores a space of partial solutions—plans, code candidates, tool sequences—guided by heuristics and budgets. Inference-time search trades compute for accuracy. See the [Search concept card](../../concepts/cards/search.md).

**Example:** Tree-of-thought explores multiple math solution paths before committing to an answer.

**Evidence of understanding:** Plot accuracy versus number of nodes expanded with a fixed timeout.

### Backtracking

Backtracking abandons partial solutions that fail constraints and returns to earlier choices. Essential when early greedy decisions lock in errors. See the [Backtracking concept card](../../concepts/cards/backtracking.md).

**Example:** If tool call returns 404, backtrack to alternate query formulation instead of hallucinating data.

**Evidence of understanding:** Log backtrack events and measure recovery rate on injected tool failures.

### Heuristics

Heuristics estimate remaining cost or promise of partial solutions to guide search toward promising branches. Good heuristics cut compute; bad ones waste it or break optimality guarantees. See the [Heuristics concept card](../../concepts/cards/heuristics.md).

**Example:** Manhattan distance guides grid navigation; an overestimated heuristic can make A* suboptimal or incomplete.

**Evidence of understanding:** Measure nodes expanded with and without the heuristic on ten random maps and report the speedup ratio.

### Termination

Termination criteria stop search, agent loops, or generation when goals are met, budgets exhausted, or progress stalls. Without them, systems loop indefinitely. See the [Termination concept card](../../concepts/cards/termination.md).

**Example:** Stop after five tool calls, success, or three consecutive no-progress iterations.

**Evidence of understanding:** Verify 100% of test runs halt within max_steps and document stop reason distribution.

## Worked example

**Book scenario:** A research workflow must plan, call tools, and reject unsupported conclusions.

**Situation:** A research workflow must plan, call tools, and reject unsupported conclusions when answering whether a policy change affects remote workers in two countries.

**Baseline:** Single-shot model answer from parametric memory—confident but unsourced.

**Application:** Decompose question into sub-queries, search policy state space with explicit backtracking when evidence conflicts, terminate when support threshold met or budget exhausted.

**Test cases:** (1) Normal: both countries covered in one doc. (2) Boundary: evidence only for one country. (3) Adversarial: contradictory paragraphs requiring branch exploration.

**Measurement:** Answer accuracy vs search nodes expanded; unsupported claim rate.

**Design question:** What stopping rule prevents infinite refinement loops on ambiguous policy text?

## Chapter hook

Run this short snippet first to anchor **reasoning as search** before the book-level sample:

```python
states = [("start", ["search US", "search CA"]), ("search US", ["merge"]), ("search CA", ["merge"])]
budget = 3
expanded = 0
agenda = ["start"]
while agenda and expanded < budget:
    node = agenda.pop(0)
    expanded += 1
    next_nodes = dict(states).get(node, [])
    agenda.extend(next_nodes)
print({"expanded": expanded, "remaining": agenda})
```

Predict the printed values, then change one line tied to **decomposition** or **search** and observe how the chapter mechanism moves.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/07-planner-verifier.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/07-planner-verifier.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    Only the plan containing every required step in dependency order should pass verification.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **decomposition** and **search**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Solve a constraint problem with explicit state search.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without decomposition and record quality, latency, and failure cases.
2. **Mechanism:** Add search while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when reasoning as search earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Architecture lens

For a production design in **Reasoning and Tool Use**, make the following explicit for **reasoning as search**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns decomposition versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the backtracking boundary expose? |
| **Evidence** | Which eval slices prove reasoning as search meets requirements before and after each release? |
| **Security** | What untrusted data crosses the termination boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover decomposition or search | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | reasoning as search is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in termination without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream decomposition behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Separate recall from deliberate search and study decomposition, candidate generation, backtracking, and stopping. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of reasoning as search without explicit decomposition.
- **Today:** Engineering teams implement reasoning as search as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but termination and governance constraints will still require explicit design.
- **What survives:** Additional inference helps when the task benefits from exploring and rejecting alternatives.

## Knowledge check

1. When does additional inference help via exploring alternatives?
2. How does backtracking appear in policy research tasks?
3. What baseline answers without search?

??? question "Answer guidance"
    Q1: When tasks need rejecting wrong branches, not just first guess. Q2: Conflict between paragraphs triggers alternate path. Q3: Zero-shot answer with no tool or retrieval loop.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain decomposition without jargon and give a counterexample.**
       *Proficient answer:* decomposition breaks complex tasks into subtasks with clearer stopping criteria and verifiable intermediate results. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare search with termination using quality, cost, latency, and risk.**
       *Proficient answer:* search explores a space of partial solutions—plans, code candidates, tool sequences—guided by heuristics and budgets; termination criteria stop search, agent loops, or generation when goals are met, budgets exhausted, or progress stalls. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after search; authorization before any side effect or retrieval of restricted data; observability at the transition reasoning as search introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Additional inference helps when the task benefits from exploring and rejecting alternatives.

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
