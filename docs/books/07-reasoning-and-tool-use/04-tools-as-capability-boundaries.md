# 7.4 — Tools as Capability Boundaries

*Book 7: Reasoning and Tool Use · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- Books 1 and 4–6
- Search and planning
- Typed software interfaces

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Design typed tools, schemas, descriptions, errors, timeouts, idempotency, permissions, and audit records.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain why tools as capability boundaries matters using the chapter scenario, not abstract definitions alone.
- Trace how **function calling** and **tool schemas** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to permissions.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    Probabilistic intent must cross a deterministic, authorized boundary before effects occur.

## Mental model

```mermaid
flowchart LR
  N0["Goal"] --> N1["Candidate plans"]
  N1["Candidate plans"] --> N2["Tools"]
  N2["Tools"] --> N3["Observations"]
  N3["Observations"] --> N4["Verifier"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **tools as capability boundaries** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### Function Calling

Function calling lets models emit structured invocations with typed arguments that runtime code validates and executes. See the [Function Calling concept card](../../concepts/cards/function-calling.md).

**Example:** Searching internal docs via a read-only tool returns live titles instead of hallucinated links.

**Evidence of understanding:** Fuzz tool arguments and confirm unauthorized calls fail before side effects.

### Tool Schemas

Tool schemas define parameter names, types, required fields, and descriptions models use to construct calls. Ambiguous schemas cause systematic argument errors. See the [Tool Schemas concept card](../../concepts/cards/tool-schemas.md).

**Example:** date_iso string format in schema prevents models passing 'next Tuesday' unparseably.

**Evidence of understanding:** Measure argument validation failure rate per tool after schema revision.

### Idempotency

Idempotent tools produce the same effect when called repeatedly with the same idempotency key. Agents retry safely only when tools support this. See the [Idempotency concept card](../../concepts/cards/idempotency.md).

**Example:** create_ticket with idempotency key 'abc' must not spawn duplicate tickets on retry.

**Evidence of understanding:** Call the same tool twice with identical keys and verify single side effect.

### Timeouts

Timeouts cap how long tools or model calls may run before cancellation. They prevent hung workflows from blocking resources indefinitely. See the [Timeouts concept card](../../concepts/cards/timeouts.md).

**Example:** A 30-second web search timeout returns partial results instead of freezing the agent.

**Evidence of understanding:** Inject slow tool responses and verify cancellation within configured timeout ± slack.

### Permissions

Permissions bind tools and data access to authenticated identities and roles. Models must not bypass authorization by guessing URLs or parameters. See the [Permissions concept card](../../concepts/cards/permissions.md).

**Example:** delete_user tool requires admin role verified server-side, not in the prompt.

**Evidence of understanding:** Attempt privileged tool calls as low-privilege identity and expect denial.

## Worked example

**Book scenario:** A research workflow must plan, call tools, and reject unsupported conclusions.

**Situation:** The research assistant calls external APIs; probabilistic tool arguments must not cause unauthorized writes.

**Baseline:** Pass raw model JSON directly to HTTP client.

**Application:** Wrap read-only search API as typed tool with schema, timeouts, idempotency keys, permission checks, structured errors returned to model.

**Test cases:** (1) Normal: valid query string. (2) Boundary: empty query rejected. (3) Adversarial: fuzz malformed types and oversized payloads.

**Measurement:** Schema rejection rate, timeout compliance, zero unauthorized mutations in red-team set.

**Design question:** Where exactly does probabilistic intent cross into deterministic execution?

## Chapter hook

Run this short snippet first to anchor **tools as capability boundaries** before the book-level sample:

```python
def search_tool(query: str) -> dict:
    if not isinstance(query, str) or not query.strip():
        raise ValueError("query required")
    if len(query) > 200:
        raise ValueError("query too long")
    return {"results": [f"hit for {query!r}"]}
for q in ["budget policy", "", 123]:
    try:
        print(search_tool(q) if isinstance(q, str) else search_tool(str(q)))
    except ValueError as e:
        print({"error": str(e)})
```

Predict the printed values, then change one line tied to **function calling** or **tool schemas** and observe how the chapter mechanism moves.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/07-planner-verifier.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/07-planner-verifier.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    Only the plan containing every required step in dependency order should pass verification.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **function calling** and **tool schemas**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Wrap a read-only API as a typed tool and fuzz its arguments.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without function calling and record quality, latency, and failure cases.
2. **Mechanism:** Add tool schemas while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when tools as capability boundaries earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Architecture lens

For a production design in **Reasoning and Tool Use**, make the following explicit for **tools as capability boundaries**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns function calling versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the idempotency boundary expose? |
| **Evidence** | Which eval slices prove tools as capability boundaries meets requirements before and after each release? |
| **Security** | What untrusted data crosses the permissions boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover function calling or tool schemas | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | tools as capability boundaries is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in permissions without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream function calling behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Design typed tools, schemas, descriptions, errors, timeouts, idempotency, permissions, and audit records. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of tools as capability boundaries without explicit function calling.
- **Today:** Engineering teams implement tools as capability boundaries as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but permissions and governance constraints will still require explicit design.
- **What survives:** Probabilistic intent must cross a deterministic, authorized boundary before effects occur.

## Knowledge check

1. Why are typed tool boundaries required?
2. How do timeouts protect the agent loop?
3. What baseline calls APIs with unvalidated model output?

??? question "Answer guidance"
    Q1: Effects need authorization and schema enforcement. Q2: Hung tools exhaust step budget. Q3: Direct exec of model-produced shell/HTTP.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain function calling without jargon and give a counterexample.**
       *Proficient answer:* function calling lets models emit structured invocations with typed arguments that runtime code validates and executes. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare tool schemas with permissions using quality, cost, latency, and risk.**
       *Proficient answer:* tool schemas define parameter names, types, required fields, and descriptions models use to construct calls; permissions bind tools and data access to authenticated identities and roles. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after tool schemas; authorization before any side effect or retrieval of restricted data; observability at the transition tools as capability boundaries introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Probabilistic intent must cross a deterministic, authorized boundary before effects occur.

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
