"""Shared accordion catalog formatting for generated index pages."""
from __future__ import annotations


def title_from_slug(s: str) -> str:
    return " ".join(w if w.isupper() and len(w) <= 4 else w.capitalize() for w in s.split("-"))


def _cell(text: str, limit: int | None = 120) -> str:
    clean = text.replace("|", "\\|").replace("\n", " ").strip()
    if limit is not None and len(clean) > limit:
        return clean[: limit - 1] + "…"
    return clean


def _accordion_section(title: str, body_lines: list[str]) -> str:
    indented = "\n".join(f"    {line}" for line in body_lines)
    return f'??? abstract "{title}"\n{indented}\n'


def _markdown_table(headers: list[str], rows: list[list[str]]) -> list[str]:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    return lines


def render_grouped_table_catalog(
    title: str,
    intro_lines: list[str],
    groups: dict[str, list[list[str]]],
    headers: list[str],
    *,
    sort_groups: bool = True,
) -> str:
    lines = [f"# {title}", ""] + intro_lines + [""]
    keys = sorted(groups) if sort_groups else list(groups)
    for group in keys:
        rows = groups[group]
        body = _markdown_table(headers, rows)
        lines.append(_accordion_section(f"{group} ({len(rows)})", body))
    return "\n".join(lines) + "\n"


def render_letter_link_index(
    title: str,
    intro_lines: list[str],
    keys: list[str],
    link_fn,
    headers: list[str] | None = None,
) -> str:
    by_letter: dict[str, list[str]] = {}
    for key in keys:
        letter = key[0].upper() if key else "#"
        if not letter.isalpha():
            letter = "#"
        by_letter.setdefault(letter, []).append(key)

    column_headers = headers or ["Topic"]
    groups: dict[str, list[list[str]]] = {}
    for letter in by_letter:
        items = sorted(by_letter[letter])
        rows = []
        for key in items:
            row = link_fn(key)
            rows.append(row if isinstance(row, list) else [row])
        groups[letter if letter != "#" else "0–9"] = rows

    return render_grouped_table_catalog(title, intro_lines, groups, column_headers)


def render_letter_bullet_index(
    title: str,
    intro_lines: list[str],
    entries: list[tuple[str, str]],
) -> str:
    """entries: (letter_key, bullet_line) sorted by letter_key then line."""
    by_letter: dict[str, list[str]] = {}
    for letter_key, line in entries:
        by_letter.setdefault(letter_key, []).append(line)

    lines = [f"# {title}", ""] + intro_lines + [""]
    for letter in sorted(by_letter):
        body = by_letter[letter]
        label = letter if letter != "#" else "0–9"
        lines.append(_accordion_section(f"{label} ({len(body)})", body))
    return "\n".join(lines) + "\n"


def classify_paper(key: str) -> str:
    if key in {
        "word2vec", "seq2seq", "attention-paper", "transformer", "bert", "elmo",
        "knowledge-distillation", "knowledge-neurons", "moe",
    }:
        return "Foundations & architecture"
    if key in {
        "gpt2", "gpt3", "t5", "scaling-laws", "chinchilla", "llama", "palm", "olmo",
        "mistral", "mixtral", "nemotron", "orca", "gqa", "rope", "sparse-autoencoder",
    }:
        return "Scale, open models & efficiency"
    if key in {
        "instructgpt", "dpo", "constitutional-ai", "self-instruct", "helpful-harmless",
        "rlhf-preference", "jailbreak-survey", "jailbreak-taxonomy",
    }:
        return "Alignment & safety"
    if key in {
        "rag", "dpr", "graph-rag", "ragas", "react", "toolformer", "mcp-spec",
        "agent-benchmark-webarena", "swebench",
    }:
        return "RAG, tools & agents"
    if key in {
        "lora", "qlora", "flash-attention", "speculative-decoding", "mamba", "clip", "whisper",
        "chain-of-thought", "tree-of-thoughts",
    }:
        return "Training, inference & reasoning"
    return "Other readings"


def classify_cloud_capability(slug: str) -> str:
    if slug in {
        "foundation-model-apis", "embedding-apis", "batch-inference", "real-time-inference",
        "model-fine-tuning", "container-serving", "gpu-compute", "edge-inference",
    }:
        return "Models & inference"
    if slug in {
        "vector-databases", "hybrid-search-services", "document-ingestion", "data-lake-for-ai",
    }:
        return "Retrieval & data"
    if slug in {
        "model-registry", "feature-stores", "ml-pipelines", "serverless-ai", "workflow-orchestration",
    }:
        return "MLOps & pipelines"
    return "Platform, security & governance"


def classify_guide(slug: str) -> str:
    if slug in {"enterprise-rag-end-to-end", "hybrid-search-engine", "multi-tenant-retrieval"}:
        return "Retrieval & knowledge"
    if slug in {"bounded-agent-assistant", "coding-agent-workspace"}:
        return "Agents & automation"
    if slug in {"eval-gated-release", "model-selection-harness", "red-team-security-harness"}:
        return "Evaluation & safety"
    if slug in {"context-engine-with-tests", "structured-extraction-api", "spec-to-production-feature"}:
        return "Product & context engineering"
    if slug in {"fine-tune-and-serve", "multimodal-document-pipeline"}:
        return "Training & multimodal"
    return "Other guides"
