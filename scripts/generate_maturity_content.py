"""Generate research readings, build guides, reference index, glossary, and full labs."""
from __future__ import annotations

import re
from pathlib import Path

from chapter_catalog import CHAPTER_HOOKS
from generate_books import BOOKS, slug
from generate_expansion import lab_slug
from guide_deep_content import GUIDE_DETAILS
from paper_deep_content import PAPER_DETAILS as BASE_PAPER_DETAILS
from paper_deep_content_extra import EXTRA_PAPER_DETAILS, EXTRA_PAPER_SPECS
from topic_knowledge import TOPIC_FACTS, get_topic_entry, normalize

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PAPERS = DOCS / "papers" / "readings"
GUIDES = DOCS / "guides"
LABS = ROOT / "labs"
DOCS_LABS = DOCS / "labs"
REFERENCE = DOCS / "reference"


def title_from_slug(s: str) -> str:
    return " ".join(w if w.isupper() and len(w) <= 4 else w.capitalize() for w in s.split("-"))


PAPER_SPECS: list[tuple[str, str, str, str, str, str]] = [
    ("word2vec", "Efficient Estimation of Word Representations in Vector Space", "Mikolov et al.", "2013", "https://arxiv.org/abs/1301.3781", "Introduced skip-gram and CBOW dense word vectors learned from co-occurrence."),
    ("seq2seq", "Sequence to Sequence Learning with Neural Networks", "Sutskever et al.", "2014", "https://arxiv.org/abs/1409.3215", "Encoder–decoder LSTM architecture for variable-length input/output mapping."),
    ("attention-paper", "Neural Machine Translation by Jointly Learning to Align and Translate", "Bahdanau et al.", "2015", "https://arxiv.org/abs/1409.0473", "Additive attention let decoders focus on relevant encoder states."),
    ("transformer", "Attention Is All You Need", "Vaswani et al.", "2017", "https://arxiv.org/abs/1706.03762", "Self-attention transformer replaced recurrence for sequence modeling."),
    ("bert", "BERT: Pre-training of Deep Bidirectional Transformers", "Devlin et al.", "2019", "https://arxiv.org/abs/1810.04805", "Masked language modeling plus next-sentence prediction for bidirectional context."),
    ("gpt3", "Language Models are Few-Shot Learners", "Brown et al.", "2020", "https://arxiv.org/abs/2005.14165", "Scale and in-context examples enable task behavior without fine-tuning."),
    ("t5", "Exploring the Limits of Transfer Learning", "Raffel et al.", "2020", "https://arxiv.org/abs/1910.10683", "Text-to-text framework unifies NLP tasks under one seq2seq objective."),
    ("rag", "Retrieval-Augmented Generation for Knowledge-Intensive NLP", "Lewis et al.", "2020", "https://arxiv.org/abs/2005.11401", "Retrieve documents at generation time to ground outputs."),
    ("dpr", "Dense Passage Retrieval for Open-Domain QA", "Karpukhin et al.", "2020", "https://arxiv.org/abs/2004.04906", "Dual-encoder dense retrieval competitive with BM25 on open QA."),
    ("instructgpt", "Training Language Models to Follow Instructions", "Ouyang et al.", "2022", "https://arxiv.org/abs/2203.02155", "RLHF aligns models to human preferences on instruction following."),
    ("lora", "LoRA: Low-Rank Adaptation of Large Language Models", "Hu et al.", "2021", "https://arxiv.org/abs/2106.09685", "Train low-rank adapters while freezing base weights."),
    ("react", "ReAct: Synergizing Reasoning and Acting", "Yao et al.", "2023", "https://arxiv.org/abs/2210.03629", "Interleave chain-of-thought with tool actions and observations."),
    ("dpo", "Direct Preference Optimization", "Rafailov et al.", "2023", "https://arxiv.org/abs/2305.18290", "Optimize preferences without explicit reward modeling."),
    ("chain-of-thought", "Chain-of-Thought Prompting Elicits Reasoning", "Wei et al.", "2022", "https://arxiv.org/abs/2201.11903", "Few-shot reasoning exemplars improve multi-step task performance."),
    ("scaling-laws", "Scaling Laws for Neural Language Models", "Kaplan et al.", "2020", "https://arxiv.org/abs/2001.08361", "Loss scales predictably with compute, parameters, and data."),
    ("chinchilla", "Training Compute-Optimal Large Language Models", "Hoffmann et al.", "2022", "https://arxiv.org/abs/2203.15556", "Optimal training balances model size and token count."),
    ("llama", "LLaMA: Open and Efficient Foundation Language Models", "Touvron et al.", "2023", "https://arxiv.org/abs/2302.13971", "High-quality open-weights models trained on public data mixtures."),
    ("toolformer", "Toolformer: Language Models Can Teach Themselves to Use Tools", "Schick et al.", "2023", "https://arxiv.org/abs/2302.04761", "Self-supervised API call insertion during pretraining."),
    ("constitutional-ai", "Constitutional AI: Harmlessness from AI Feedback", "Bai et al.", "2022", "https://arxiv.org/abs/2212.08073", "Principle-guided critique and revision for safer assistants."),
    ("moe", "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer", "Shazeer et al.", "2017", "https://arxiv.org/abs/1701.06538", "Conditional computation activates subsets of experts per token."),
    ("clip", "Learning Transferable Visual Models From Natural Language Supervision", "Radford et al.", "2021", "https://arxiv.org/abs/2103.00020", "Contrastive image–text pretraining enables zero-shot vision tasks."),
    ("whisper", "Robust Speech Recognition via Large-Scale Weak Supervision", "Radford et al.", "2022", "https://arxiv.org/abs/2212.04356", "Multilingual ASR from weakly labeled audio at scale."),
    ("speculative-decoding", "Fast Inference from Transformers via Speculative Decoding", "Leviathan et al.", "2023", "https://arxiv.org/abs/2211.17192", "Draft model proposes tokens; target model verifies in parallel."),
    ("flash-attention", "FlashAttention: Fast and Memory-Efficient Exact Attention", "Dao et al.", "2022", "https://arxiv.org/abs/2205.14135", "IO-aware attention algorithm reduces memory and speeds training/inference."),
    ("rlhf-preference", "Learning to Summarize from Human Feedback", "Stiennon et al.", "2020", "https://arxiv.org/abs/2009.01325", "Early large-scale RLHF for summarization quality."),
    ("self-instruct", "Self-Instruct: Aligning Language Models with Self-Generated Instructions", "Wang et al.", "2023", "https://arxiv.org/abs/2212.10560", "Bootstrap instruction data from a seed set."),
    ("tree-of-thoughts", "Tree of Thoughts: Deliberate Problem Solving with LLMs", "Yao et al.", "2023", "https://arxiv.org/abs/2305.10601", "Search over intermediate reasoning states improves hard tasks."),
    ("graph-rag", "From Local to Global: A Graph RAG Approach to Query-Focused Summarization", "Edge et al.", "2024", "https://arxiv.org/abs/2404.16130", "Graph structure over corpus supports global summarization queries."),
    ("mamba", "Mamba: Linear-Time Sequence Modeling with Selective State Spaces", "Gu & Dao", "2023", "https://arxiv.org/abs/2312.00752", "Selective SSMs offer recurrent-like efficiency with strong quality."),
    ("jailbreak-survey", "Survey of Attacks and Defenses in LLM Security (representative)", "Various", "2024", "https://owasp.org/www-project-top-10-for-large-language-model-applications/", "Catalog of prompt injection and tool abuse patterns."),
    ("knowledge-neurons", "Knowledge Neurons in Pretrained Transformers", "Dai et al.", "2022", "https://arxiv.org/abs/2104.08696", "Localized parameters correlate with factual recall."),
    ("ragas", "RAGAS: Automated Evaluation of Retrieval Augmented Generation", "Es et al.", "2023", "https://arxiv.org/abs/2309.15217", "Faithfulness and context precision metrics for RAG pipelines."),
    ("olmo", "OLMo: Accelerating the Science of Language Models", "Groeneveld et al.", "2024", "https://arxiv.org/abs/2402.00838", "Fully open pipeline for reproducible LM research."),
    ("agent-benchmark-webarena", "WebArena: A Realistic Web Environment for Agents", "Zhou et al.", "2024", "https://arxiv.org/abs/2307.13854", "Benchmark for autonomous web agents on realistic tasks."),
    ("mcp-spec", "Model Context Protocol Specification", "Anthropic", "2024", "https://modelcontextprotocol.io/", "Standard for tools, resources, and prompts between clients and servers."),
]

PAPER_DETAILS = {**BASE_PAPER_DETAILS, **EXTRA_PAPER_DETAILS}
ALL_PAPER_SPECS = PAPER_SPECS + EXTRA_PAPER_SPECS


def paper_chapter_href(path: str) -> str | None:
    """Normalize chapter path from paper reading pages and drop missing targets."""
    href = path.replace("../books/", "../../books/")
    rel = href.replace("../../", "", 1) if href.startswith("../../") else href.lstrip("./")
    if not (DOCS / rel).is_file():
        return None
    return href


def paper_concept_href(slug: str) -> str | None:
    """Link to concept card or featured concept if it exists."""
    key = normalize(slug)
    card = DOCS / "concepts" / "cards" / f"{key}.md"
    featured = DOCS / "concepts" / f"{key}.md"
    if card.is_file():
        return f"../../concepts/cards/{key}.md"
    if featured.is_file():
        return f"../../concepts/{key}.md"
    return None


def guide_pattern_href(slug: str) -> str | None:
    if (DOCS / "patterns" / f"{slug}.md").is_file():
        return f"../patterns/{slug}.md"
    return None


def guide_lab_href(slug: str) -> str | None:
    doc = DOCS / "labs" / f"{slug}.md"
    if doc.is_file():
        return f"../labs/{slug}.md"
    return None


def render_paper(ps: tuple[str, str, str, str, str, str]) -> str:
    key, title, authors, year, link, contribution = ps
    detail = PAPER_DETAILS.get(key)
    if not detail:
        detail = {
            "problem": "See the original paper for the motivating problem.",
            "prior_art": "Review contemporaneous baselines cited in the paper.",
            "core_idea": contribution,
            "evidence": ["Review datasets, baselines, and ablations in the original paper."],
            "limitations": ["Check assumptions and missing comparisons in the paper."],
            "impact": "Trace follow-up systems and papers that adopted or rejected the idea.",
            "reproduction": "Define the smallest experiment that would falsify the central claim.",
            "related_chapters": [],
            "related_concepts": [],
        }
    evidence = "\n".join(f"- {item}" for item in detail["evidence"])
    limitations = "\n".join(f"- {item}" for item in detail["limitations"])
    related = ""
    if detail["related_chapters"]:
        chapter_links = []
        for ch in detail["related_chapters"]:
            href = paper_chapter_href(ch)
            if href:
                label = Path(href).name.replace(".md", "").replace("-", " ").title()
                chapter_links.append(f"- [{label}]({href})")
        if chapter_links:
            related += "\n## Related chapters\n\n" + "\n".join(chapter_links) + "\n"
    if detail["related_concepts"]:
        concept_links = []
        for c in detail["related_concepts"]:
            href = paper_concept_href(c)
            if href:
                concept_links.append(f"- [{title_from_slug(c)}]({href})")
        if concept_links:
            related += "\n## Related concepts\n\n" + "\n".join(concept_links) + "\n"
    return f"""# {title}

## Citation

{authors}. *{title}.* {year}. [{link}]({link})

## One-sentence contribution

{contribution}

## Problem

{detail["problem"]}

## Prior art

{detail["prior_art"]}

## Core idea

{detail["core_idea"]}

## Evidence

{evidence}

## Limitations

{limitations}

## Lasting impact

{detail["impact"]}

## Reproduction exercise

{detail["reproduction"]}
{related}"""


def generate_readings() -> int:
    PAPERS.mkdir(parents=True, exist_ok=True)
    lines = ["# Research Readings Catalog", "", f"{len(ALL_PAPER_SPECS)} primary-source summaries.", ""]
    for spec in ALL_PAPER_SPECS:
        key = spec[0]
        (PAPERS / f"{key}.md").write_text(render_paper(spec), encoding="utf-8")
        lines.append(f"- [{spec[1]}]({key}.md)")
    (PAPERS / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(ALL_PAPER_SPECS)


BUILD_GUIDES: list[tuple[str, str, str, list[str], str]] = [
    ("enterprise-rag-end-to-end", "Enterprise RAG End to End", "Ship authorized hybrid RAG with citations and stage evals.", ["Ingestion manifest", "Hybrid retrieval", "Reranker", "Grounded generation", "Citation validator", "Release gate"], "06-knowledge-and-retrieval-systems"),
    ("bounded-agent-assistant", "Bounded Agent Assistant", "Multi-step agent with typed tools, checkpoints, and approval.", ["State machine", "Tool schemas", "Human approval", "Checkpoint store", "Eval traces"], "08-agent-systems"),
    ("context-engine-with-tests", "Context Engine With Tests", "Versioned prompts, memory policy, token budgets, regression tests.", ["Context builder", "Section budgets", "Prompt versions", "Eval dataset"], "05-prompt-and-context-engineering"),
    ("model-selection-harness", "Model Selection Harness", "Vendor-neutral benchmark report for task-specific model choice.", ["Task dataset", "Candidate models", "Cost/latency log", "Selection ADR"], "04-transformers-and-foundation-models"),
    ("eval-gated-release", "Eval-Gated Release Pipeline", "CI harness with slices, thresholds, and rollback evidence.", ["Gold cases", "Slice metrics", "Release gate", "Canary plan"], "10-evaluation-safety-and-governance"),
    ("hybrid-search-engine", "Hybrid Search Engine", "Lexical + dense retrieval with fusion and offline eval.", ["BM25 index", "Vector index", "RRF fusion", "recall@k eval"], "06-knowledge-and-retrieval-systems"),
    ("structured-extraction-api", "Structured Extraction API", "Schema-validated extraction behind a REST boundary.", ["JSON Schema", "Validator", "Repair loop", "Adversarial tests"], "05-prompt-and-context-engineering"),
    ("multi-tenant-retrieval", "Multi-Tenant Retrieval Platform", "Tenant-scoped indexes, ACL filters, and audit logs.", ["Tenant metadata", "AuthZ filters", "Isolation tests"], "12-cloud-and-enterprise-ai-architecture"),
    ("coding-agent-workspace", "Coding Agent Workspace", "Repo instructions, skills, and review gates for AI coding.", ["AGENTS.md", "Skills", "CI checks", "Review rubric"], "09-ai-software-and-product-engineering"),
    ("fine-tune-and-serve", "Fine-Tune and Serve a Small Model", "LoRA adaptation with eval, registry, and rollback.", ["Data card", "LoRA train", "Eval report", "Serving endpoint"], "11-training-serving-and-ai-operations"),
    ("red-team-security-harness", "Red-Team Security Harness", "Prompt injection and tool abuse tests in CI.", ["Attack set", "Mitigations", "Incident runbook"], "10-evaluation-safety-and-governance"),
    ("multimodal-document-pipeline", "Multimodal Document Pipeline", "OCR, layout, extraction with provenance.", ["Parse/OCR", "Field eval", "Provenance metadata"], "13-multimodal-and-frontier-systems"),
    ("spec-to-production-feature", "Spec-to-Production AI Feature", "Discovery through spec, implementation, eval, and rollout.", ["Problem brief", "Executable spec", "Feature flag rollout"], "09-ai-software-and-product-engineering"),
]


def render_build_guide(key: str, title: str, goal: str, phases: list[str], book: str) -> str:
    detail = GUIDE_DETAILS.get(key)
    if not detail:
        phase_lines = "\n".join(
            f"{i+1}. **{p}** — deliverable and acceptance check" for i, p in enumerate(phases)
        )
        return f"""# {title}

## Goal

{goal}

## Prerequisites

Complete the matching [guided book](../books/{book}/index.md) and related labs.

## Build phases

{phase_lines}

## Evidence package

- Short specification with acceptance criteria
- Runnable artifact or architecture diagram
- Evaluation report with slices and failure analysis
- At least one ADR for a major design choice
- Rollback or fallback plan

## Exit criteria

You can demo the system on normal, boundary, and adversarial cases; explain measured trade-offs; and defend why simpler alternatives were insufficient.
"""

    phase_blocks: list[str] = []
    for i, phase in enumerate(detail.phases, 1):
        steps = "\n".join(f"   - {s}" for s in phase.steps)
        acceptance = "\n".join(f"   - {a}" for a in phase.acceptance)
        commands = ""
        if phase.commands:
            commands = "\n\n   **Commands:**\n\n   ```bash\n   " + "\n   ".join(phase.commands) + "\n   ```"
        phase_blocks.append(
            f"### {i}. {phase.name}\n\n**Goal:** {phase.goal}\n\n**Steps:**\n{steps}\n\n**Acceptance:**\n{acceptance}{commands}"
        )

    pattern_lines = []
    for p in detail.related_patterns:
        href = guide_pattern_href(p)
        if href:
            pattern_lines.append(f"- [{title_from_slug(p)}]({href})")
    patterns = "\n".join(pattern_lines) if pattern_lines else "- See the [pattern catalog](../patterns/index.md)."

    lab_lines = []
    for lab in detail.related_labs:
        href = guide_lab_href(lab)
        if href:
            lab_lines.append(f"- [{title_from_slug(lab)}]({href})")
    labs = "\n".join(lab_lines) if lab_lines else "- See the [lab catalog](../../labs/index.md)."
    troubleshooting = "\n".join(f"- {t}" for t in detail.troubleshooting)

    return f"""# {title}

## Goal

{goal}

## Overview

{detail.overview}

## Architecture

{detail.architecture_notes}

## Prerequisites

Complete the matching [guided book](../books/{book}/index.md) and related labs.

## Build phases

{chr(10).join(phase_blocks)}

## Troubleshooting

{troubleshooting}

## Related patterns

{patterns}

## Related labs

{labs}

## Evidence package

- Short specification with acceptance criteria
- Runnable artifact or architecture diagram
- Evaluation report with slices and failure analysis
- At least one ADR for a major design choice
- Rollback or fallback plan

## Exit criteria

You can demo the system on normal, boundary, and adversarial cases; explain measured trade-offs; and defend why simpler alternatives were insufficient.
"""


def generate_build_guides() -> int:
    GUIDES.mkdir(parents=True, exist_ok=True)
    lines = ["# Build Guides", "", "End-to-end projects from spec to evidence.", ""]
    for key, title, goal, phases, book in BUILD_GUIDES:
        (GUIDES / f"{key}.md").write_text(render_build_guide(key, title, goal, phases, book), encoding="utf-8")
        lines.append(f"- [{title}]({key}.md)")
    (GUIDES / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(BUILD_GUIDES)


QUESTION_SPECS: list[tuple[str, str, list[tuple[str, str]]]] = [
    ("Models and learning", "models-and-learning", [
        ("What does it mean for a model to learn?", "../books/01-foundations-of-intelligence/05-learning-and-generalization.md"),
        ("What are weights and parameters?", "../concepts/cards/training.md"),
        ("How does an LLM generate text?", "../books/04-transformers-and-foundation-models/05-inference-and-sampling.md"),
        ("Why do reasoning models take longer?", "../concepts/cards/test-time-compute.md"),
        ("When should I fine-tune versus prompt?", "../books/11-training-serving-and-ai-operations/01-choosing-adaptation.md"),
    ]),
    ("Language and knowledge", "language-and-knowledge", [
        ("What is a token?", "../concepts/tokens.md"),
        ("Why do embeddings work?", "../concepts/embeddings.md"),
        ("When should I use keyword, vector, or hybrid search?", "../concepts/cards/hybrid-search.md"),
        ("When should I use RAG rather than fine-tuning?", "../books/06-knowledge-and-retrieval-systems/01-knowledge-outside-the-model.md"),
        ("Why does RAG hallucinate?", "../books/06-knowledge-and-retrieval-systems/05-rag-generation-and-citations.md"),
        ("What is BM25?", "../concepts/cards/bm25.md"),
        ("How do rerankers help?", "../concepts/reranking.md"),
    ]),
    ("Context, tools, and agents", "context-tools-agents", [
        ("How does an assistant remember?", "../books/05-prompt-and-context-engineering/04-conversation-and-memory.md"),
        ("What is context engineering?", "../books/05-prompt-and-context-engineering/03-context-construction.md"),
        ("What is the difference between a skill and a harness?", "../concepts/skills-harnesses.md"),
        ("What is MCP?", "../concepts/cards/mcp.md"),
        ("How is an agent different from a workflow?", "../concepts/agents.md"),
        ("When should humans approve an action?", "../patterns/human-approval-gate.md"),
        ("How do tool schemas prevent abuse?", "../concepts/tool-calling.md"),
    ]),
    ("Engineering and operations", "engineering-and-operations", [
        ("How do I build with specifications?", "../guides/spec-to-production-feature.md"),
        ("How should AI systems be tested?", "../books/09-ai-software-and-product-engineering/04-testing-ai-systems.md"),
        ("How do I choose cloud services?", "../books/12-cloud-and-enterprise-ai-architecture/index.md"),
        ("How do I operate an AI service?", "../books/11-training-serving-and-ai-operations/06-llmops.md"),
        ("How do I govern enterprise AI?", "../books/10-evaluation-safety-and-governance/06-governance-and-assurance.md"),
        ("How do eval gates work in CI?", "../guides/eval-gated-release.md"),
    ]),
    ("Security and safety", "security-and-safety", [
        ("What is prompt injection?", "../concepts/prompt-injection.md"),
        ("How do I red-team an assistant?", "../guides/red-team-security-harness.md"),
        ("What are eval slices?", "../concepts/cards/slices.md"),
        ("How do I calibrate LLM judges?", "../papers/readings/ragas.md"),
    ]),
    ("Research literacy", "research-literacy", [
        ("How do I read an AI paper?", "../papers/paper-reading-template.md"),
        ("What did the Transformer change?", "../papers/readings/transformer.md"),
        ("What did RAG add to generation?", "../papers/readings/rag.md"),
        ("How do I reproduce a frontier claim?", "../books/13-multimodal-and-frontier-systems/06-how-to-track-the-frontier.md"),
    ]),
]


def generate_question_index() -> None:
    lines = ["# Question Index", "", "Navigate by question to books, concepts, patterns, guides, and papers.", ""]
    for section, _anchor, items in QUESTION_SPECS:
        lines.append(f"## {section}")
        lines.append("")
        for q, link in items:
            lines.append(f"- **{q}** → [{link.split('/')[-1].replace('.md','')}]({link})")
        lines.append("")
    (REFERENCE / "question-index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def generate_glossary() -> int:
    lines = [
        "# Glossary",
        "",
        "Alphabetical definitions for AIEBOK catalog terms. See [concept cards](../concepts/cards/index.md) for expanded entries.",
        "",
    ]
    for key in sorted(TOPIC_FACTS):
        explanation, _, _ = get_topic_entry(title_from_slug(key))
        first = explanation.split(".")[0].strip()
        if not first.startswith("**"):
            first = f"**{title_from_slug(key)}:** {first}"
        else:
            first = first.replace("**", f"**{title_from_slug(key)}:** ", 1)
        lines.append(f"- {first}.")
    (REFERENCE / "glossary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(TOPIC_FACTS)


def render_lab_docs(book_no: int, chapter_no: int, title: str, practice: str, ls: str, book_title: str) -> tuple[str, str, str, str]:
    hook = CHAPTER_HOOKS.get((book_no, chapter_no), "print('ok')")
    main_py = f'"""Lab {book_no}.{chapter_no}: {title}"""\n\n{hook}\n'
    test_py = f'''"""Tests for lab {book_no}.{chapter_no}."""
import subprocess
import sys
from pathlib import Path


def test_main_exits_zero():
    result = subprocess.run(
        [sys.executable, str(Path(__file__).parent / "main.py")],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip()
'''

    readme = f"""# Lab {book_no}.{chapter_no} — {title}

## Objective

{practice}

## Prerequisites

- Book {book_no}: {book_title}, chapter {chapter_no}
- Python 3.10+

## Time estimate

45–60 minutes

## Run

```bash
python main.py
python -m pytest test_lab.py -q
```

## Tasks

1. Run `main.py` and predict the output before executing.
2. Modify one line tied to the chapter mechanism; observe the change.
3. Add one boundary case and one adversarial case as code or documented input.
4. Record latency or quality notes compared to a naive baseline.

## Expected observations

Output should be non-empty and change predictably when the chapter mechanism is altered.

## Reflection

- What failure mode appeared first when you stressed the baseline?
- Which metric would you use before adding complexity?

## Extensions

- Add a second test case to `test_lab.py`
- Link results to the matching [concept card](../../docs/concepts/cards/index.md)
"""

    doc = f"""# Lab {book_no}.{chapter_no} — {title}

## Objective

{practice}

## Prerequisites

Book [{book_title}](../books/{book_no:02d}-{slug(book_title)}/index.md), chapter {chapter_no}.

## Run

```bash
python labs/{ls}/main.py
python -m pytest labs/{ls}/test_lab.py -q
```

## Exercises

1. Predict output, run `main.py`, compare.
2. Modify one mechanism-specific line and re-run tests.
3. Document normal, boundary, and adversarial cases.
4. Compare against a simpler baseline approach.

## Exit criteria

`main.py` runs cleanly and `test_lab.py` passes; you can explain *why* behavior changed, not only that it ran.
"""
    return main_py, test_py, readme, doc


STARTER_LABS: list[tuple[str, str, str, str, list[str]]] = [
    (
        "01-cosine-similarity",
        "Cosine Similarity",
        "Compute cosine similarity from first principles and rank paraphrase candidates.",
        "03-language-and-representation",
        [
            "Predict ranked output before running `main.py`.",
            "Add orthogonal and zero-vector cases to `test_lab.py`.",
            "Compare cosine vs dot product on unnormalized vectors.",
            "Document when magnitude should matter for your retrieval task.",
        ],
    ),
    (
        "02-semantic-search",
        "Semantic Search",
        "Build a hashing-vector search pipeline over a tiny document set.",
        "03-language-and-representation",
        [
            "Inspect token buckets and explain why paraphrases score higher than unrelated docs.",
            "Add a hard-negative document that shares tokens but wrong intent.",
            "Measure recall@1 on five hand-written queries.",
            "List what breaks if you change embedding dimensions.",
        ],
    ),
    (
        "03-basic-rag",
        "Basic RAG",
        "Wire retrieve → context → answer stages without an external LLM API.",
        "06-knowledge-and-retrieval-systems",
        [
            "Trace retrieval scores for a query with no lexical overlap.",
            "Add an abstention path when no evidence passes threshold.",
            "Verify citations appear only when evidence is used.",
            "Compare answer quality with k=1 vs k=2 retrieval.",
        ],
    ),
    (
        "04-agent-loop",
        "Agent Loop",
        "Run a bounded state machine with explicit plan/act/observe steps.",
        "08-agent-systems",
        [
            "Diagram the state transitions for the default goal.",
            "Add a step limit failure and verify graceful stop.",
            "Insert one invalid action and define recovery behavior.",
            "Log observations to a list you can inspect after the run.",
        ],
    ),
    (
        "05-eval-harness",
        "Eval Harness",
        "Score candidate outputs with slices and a release gate.",
        "10-evaluation-safety-and-governance",
        [
            "Add a failing general case and observe release block.",
            "Add a failing safety case and confirm it blocks release even if average score is high.",
            "Define one new slice with two cases in `main.py`.",
            "Document which metric you would track in production.",
        ],
    ),
]


def render_starter_readme(slug: str, title: str, objective: str, book: str, tasks: list[str]) -> str:
    task_lines = "\n".join(f"{i+1}. {t}" for i, t in enumerate(tasks))
    return f"""# Lab — {title}

## Objective

{objective}

## Prerequisites

- Relevant [guided book](../../docs/books/{book}/index.md) chapters
- Python 3.10+

## Time estimate

30–45 minutes

## Run

```bash
python main.py
python -m pytest test_lab.py -q
```

## Notebook

Open [`lab.ipynb`](lab.ipynb) for a guided, step-by-step version (sync your final code into `main.py`).

## Tasks

{task_lines}

## Reflection

- What broke first when you changed inputs?
- Which simpler baseline would you compare against in a design review?

## Extensions

- Add another test to `test_lab.py`
- Link your observations to a [concept card](../../docs/concepts/index.md)
"""


def render_starter_test(slug: str) -> str:
    return f'''"""Tests for starter lab {slug}."""
import subprocess
import sys
from pathlib import Path


def test_main_exits_zero():
    result = subprocess.run(
        [sys.executable, str(Path(__file__).parent / "main.py")],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip()
'''


def upgrade_starter_labs() -> int:
    for slug, title, objective, book, tasks in STARTER_LABS:
        lab_dir = LABS / slug
        if not lab_dir.is_dir():
            continue
        (lab_dir / "README.md").write_text(
            render_starter_readme(slug, title, objective, book, tasks), encoding="utf-8"
        )
    return len(STARTER_LABS)


def upgrade_labs() -> int:
    count = 0
    for book_no, book in enumerate(BOOKS, 1):
        for chapter_no, chapter in enumerate(book["chapters"], 1):
            title, _, _, practice, _ = chapter
            ls = lab_slug(book_no, chapter_no, title)
            lab_dir = LABS / ls
            lab_dir.mkdir(parents=True, exist_ok=True)
            main_py, test_py, readme, doc = render_lab_docs(
                book_no, chapter_no, title, practice, ls, book["title"]
            )
            (lab_dir / "main.py").write_text(main_py, encoding="utf-8")
            (lab_dir / "test_lab.py").write_text(test_py, encoding="utf-8")
            (lab_dir / "README.md").write_text(readme, encoding="utf-8")
            (DOCS_LABS / f"{ls}.md").write_text(doc, encoding="utf-8")
            count += 1
    return count


def update_papers_index(readings: int) -> None:
    (DOCS / "papers" / "index.md").write_text(
        f"""# Research Reading Program

Read primary sources to understand how ideas evolve, not to memorize every formula.

## Catalog

**{readings} reading summaries** in [readings/index.md](readings/index.md).

## Suggested sequence

Word2Vec → seq2seq → attention → Transformer → BERT/GPT → RAG/DPR → instruction tuning/RLHF → LoRA → ReAct → DPO → tool protocols → agent benchmarks.

## Seminar rhythm

1. State the problem without using the paper's solution.
2. Reconstruct the strongest prior approach.
3. Identify the smallest key innovation.
4. Examine evidence and ablations.
5. List limitations and invalid generalizations.
6. Trace follow-up work and the principle that survived.

Use the [paper reading template](paper-reading-template.md) for every entry.
""",
        encoding="utf-8",
    )


def main() -> None:
    readings = generate_readings()
    guides = generate_build_guides()
    generate_question_index()
    glossary = generate_glossary()
    chapter_labs = upgrade_labs()
    starter_labs = upgrade_starter_labs()
    update_papers_index(readings)
    print(
        f"Generated {readings} readings, {guides} build guides, glossary {glossary} terms, "
        f"upgraded {chapter_labs} chapter labs and {starter_labs} starter labs."
    )


if __name__ == "__main__":
    main()
