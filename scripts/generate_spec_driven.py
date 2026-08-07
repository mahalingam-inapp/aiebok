"""Write spec-driven workflow page and sample templates."""
from __future__ import annotations

from pathlib import Path

from spec_driven_content import render_workflow_page

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / "docs" / "getting-started" / "spec-driven-workflow.md"
TEMPLATES = ROOT / "templates" / "spec-driven"

SAMPLE_ACCEPTANCE = """\
# Copy to specs/lab-XXXX-acceptance.yaml for any lab
lab: "example — replace with book.chapter title"
cases:
  - name: normal
    input: "typical user request"
    expect_contains: "expected phrase or metric"
  - name: boundary
    input: "edge case at limit"
    expect_contains: "graceful handling"
  - name: adversarial
    input: "malicious or ambiguous input"
    expect_contains: "abstain or require approval"
"""

SAMPLE_CURSOR_RULE = """\
---
description: Spec-first lab and feature workflow
globs: labs/**, specs/**, openspec/**
---
- Read acceptance specs and failing tests before editing implementation files
- Write or update acceptance cases before changing production logic
- Run: python -m pytest test_lab.py -q (or path in AGENTS.md)
- Minimal diff: implement only what the spec requires
- When openspec/changes/<id>/ is active, treat delta specs as authoritative
"""

SAMPLE_AGENTS_SNIPPET = """\
## Spec-driven workflow

1. Read `specs/` or active `openspec/changes/<id>/` before coding.
2. Use **Cursor Plan** mode to review acceptance cases with the agent.
3. With **OpenSpec**: `/opsx:explore` → `/opsx:propose` → review → `/opsx:apply` → `/opsx:archive`.
4. Verify: `python -m pytest test_lab.py -q` (or project test command).

See [spec-driven workflow](docs/getting-started/spec-driven-workflow.md).
"""


def main() -> None:
    WORKFLOW.write_text(render_workflow_page(), encoding="utf-8")
    TEMPLATES.mkdir(parents=True, exist_ok=True)
    (TEMPLATES / "lab-acceptance.yaml").write_text(SAMPLE_ACCEPTANCE, encoding="utf-8")
    (TEMPLATES / "cursor-spec-driven.mdc").write_text(SAMPLE_CURSOR_RULE, encoding="utf-8")
    (TEMPLATES / "AGENTS-spec-snippet.md").write_text(SAMPLE_AGENTS_SNIPPET, encoding="utf-8")
    print(f"Wrote {WORKFLOW.relative_to(ROOT)} and templates under {TEMPLATES.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
