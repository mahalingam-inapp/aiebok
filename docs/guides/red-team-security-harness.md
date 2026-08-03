# Red-Team Security Harness

## Goal

Prompt injection and tool abuse tests in CI.

## Overview

Automate prompt injection, tool abuse, and data exfiltration tests in CI. Pair attack cases with mitigations and an incident runbook so failures are detected before attackers find them.

## Architecture

The harness loads an attack set categorized by technique: direct injection, indirect injection via retrieved content, tool parameter abuse, and jailbreak variants. Tests run against the full stack with mitigations enabled. Failures map to mitigation controls and runbook steps. Reports feed security review gates.

## Prerequisites

Complete the matching [guided book](../books/10-evaluation-safety-and-governance/index.md) and related labs.

## Build phases

### 1. Attack set

**Goal:** Catalog realistic attacks aligned to system boundaries.

**Steps:**
   - Collect attacks per surface: user input, retrieved docs, tool args, system prompts.
   - Tag cases: severity, expected behavior (block, sanitize, abstain).
   - Include variants from public benchmarks adapted to your domain.
   - Version attack set; review additions like production incident cases.

**Acceptance:**
   - At least 40 cases covering all exposed surfaces.
   - Each case documents expected safe behavior, not just 'should not crash'.
   - Attack set checksum pinned in CI config.

   **Commands:**

   ```bash
   python security/validate_attacks.py --path data/attacks.jsonl
   python security/run_redteam.py --suite data/attacks.jsonl --out reports/redteam.json
   ```
### 2. Mitigations

**Goal:** Implement and test controls for each attack category.

**Steps:**
   - Map attacks to controls: input delimiters, retrieval sanitization, tool allowlists.
   - Implement policy checks before model and tool execution.
   - Verify mitigations with targeted unit tests per control.
   - Document residual risk where mitigations are partial.

**Acceptance:**
   - Every P0 attack category has at least one enforced mitigation.
   - Mitigation bypass attempts fail closed in harness runs.
   - Control mapping published in security/architecture.md.

   **Commands:**

   ```bash
   python -m pytest tests/test_injection_guard.py -q
   python security/run_redteam.py --suite data/attacks.jsonl --mitigations on
   ```
### 3. Incident runbook

**Goal:** Prepare response steps when red-team or live incidents occur.

**Steps:**
   - Define severity levels and on-call escalation paths.
   - Write runbook: isolate feature flag, preserve logs, notify stakeholders.
   - Include template comms and post-incident eval additions.
   - Run tabletop exercise against a simulated harness failure.

**Acceptance:**
   - Runbook executable in dry-run: flag off, logs captured, ticket filed.
   - Post-incident step adds failing case to attack set.
   - Tabletop completed with timed actions under 30 minutes.

   **Commands:**

   ```bash
   python security/tabletop.py --scenario injection_bypass --dry-run
   python deploy/feature_flag.py --disable risky-tool --dry-run
   ```

## Troubleshooting

- Harness passes but manual jailbreaks succeed: expand attack set with compositional and multilingual cases.
- Mitigation breaks UX: tune sanitize vs block thresholds per surface.
- Flaky tool-abuse tests: mock tools in CI; run full-stack red-team nightly.
- Runbook stale after refactor: link runbook controls to harness case ids for auto-reminders.

## Related patterns

- [Prompt Injection Guard](../patterns/prompt-injection-guard.md)
- [Tool Sandbox](../patterns/tool-sandbox.md)
- [Adversarial Eval Suite](../patterns/adversarial-eval-suite.md)
- [Human Approval Gate](../patterns/human-approval-gate.md)

## Related labs

- [1004 Security Of Ai Systems](../labs/1004-security-of-ai-systems.md)
- [0505 Context Failure And Security](../labs/0505-context-failure-and-security.md)
- [0704 Tools As Capability Boundaries](../labs/0704-tools-as-capability-boundaries.md)
- [1005 Responsible Ai And Risk](../labs/1005-responsible-ai-and-risk.md)

## Evidence package

- Short specification with acceptance criteria
- Runnable artifact or architecture diagram
- Evaluation report with slices and failure analysis
- At least one ADR for a major design choice
- Rollback or fallback plan

## Exit criteria

You can demo the system on normal, boundary, and adversarial cases; explain measured trade-offs; and defend why simpler alternatives were insufficient.
