# Bounded Agent Assistant

## Goal

Multi-step agent with typed tools, checkpoints, and approval.

## Overview

Implement a multi-step assistant that plans, calls typed tools, and pauses for human approval on sensitive actions. Checkpoints make runs resumable and eval traces make behavior auditable.

## Architecture

The agent runtime is a finite state machine: plan, act, observe, approve, complete. Tools expose JSON Schema contracts and run in a sandbox with explicit timeouts. Checkpoints persist state to durable storage after each tool call. A separate approval service gates destructive or high-cost actions before execution resumes.

## Prerequisites

Complete the matching [guided book](../books/08-agent-systems/index.md) and related labs.

## Build phases

### 1. State machine

**Goal:** Define explicit agent states and transitions with no hidden loops.

**Steps:**
   - Model states: idle, planning, awaiting_tool, awaiting_approval, completed, failed.
   - Implement transition guards: max steps, max tool calls, budget exhaustion.
   - Emit structured events on every transition for trace reconstruction.
   - Add a cancel path that cleanly terminates in-flight tool calls.

**Acceptance:**
   - Every run ends in a terminal state within the configured step budget.
   - Transition log replay reconstructs the full run without re-invoking tools.
   - Cancel from any non-terminal state within 2 seconds.

   **Commands:**

   ```bash
   python agent/fsm.py --demo --max-steps 10
   python -m pytest tests/test_agent_fsm.py -q
   ```
### 2. Tool schemas

**Goal:** Register tools with typed inputs, outputs, and capability tags.

**Steps:**
   - Define JSON Schema for each tool's arguments and return type.
   - Tag tools with capability labels: read, write, external, destructive.
   - Implement a tool registry that validates args before dispatch.
   - Add mock implementations for local development without external APIs.

**Acceptance:**
   - Invalid tool args rejected before dispatch with schema error details.
   - Registry lists capability tags consumable by the approval policy.
   - Mock tools return deterministic fixtures for eval replay.

   **Commands:**

   ```bash
   python tools/validate_schema.py --tool search_docs --args '{"query": "test"}'
   python agent/run.py --tools mock --goal "summarize open tickets"
   ```
### 3. Human approval

**Goal:** Pause destructive or ambiguous actions until a human approves.

**Steps:**
   - Define approval rules keyed on capability tags and estimated cost.
   - Serialize pending action payload for reviewer UI or CLI prompt.
   - Implement approve/reject/edit paths that resume or replan the run.
   - Log approver identity, timestamp, and decision rationale.

**Acceptance:**
   - Write-capable tools never execute without an approval record.
   - Rejected actions trigger replan without corrupting checkpoint state.
   - Approval timeout defaults to safe abort, not auto-approve.

   **Commands:**

   ```bash
   python agent/run.py --require-approval --goal "delete temp files"
   python approval/cli.py --pending runs/latest/pending.json
   ```
### 4. Checkpoint store

**Goal:** Persist resumable state after each tool observation.

**Steps:**
   - Design checkpoint schema: run_id, step, messages, tool_results, pending_action.
   - Write checkpoints to SQLite or local JSON with atomic rename.
   - Implement resume-from-checkpoint that skips completed tool calls.
   - Add retention policy and purge for completed runs older than N days.

**Acceptance:**
   - Killing the process mid-run and resuming produces identical final output.
   - Checkpoint size bounded; large tool outputs stored by reference.
   - No duplicate tool side effects on resume.

   **Commands:**

   ```bash
   python agent/run.py --checkpoint-dir tmp/checkpoints --goal "file inventory"
   python agent/resume.py --run-id abc123
   ```
### 5. Eval traces

**Goal:** Score agent runs on task success, tool discipline, and safety.

**Steps:**
   - Record full traces: states, tool calls, approvals, final outcome.
   - Build eval cases with expected tool sequences and forbidden actions.
   - Score success rate, unnecessary tool calls, and approval bypass attempts.
   - Integrate trace eval into CI with regression thresholds.

**Acceptance:**
   - Eval suite covers happy path, approval-required, and budget-exceeded cases.
   - Trace diff highlights tool sequence changes between agent versions.
   - CI fails on approval-bypass or destructive-action-without-approval.

   **Commands:**

   ```bash
   python eval/agent_traces.py --cases tests/agent_cases.jsonl --out reports/traces.json
   python eval/score_traces.py --report reports/traces.json --min-success 0.85
   ```

## Troubleshooting

- Agent loops on the same tool: tighten transition guards and add duplicate-call detection in the FSM.
- Checkpoint resume duplicates side effects: store tool call ids and skip already-completed calls.
- Approval stalls block UX: set timeouts, surface pending actions in a queue, and allow delegated approvers.
- Eval traces too large: store tool outputs by reference and truncate observation payloads in logs.

## Related patterns

- [Planner Executor](../patterns/planner-executor.md)
- [Human Approval Gate](../patterns/human-approval-gate.md)
- [Durable Checkpoint](../patterns/durable-checkpoint.md)
- [Tool Sandbox](../patterns/tool-sandbox.md)
- [Observability Traces](../patterns/observability-traces.md)

## Related labs

- [0802 The Agent Loop](../labs/0802-the-agent-loop.md)
- [0803 Agent Memory And Recovery](../labs/0803-agent-memory-and-recovery.md)
- [0804 Agent Patterns](../labs/0804-agent-patterns.md)
- [0704 Tools As Capability Boundaries](../labs/0704-tools-as-capability-boundaries.md)

## Evidence package

- Short specification with acceptance criteria
- Runnable artifact or architecture diagram
- Evaluation report with slices and failure analysis
- At least one ADR for a major design choice
- Rollback or fallback plan

## Exit criteria

You can demo the system on normal, boundary, and adversarial cases; explain measured trade-offs; and defend why simpler alternatives were insufficient.
