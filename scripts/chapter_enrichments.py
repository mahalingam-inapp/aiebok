"""Chapter-specific enrichments: failures, architecture, hooks, mastery exemplars."""
from __future__ import annotations


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
    plain = {
        "goal-directed behavior": "selects actions toward an explicit objective rather than producing unconstrained text",
        "bm25": "matches exact terms and identifiers when queries contain discriminative keywords",
        "dense retrieval": "finds paraphrases and semantic neighbors when lexical overlap is weak",
        "plan-act-observe": "separates choosing an action, executing it, and updating state from observations",
        "prompt injection": "treats untrusted content as data while preserving trusted instruction hierarchy",
        "attention": "routes information based on content similarity between positions",
        "kv cache": "avoids recomputing prefix states during autoregressive decoding",
        "hybrid search": "combines lexical and dense signals when neither alone covers the query distribution",
        "reciprocal rank fusion": "boosts documents that rank well in multiple retrievers without score calibration",
    }
    return plain.get(topic.lower(), "changes system behavior in ways that must be measured, not assumed")


def mastery_exemplars(title: str, topics: list[str], principle: str) -> str:
    t0, t1, t_last = topics[0], topics[1], topics[-1]
    lines = [
        f"1. **Explain {t0} without jargon and give a counterexample.**",
        f"   *Proficient answer:* {t0.title()} is the mechanism that {_plain(t0)}. Counterexample: applying it when the task is fully deterministic and cheaper to hard-code.",
        f"2. **Compare {t1} with {t_last} using quality, cost, latency, and risk.**",
        f"   *Proficient answer:* {t1.title()} improves quality when {_plain(t1)}, at higher latency/cost; {t_last} mainly affects risk or operations when misconfigured—for example silent wrong decisions or runaway spend.",
        "3. **Design a minimal experiment that tests the chapter's central claim.**",
        "   *Proficient answer:* Fix a baseline and three cases (normal, boundary, adversarial). Add only the chapter mechanism, measure one task metric plus cost/latency, and pre-register what result would falsify the claim.",
        "4. **Identify which component should own validation, authorization, and observability.**",
        f"   *Proficient answer:* Validation belongs at the typed boundary after {t1.lower()}; authorization before any side effect or retrieval of restricted data; observability at the transition {title.lower()} introduces in the book visual.",
        "5. **State what would remain true if today's leading libraries and vendors disappeared.**",
        f"   *Proficient answer:* {principle}",
    ]
    return "\n".join(f"    {line}" for line in lines)


def chapter_hook(title: str, topics: list[str], book_no: int, chapter_no: int) -> str:
    hooks: dict[tuple[int, int], str] = {
        (1, 1): '''GOAL = "route P1 incidents to on-call"
actions = ["classify", "route", "notify"]
state = {"tickets_seen": 0}
for action in actions:
    state["tickets_seen"] += 1
    print({"goal": GOAL, "action": action, "state": state})''',
        (1, 3): '''GRID = ["S##", "# #", "##G"]
start = GRID[0].index("S")
print("start", start, "goal", GRID[-1].index("G"))''',
        (3, 3): '''text = "unbelievable"
pairs = [(text[i:i+2], 1) for i in range(len(text)-1)]
print(sorted(pairs, key=lambda x: -x[1])[:3])''',
        (4, 2): '''import math
q, k = [1.0, 0.0], [0.9, 0.1]
score = sum(a*b for a,b in zip(q,k)) / (math.sqrt(sum(a*a for a in q)) * math.sqrt(sum(b*b for b in k)))
print("attention weight", round(score, 3))''',
        (5, 2): '''schema = {"type": "object", "required": ["total"], "properties": {"total": {"type": "number"}}}
payload = {"total": "12.50"}
valid = isinstance(payload.get("total"), (int, float))
print("valid" if valid else "reject: total must be numeric")''',
        (6, 3): '''docs = {"a": "PTO accrual cap is 240 hours", "b": "Leave policy overview"}
query = set("pto cap".split())
scores = {k: len(query & set(v.lower().split())) for k, v in docs.items()}
print("ranking", sorted(scores.items(), key=lambda x: -x[1]))''',
        (6, 4): '''rank_a = ["doc-leave", "doc-expense", "doc-security"]
rank_b = ["doc-expense", "doc-leave", "doc-onboarding"]
def rrf(lists, k=60):
    scores = {}
    for ranking in lists:
        for rank, doc in enumerate(ranking, 1):
            scores[doc] = scores.get(doc, 0) + 1/(k+rank)
    return sorted(scores.items(), key=lambda x: -x[1])
print(rrf([rank_a, rank_b])[:2])''',
        (7, 4): '''def search_tool(query: str) -> dict:
    if not query.strip():
        raise ValueError("query required")
    return {"results": [f"hit for {query!r}"]}
print(search_tool("budget policy"))''',
        (8, 2): '''state = {"step": 0, "observations": [], "done": False}
while not state["done"] and state["step"] < 3:
    state["step"] += 1
    state["observations"].append(f"obs-{state['step']}")
    state["done"] = state["step"] == 3
print(state)''',
        (10, 1): '''cases = [
    {"id": 1, "input": "reset password", "must": "link to policy"},
    {"id": 2, "input": "delete tenant", "must": "require approval"},
]
for case in cases:
    print(case["id"], case["must"])''',
        (11, 4): '''batch_sizes = [1, 4, 8]
for b in batch_sizes:
    throughput = b / (1 + 0.1 * (b - 1))
    print(f"batch={b} relative_throughput={throughput:.2f}")''',
    }
    default = f'''# Chapter hook: {title}
focus = "{topics[0]}"
related = "{topics[1] if len(topics) > 1 else topics[0]}"
print({{"chapter": "{book_no}.{chapter_no}", "focus": focus, "pairs_with": related}})'''
    return hooks.get((book_no, chapter_no), default)


def render_chapter_hook(title: str, topics: list[str], book_no: int, chapter_no: int) -> str:
    code = chapter_hook(title, topics, book_no, chapter_no)
    return f"""## Chapter hook

Run this short snippet first to anchor **{title.lower()}** before the book-level sample:

```python
{code}
```

Predict the printed values, then change one line tied to **{topics[0]}** or **{topics[1]}** and observe how the chapter mechanism moves."""
