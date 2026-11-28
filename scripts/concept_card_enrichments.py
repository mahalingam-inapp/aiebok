"""Extra sections for concept cards: categories, relations, and chapter links."""
from __future__ import annotations

import re
from functools import lru_cache

from generate_books import BOOKS, slug
from topic_knowledge import TOPIC_FACTS, normalize

CATEGORY_DEFAULTS: dict[str, dict[str, list[str] | str]] = {
    "retrieval": {
        "when_to_use": "Use when answers must cite private or changing documents, identifiers and paraphrases both appear in queries, or model parametric knowledge is insufficient.",
        "when_not": "Skip when a deterministic query, small fixed FAQ, or fine-tuned behavior already meets requirements with lower ops cost.",
        "failure_modes": [
            "Recall failure on acronym-heavy or multi-hop questions",
            "Stale index after document or embedding model change",
            "Cross-tenant leakage when metadata filters are missing",
        ],
    },
    "training": {
        "when_to_use": "Use when behavior must change systematically across many examples and prompts alone cannot reach quality or format targets.",
        "when_not": "Skip when RAG, better prompts, or routing fix the gap with less regression risk.",
        "failure_modes": [
            "Overfitting small curated sets",
            "Catastrophic forgetting of general capabilities",
            "Train-serve skew from preprocessing differences",
        ],
    },
    "inference": {
        "when_to_use": "Use when optimizing latency, cost, or throughput of generation and serving paths.",
        "when_not": "Skip micro-optimizations before measuring end-to-end SLOs and quality slices.",
        "failure_modes": [
            "KV cache bugs causing repetition or truncation",
            "Sampling settings that look fluent but fail eval slices",
            "Batching that violates latency SLOs",
        ],
    },
    "agents": {
        "when_to_use": "Use when tasks require multi-step decisions, tool use, or recovery across variable inputs.",
        "when_not": "Skip when a deterministic workflow with fixed steps is clearer and safer.",
        "failure_modes": [
            "Runaway loops without step or cost limits",
            "Tool calls with excessive privilege",
            "Lost state after partial failures",
        ],
    },
    "evaluation": {
        "when_to_use": "Use before every release, model swap, prompt change, or retrieval index migration.",
        "when_not": "Skip aggregate-only metrics when slices or safety cases can hide regressions.",
        "failure_modes": [
            "Benchmark overfitting without production-like queries",
            "Stale eval sets that no longer match user behavior",
            "LLM judges drifting from human standards",
        ],
    },
    "security": {
        "when_to_use": "Use for any system combining untrusted user content, tools, or external retrieval.",
        "when_not": "Do not treat a single prompt rule as sufficient without tests and monitoring.",
        "failure_modes": [
            "Prompt injection via retrieved or pasted content",
            "Tool abuse exfiltrating secrets",
            "Missing authorization on retrieval paths",
        ],
    },
    "default": {
        "when_to_use": "Use when the mechanism directly addresses a measured gap versus simpler baselines on your workload.",
        "when_not": "Skip when complexity, latency, or ops burden exceeds demonstrated benefit.",
        "failure_modes": [
            "Applying the technique without a baseline comparison",
            "Ignoring boundary and adversarial inputs",
            "Optimizing demo cases instead of production slices",
        ],
    },
}

TOPIC_CATEGORY: dict[str, str] = {}
_category_rules: list[tuple[str, str]] = [
    ("retrieval", r"retriev|rag|bm25|embed|vector|rerank|chunk|index|hybrid-search|dense-"),
    ("training", r"train|fine-tun|lora|sft|dpo|rlhf|dataset|curat|pretrain|loss|gradient|optim"),
    ("inference", r"infer|sampl|logit|kv-cache|batch|latency|decode|token|context-window"),
    ("agents", r"agent|tool|mcp|plan-act|checkpoint|approval|autonom|workflow"),
    ("evaluation", r"eval|metric|rubric|slice|benchmark|calibrat|ablat|faithful|precision|recall"),
    ("security", r"secur|inject|jailbreak|auth|acl|threat|red-team|govern|audit|privacy"),
]

for key in TOPIC_FACTS:
    cat = "default"
    for name, pattern in _category_rules:
        if re.search(pattern, key):
            cat = name
            break
    TOPIC_CATEGORY[key] = cat


@lru_cache(maxsize=1)
def topic_chapter_links() -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for book_no, book in enumerate(BOOKS, 1):
        book_slug = f"{book_no:02d}-{slug(book['title'])}"
        for ch_no, chapter in enumerate(book["chapters"], 1):
            ch_slug = f"{ch_no:02d}-{slug(chapter[0])}"
            href = f"../books/{book_slug}/{ch_slug}.md"
            for topic in chapter[2]:
                mapping.setdefault(normalize(topic), []).append(href)
    return mapping


@lru_cache(maxsize=1)
def topic_related_concepts() -> dict[str, list[str]]:
    cooccur: dict[str, set[str]] = {k: set() for k in TOPIC_FACTS}
    for book in BOOKS:
        for chapter in book["chapters"]:
            keys = [normalize(t) for t in chapter[2]]
            for i, a in enumerate(keys):
                for b in keys:
                    if a != b and b in TOPIC_FACTS:
                        cooccur.setdefault(a, set()).add(b)
    return {k: sorted(v)[:5] for k, v in cooccur.items() if v}


# Practicums give these concepts a concrete comparison and a directly runnable exercise.
MODEL_POLICY_NOTES = {
    "mixture-of-experts": ("sparse-model-architectures", "Use when a larger parameter budget is plausible at bounded token compute.",
                           "Favor a dense baseline for workloads that cannot accommodate resident experts or inter-device traffic.",
                           "Count active and resident weights, including shared layers.",
                           "A router concentrates a burst on a few experts."),
    "expert-parallelism": ("sparse-model-architectures", "Use when a device cannot efficiently host the entire expert bank.",
                          "Avoid increasing parallelism if small batches cannot amortize synchronization.",
                          "Measure local and remote assignments and record maximum rank load.",
                          "A straggler rank dominates latency despite low average utilization."),
    "expert-load-balancing": ("sparse-model-architectures", "Use when bursts or recurring request shapes concentrate assignments.",
                              "Equal assignment counts alone do not establish equal quality or execution cost.",
                              "Record rerouted and overflow assignments alongside the original choices.",
                              "Rerouting reduces overflow but sends tokens to experts that perform poorly on the task."),
    "grouped-query-attention": ("sparse-model-architectures", "Use when KV memory or bandwidth constrains decoding.",
                               "Avoid assuming a checkpoint trained with independent KV heads can be converted without quality evaluation.",
                               "Count KV heads, not query heads, when estimating cached elements.",
                               "More contexts fit in memory but long-context quality drops."),
    "multi-head-latent-attention": ("sparse-model-architectures", "Use when comparing architectures that compress token history for decoding.",
                                  "A theoretical cache reduction alone cannot predict speed on a runtime lacking suitable kernels.",
                                  "Include positional cache components and record runtime precision.",
                                  "The cache is smaller but decompression or projection work increases latency."),
    "hybrid-attention-backbones": ("sparse-model-architectures", "Use when long contexts make per-layer KV growth expensive.",
                                   "Require separate evidence for tasks that depend on exact long-range recall.",
                                   "Account for recurrent state and full-attention KV separately.",
                                   "Memory estimates overlook state that scales with the number of active sequences."),
    "speculative-decoding": ("reasoning-efficient-inference", "Use when a cheap draft tends to predict several tokens the target can accept.",
                             "Skip when low acceptance or saturated target batches erase gains.",
                             "Compare with target-only decoding on the same prompts and settings.",
                             "An incorrect sampling correction changes the target distribution."),
    "continuous-batching": ("reasoning-efficient-inference", "Use when request lengths vary and generation steps leave reusable capacity.",
                            "Single-request latency benchmarks cannot justify changing a shared scheduler.",
                            "Benchmark short and long requests at several arrival rates.",
                            "Higher throughput conceals increased time to first token for cold requests."),
    "contextual-bandits": ("decision-models-and-policies", "Use for repeated one-step choices with observable feedback.",
                           "Use a sequential model when choices materially change future states and rewards.",
                           "Log the eligible actions, selected action, propensity and outcome.",
                           "Selection probabilities are missing or detached from the policy version."),
    "off-policy-evaluation": ("decision-models-and-policies", "Use to assess a target decision policy from data collected by another policy.",
                             "Withhold the estimate when the target selects actions outside the logging policy's support.",
                             "Inspect overlap and effective sample size before comparing values.",
                             "A handful of high-weight rows dominate the estimate."),
    "decision-transformer": ("decision-models-and-policies", "Use to study return-conditioned policies when trajectory data cover relevant states and actions.",
                             "Avoid relying on unreachable target returns or unsupported actions.",
                             "Compare with behavior cloning and a simple planner on the same evaluation environments.",
                             "Target returns outside the training range produce unreliable actions."),
    "constrained-assignment": ("decision-models-and-policies", "Use when individually promising actions compete for shared capacity or violate combination rules.",
                               "Use simple ranking when actions are independent and share no relevant constraints.",
                               "Check feasibility and objective value against a tiny exact reference.",
                               "A greedy choice consumes capacity needed by a higher-value combination."),
}


def card_enrichment(key: str) -> dict[str, list[str] | str]:
    cat = TOPIC_CATEGORY.get(key, "default")
    defaults = CATEGORY_DEFAULTS[cat]
    chapters = topic_chapter_links().get(key, [])[:3]
    related = topic_related_concepts().get(key, [])[:4]
    checklist = [
        "State the decision this mechanism supports before implementation.",
        "Compare against a simpler baseline on normal, boundary, and adversarial cases.",
        "Define metrics, slices, and rollback before production rollout.",
    ]
    if cat == "retrieval":
        checklist.append("Version embedding model, index, and preprocessing together.")
    elif cat == "agents":
        checklist.append("Bound steps, cost, tools, and human approval for side effects.")
    elif cat == "evaluation":
        checklist.append("Report worst-slice performance, not aggregate alone.")
    if key in MODEL_POLICY_NOTES:
        course, use, limit, check, failure = MODEL_POLICY_NOTES[key]
        return {
            "when_to_use": use, "when_not": limit, "failure_modes": [failure],
            "checklist": [check], "chapters": chapters, "related": related, "course": course,
        }
    return {
        "when_to_use": defaults["when_to_use"],
        "when_not": defaults["when_not"],
        "failure_modes": defaults["failure_modes"],
        "checklist": checklist,
        "chapters": chapters,
        "related": related,
    }
