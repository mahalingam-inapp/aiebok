# 7.5 — MCP and Integration Protocols

<p class="study-position" data-course="07-reasoning-and-tool-use" data-lecture="05-mcp-and-integration-protocols.md">Integrations and reasoning cost · Lecture 5 of 6</p>

[← Tools as Capability Boundaries](04-tools-as-capability-boundaries.md) · [Course outline](index.md#course-outline){ .study-overview } · [Reasoning-System Economics →](06-reasoning-system-economics.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Search and planning**

    - [Reasoning as Search](01-reasoning-as-search.md)
    - [Planning](02-planning.md)

    **Verification and tool contracts**

    - [Verification and Critique](03-verification-and-critique.md)
    - [Tools as Capability Boundaries](04-tools-as-capability-boundaries.md)

    **Integrations and reasoning cost**

    - **MCP and Integration Protocols** (current)
    - [Reasoning-System Economics](06-reasoning-system-economics.md)

*Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

[Download the course notebook](../../assets/notebooks/07-reasoning-and-tool-use.ipynb){ download } · Use the exercise under **Lecture 05**.

## Before you begin

- Courses 01 and 04–06 or equivalent experience
- Search and planning
- Typed software interfaces

## Why this chapter exists

Understand clients, servers, tools, resources, prompts, discovery, transport, authentication, and protocol security.

## A discovered tool is still a dependency

A connector’s lookup contract changes and starts returning a nullable address. The workflow used to assume the field was always populated.

Keep a compatibility check at the tool boundary and treat missing data explicitly. A protocol simplifies discovering capabilities, while the application still owns compatibility, permitted usage, and the fallback.

## Learning objectives

- Explain why mcp and integration protocols matters using the chapter scenario, not abstract definitions alone.
- Trace how **MCP** and **resources** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to authentication.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    Protocols standardize capability exchange; they do not remove authorization or trust decisions.

## Mental model

```mermaid
flowchart LR
  N0["Goal"] --> N1["Candidate plans"]
  N1["Candidate plans"] --> N2["Tools"]
  N2["Tools"] --> N3["Observations"]
  N3["Observations"] --> N4["Verifier"]
```

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### MCP

Model Context Protocol standardizes how clients discover tools, resources, and prompts from servers. It reduces bespoke integration code but not trust decisions. See the [MCP concept card](../../concepts/cards/mcp.md).

**Example:** An MCP server exposes filesystem read tools; the client still enforces path allowlists.

**Evidence of understanding:** Connect a hostile client and verify server rejects out-of-scope resource requests.

### Resources

MCP resources expose readable data—files, records, configs—to clients with URI identifiers. Resource access must respect same authorization as APIs. See the [Resources concept card](../../concepts/cards/resources.md).

**Example:** resource://policy/2024 exposes the PDF bytes; listing must not leak unauthorized URIs.

**Evidence of understanding:** Enumerate resources as unprivileged user and confirm restricted URIs are absent.

### Tool Discovery

Tool discovery lets clients list available tools and schemas at runtime instead of hardcoding integrations. Discovery responses must be filtered by permission. See the [Tool Discovery concept card](../../concepts/cards/tool-discovery.md).

**Example:** A client sees only search_docs, not admin_delete, when connected with read-only scope.

**Evidence of understanding:** Compare discovered tool list across role configurations in automated tests.

### Transports

MCP transports—stdio, SSE, HTTP—carry protocol messages between clients and servers. Choice affects latency, deployment, and security boundaries. See the [Transports concept card](../../concepts/cards/transports.md).

**Example:** Stdio suits local IDE agents; SSE suits remote servers behind auth proxies.

**Evidence of understanding:** Measure round-trip latency for tool call over each transport in your deployment.

### Authentication

Authentication verifies identity of users, clients, and services before access to models, tools, or data. It applies equally to MCP sessions, enterprise assistants, and REST APIs. See the [Authentication concept card](../../concepts/cards/authentication.md).

**Example:** OAuth tokens gate MCP server access; SSO identifies employees before internal doc retrieval.

**Evidence of understanding:** Reject unauthenticated requests and verify token expiry across MCP and HTTP entry points.

## Worked example

**Book scenario:** A research workflow must plan, call tools, and reject unsupported conclusions.

**Situation:** Internal tools expose HR policies via MCP; a hostile client attempts discovery of admin-only resources.

**Baseline:** Trust any connected client equally.

**Application:** Implement local MCP server exposing read tools, authenticate clients, validate hostile list-resources requests, log transport errors, deny escalation paths.

**Test cases:** (1) Normal: authorized client lists tools. (2) Boundary: expired token. (3) Adversarial: client requests resource outside declared scope.

**Measurement:** Unauthorized access attempts blocked, discovery latency, audit log completeness.

**Design question:** What does MCP standardize—and what must your org still decide?

## Follow the code

Run this short Python demonstration of **mcp and integration protocols**. Identify the input, the decision or calculation, and the printed result.

```python
CHAPTER = "7.5"
print("chapter hook:", CHAPTER)
CLIENT_SCOPES = {"analyst": ["search_policy"]}
REQUEST = {"client": "analyst", "tool": "admin_delete"}
def authorize(client, tool):
    return tool in CLIENT_SCOPES.get(client, [])
print({"allowed": authorize(REQUEST["client"], REQUEST["tool"])})
print("---")
print("change one input above, predict output, re-run")
```

Predict the result before you run it. Change one input, then explain the resulting difference using the mechanism from the worked example.

For a longer implementation, run the [course code sample](../../code-samples/07-planner-verifier.py). Only the plan containing every required step in dependency order should pass verification.

## Engineering practice

**Build:** Implement a small local MCP server and test a hostile client request.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without mcp and record quality, latency, and failure cases.
2. **Mechanism:** Add resources while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when mcp and integration protocols earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

**Section checkpoint**

List the minimum tool fields and estimate the budget for one verification retry.

Compare your prediction with the chapter demonstration and explain which input changed the result. The [course notebook](../../assets/notebooks/07-reasoning-and-tool-use.ipynb){ download } contains the runnable examples and a checked experiment. See [notebook setup](../../labs/notebooks/index.md) if you are new to Jupyter.

## Spec-driven habit

Every chapter lab pairs reading with **executable acceptance**. Before implementing book 7.5 — mcp and integration protocols:

1. Draft cases in `test_lab.py` or `specs/lab-0705.yaml`.
2. Use [Cursor Plan/Agent](https://cursor.com/) with "read spec first, then minimal diff".
3. Or use [OpenSpec](https://openspec.dev/) `/opsx:propose` so requirements live in `openspec/` next to code.

→ [Spec-driven workflow guide](../../getting-started/spec-driven-workflow.md) · [Lab 7.5](../../labs/0705-mcp-and-integration-protocols.md)


## Architecture lens

For a production design in **Reasoning and Tool Use**, make the following explicit for **mcp and integration protocols**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns mcp versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the tool discovery boundary expose? |
| **Evidence** | Which eval slices prove mcp and integration protocols meets requirements before and after each release? |
| **Security** | What untrusted data crosses the authentication boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover mcp or resources | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | mcp and integration protocols is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in authentication without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream mcp behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Understand clients, servers, tools, resources, prompts, discovery, transport, authentication, and protocol security. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of mcp and integration protocols without explicit mcp.
- **Today:** Engineering teams implement mcp and integration protocols as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but authentication and governance constraints will still require explicit design.
- **What survives:** Protocols standardize capability exchange; they do not remove authorization or trust decisions.

## Knowledge check

1. What does MCP standardize versus leave to implementers?
2. How is tool discovery different from authorization?
3. What integration baseline has no auth on local tools?

??? question "Answer guidance"
    Q1: Capability advertisement and transport—not trust decisions. Q2: Discovery lists possibilities; auth gates each call. Q3: Open localhost port executing any JSON command.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain MCP without jargon and give a counterexample.**
       *Proficient answer:* model context protocol standardizes how clients discover tools, resources, and prompts from servers. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare resources with authentication using quality, cost, latency, and risk.**
       *Proficient answer:* mcp resources expose readable data—files, records, configs—to clients with uri identifiers; authentication verifies identity of users, clients, and services before access to models, tools, or data. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after resources; authorization before any side effect or retrieval of restricted data; observability at the transition mcp and integration protocols introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Protocols standardize capability exchange; they do not remove authorization or trust decisions.

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

## Continue

[← Tools as Capability Boundaries](04-tools-as-capability-boundaries.md) · [Course outline](index.md#course-outline){ .study-overview } · [Reasoning-System Economics →](06-reasoning-system-economics.md)
{: .study-directions .study-directions--footer }
