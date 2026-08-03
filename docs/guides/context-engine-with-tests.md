# Context Engine With Tests

## Goal

Versioned prompts, memory policy, token budgets, regression tests.

## Overview

Build a versioned context assembly layer that packs prompts, memory, and retrieved sections under explicit token budgets. Regression tests lock behavior so prompt or policy changes do not silently shift outputs.

## Architecture

The context engine sits between upstream data sources and the model gateway. It loads prompt templates by version, applies section-specific budgets, and emits a deterministic context bundle. Memory policy decides what persists across turns. A fixture-based eval dataset compares assembled contexts and downstream outputs before merge.

## Prerequisites

Complete the matching [guided book](../books/05-prompt-and-context-engineering/index.md) and related labs.

## Build phases

### 1. Context builder

**Goal:** Assemble multi-section prompts from templates and dynamic inputs.

**Steps:**
   - Define section types: system, instructions, memory, retrieval, user.
   - Implement a builder that merges sections in fixed priority order.
   - Support variable substitution with explicit missing-key errors.
   - Serialize output as messages[] plus metadata (versions, token estimate).

**Acceptance:**
   - Same inputs and versions produce byte-identical context bundles.
   - Missing required variables fail fast with section name in error.
   - Builder unit tests cover all section types and edge cases.

   **Commands:**

   ```bash
   python context/build.py --template prompts/v1.yaml --vars vars.json --out ctx.json
   python -m pytest tests/test_context_builder.py -q
   ```
### 2. Section budgets

**Goal:** Enforce per-section and total token limits with graceful truncation.

**Steps:**
   - Assign max tokens per section based on task priority.
   - Implement truncation strategies: tail-keep for memory, head-keep for retrieval.
   - Reserve headroom for model completion tokens in total budget math.
   - Log which sections were truncated and by how many tokens.

**Acceptance:**
   - Assembled context never exceeds configured total token budget.
   - Truncation order respects priority: system > instructions > retrieval > memory.
   - Truncation metadata present in output for debugging.

   **Commands:**

   ```bash
   python context/build.py --budget 4096 --vars vars.json | python context/token_report.py
   python eval/budget_cases.py --suite tests/budget_overflow.jsonl
   ```
### 3. Prompt versions

**Goal:** Pin and migrate prompt templates without breaking callers.

**Steps:**
   - Store templates in versioned files: prompts/{name}/v{semver}.yaml.
   - Expose a version resolver: explicit pin, latest stable, or canary tag.
   - Document changelog entries when template semantics change.
   - Add compatibility tests that old pinned versions still parse.

**Acceptance:**
   - Callers can pin prompt_version and get stable behavior across deploys.
   - Canary tag routes a configurable fraction of traffic to draft templates.
   - Breaking template changes require a major version bump in changelog.

   **Commands:**

   ```bash
   python prompts/list_versions.py --name support_assistant
   python context/build.py --template support_assistant --version 2.1.0
   ```
### 4. Eval dataset

**Goal:** Regression-test context assembly and downstream behavior.

**Steps:**
   - Curate cases: input vars, expected section presence, forbidden content.
   - Snapshot assembled contexts; diff on CI when builder logic changes.
   - Add optional model-in-the-loop checks with a local mock LLM.
   - Tag cases by slice: language, domain, long-context, adversarial injection.

**Acceptance:**
   - CI fails when context snapshot diff exceeds approved baseline.
   - At least 20 cases covering truncation, missing vars, and injection attempts.
   - Slice report shows no regression on critical tags.

   **Commands:**

   ```bash
   python eval/context_regression.py --update-snapshots
   python eval/context_regression.py --check
   python -m pytest tests/test_context_eval.py -q
   ```

## Troubleshooting

- Token counts drift from provider: reconcile with the same tokenizer the gateway uses and add a calibration offset.
- Snapshots churn on ordering: sort retrieval sections by score and stabilize tie-breaking.
- Memory bloat evicts retrieval: lower memory budget or summarize older turns before assembly.
- Injection in user content reaches system section: sanitize or delimit untrusted sections explicitly.

## Related patterns

- [Context Budget Packing](../patterns/context-budget-packing.md)
- [Prompt Versioning](../patterns/prompt-versioning.md)
- [Context Compressor](../patterns/context-compressor.md)
- [Offline Eval Regression](../patterns/offline-eval-regression.md)

## Related labs

- [0503 Context Construction](../labs/0503-context-construction.md)
- [0504 Conversation And Memory](../labs/0504-conversation-and-memory.md)
- [0506 Prompt And Context Operations](../labs/0506-prompt-and-context-operations.md)
- [0505 Context Failure And Security](../labs/0505-context-failure-and-security.md)

## Evidence package

- Short specification with acceptance criteria
- Runnable artifact or architecture diagram
- Evaluation report with slices and failure analysis
- At least one ADR for a major design choice
- Rollback or fallback plan

## Exit criteria

You can demo the system on normal, boundary, and adversarial cases; explain measured trade-offs; and defend why simpler alternatives were insufficient.
