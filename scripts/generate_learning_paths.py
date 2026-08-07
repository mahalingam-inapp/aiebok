"""Generate role-based learning paths with ordered chapter, lab, and guide links."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from generate_books import BOOKS, slug
from generate_expansion import lab_slug
from generate_maturity_content import STARTER_LABS

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "docs" / "getting-started" / "learning-paths"
REPO_BLOB = "https://github.com/mahalingam-inapp/aiebok/blob/main"
DOCS_PREFIX = "../.."
START_HERE_PREFIX = ".."

PATH_ICONS = [
    "map-legend",
    "robot",
    "sitemap",
    "chart-line",
    "school",
]


def _link(label: str, href: str) -> str:
    return f'[{label}]({href}){{target="_blank" rel="noopener"}}'


def _book_dir(book_no: int) -> str:
    return f"{book_no:02d}-{slug(BOOKS[book_no - 1]['title'])}"


def _chapter_href(book_no: int, chapter_no: int) -> str:
    title = BOOKS[book_no - 1]["chapters"][chapter_no - 1][0]
    return f"{DOCS_PREFIX}/books/{_book_dir(book_no)}/{chapter_no:02d}-{slug(title)}.md"


def _chapter_label(book_no: int, chapter_no: int) -> str:
    title = BOOKS[book_no - 1]["chapters"][chapter_no - 1][0]
    return f"Book {book_no:02d} · Ch. {chapter_no} — {title}"


def _lab_href(book_no: int, chapter_no: int) -> str:
    title = BOOKS[book_no - 1]["chapters"][chapter_no - 1][0]
    return f"{DOCS_PREFIX}/labs/{lab_slug(book_no, chapter_no, title)}.md"


def _lab_label(book_no: int, chapter_no: int) -> str:
    title = BOOKS[book_no - 1]["chapters"][chapter_no - 1][0]
    return f"Lab {book_no:02d}.{chapter_no:02d} — {title}"


def _starter_notebook_href(slug_name: str) -> str:
    return f"{REPO_BLOB}/labs/{slug_name}/lab.ipynb"


@dataclass(frozen=True)
class Step:
    kind: str
    label: str
    href: str


def chapter_step(book_no: int, chapter_no: int) -> Step:
    return Step("Chapter", _chapter_label(book_no, chapter_no), _chapter_href(book_no, chapter_no))


def lab_step(book_no: int, chapter_no: int) -> Step:
    return Step("Lab", _lab_label(book_no, chapter_no), _lab_href(book_no, chapter_no))


def starter_step(slug_name: str) -> Step:
    title = next(row[1] for row in STARTER_LABS if row[0] == slug_name)
    return Step(
        "Starter lab",
        f"Starter lab — {title} (notebook)",
        _starter_notebook_href(slug_name),
    )


def guide_step(slug_name: str, label: str | None = None) -> Step:
    return Step("Build guide", label or slug_name.replace("-", " ").title(), f"{DOCS_PREFIX}/guides/{slug_name}.md")


def architecture_step(slug_name: str, label: str | None = None) -> Step:
    return Step(
        "Architecture studio",
        label or slug_name.replace("-", " ").title(),
        f"{DOCS_PREFIX}/architectures/{slug_name}.md",
    )


def page_step(kind: str, label: str, filename: str) -> Step:
    return Step(kind, label, f"{START_HERE_PREFIX}/{filename}")


def book_sequence(book_no: int, chapters: range | list[int] | None = None) -> list[Step]:
    book = BOOKS[book_no - 1]
    indices = list(chapters) if chapters is not None else range(1, len(book["chapters"]) + 1)
    steps: list[Step] = []
    for chapter_no in indices:
        steps.append(chapter_step(book_no, chapter_no))
        steps.append(lab_step(book_no, chapter_no))
    return steps


def full_curriculum_with_starters() -> list[Step]:
    """Books 01–13 in order, chapter + lab, with starter labs at canonical checkpoints."""
    starter_after: dict[tuple[int, int], str] = {
        (3, 5): "01-cosine-similarity",
        (3, 6): "02-semantic-search",
        (6, 3): "03-basic-rag",
        (8, 2): "04-agent-loop",
        (10, 1): "05-eval-harness",
    }
    steps: list[Step] = []
    for book_no in range(1, len(BOOKS) + 1):
        for chapter_no in range(1, len(BOOKS[book_no - 1]["chapters"]) + 1):
            steps.append(chapter_step(book_no, chapter_no))
            steps.append(lab_step(book_no, chapter_no))
            starter = starter_after.get((book_no, chapter_no))
            if starter:
                steps.append(starter_step(starter))
    return steps


@dataclass(frozen=True)
class LearningPath:
    rank: int
    title: str
    duration: str
    audience: str
    outcome: str
    steps: tuple[Step, ...]


PATHS: tuple[LearningPath, ...] = (
    LearningPath(
        rank=1,
        title="Product & technical leader",
        duration="~8 weeks",
        audience="Product managers and technical leaders who need capability literacy, risk framing, and build-versus-buy judgment—not daily implementation.",
        outcome="Explain model boundaries, evaluation gates, responsible-AI trade-offs, and enterprise adoption patterns to engineering and business stakeholders.",
        steps=(
            page_step("Orientation", "First 30 minutes — local setup and site map", "first-30-minutes.md"),
            page_step("Orientation", "How to use AIEBOK", "how-to-use.md"),
            chapter_step(4, 6),
            chapter_step(5, 1),
            chapter_step(5, 5),
            guide_step("model-selection-harness", "Build guide — model selection harness"),
            chapter_step(10, 1),
            lab_step(10, 1),
            starter_step("05-eval-harness"),
            chapter_step(10, 5),
            guide_step("eval-gated-release", "Build guide — eval-gated release"),
            chapter_step(9, 6),
            chapter_step(12, 1),
            lab_step(12, 1),
            architecture_step("enterprise-rag", "Architecture studio — enterprise RAG"),
            chapter_step(12, 6),
            guide_step("enterprise-rag-end-to-end", "Build guide — enterprise RAG end-to-end"),
        ),
    ),
    LearningPath(
        rank=2,
        title="Coding-agent specialist",
        duration="~10 weeks",
        audience="Software engineers building spec-to-code workflows, tool-using agents, and guarded automation with explicit approval gates.",
        outcome="Ship a bounded coding-agent workflow with structured outputs, tool boundaries, regression evals, and a documented approval policy.",
        steps=(
            page_step("Orientation", "First 30 minutes — clone repo and run MkDocs", "first-30-minutes.md"),
            page_step("Orientation", "Spec-driven workflow — OpenSpec + Cursor", "spec-driven-workflow.md"),
            chapter_step(3, 5),
            lab_step(3, 5),
            starter_step("01-cosine-similarity"),
            chapter_step(3, 6),
            lab_step(3, 6),
            starter_step("02-semantic-search"),
            chapter_step(5, 1),
            lab_step(5, 1),
            chapter_step(5, 2),
            lab_step(5, 2),
            guide_step("structured-extraction-api", "Build guide — structured extraction API"),
            chapter_step(5, 3),
            lab_step(5, 3),
            guide_step("context-engine-with-tests", "Build guide — context engine with tests"),
            chapter_step(7, 4),
            lab_step(7, 4),
            chapter_step(8, 1),
            lab_step(8, 1),
            chapter_step(8, 2),
            lab_step(8, 2),
            starter_step("04-agent-loop"),
            guide_step("bounded-agent-assistant", "Build guide — bounded agent assistant"),
            chapter_step(9, 2),
            lab_step(9, 2),
            chapter_step(9, 3),
            lab_step(9, 3),
            guide_step("coding-agent-workspace", "Build guide — coding-agent workspace"),
            guide_step("spec-to-production-feature", "Build guide — spec to production feature"),
            chapter_step(10, 1),
            lab_step(10, 1),
            starter_step("05-eval-harness"),
            chapter_step(10, 4),
            lab_step(10, 4),
            guide_step("red-team-security-harness", "Build guide — red-team security harness"),
        ),
    ),
    LearningPath(
        rank=3,
        title="Software architect",
        duration="~12 weeks",
        audience="Architects designing production AI systems who need cross-cutting views of models, retrieval, agents, safety, and cloud landing zones.",
        outcome="Produce five ADRs and two threat models covering retrieval, agent orchestration, evaluation gates, and enterprise deployment boundaries.",
        steps=(
            chapter_step(1, 1),
            chapter_step(4, 6),
            lab_step(4, 6),
            chapter_step(5, 3),
            lab_step(5, 3),
            chapter_step(6, 1),
            lab_step(6, 1),
            chapter_step(6, 3),
            lab_step(6, 3),
            starter_step("03-basic-rag"),
            chapter_step(6, 6),
            lab_step(6, 6),
            architecture_step("enterprise-rag", "Architecture studio — enterprise RAG"),
            guide_step("enterprise-rag-end-to-end", "Build guide — enterprise RAG end-to-end"),
            chapter_step(7, 4),
            lab_step(7, 4),
            chapter_step(8, 1),
            lab_step(8, 1),
            chapter_step(8, 4),
            lab_step(8, 4),
            chapter_step(9, 1),
            lab_step(9, 1),
            chapter_step(10, 1),
            lab_step(10, 1),
            chapter_step(10, 4),
            lab_step(10, 4),
            chapter_step(11, 4),
            lab_step(11, 4),
            chapter_step(12, 1),
            lab_step(12, 1),
            chapter_step(12, 2),
            lab_step(12, 2),
            chapter_step(12, 3),
            lab_step(12, 3),
            architecture_step("multi-cloud-ai-landing-zone", "Architecture studio — multi-cloud AI landing zone"),
        ),
    ),
    LearningPath(
        rank=4,
        title="ML engineer",
        duration="~16 weeks",
        audience="Machine-learning engineers focused on training pipelines, embeddings, transformers, serving, and operational evaluation—not product UX.",
        outcome="Deliver a fine-tuned or adapted model with profiling, slice evaluation, serving plan, and LLMOps monitoring hooks.",
        steps=(
            *book_sequence(2),
            chapter_step(3, 4),
            lab_step(3, 4),
            chapter_step(3, 5),
            lab_step(3, 5),
            starter_step("01-cosine-similarity"),
            chapter_step(3, 6),
            lab_step(3, 6),
            starter_step("02-semantic-search"),
            chapter_step(4, 1),
            lab_step(4, 1),
            chapter_step(4, 2),
            lab_step(4, 2),
            chapter_step(4, 3),
            lab_step(4, 3),
            chapter_step(4, 4),
            lab_step(4, 4),
            guide_step("model-selection-harness", "Build guide — model selection harness"),
            chapter_step(11, 1),
            lab_step(11, 1),
            chapter_step(11, 2),
            lab_step(11, 2),
            chapter_step(11, 3),
            lab_step(11, 3),
            chapter_step(11, 4),
            lab_step(11, 4),
            guide_step("fine-tune-and-serve", "Build guide — fine-tune and serve"),
            chapter_step(11, 6),
            lab_step(11, 6),
            chapter_step(10, 2),
            lab_step(10, 2),
            chapter_step(10, 3),
            lab_step(10, 3),
            guide_step("eval-gated-release", "Build guide — eval-gated release"),
        ),
    ),
    LearningPath(
        rank=5,
        title="AI engineer",
        duration="~24 weeks",
        audience="Practitioners building end-to-end AI systems who want the full AIEBOK arc—foundations through frontier systems—with runnable evidence at every stage.",
        outcome="Complete the thirteen-book curriculum, five starter labs, and a capstone project with evaluation, failure analysis, and architecture defense.",
        steps=tuple(full_curriculum_with_starters()),
    ),
)


def path_filename(path: LearningPath) -> str:
    return f"{path.rank:02d}-{slug(path.title)}.md"


def _clip(text: str, limit: int) -> str:
    clean = text.replace("\n", " ").strip()
    if len(clean) <= limit:
        return clean
    return clean[: limit - 1].rstrip() + "…"


def render_path_overview(paths: tuple[LearningPath, ...]) -> str:
    lines = ['<div class="grid cards" markdown>', ""]
    for path in paths:
        icon = PATH_ICONS[path.rank - 1]
        filename = path_filename(path)
        lines.extend(
            [
                f"-   :material-{icon}:{{ .lg .middle }} __{path.title}__",
                "",
                f"    **{path.duration}** · {len(path.steps)} steps · {_clip(path.audience, 95)}",
                "",
                f"    [Open path →]({filename})",
                "",
            ]
        )
    lines.extend(["</div>", ""])
    return "\n".join(lines)


def render_path_table(steps: tuple[Step, ...]) -> str:
    lines = [
        "| Step | Type | Open |",
        "|:---:|---|---|",
    ]
    for index, step in enumerate(steps, 1):
        lines.append(f"| **{index}** | {step.kind} | {_link(step.label, step.href)} |")
    return "\n".join(lines)


def render_index_page(paths: tuple[LearningPath, ...]) -> str:
    lines = [
        "# Learning Paths",
        "",
        "Role-based **sequences** that mix chapters, labs, build guides, and architecture studios "
        "in the order we recommend. Paths are sorted from **least to most** technical depth and time commitment.",
        "",
        "Each path has its **own page** so you can bookmark or share a direct link.",
        "",
        "!!! tip \"Keep your path page open\"",
        "    Every step link opens in a **new tab** so you can treat the path page as your checklist while reading or coding.",
        "",
        "## Choose a path",
        "",
        render_path_overview(paths),
        "## All paths",
        "",
        "| # | Path | Duration | Steps |",
        "|:---:|---|---|---:|",
    ]
    for path in paths:
        filename = path_filename(path)
        lines.append(
            f"| {path.rank} | [{path.title}]({filename}) | {path.duration} | {len(path.steps)} |"
        )
    lines.extend(
        [
            "",
            "## How to use a path",
            "",
            "1. Pick the path that matches your role and available time.",
            "2. Work through steps **in order**—read the chapter, then run the matching lab when one appears.",
            "3. Starter-lab steps link to **notebooks in the repository**; chapter and guide steps stay on this site.",
            "4. When a path references an architecture studio, sketch an ADR or threat model before moving on.",
            "",
            "## Related",
            "",
            f"- {_link('Newcomer guide', f'{START_HERE_PREFIX}/newcomer-guide.md')}",
            f"- {_link('Hands-on start', f'{DOCS_PREFIX}/labs/start-here.md')}",
            f"- {_link('Book catalog', f'{DOCS_PREFIX}/books/index.md')}",
            f"- {_link('Build guides', f'{DOCS_PREFIX}/guides/index.md')}",
            "",
        ]
    )
    return "\n".join(lines)


def render_path_page(path: LearningPath, paths: tuple[LearningPath, ...]) -> str:
    prev_path = next((p for p in paths if p.rank == path.rank - 1), None)
    next_path = next((p for p in paths if p.rank == path.rank + 1), None)
    nav_lines = ["## Path navigation", ""]
    if prev_path:
        nav_lines.append(f"← Previous: [{prev_path.title}]({path_filename(prev_path)})")
    else:
        nav_lines.append(f"← [All learning paths](index.md)")
    nav_lines.append("")
    if next_path:
        nav_lines.append(f"Next: [{next_path.title}]({path_filename(next_path)}) →")
    nav_lines.append("")

    return "\n".join(
        [
            f"# {path.title}",
            "",
            f"**Duration:** {path.duration} · **Steps:** {len(path.steps)} · **Complexity rank:** {path.rank} of {len(paths)}",
            "",
            path.audience,
            "",
            f"**Outcome:** {path.outcome}",
            "",
            "!!! tip \"Share this path\"",
            f"    Send this page URL to teammates who need the **{path.title}** track.",
            "",
            "## Sequence",
            "",
            render_path_table(path.steps),
            "",
            *nav_lines,
            "## Related",
            "",
            f"- [Learning paths overview](index.md)",
            f"- {_link('Newcomer guide', f'{START_HERE_PREFIX}/newcomer-guide.md')}",
            f"- {_link('Hands-on start', f'{DOCS_PREFIX}/labs/start-here.md')}",
            "",
        ]
    )


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ordered = tuple(sorted(PATHS, key=lambda path: path.rank))
    (OUTPUT_DIR / "index.md").write_text(render_index_page(ordered), encoding="utf-8")
    for path in ordered:
        (OUTPUT_DIR / path_filename(path)).write_text(
            render_path_page(path, ordered), encoding="utf-8"
        )
    legacy = ROOT / "docs" / "getting-started" / "learning-paths.md"
    if legacy.is_file():
        legacy.unlink()
    print(f"Wrote {OUTPUT_DIR.relative_to(ROOT)} ({len(PATHS)} path pages + index).")


if __name__ == "__main__":
    main()
