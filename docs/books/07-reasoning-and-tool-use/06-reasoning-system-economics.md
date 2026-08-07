# 7.6 — Reasoning-System Economics

*Book 7: Reasoning and Tool Use · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- Books 1 and 4–6
- Search and planning
- Typed software interfaces

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Balance accuracy, latency, token use, parallel candidates, tool calls, caches, failure rates, and task value.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain why reasoning-system economics matters using the chapter scenario, not abstract definitions alone.
- Trace how **test-time compute** and **latency** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to budgets.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    Spend additional computation only where expected outcome improvement justifies it.

## Mental model

```mermaid
flowchart LR
  N0["Goal"] --> N1["Candidate plans"]
  N1["Candidate plans"] --> N2["Tools"]
  N2["Tools"] --> N3["Observations"]
  N3["Observations"] --> N4["Verifier"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **reasoning-system economics** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### Test-Time Compute

Test-time compute spends extra inference—search, sampling, verification—at query time to improve accuracy. It trades latency and cost for quality on hard inputs. See the [Test-Time Compute concept card](../../concepts/cards/test-time-compute.md).

**Example:** Spending 5× tokens on best-of-N may be worth it for $10k loan decisions only.

**Evidence of understanding:** Plot quality versus total tokens and mark Pareto-optimal operating points.

### Latency

Latency is time from request to usable response—dominated by model, retrieval, tools, and serialization. User workflows break when p95 exceeds interaction tolerance. See the [Latency concept card](../../concepts/cards/latency.md).

**Example:** Adding reranking adds 200ms; measure whether task success gain justifies it.

**Evidence of understanding:** Track p50 and p95 end-to-end latency with breakdown by stage in traces.

### Cost-Quality Curves

Cost-quality curves plot spend—tokens, GPU seconds, API dollars—against task metrics. They guide routing and when to stop adding compute. See the [Cost-Quality Curves concept card](../../concepts/cards/cost-quality-curves.md).

**Example:** Best-of-N may lift accuracy 2 points for 4× cost—acceptable only above a revenue threshold.

**Evidence of understanding:** Generate curve points for three strategies and document chosen operating point rationale.

### Routing

Routing directs requests to models, tools, or strategies by task type, risk, or budget. Routers encode product policy about cheap versus capable paths. See the [Routing concept card](../../concepts/cards/routing.md).

**Example:** Simple FAQs route to small model; compliance questions route to audited large model.

**Evidence of understanding:** Log routing decisions and compare quality and cost versus always-large baseline.

### Budgets

Budgets cap tokens, tool calls, wall time, or dollars per task or session. Hard budgets prevent runaway agents and make economics predictable. See the [Budgets concept card](../../concepts/cards/budgets.md).

**Example:** A research agent stops after $0.50 API spend or ten tool calls, whichever comes first.

**Evidence of understanding:** Verify 100% of runs respect budget caps in stress tests with tempting infinite loops.

## Worked example

**Book scenario:** A research workflow must plan, call tools, and reject unsupported conclusions.

**Situation:** Leadership wants higher answer quality but budget caps tokens and tool calls per research task.

**Baseline:** Always run best-of-5 with full verifier loop—quality up, costs unsustainable.

**Application:** Plot cost-quality curves for single-pass, best-of-N, verifier loops; route easy queries cheaply, spend test-time compute only on high-value uncertain cases.

**Test cases:** (1) Normal: low-uncertainty FAQ. (2) Boundary: uncertainty score near routing threshold. (3) Adversarial: attacker triggers expensive loops via ambiguous queries.

**Measurement:** Quality by route tier, average $/task, loop explosion incidents.

**Design question:** What signal routes a query to expensive reasoning without sending everything there?

## Chapter hook

Run this short snippet first to anchor **reasoning-system economics** before the book-level sample:

```python
routes = [
    {"name": "single", "cost": 1, "quality": 0.78},
    {"name": "best3", "cost": 3, "quality": 0.86},
    {"name": "verify", "cost": 5, "quality": 0.91},
]
def pick(uncertainty, budget):
    opts = [r for r in routes if r["cost"] <= budget]
    if uncertainty < 0.3:
        return opts[0]
    return max(opts, key=lambda r: r["quality"])
print(pick(0.25, 4))
print(pick(0.8, 4))
```

Predict the printed values, then change one line tied to **test-time compute** or **latency** and observe how the chapter mechanism moves.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/07-planner-verifier.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/07-planner-verifier.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    Only the plan containing every required step in dependency order should pass verification.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **test-time compute** and **latency**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Plot quality and cost for single-pass, best-of-N, and verifier loops.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without test-time compute and record quality, latency, and failure cases.
2. **Mechanism:** Add latency while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when reasoning-system economics earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Spec-driven habit

Every chapter lab pairs reading with **executable acceptance**. Before implementing book 7.6 — reasoning-system economics:

1. Draft cases in `test_lab.py` or `specs/lab-0706.yaml`.
2. Use [Cursor Plan/Agent](https://cursor.com/) with "read spec first, then minimal diff".
3. Or use [OpenSpec](https://openspec.dev/) `/opsx:propose` so requirements live in `openspec/` next to code.

→ [Spec-driven workflow guide](../../getting-started/spec-driven-workflow.md) · [Lab 7.6](../../labs/0706-reasoning-system-economics.md)


## Architecture lens

For a production design in **Reasoning and Tool Use**, make the following explicit for **reasoning-system economics**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns test-time compute versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the cost-quality curves boundary expose? |
| **Evidence** | Which eval slices prove reasoning-system economics meets requirements before and after each release? |
| **Security** | What untrusted data crosses the budgets boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover test-time compute or latency | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | reasoning-system economics is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in budgets without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream test-time compute behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Balance accuracy, latency, token use, parallel candidates, tool calls, caches, failure rates, and task value. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of reasoning-system economics without explicit test-time compute.
- **Today:** Engineering teams implement reasoning-system economics as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but budgets and governance constraints will still require explicit design.
- **What survives:** Spend additional computation only where expected outcome improvement justifies it.

## Knowledge check

1. When is extra test-time compute worth the cost?
2. How do attackers exploit unbounded reasoning loops?
3. What baseline always maximizes quality?

??? question "Answer guidance"
    Q1: When expected value of correctness gain exceeds marginal cost on slice. Q2: Ambiguity triggers repeated tool/model cycles. Q3: Best-of-N plus verifier on every query.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain test-time compute without jargon and give a counterexample.**
       *Proficient answer:* test-time compute spends extra inference—search, sampling, verification—at query time to improve accuracy. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare latency with budgets using quality, cost, latency, and risk.**
       *Proficient answer:* latency is time from request to usable response—dominated by model, retrieval, tools, and serialization; budgets cap tokens, tool calls, wall time, or dollars per task or session. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after latency; authorization before any side effect or retrieval of restricted data; observability at the transition reasoning-system economics introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Spend additional computation only where expected outcome improvement justifies it.

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
