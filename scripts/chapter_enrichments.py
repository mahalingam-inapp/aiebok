"""Chapter-specific enrichments using chapter_catalog and topic_knowledge."""
from __future__ import annotations

from chapter_catalog import (
    get_chapter_hook,
    get_knowledge_check,
    get_worked_example,
)


def learning_objectives(title: str, topics: list[str], summary: str) -> str:
    t0, t1 = topics[0], topics[1] if len(topics) > 1 else topics[0]
    return "\n".join(
        [
            f"- Explain why {title.lower()} matters using the chapter scenario, not abstract definitions alone.",
            f"- Trace how **{t0}** and **{t1}** interact in the book-level visual.",
            f"- Implement or design the bounded practice while holding evaluation cases fixed.",
            f"- Diagnose at least two failure modes specific to {topics[-1].lower()}.",
            f"- Decide where this chapter's mechanism belongs in a production architecture and what evidence justifies it.",
        ]
    )


def render_worked_example(
    book_no: int,
    chapter_no: int,
    title: str,
    summary: str,
    topics: list[str],
    scenario: str,
) -> str:
    body = get_worked_example(book_no, chapter_no, title, summary, topics, scenario)
    return f"""**Book scenario:** {scenario}

{body}"""


def engineering_practice(practice: str, topics: list[str], title: str) -> str:
    return f"""**Build:** {practice}

Work in three passes tailored to this chapter:

1. **Baseline:** Implement the task without {topics[0].lower()} and record quality, latency, and failure cases.
2. **Mechanism:** Add {topics[1].lower()} while keeping inputs and evaluation fixed; note what changed in intermediate state.
3. **Judgment:** Compare outcomes on normal, boundary, and adversarial cases; document when {title.lower()} earns its operational cost.

Capture assumptions, test cases, results, and one architecture decision record. A successful lab explains *why* behavior changed, not merely that the program ran."""


def failure_clinic(title: str, topics: list[str], summary: str) -> str:
    t0, t1, t_last = topics[0], topics[1], topics[-1]
    return f"""Reproduce failures at the chapter boundary—do not debug only final output.

| Failure | Symptom | Likely cause | First response |
|---|---|---|---|
| **Baseline illusion** | The system looks fine on demo prompts but fails on the book scenario | Evaluation cases do not cover {t0.lower()} or {t1.lower()} | Add the chapter's normal, boundary, and adversarial cases before tuning |
| **Mechanism mismatch** | Adding complexity does not improve the measured outcome | {title.lower()} is applied at the wrong layer or without fixing inputs | Trace the book visual and verify the transition this chapter owns |
| **Silent degradation** | Outputs remain fluent while decisions become wrong | Failure in {t_last.lower()} without observability at that boundary | Log intermediate state, version config, and compare against the baseline |
| **Operational drift** | Quality changes after deploy though prompts are unchanged | Data, permissions, or upstream {t0.lower()} behavior shifted | Pin versions, inspect ingestion and policy filters, re-run slice evals |

{summary.split('.')[0]}. When triaging, preserve full inputs, retrieved evidence, tool traces, and model or index versions."""


def architecture_lens(title: str, topics: list[str], book_title: str) -> str:
    t0, t_mid, t_last = topics[0], topics[2] if len(topics) > 2 else topics[1], topics[-1]
    return f"""For a production design in **{book_title}**, make the following explicit for **{title.lower()}**:

| Concern | Question to answer |
|---|---|
| **Ownership** | Which service owns {t0.lower()} versus downstream consumers of its output? |
| **Contract** | What typed inputs, outputs, errors, and version does the {t_mid.lower()} boundary expose? |
| **Evidence** | Which eval slices prove {title.lower()} meets requirements before and after each release? |
| **Security** | What untrusted data crosses the {t_last.lower()} boundary and how is it sanitized or authorized? |
| **Operations** | What is logged at this chapter's transition, what triggers retry or rollback, and what is cached? |
| **Economics** | Which resource—tokens, retrieval calls, GPU seconds, human review—dominates cost for this mechanism? |"""


def evolution_lens(title: str, topics: list[str], principle: str) -> str:
    t0 = topics[0]
    return f"""- **Yesterday:** Manual playbooks, brittle rules, or single-pass models handled parts of {title.lower()} without explicit {t0.lower()}.
- **Today:** Engineering teams implement {title.lower()} as testable components with baselines, typed boundaries, and stage-specific evaluation.
- **Tomorrow:** Better automation may reduce toil, but {topics[-1].lower()} and governance constraints will still require explicit design.
- **What survives:** {principle}"""


def _plain(topic: str) -> str:
    from topic_knowledge import get_topic_entry

    explanation, _, _ = get_topic_entry(topic)
    return explanation.split(".")[0].lower()


def mastery_exemplars(title: str, topics: list[str], principle: str) -> str:
    t0, t1, t_last = topics[0], topics[1], topics[-1]
    lines = [
        f"1. **Explain {t0} without jargon and give a counterexample.**",
        f"   *Proficient answer:* {_plain(t0)}. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.",
        f"2. **Compare {t1} with {t_last} using quality, cost, latency, and risk.**",
        f"   *Proficient answer:* {_plain(t1)}; {_plain(t_last)}. Trade quality gains against operational and security cost on the chapter scenario.",
        "3. **Design a minimal experiment that tests the chapter's central claim.**",
        "   *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.",
        "4. **Identify which component should own validation, authorization, and observability.**",
        f"   *Proficient answer:* Validation belongs at the typed boundary after {t1.lower()}; authorization before any side effect or retrieval of restricted data; observability at the transition {title.lower()} introduces in the book visual.",
        "5. **State what would remain true if today's leading libraries and vendors disappeared.**",
        f"   *Proficient answer:* {principle}",
    ]
    return "\n".join(f"    {line}" for line in lines)


def render_knowledge_check(book_no: int, chapter_no: int, topics: list[str]) -> str:
    q1, q2, q3, guidance = get_knowledge_check(book_no, chapter_no, topics)
    return f"""1. {q1}
2. {q2}
3. {q3}

??? question "Answer guidance"
    {guidance}"""


def render_chapter_hook(title: str, topics: list[str], book_no: int, chapter_no: int) -> str:
    code = get_chapter_hook(book_no, chapter_no, title, topics)
    return f"""## Chapter hook

Run this short snippet first to anchor **{title.lower()}** before the book-level sample:

```python
{code}
```

Predict the printed values, then change one line tied to **{topics[0]}** or **{topics[1]}** and observe how the chapter mechanism moves."""
