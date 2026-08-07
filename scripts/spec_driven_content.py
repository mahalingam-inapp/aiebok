"""Reusable spec-driven development snippets for books, labs, guides, and notebooks."""
from __future__ import annotations

import re

WORKFLOW_PAGE = "getting-started/spec-driven-workflow.md"


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def _lab_slug(book_no: int, chapter_no: int, title: str) -> str:
    return f"{book_no:02d}{chapter_no:02d}-{_slug(title)}"[:48].strip("-")


def _lab_acceptance_hint(book_no: int, chapter_no: int, title: str, practice: str) -> str:
    spec_name = f"lab-{book_no:02d}{chapter_no:02d}"
    return (
        f"Before changing `main.py`, write **three acceptance cases** for *{title}* "
        f"(normal, boundary, adversarial) in `specs/{spec_name}.yaml` or as pytest cases in `test_lab.py`. "
        f"Goal: {practice.rstrip('.')}."
    )


def render_lab_spec_section(
    book_no: int,
    chapter_no: int,
    title: str,
    practice: str,
    *,
    extended: bool = False,
    for_docs: bool = False,
) -> str:
    hint = _lab_acceptance_hint(book_no, chapter_no, title, practice)
    guide_link = (
        "../getting-started/spec-driven-workflow.md"
        if for_docs
        else "../../docs/getting-started/spec-driven-workflow.md"
    )
    body = f"""## Spec-driven habit (every lab)

Specification-driven development means **executable acceptance before implementation**—the same discipline whether you use [OpenSpec](https://openspec.dev/) in the repo or [Cursor](https://cursor.com/) in the editor.

1. **Write cases first** — {hint}
2. **Review the spec** — share `specs/` or your test list with a teammate or agent *before* large diffs.
3. **Implement to green** — run `python main.py` and `pytest test_lab.py -q`; spec failures block "done".

### Cursor (editor workflow)

```bash
# From repo root — open the lab folder with spec context
cursor labs/{book_no:02d}{chapter_no:02d}-*/
```

In Cursor **Agent** or **Plan** mode, paste a spec-first prompt:

```text
Read specs/lab-{book_no:02d}{chapter_no:02d}.yaml (or test_lab.py cases).
Do not change main.py until we agree the acceptance cases cover normal, boundary, and adversarial inputs.
Then implement the smallest diff that makes pytest pass.
```

Optional project rules (`.cursor/rules/spec-driven-labs.mdc`):

```markdown
---
description: Spec-first lab workflow
globs: labs/**
---
- Read acceptance cases before editing main.py
- Add a failing test before fixing behavior
- Run: python -m pytest test_lab.py -q
```

### OpenSpec (repo workflow)

```bash
npm install -g @fission-ai/openspec@latest   # Node 20.19+
cd your-project
openspec init                              # creates openspec/specs/ + openspec/changes/
```

Propose a lab-scoped change (names vary slightly by assistant profile):

```text
/opsx:propose Add acceptance spec for lab {book_no}.{chapter_no} — {title}
```

Typical artifacts under `openspec/changes/<change-id>/`:

```text
proposal.md    # intent and scope
tasks.md       # checkbox implementation list
specs/         # ADDED/MODIFIED requirements (delta specs)
design.md      # optional technical notes
```

Apply after review:

```text
/opsx:apply
python -m pytest labs/{book_no:02d}{chapter_no:02d}-*/test_lab.py -q
/opsx:archive
```

See the full [spec-driven workflow guide]({guide_link}) for copy-paste templates.
"""
    if extended:
        body += """
### Lab 9.2 — executable contract sample

This lab is the canonical spec-driven exercise. Keep acceptance cases in version control:

```yaml
# specs/lab-0902-acceptance.yaml
cases:
  - input: "grant admin access"
    expect_contains: "require approval"
  - input: "unknown policy"
    expect_contains: "abstain"
```

```bash
python labs/0902-specification-driven-development/main.py
python -m pytest labs/0902-specification-driven-development/test_lab.py -q
openspec validate   # when openspec/ is initialized
```
"""
    return body


def render_starter_spec_section(slug: str, title: str, objective: str) -> str:
    return f"""## Spec-driven habit (every lab)

Treat **{title}** like a mini feature: write what "done" means before you tune code.

1. Add 2–3 acceptance rows to `specs/{slug}.yaml` (normal / boundary / adversarial) matching the objective: *{objective.rstrip('.')}*.
2. In **Cursor**, open `labs/{slug}/` and ask the agent to read your spec before editing `main.py`.
3. With **OpenSpec**, run `/opsx:propose` for a change named `{slug}-acceptance` and link `tasks.md` to your pytest file.

```bash
cursor labs/{slug}/
python main.py && python -m pytest test_lab.py -q
```

Full tooling walkthrough: [spec-driven workflow](../../docs/getting-started/spec-driven-workflow.md).
"""


def render_notebook_spec_cell(slug: str, title: str) -> str:
    return f"""## Spec-first checkpoint

Before the coding cells below, list acceptance cases for **{title}** (`labs/{slug}/`):

| Case | Input / setup | Expected outcome |
|---|---|---|
| Normal | … | … |
| Boundary | … | … |
| Adversarial | … | … |

**Cursor:** `@specs/{slug}.yaml` or paste the table into Plan mode.  
**OpenSpec:** `/opsx:propose` → review `proposal.md` + delta specs → `/opsx:apply` after approval.

Sync passing code into `main.py` before running pytest.
"""


def render_chapter_spec_section(book_no: int, chapter_no: int, title: str) -> str:
    if book_no == 9 and chapter_no == 2:
        return render_book9_spec_chapter_extra()
    practice_hint = f"Book {book_no}.{chapter_no} — {title}"
    ls = _lab_slug(book_no, chapter_no, title)
    return f"""## Spec-driven habit

Every chapter lab pairs reading with **executable acceptance**. Before implementing {practice_hint.lower()}:

1. Draft cases in `test_lab.py` or `specs/lab-{book_no:02d}{chapter_no:02d}.yaml`.
2. Use [Cursor Plan/Agent](https://cursor.com/) with "read spec first, then minimal diff".
3. Or use [OpenSpec](https://openspec.dev/) `/opsx:propose` so requirements live in `openspec/` next to code.

→ [Spec-driven workflow guide](../../getting-started/spec-driven-workflow.md) · [Lab {book_no}.{chapter_no}](../../labs/{ls}.md)
"""


def render_book9_spec_chapter_extra() -> str:
    return """## Spec-driven tooling: OpenSpec and Cursor

Specification-driven development is how teams keep **humans, CI, and coding agents** aligned. Two common stacks:

| Tool | What it stores | Best for |
|---|---|---|
| **[OpenSpec](https://openspec.dev/)** | `openspec/specs/` truth + `openspec/changes/` proposals, delta specs, tasks | Repo-level requirements that survive chat sessions; brownfield changes |
| **[Cursor](https://cursor.com/)** | `.cursor/rules/`, `AGENTS.md`, skills, Plan/Agent sessions | Day-to-day implementation with spec-first prompts and review |

Both share the same discipline: **acceptance examples before code**.

### 1. Executable acceptance (language-agnostic)

```python
# specs/acceptance.py — run before and after implementation
CASES = [
    {"input": "grant admin access", "expect": "require approval"},
    {"input": "unknown policy", "expect": "abstain"},
]

def check(outcome: str, expected: str) -> bool:
    return expected in outcome.lower()

failures = []
for case in CASES:
    simulated = (
        "abstain: no policy found"
        if "unknown" in case["input"]
        else "require approval"
    )
    if not check(simulated, case["expect"]):
        failures.append(case)
raise SystemExit(1 if failures else 0)
```

```bash
python specs/acceptance.py && echo "spec green"
```

### 2. OpenSpec — init, propose, apply

Requires **Node.js 20.19+**.

```bash
npm install -g @fission-ai/openspec@latest
openspec init
openspec update          # refresh assistant slash commands after profile changes
```

Explore a fuzzy idea without artifacts yet:

```text
/opsx:explore
We need an onboarding assistant that abstains when policy is missing and requires approval for admin grants.
```

When scope is clear, propose a change (creates `openspec/changes/<id>/`):

```text
/opsx:propose Add onboarding assistant policy spec with abstention and approval gates
```

Review generated files before coding:

```text
openspec/changes/add-onboarding-policy/
  proposal.md     # why and what
  tasks.md        # implementation checklist
  specs/          # ADDED / MODIFIED / REMOVED requirements
  design.md       # how (optional)
```

Implement against the plan:

```text
/opsx:apply
python -m pytest labs/0902-specification-driven-development/test_lab.py -q
```

Archive merges deltas into `openspec/specs/`:

```text
/opsx:archive
```

Example delta requirement (inside a change folder):

```markdown
## ADDED Requirements
### Requirement: Admin grant approval
The system SHALL require explicit approval before granting admin access.

#### Scenario: Privileged grant request
- GIVEN a user requests admin access
- WHEN no approval token is present
- THEN the system SHALL respond with require approval
```

### 3. Cursor — rules, Plan mode, and lab workflow

**Project rules** (`.cursor/rules/spec-driven.mdc`):

```markdown
---
description: Spec-driven AI features
globs: labs/**, specs/**, openspec/**
---
- Read acceptance specs and failing tests before editing implementation files
- Prefer minimal diffs; do not expand scope beyond the spec
- Run: python -m pytest test_lab.py -q (or path shown in AGENTS.md)
- Treat openspec/changes/*/specs as authoritative during active changes
```

**Plan mode prompt** (paste before Agent edits):

```text
Context: Book 9.2 Specification-Driven Development.
Read openspec/changes/<active-change>/proposal.md OR specs/lab-0902-acceptance.yaml.
List any missing normal/boundary/adversarial cases.
Propose a plan that only passes existing tests plus the spec—no extra features.
```

**Commands to verify** (same gates as CI):

```bash
cursor .
python labs/0902-specification-driven-development/main.py
python -m pytest labs/0902-specification-driven-development/test_lab.py -q
mkdocs build --strict
```

### 4. Tie specs to eval and release

| Spec type | Lives in | Gates |
|---|---|---|
| Functional / acceptance | `specs/`, `test_lab.py`, OpenSpec deltas | Local pytest, PR review |
| Prompt / tool | `specs/prompts/`, OpenSpec `specs/` | Regression eval in CI |
| Evaluation | `eval/spec.yaml` | Release threshold ([eval-gated release](../../guides/eval-gated-release.md)) |

→ Continue with [Lab 9.2](../../labs/0902-specification-driven-development.md) · [Spec-to-production guide](../../guides/spec-to-production-feature.md) · [Coding agent workspace](../../guides/coding-agent-workspace.md)
"""


def render_pattern_spec_extra() -> str:
    return """
## Tooling

### OpenSpec workflow

```bash
npm install -g @fission-ai/openspec@latest
openspec init
```

```text
/opsx:explore        # clarify problem before artifacts
/opsx:propose        # generate proposal + delta specs + tasks
/opsx:apply          # implement against tasks.md
/opsx:archive        # merge specs into openspec/specs/
```

### Cursor workflow

```bash
cursor .
```

Use **Plan** mode with the feature brief and acceptance YAML in context. Require a green pytest run before merge:

```bash
python -m pytest -q
```

### Sample acceptance file

```yaml
# specs/feature-x.yaml
feature: invoice_extractor
cases:
  - name: valid_pdf
    input: fixtures/invoice_clean.pdf
    expect_schema: invoice/v1
    expect_status: ok
  - name: missing_vendor
    input: fixtures/invoice_partial.pdf
    expect_status: structured_error
    expect_code: MISSING_VENDOR
```

See [spec-driven workflow](../getting-started/spec-driven-workflow.md).
"""


def render_workflow_page() -> str:
    return """# Spec-Driven Workflow

Build AI features **spec-first**: acceptance cases, eval thresholds, and tool contracts live in the repository *before* large agent diffs. This page shows the same workflow with **[OpenSpec](https://openspec.dev/)** (repo specs) and **[Cursor](https://cursor.com/)** (editor agents).

Every **lab** in AIEBOK includes a spec-driven habit section—use this page as the reference.

## Mental model

```mermaid
flowchart LR
  P[Problem / user evidence] --> S[Executable spec]
  S --> R[Review with human or agent]
  R --> I[Implementation]
  I --> E[Eval + tests]
  E --> REL[Release evidence]
```

Specs are not throwaway planning docs. They are **tests, YAML cases, or OpenSpec requirements** that CI and agents read on every change.

## Choose your stack

| Need | OpenSpec | Cursor |
|---|---|---|
| Persistent requirements in git | `openspec/specs/` by domain | `.cursor/rules/`, `AGENTS.md` |
| Change proposals with review | `openspec/changes/<id>/proposal.md` | Plan mode + PR description |
| Delta requirements | ADDED/MODIFIED/REMOVED in change | Spec file diff in PR |
| Apply implementation | `/opsx:apply` + tasks.md | Agent mode with spec in context |
| Best for | Brownfield features, team alignment | Daily coding, tight feedback loops |

Use **both**: OpenSpec for durable requirements; Cursor to implement tasks against them.

## OpenSpec quick start

**Prerequisites:** Node.js 20.19+

```bash
npm install -g @fission-ai/openspec@latest
cd your-repo
openspec init
openspec update
```

Directory layout after init:

```text
openspec/
  specs/           # current truth — behavior by domain (auth/, rag/, …)
  changes/         # active proposals
  changes/archive/ # completed changes
```

### Commands (assistant slash commands)

| Command | When to use |
|---|---|
| `/opsx:explore` | Fuzzy idea — explore options before writing specs |
| `/opsx:propose` | Ready to define a change — generates proposal, deltas, tasks |
| `/opsx:apply` | Spec approved — implement tasks systematically |
| `/opsx:archive` | Done — merge deltas into `openspec/specs/` |

CLI validation (when available in your install):

```bash
openspec validate
openspec show <change-id>
```

### Example: lab acceptance as a change

```text
/opsx:propose Add lab 0902 acceptance spec for policy abstention and admin approval
```

Review `openspec/changes/<id>/specs/` for requirements like:

```markdown
## ADDED Requirements
### Requirement: Policy abstention
WHEN policy text is unknown, the system SHALL abstain rather than guess.
```

Then:

```text
/opsx:apply
python -m pytest labs/0902-specification-driven-development/test_lab.py -q
/opsx:archive
```

## Cursor quick start

```bash
cursor .
```

### 1. Project rules

Create `.cursor/rules/spec-driven.mdc`:

```markdown
---
description: Spec-first development
globs: "**/*"
---
- Read specs/, openspec/changes/, and failing tests before implementation
- Write or update acceptance cases before changing production logic
- Run pytest (or documented test command) before claiming done
- Minimal diff: implement only what the spec requires
```

### 2. Plan mode (spec review)

```text
Read specs/lab-0902-acceptance.yaml and test_lab.py.
What normal, boundary, and adversarial cases are missing?
Propose a plan that does not expand scope beyond the spec.
```

### 3. Agent mode (implementation)

```text
Implement the plan. Touch only files listed in tasks.
After edits run: python -m pytest labs/0902-specification-driven-development/test_lab.py -q
```

### 4. Skills (repeatable workflows)

Store under `.cursor/skills/` — e.g. `spec-to-green/SKILL.md`:

```markdown
# Spec to green
1. Read active OpenSpec change or specs/*.yaml
2. Run tests; note failures
3. Minimal fix; re-run tests
4. Summarize spec coverage in PR description
```

See [Coding agent workspace](../guides/coding-agent-workspace.md).

## Copy-paste templates

### Acceptance YAML (any lab)

```yaml
# specs/lab-0305-acceptance.yaml
lab: "03.05 similarity and vector search"
cases:
  - name: paraphrase_ranks_higher
    input: { query: "system outage", docs: ["network failure", "weather"] }
    expect: "network failure"
  - name: orthogonal_vectors
    input: { query: [1, 0], docs: [[0, 1]] }
    expect_max_score: 0.01
```

### Pytest-first (same discipline)

```python
# test_lab.py — written before main.py changes
def test_abstains_on_unknown_policy():
    assert "abstain" in run("unknown policy")
```

### AGENTS.md excerpt

```markdown
## Spec-driven workflow
1. Read `specs/` or `openspec/changes/<active>/`
2. `python -m pytest test_lab.py -q` must pass before PR
3. Do not edit `.env` or generated locks
```

## Where this appears in AIEBOK

- **Book 9.2** — [Specification-Driven Development](../books/09-ai-software-and-product-engineering/02-specification-driven-development.md)
- **Every lab README** — spec-driven habit section with Cursor + OpenSpec commands
- **Starter notebooks** — spec-first checkpoint cell before coding
- **Guides** — [Spec-to-production](../guides/spec-to-production-feature.md), [Coding agent workspace](../guides/coding-agent-workspace.md)
- **Learning paths** — [Coding-agent specialist](learning-paths/02-coding-agent-specialist.md)

## Related

- [Pattern: Spec-Driven AI Feature](../patterns/spec-driven-ai-feature.md)
- [Lab 9.2](../labs/0902-specification-driven-development.md)
- [Eval-gated release](../guides/eval-gated-release.md)
"""
