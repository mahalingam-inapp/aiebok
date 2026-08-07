# 13.4 — Computer Use and Embodied Action

*Book 13: Multimodal and Frontier Systems · Read 25 min · Worked example 20 min · Code/design practice 45–60 min · Review 10 min*

## Before you begin

- Books 3–12 as relevant
- Evidence-oriented research reading
- Risk awareness

If a prerequisite is unfamiliar, use site search and read only enough to explain it and complete a small example. Do not block progress by mastering every upstream topic first.

## Why this chapter exists

Model perception–action loops, UI grounding, coordinate and semantic actions, recovery, permissions, and physical-world constraints.

The engineering objective is not to memorize vocabulary. By the end, you should be able to describe the mechanism, build or inspect a small implementation, recognize its failure modes, and decide where it belongs in a larger system.

## Learning objectives

- Explain why computer use and embodied action matters using the chapter scenario, not abstract definitions alone.
- Trace how **computer use** and **visual grounding** interact in the book-level visual.
- Implement or design the bounded practice while holding evaluation cases fixed.
- Diagnose at least two failure modes specific to robotics interfaces.
- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.

!!! note "Enduring principle"
    Acting through interfaces adds uncertainty and irreversible side effects to ordinary agent loops.

## Mental model

```mermaid
flowchart LR
  N0["Multimodal input"] --> N1["Representation"]
  N1["Representation"] --> N2["Fusion or action"]
  N2["Fusion or action"] --> N3["Provenance"]
  N3["Provenance"] --> N4["Evaluation"]
```

Read the visual from left to right, then trace failures from right to left. The diagram is a book-level map; this chapter explains how **computer use and embodied action** changes one or more transitions.

## Core concepts

The concepts form a system, not a vocabulary list. Read each section below before attempting the practice exercise.

### Computer Use

Computer use agents perceive screens and emit mouse/keyboard actions to complete software tasks. See the [Computer Use concept card](../../concepts/cards/computer-use.md).

**Example:** Agent fills expense form in internal web app from receipt image with confirmation gates.

**Evidence of understanding:** Task success rate on sandboxed UI benchmark with zero unauthorized actions.

### Visual Grounding

Visual grounding links language to regions or objects in images—pointing, bounding boxes, UI elements. See the [Visual Grounding concept card](../../concepts/cards/visual-grounding.md).

**Example:** Model clicks 'Submit' button coordinates in screenshot for computer-use agent.

**Evidence of understanding:** Measure grounding accuracy IoU on labeled UI element dataset.

### Action Spaces

Action spaces define allowed agent operations—click, type, scroll, API call—with granularity affecting reliability. See the [Action Spaces concept card](../../concepts/cards/action-spaces.md).

**Example:** Semantic actions ('open_settings') beat raw coordinates when UI reskins change layout.

**Evidence of understanding:** Compare success rate semantic versus coordinate actions after UI theme change.

### Recovery

Recovery restores consistent state after crashes, tool failures, or partial commits. It requires durable checkpoints and compensating actions. See the [Recovery concept card](../../concepts/cards/recovery.md).

**Example:** After payment timeout, recovery verifies ledger state before retry or refund.

**Evidence of understanding:** Inject crash at each step and verify recovery reaches consistent terminal state.

### Robotics Interfaces

Robotics interfaces connect AI planners to sensors and actuators with safety interlocks and real-time constraints. See the [Robotics Interfaces concept card](../../concepts/cards/robotics-interfaces.md).

**Example:** Warehouse robot API accepts move commands only within geofenced zones with E-stop.

**Evidence of understanding:** Simulate estop latency and command rejection outside safety envelope.

## Worked example

**Book scenario:** A document system must combine tables, charts, and text without losing source provenance.

**Situation:** Prototype automates browser-based benefits enrollment; wrong click is hard to reverse.

**Baseline:** Agent clicks immediately from model coordinates—misclicks enroll wrong plan.

**Application:** Design computer-use loop with UI grounding, semantic action targets (button labels not raw x,y), confirmation for irreversible steps, recovery path on layout change.

**Test cases:** (1) Normal: stable form fill. (2) Boundary: dynamic DOM reload mid-task. (3) Adversarial: deceptive button labels ("No" means confirm).

**Measurement:** Task success, misclick rate, recovery success, human confirmation bypass attempts.

**Design question:** When are coordinate actions unacceptable compared to semantic targeting?

## Chapter hook

Run this short snippet first to anchor **computer use and embodied action** before the book-level sample:

```python
CHAPTER = "13.4"
print("chapter hook:", CHAPTER)
actions = [
    {"type": "click_semantic", "target": "Submit enrollment", "risk": "high"},
    {"type": "click_xy", "x": 120, "y": 400, "risk": "high"},
]
for a in actions:
    needs_confirm = a["risk"] == "high"
    print(a["type"], "confirm:", needs_confirm)
print("---")
print("change one input above, predict output, re-run")
```

Predict the printed values, then change one line tied to **computer use** or **visual grounding** and observe how the chapter mechanism moves.

## Runnable code sample

The following dependency-free sample supports this book. Download it from the [code-sample library](../../code-samples/13-multimodal-provenance.py) or run the matching file under `examples/`.

```python
--8<-- "docs/code-samples/13-multimodal-provenance.py"
```

Expected output is printed to the terminal. Before running it, predict which values or decisions should change. Then introduce one failure and convert the observation into a test.

??? success "Expected observation"
    Only evidence above the confidence threshold is emitted, and every output retains source, page, and modality.

This is a **book-level sample**. Its relevance to this chapter is the boundary between **computer use** and **visual grounding**. Modify that boundary, not unrelated lines, when completing the chapter exercise.

## Engineering practice

**Build:** Design a safe browser task with confirmation and recovery.

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without computer use and record quality, latency, and failure cases.
2. **Mechanism:** Add visual grounding while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when computer use and embodied action earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran.

## Spec-driven habit

Every chapter lab pairs reading with **executable acceptance**. Before implementing book 13.4 — computer use and embodied action:

1. Draft cases in `test_lab.py` or `specs/lab-1304.yaml`.
2. Use [Cursor Plan/Agent](https://cursor.com/) with "read spec first, then minimal diff".
3. Or use [OpenSpec](https://openspec.dev/) `/opsx:propose` so requirements live in `openspec/` next to code.

→ [Spec-driven workflow guide](../../getting-started/spec-driven-workflow.md) · [Lab 13.4](../../labs/1304-computer-use-and-embodied-action.md)


## Architecture lens

For a production design in **Multimodal and Frontier Systems**, make the following explicit for **computer use and embodied action**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns computer use versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the action spaces boundary expose? |
| **Evidence** | Which eval slices prove computer use and embodied action meets requirements before and after each release? |
| **Security** | What untrusted data crosses the robotics interfaces boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |

## Failure clinic

Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover computer use or visual grounding | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | computer use and embodied action is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in robotics interfaces without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream computer use behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

Model perception–action loops, UI grounding, coordinate and semantic actions, recovery, permissions, and physical-world constraints. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions.

## Evolution lens

- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of computer use and embodied action without explicit computer use.
- **Today:** Engineering teams implement computer use and embodied action as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but robotics interfaces and governance constraints will still require explicit design.
- **What survives:** Acting through interfaces adds uncertainty and irreversible side effects to ordinary agent loops.

## Knowledge check

1. Why do interface actions add irreversible risk?
2. How does recovery work when UI layout shifts?
3. What computer-use baseline clicks without confirmation?

??? question "Answer guidance"
    Q1: UI actions change real account state. Q2: Re-ground elements, rewind to last checkpoint. Q3: Raw coordinate agent on production HR portal.

## Mastery questions

??? tip "Model answers (proficient level)"
        1. **Explain computer use without jargon and give a counterexample.**
       *Proficient answer:* computer use agents perceive screens and emit mouse/keyboard actions to complete software tasks. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.
    2. **Compare visual grounding with robotics interfaces using quality, cost, latency, and risk.**
       *Proficient answer:* visual grounding links language to regions or objects in images—pointing, bounding boxes, ui elements; robotics interfaces connect ai planners to sensors and actuators with safety interlocks and real-time constraints. Trade quality gains against operational and security cost on the chapter scenario.
    3. **Design a minimal experiment that tests the chapter's central claim.**
       *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.
    4. **Identify which component should own validation, authorization, and observability.**
       *Proficient answer:* Validation belongs at the typed boundary after visual grounding; authorization before any side effect or retrieval of restricted data; observability at the transition computer use and embodied action introduces in the book visual.
    5. **State what would remain true if today's leading libraries and vendors disappeared.**
       *Proficient answer:* Acting through interfaces adds uncertainty and irreversible side effects to ordinary agent loops.

## Self-assessment rubric

| Level | Evidence |
|---|---|
| Not yet | Can repeat terms but cannot trace the visual or predict the sample. |
| Developing | Can explain the mechanism and complete the normal case with help. |
| Proficient | Can implement the exercise, diagnose a failure, and compare a baseline. |
| Transfer | Can defend an architecture choice in a new domain with evaluation evidence. |

## Evidence and further study

- Primary papers for the selected modality or frontier claim
- Model and dataset cards for every reproduced system

Use primary sources for technical claims and official documentation for current product behavior. Record the version or access date for evolving material.

## Continue

Return to the [book index](index.md) or use site search to follow the chapter's concepts into the knowledge-area and reference pages.
