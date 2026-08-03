# Coding Agent Workspace

## Goal

Repo instructions, skills, and review gates for AI coding.

## Overview

Configure a repository for AI-assisted development with explicit agent instructions, reusable skills, CI guardrails, and a code review rubric. The goal is predictable agent behavior that passes the same quality gates as human contributors.

## Architecture

AGENTS.md defines repo conventions, test commands, and forbidden paths. Skills package repeatable workflows as markdown instructions with scoped tools. CI runs lint, tests, and optional agent-eval fixtures. The review rubric scores diffs for correctness, test coverage, scope discipline, and security.

## Prerequisites

Complete the matching [guided book](../books/09-ai-software-and-product-engineering/index.md) and related labs.

## Build phases

### 1. AGENTS.md

**Goal:** Document how agents should navigate and change the repo.

**Steps:**
   - List build/test commands, directory ownership, and formatting rules.
   - Specify files agents must not edit (.env, secrets, generated locks).
   - Define branch naming, commit message format, and PR checklist.
   - Include examples of good vs over-scoped agent diffs.

**Acceptance:**
   - New agent session can run tests using only AGENTS.md instructions.
   - Forbidden paths explicitly listed with rationale.
   - Document updated when repo layout or test entrypoints change.

   **Commands:**

   ```bash
   cat AGENTS.md
   python -m pytest -q  # verify documented test command works
   ```
### 2. Skills

**Goal:** Package repeatable agent workflows as reusable skill files.

**Steps:**
   - Identify frequent tasks: add endpoint, fix CI, write migration.
   - Author SKILL.md per task with steps, constraints, and verification commands.
   - Keep skills focused; split when workflow exceeds one screen.
   - Reference skills from AGENTS.md with trigger phrases.

**Acceptance:**
   - At least three skills cover test-fix, feature-add, and refactor paths.
   - Each skill ends with verification commands and expected outputs.
   - Skills do not duplicate conflicting instructions.

   **Commands:**

   ```bash
   ls .cursor/skills/
   head -40 .cursor/skills/add-api-endpoint/SKILL.md
   ```
### 3. CI checks

**Goal:** Enforce automated quality gates on agent-generated PRs.

**Steps:**
   - Ensure CI runs lint, typecheck, and unit tests on every PR.
   - Add diff size or path allowlist checks for agent branches if needed.
   - Optional: run agent-eval fixtures that simulate common tasks.
   - Fail CI with actionable logs; link fix commands in AGENTS.md.

**Acceptance:**
   - CI green required before merge; no skipped required checks.
   - Failed CI output references local repro command.
   - Agent-eval job completes in under 10 minutes on mock tasks.

   **Commands:**

   ```bash
   python -m pytest -q
   ruff check .
   python scripts/agent_eval_smoke.py
   ```
### 4. Review rubric

**Goal:** Score agent diffs consistently for human or automated review.

**Steps:**
   - Define rubric dimensions: correctness, tests, scope, security, docs.
   - Write scoring guide: what earns pass vs request-changes per dimension.
   - Apply rubric to sample agent PRs and calibrate among reviewers.
   - Publish rubric in docs/review/agent-rubric.md.

**Acceptance:**
   - Rubric used on at least five sample PRs with inter-rater notes.
   - Security dimension catches secrets and missing input validation.
   - Scope dimension flags unrelated file changes.

   **Commands:**

   ```bash
   python scripts/score_pr_rubric.py --diff patches/sample.patch
   ```

## Troubleshooting

- Agent ignores AGENTS.md: shorten file, put test command at top, and reference skills inline.
- CI passes but production breaks: add integration tests and staging deploy step to rubric.
- Skills conflict with cursor rules: reconcile into one authoritative section per topic.
- Over-scoped diffs: add explicit 'minimal diff' rule and CI path filter for sensitive dirs.

## Related patterns

- [Spec Driven Ai Feature](../patterns/spec-driven-ai-feature.md)
- [Observability Traces](../patterns/observability-traces.md)
- [Adversarial Eval Suite](../patterns/adversarial-eval-suite.md)
- [Human Review Queue](../patterns/human-review-queue.md)

## Related labs

- [0903 Ai Native Development Workflow](../labs/0903-ai-native-development-workflow.md)
- [0902 Specification Driven Development](../labs/0902-specification-driven-development.md)
- [0904 Testing Ai Systems](../labs/0904-testing-ai-systems.md)
- [0801 Agent Or Workflow](../labs/0801-agent-or-workflow.md)

## Evidence package

- Short specification with acceptance criteria
- Runnable artifact or architecture diagram
- Evaluation report with slices and failure analysis
- At least one ADR for a major design choice
- Rollback or fallback plan

## Exit criteria

You can demo the system on normal, boundary, and adversarial cases; explain measured trade-offs; and defend why simpler alternatives were insufficient.
