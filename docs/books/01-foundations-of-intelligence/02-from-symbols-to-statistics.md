# 1.2 — From Symbols to Statistics

*Book 1: Foundations of Intelligence · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- No AI background required
- Comfort reading simple Python
- Basic algebra

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Trace the path from symbolic rules and expert systems to statistical learning, deep learning, foundation models, and agents. Each era solved different problems and retained useful ideas.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain why from symbols to statistics matters using the chapter scenario, not abstract definitions alone.
- Trace how **symbolic AI** and **expert systems** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to deep learning.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    New paradigms usually absorb rather than erase earlier engineering techniques.

## Mental model

```mermaid
flowchart LR
  N0["Goal"] --> N1["State model"]
  N1["State model"] --> N2["Search or learn"]
  N2["Search or learn"] --> N3["Decision"]
  N3["Decision"] --> N4["Feedback"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **from symbols to statistics** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### Symbolic Ai

Symbolic AI represents knowledge as explicit rules, facts, and logical relations rather than learned weights. It remains valuable when constraints are crisp, auditable, and change infrequently. See the [Symbolic Ai concept card](../../concepts/cards/symbolic-ai.md).

**Example:** A tax-credit eligibility checker can encode statutory thresholds as rules that always produce the same answer for the same inputs.

**Evidence of understanding:** Compare rule coverage against a held-out set of edge cases and report precision on legally ambiguous scenarios.

### Expert Systems

Expert systems capture domain heuristics in if-then rules curated by specialists, often with explanation traces. They trade flexibility for transparency and predictable behavior in narrow domains. See the [Expert Systems concept card](../../concepts/cards/expert-systems.md).

**Example:** A manufacturing diagnostic system asks sequential sensor questions and explains which rule fired when recommending a shutdown.

**Evidence of understanding:** Audit ten decisions and verify each cites the rule chain that produced the recommendation.

### Knowledge Representation

Knowledge representation chooses how facts, relations, and uncertainty are stored—graphs, frames, schemas, or vectors. The representation determines what queries and updates are cheap or hard. See the [Knowledge Representation concept card](../../concepts/cards/knowledge-representation.md).

**Example:** Modeling product compatibility as a graph makes 'works-with' queries fast; flattening to text loses compositional structure.

**Evidence of understanding:** Run three query types on the same facts in two representations and compare answer latency and correctness.

### Statistical Learning

Statistical learning infers patterns from data with explicit assumptions about noise, independence, and generalization. It replaced brittle hand rules where variability and scale made manual encoding impractical. See the [Statistical Learning concept card](../../concepts/cards/statistical-learning.md).

**Example:** Spam filtering learned from labeled inboxes outperforms keyword lists when attackers vary phrasing continuously.

**Evidence of understanding:** Report train versus validation error and show the simplest model that meets the decision threshold.

### Deep Learning

Deep learning stacks differentiable layers that learn hierarchical features from raw inputs. It excels when hand-crafted features are incomplete but demands data, compute, and careful evaluation. See the [Deep Learning concept card](../../concepts/cards/deep-learning.md).

**Example:** Vision models learn edge and shape detectors automatically where manual feature design for every object class is infeasible.

**Evidence of understanding:** Compare a linear baseline to a small network on the same split and justify the added complexity with slice metrics.

## Worked example

**Book scenario:** A support team must route incidents without mistaking fluent descriptions for reliable decisions.

**Situation:** The same support team tried a brittle rule engine: IF body CONTAINS "urgent" THEN P1. Marketing emails now preempt real outages.

**Baseline:** Hand-maintained regular expressions over ticket text with no learning loop.

**Application:** Run the rule engine on historical tickets, log brittleness points, then overlay frequency statistics on token co-occurrence with confirmed P1 labels—showing where symbols help (exact SKU codes) and where statistics help (paraphrased outages).

**Test cases:** (1) Normal: exact match "URGENT: payment gateway offline." (2) Boundary: "urgent feature request" vs "urgent—revenue stop." (3) Adversarial: attacker marks newsletter as URGENT.

**Measurement:** Compare rule-only precision/recall against a bag-of-words logistic baseline on a frozen 500-ticket set; tabulate false P1 cost.

**Design question:** For which incident classes should you keep symbolic rules in production even after adding statistical models?

## Chapter hook

Run this short snippet first to anchor **from symbols to statistics** before the book-level sample:

```python
RULES = [("urgent", "P1"), ("question", "P3")]
tickets = [
    "URGENT: payment gateway offline",
    "urgent feature request for dashboard",
    "question about invoice format",
]
def rule_route(text):
    lower = text.lower()
    for kw, sev in RULES:
        if kw in lower:
            return sev
    return "P2"
for t in tickets:
    print({"ticket": t[:40], "route": rule_route(t)})
```

Predict the printed values, then change one line tied to **symbolic AI** or **expert systems** and observe how the chapter mechanism moves.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/01-search-planning.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/01-search-planning.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    A* should reach the same shortest path as breadth-first search while often expanding fewer states when the heuristic is informative.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **symbolic AI** and **expert systems**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Implement a tiny rule engine and document where it becomes brittle.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without symbolic ai and record quality, latency, and failure cases.
2. **Mechanism:** Add expert systems while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when from symbols to statistics earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Spec-driven habit

Every chapter lab pairs reading with **executable acceptance**. Before implementing book 1.2 — from symbols to statistics:

1. Draft cases in `test_lab.py` or `specs/lab-0102.yaml`.
2. Use [Cursor Plan/Agent](https://cursor.com/) with "read spec first, then minimal diff".
3. Or use [OpenSpec](https://openspec.dev/) `/opsx:propose` so requirements live in `openspec/` next to code.

→ [Spec-driven workflow guide](../../getting-started/spec-driven-workflow.md) · [Lab 1.2](../../labs/0102-from-symbols-to-statistics.md)


## Architecture lens

For a production design in **Foundations of Intelligence**, make the following explicit for **from symbols to statistics**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns symbolic ai versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the knowledge representation boundary expose? |
| **Evidence** | Which eval slices prove from symbols to statistics meets requirements before and after each release? |
| **Security** | What untrusted data crosses the deep learning boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover symbolic ai or expert systems | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | from symbols to statistics is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in deep learning without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream symbolic ai behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Trace the path from symbolic rules and expert systems to statistical learning, deep learning, foundation models, and agents. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of from symbols to statistics without explicit symbolic ai.
- **Today:** Engineering teams implement from symbols to statistics as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but deep learning and governance constraints will still require explicit design.
- **What survives:** New paradigms usually absorb rather than erase earlier engineering techniques.

## Knowledge check

1. Where did symbolic AI help in the incident router, and where did it become brittle?
2. What symptom would indicate the team jumped to deep learning too early?
3. What simpler statistical baseline should precede any neural approach?

??? question "Answer guidance"
    Q1: Symbols help for exact policy codes; brittleness appears when paraphrases bypass keywords. Q2: Small labeled set still dominated by regex false positives yet team deploys a large model without slice metrics. Q3: Logistic regression on TF–IDF with the same 500-ticket eval.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain symbolic AI without jargon and give a counterexample.**
       *Proficient answer:* symbolic ai represents knowledge as explicit rules, facts, and logical relations rather than learned weights. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare expert systems with deep learning using quality, cost, latency, and risk.**
       *Proficient answer:* expert systems capture domain heuristics in if-then rules curated by specialists, often with explanation traces; deep learning stacks differentiable layers that learn hierarchical features from raw inputs. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after expert systems; authorization before any side effect or retrieval of restricted data; observability at the transition from symbols to statistics introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* New paradigms usually absorb rather than erase earlier engineering techniques.

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
