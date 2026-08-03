"""Build a lightweight companion PDF for offline study (static asset on GitHub Pages)."""
from __future__ import annotations

from pathlib import Path

from fpdf import FPDF
from fpdf.enums import XPos, YPos
from generate_books import BOOKS, slug
from topic_knowledge import TOPIC_FACTS, get_topic_entry

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "docs" / "assets"
OUTPUT = ASSETS / "aiebok-companion.pdf"


def ascii_safe(text: str) -> str:
    """Keep PDF core-font output compatible with Helvetica latin-1."""
    return (
        text.replace("\u2014", " - ")
        .replace("\u2013", "-")
        .replace("\u2018", "'")
        .replace("\u2019", "'")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
        .replace("\u2026", "...")
        .encode("latin-1", errors="replace")
        .decode("latin-1")
    )


class CompanionPDF(FPDF):
    def footer(self) -> None:
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(
            0,
            10,
            ascii_safe(f"AIEBOK Companion - page {self.page_no()}"),
            align="C",
        )


def add_wrapped(pdf: FPDF, text: str, size: int = 10) -> None:
    pdf.set_font("Helvetica", size=size)
    pdf.multi_cell(0, 5, ascii_safe(text))
    pdf.ln(2)


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    pdf = CompanionPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 12, "AIEBOK Companion", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "", 11)
    add_wrapped(
        pdf,
        "Offline study companion for the AI Engineering Body of Knowledge. "
        "The full interactive site includes labs, notebooks, and search. "
        "This PDF summarizes structure, books, and a glossary sample.",
    )

    pdf.add_page()
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, "Guided books", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "", 10)
    for i, book in enumerate(BOOKS, 1):
        add_wrapped(pdf, f"{i:02d}. {book['title']} - {book['goal'][:200]}")

    pdf.add_page()
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, "Glossary sample (A-C)", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", "", 9)
    for key in sorted(TOPIC_FACTS)[:80]:
        expl, _, _ = get_topic_entry(key)
        line = f"{key}: {expl.split('.')[0]}."
        if len(line) > 120:
            line = line[:117] + "..."
        add_wrapped(pdf, line, size=9)

    pdf.add_page()
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, "Using this with GitHub Pages", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    add_wrapped(
        pdf,
        "Host: deploy MkDocs to GitHub Pages (static HTML). "
        "Labs: run Python locally or in GitHub Codespaces / Dev Container. "
        "Starter lab notebooks: open lab.ipynb from the labs/ directory in the repository. "
        "Print full site: use the Print Site plugin page in the Reference section.",
    )

    pdf.output(str(OUTPUT))
    print(f"Wrote {OUTPUT} ({OUTPUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
