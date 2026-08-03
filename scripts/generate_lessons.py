"""Generate standalone guided lessons and index."""
from __future__ import annotations

from pathlib import Path

from catalog_helpers import _accordion_section, _cell, _markdown_table
from generate_books import BOOKS, slug
from ka_deep_content import KA_SPECS, chapter_href, lab_slug
from site_stats import collect_site_stats
from topic_knowledge import normalize

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "docs" / "lessons"
DOCS = ROOT / "docs"
CONCEPTS = DOCS / "concepts" / "cards"


def concept_href(topic: str) -> str | None:
    key = normalize(topic)
    if (CONCEPTS / f"{key}.md").is_file():
        return f"../concepts/cards/{key}.md"
    if (DOCS / "concepts" / f"{key}.md").is_file():
        return f"../concepts/{key}.md"
    return None

SUPPLEMENTAL: list[tuple[str, str, str, str, list[str], str]] = [
    ("eval-fundamentals", "Evaluation Fundamentals", "Define metrics from decisions, not convenience.", "../books/10-evaluation-safety-and-governance/01-evaluation-as-requirements.md", ["rubrics", "slices", "baselines"], "Write acceptance criteria before choosing metrics."),
    ("security-basics", "Security Basics for Assistants", "Threat-model untrusted content and tools.", "../books/10-evaluation-safety-and-governance/04-security-of-ai-systems.md", ["prompt injection", "adversarial tests", "authorization"], "Run three injection cases and document mitigations."),
    ("cost-modeling", "Cost Modeling for LLM Features", "Estimate token, retrieval, and human-review cost.", "../books/11-training-serving-and-ai-operations/06-llmops.md", ["FinOps", "batching", "model routing"], "Build unit economics for one user journey."),
    ("adr-for-ai", "Architecture Decisions for AI", "Record trade-offs with eval evidence.", "../books/12-cloud-and-enterprise-ai-architecture/06-enterprise-operating-model.md", ["audit evidence", "governance", "canaries"], "Write one ADR for a model or retrieval choice."),
    ("human-review", "Human Review Design", "Route low-confidence outputs to reviewers.", "../books/09-ai-software-and-product-engineering/05-human-centered-ai-ux.md", ["human review", "abstention", "calibration"], "Define review SLA and escalation path."),
    ("data-cards", "Data Cards and Lineage", "Document datasets used for training and eval.", "../books/11-training-serving-and-ai-operations/03-dataset-engineering.md", ["data provenance", "data curation", "slices"], "Produce a data card for one eval set."),
    ("hybrid-search-lab", "Hybrid Search Deep Dive", "Combine lexical and dense retrieval with fusion.", "../guides/hybrid-search-engine.md", ["BM25", "dense retrieval", "hybrid search"], "Show a query where fusion beats either method alone."),
    ("citation-quality", "Citation Quality", "Validate that answers align with sources.", "../books/06-knowledge-and-retrieval-systems/05-rag-generation-and-citations.md", ["faithfulness", "RAG", "retrieval"], "Flag one unsupported sentence in a generated answer."),
    ("tool-contracts", "Tool Contracts", "Design JSON schemas and auth for tools.", "../books/07-reasoning-and-tool-use/04-tools-as-capability-boundaries.md", ["tool schemas", "function calling", "authorization"], "Reject one out-of-schema tool call in tests."),
    ("agent-checkpoints", "Agent Checkpoints", "Persist state across failures.", "../books/08-agent-systems/03-agent-memory-and-recovery.md", ["checkpoints", "idempotency", "recovery"], "Resume an agent after simulated crash."),
    ("mcp-integration", "MCP Integration", "Connect clients to tool servers with MCP.", "../books/07-reasoning-and-tool-use/05-mcp-and-integration-protocols.md", ["MCP", "tool schemas", "function calling"], "List tools from a mock MCP server."),
    ("structured-outputs", "Structured Outputs in Production", "Validate JSON against business schemas.", "../books/05-prompt-and-context-engineering/02-structured-generation.md", ["JSON Schema", "structured output", "validation"], "Repair or reject invalid model JSON."),
    ("long-context", "Long Context Trade-offs", "Choose long context vs RAG vs fine-tune.", "../books/13-multimodal-and-frontier-systems/05-long-context-world-models-and-continual-learning.md", ["context windows", "RAG", "chunking"], "Compare cost/latency for three grounding strategies."),
    ("multimodal-docs", "Document Intelligence", "Parse layout and extract fields with provenance.", "../books/13-multimodal-and-frontier-systems/01-vision-and-document-intelligence.md", ["OCR", "vision encoders", "provenance"], "Extract three fields with source coordinates."),
    ("cloud-landing", "Cloud Landing Zone for AI", "Map capabilities to providers neutrally.", "../cloud/capabilities/index.md", ["identity", "authentication", "tracing"], "Fill capability map for one architecture."),
    ("canary-releases", "Canary Releases for Models", "Compare live metrics with guardrails.", "../guides/eval-gated-release.md", ["canaries", "slices", "monitoring"], "Define canary success and abort criteria."),
    ("red-team-basics", "Red Team Basics", "Maintain attack suites in CI.", "../guides/red-team-security-harness.md", ["adversarial tests", "prompt injection", "slices"], "Add one novel injection case to the suite."),
    ("spec-writing", "Specification Writing", "Turn ambiguous asks into testable specs.", "../books/09-ai-software-and-product-engineering/02-specification-driven-development.md", ["functional specifications", "acceptance criteria", "contract tests"], "Convert one user story into executable examples."),
    ("coding-agents", "Coding Agent Workspace", "Configure repo instructions and review gates.", "../guides/coding-agent-workspace.md", ["skills", "repo instructions", "code review"], "Complete one bounded task with review checklist."),
    ("enterprise-rag", "Enterprise RAG Overview", "End-to-end grounded retrieval system.", "../guides/enterprise-rag-end-to-end.md", ["RAG", "hybrid search", "faithfulness"], "Diagram ingestion-to-answer path with ACLs."),
    ("reasoning-economics", "Reasoning Economics", "Budget test-time compute deliberately.", "../books/07-reasoning-and-tool-use/06-reasoning-system-economics.md", ["test-time compute", "planning", "verifiers"], "Compare cost/quality for single-pass vs multi-step."),
    ("multi-agent", "Multi-Agent Coordination", "Supervisor–worker patterns and failure handling.", "../books/08-agent-systems/05-multi-agent-systems.md", ["supervisor-worker", "checkpoints", "planning"], "Document one handoff failure and fix."),
    ("product-discovery", "AI Product Discovery", "Find problems worth automating.", "../books/09-ai-software-and-product-engineering/01-discovering-the-right-problem.md", ["user research", "baseline workflow", "ROI"], "Interview workflow and quantify baseline pain."),
    ("adoption-metrics", "Adoption and Value", "Measure usage persistence after launch.", "../books/09-ai-software-and-product-engineering/06-experiments-adoption-and-value.md", ["adoption", "A/B tests", "monitoring"], "Define primary and guardrail metrics for an experiment."),
    ("responsible-ai", "Responsible AI Review", "Assess harm, bias, and misuse paths.", "../books/10-evaluation-safety-and-governance/05-responsible-ai-and-risk.md", ["human evaluation", "values", "slices"], "Complete a risk worksheet for one feature."),
    ("governance", "Governance and Assurance", "Inventory models and enforce release gates.", "../books/10-evaluation-safety-and-governance/06-governance-and-assurance.md", ["AI inventory", "audit evidence", "governance"], "List owners and evidence for one production model."),
    ("lora-practice", "LoRA in Practice", "Adapt a base model with low-rank adapters.", "../guides/fine-tune-and-serve.md", ["LoRA", "SFT", "slices"], "Compare base vs adapter on held-out slice."),
    ("serving-basics", "Serving and Routing", "Deploy endpoints with fallbacks.", "../books/11-training-serving-and-ai-operations/05-deployment-and-routing.md", ["model routing", "fallback degrade", "autoscaling"], "Load-test one endpoint and record P95 latency."),
    ("quantization", "Quantization Trade-offs", "Reduce memory with quality checks.", "../books/11-training-serving-and-ai-operations/04-inference-infrastructure.md", ["quantization", "KV cache", "batching"], "Measure quality delta for one quantized model."),
    ("identity-trust", "Identity and Trust Boundaries", "Separate tenants and secrets.", "../books/12-cloud-and-enterprise-ai-architecture/02-identity-data-and-trust-boundaries.md", ["authentication", "authorization", "multi-tenancy"], "Diagram trust zones for one assistant."),
    ("aws-ai-map", "AWS Managed AI Map", "Translate capabilities to AWS services.", "../books/12-cloud-and-enterprise-ai-architecture/03-aws-managed-ai.md", ["Amazon Bedrock", "SageMaker", "hybrid search"], "Map one architecture to AWS SKUs."),
    ("azure-ai-map", "Azure Managed AI Map", "Translate capabilities to Azure services.", "../books/12-cloud-and-enterprise-ai-architecture/04-azure-managed-ai.md", ["Azure OpenAI", "Azure AI Search", "authentication"], "Map one architecture to Azure SKUs."),
    ("gcp-ai-map", "Google Cloud AI Map", "Translate capabilities to GCP services.", "../books/12-cloud-and-enterprise-ai-architecture/05-google-cloud-and-portable-patterns.md", ["Vertex AI", "Cloud IAM", "portable interfaces"], "Map one architecture to GCP SKUs."),
    ("speech-basics", "Speech and Audio Pipelines", "ASR and TTS integration patterns.", "../books/13-multimodal-and-frontier-systems/02-speech-and-audio.md", ["speech recognition", "latency", "batching"], "Transcribe a sample clip and measure WER proxy."),
    ("image-gen", "Image Generation Controls", "Safety, provenance, and cost for generative media.", "../books/13-multimodal-and-frontier-systems/03-image-and-video-generation.md", ["provenance", "responsible AI", "monitoring"], "Document policy for generated asset storage."),
    ("computer-use", "Computer Use Risks", "Bound UI automation actions.", "../books/13-multimodal-and-frontier-systems/04-computer-use-and-embodied-action.md", ["action spaces", "approval gates", "tool sandbox"], "List irreversible actions requiring approval."),
    ("frontier-tracking", "Track the Frontier", "Evaluate hype with reproduction discipline.", "../books/13-multimodal-and-frontier-systems/06-how-to-track-the-frontier.md", ["reproduction", "benchmarks", "ablations"], "Reproduce one small claim with baseline."),
    ("paper-reading", "Read a Paper Critically", "Extract claims, evidence, and limits.", "../papers/paper-reading-template.md", ["ablations", "scaling laws", "reproduction"], "Summarize one paper using the template."),
    ("transformer-paper", "Transformer Paper Seminar", "Connect Attention Is All You Need to code.", "../papers/readings/transformer.md", ["multi-head attention", "position", "residual connections"], "Sketch one encoder block diagram from memory."),
    ("rag-paper", "RAG Paper Seminar", "Ground generation with retrieved evidence.", "../papers/readings/rag.md", ["RAG", "retrieval", "faithfulness"], "Identify one failure mode RAG does not fix."),
    ("rlhf-paper", "RLHF and Preferences", "Align models with human feedback.", "../papers/readings/instructgpt.md", ["SFT", "human evaluation", "instruction tuning"], "Contrast SFT-only vs preference-trained behavior."),
    ("agent-benchmarks", "Agent Benchmarks", "Interpret WebArena-style evaluations.", "../papers/readings/agent-benchmark-webarena.md", ["benchmarks", "action spaces", "task success"], "Define success criteria for one agent task."),
    ("mcp-spec-lesson", "MCP Specification", "Standardize tool and resource access.", "../papers/readings/mcp-spec.md", ["MCP", "tool schemas", "portable interfaces"], "Compare MCP to ad-hoc REST tool wrappers."),
]


def render_lesson(
    lesson_id: str,
    title: str,
    objective: str,
    read_link: str,
    concepts: list[str],
    exercise: str,
    lab_link: str | None = None,
) -> str:
    concept_lines = "\n".join(
        f"- [{c}]({href})"
        for c in concepts
        if (href := concept_href(c))
    ) or "- See the [concept card index](../concepts/cards/index.md)."
    lab_section = f"\n## Practice\n\n- Run [lab]({lab_link})\n" if lab_link else ""
    return f"""# {title}

**Lesson ID:** `{lesson_id}`

## Objective

{objective}

## Read

- Primary: [{title}]({read_link})

## Core concepts

{concept_lines}

## Exercise

{exercise}
{lab_section}
## Check yourself

1. What problem does this lesson solve that a generic LLM call does not?
2. What baseline would you compare against before adding complexity?
3. What failure mode appears first under stress?

## Unlock

Completing this lesson prepares you for the next item in your [knowledge-area path](../knowledge-areas/index.md) and related [build guides](../guides/index.md).
"""


def normalize_slug(topic: str) -> str:
    import re
    return re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")


def title_from_slug(s: str) -> str:
    return " ".join(w if w.isupper() and len(w) <= 4 else w.capitalize() for w in s.split("-"))


def render_lessons_index(
    ka_groups: list[tuple[str, str, list[tuple[str, str, str, str, str | None]]]],
    supplemental: list[tuple[str, str, str, str]],
) -> str:
    stats = collect_site_stats()
    lines = [
        "# Guided Lessons",
        "",
        f"**{stats.total_lessons} guided lessons** — {stats.ka_lessons} aligned to knowledge areas "
        f"plus {stats.supplemental_lessons} supplemental cross-cutting lessons.",
        "",
        "Each row links the lesson, chapter reading, matching lab, and objective. "
        "Expand a knowledge area or use search (`/`).",
        "",
    ]
    for ka_file, ka_title, items in ka_groups:
        rows = [
            [
                f"`{lesson_id}`",
                f"[{title}]({lesson_id}.md)",
                _cell(objective, None),
                f"[chapter]({read_link})",
                f"[lab]({lab_link})" if lab_link else "—",
            ]
            for lesson_id, title, objective, read_link, lab_link in items
        ]
        lines.append(
            _accordion_section(
                f"{ka_title} · `{ka_file}` ({len(items)})",
                _markdown_table(["ID", "Lesson", "Objective", "Read", "Lab"], rows),
            )
        )
    if supplemental:
        rows = [
            [
                f"`{lesson_id}`",
                f"[{title}]({lesson_id}.md)",
                _cell(objective, None),
                f"[reading]({read_link})",
            ]
            for lesson_id, title, objective, read_link in supplemental
        ]
        lines.append(
            _accordion_section(
                f"Supplemental cross-cutting ({len(supplemental)})",
                _markdown_table(["ID", "Lesson", "Objective", "Read"], rows),
            )
        )
    return "\n".join(lines) + "\n"


def generate() -> int:
    LESSONS.mkdir(parents=True, exist_ok=True)
    ka_groups: list[tuple[str, str, list[tuple[str, str, str, str, str | None]]]] = []
    ka_index: dict[str, int] = {}
    count = 0

    for ka_file, ka_title, _, book_no, _, _, lesson_indices in KA_SPECS:
        if ka_file not in ka_index:
            ka_index[ka_file] = len(ka_groups)
            ka_groups.append((ka_file, ka_title, []))
        group_items = ka_groups[ka_index[ka_file]][2]

        for i, ch_no in enumerate(lesson_indices, 1):
            lesson_id = f"{ka_file}-{i:02d}"
            href, ch_title = chapter_href(book_no, ch_no)
            ch = BOOKS[book_no - 1]["chapters"][ch_no - 1]
            ls = lab_slug(book_no, ch_no, ch_title)
            concepts = ch[2][:3]
            text = render_lesson(
                lesson_id,
                ch_title,
                ch[3],
                href.replace("../", "../"),  # from docs/lessons -> ../books/...
                concepts,
                f"Apply the chapter insight: {ch[4]}",
                f"../labs/{ls}.md",
            )
            (LESSONS / f"{lesson_id}.md").write_text(text, encoding="utf-8")
            group_items.append((lesson_id, ch_title, ch[3], href, f"../labs/{ls}.md"))
            count += 1

    supplemental: list[tuple[str, str, str, str]] = []
    for slug_id, title, objective, read_link, concepts, exercise in SUPPLEMENTAL:
        lesson_id = f"sup-{slug_id}"
        text = render_lesson(lesson_id, title, objective, read_link, concepts, exercise)
        (LESSONS / f"{lesson_id}.md").write_text(text, encoding="utf-8")
        supplemental.append((lesson_id, title, objective, read_link))
        count += 1

    (LESSONS / "index.md").write_text(render_lessons_index(ka_groups, supplemental), encoding="utf-8")
    return count


def main() -> None:
    n = generate()
    print(f"Generated {n} guided lessons.")


if __name__ == "__main__":
    main()
