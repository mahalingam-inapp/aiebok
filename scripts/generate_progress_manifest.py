"""Generate progress-manifest.json for the client-side reading tracker."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from generate_books import BOOKS, slug
from site_stats import collect_site_stats

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "assets" / "progress-manifest.json"


def main() -> None:
    stats = collect_site_stats()
    items: list[dict] = []

    for path, title in [
        ("getting-started/newcomer-guide.md", "Newcomer guide"),
        ("getting-started/first-30-minutes.md", "First 30 minutes"),
        ("labs/start-here.md", "Hands-on start"),
    ]:
        items.append(
            {
                "id": f"on-{slug(title)}",
                "path": path,
                "title": title,
                "track": "onboarding",
            }
        )

    for book_no, book in enumerate(BOOKS, 1):
        book_dir = f"{book_no:02d}-{slug(book['title'])}"
        for ch_no, chapter in enumerate(book["chapters"], 1):
            ch_title = chapter[0]
            ch_file = f"{ch_no:02d}-{slug(ch_title)}.md"
            items.append(
                {
                    "id": f"b{book_no:02d}c{ch_no:02d}",
                    "path": f"books/{book_dir}/{ch_file}",
                    "title": ch_title,
                    "track": "books",
                    "book": book["title"],
                    "bookNo": book_no,
                    "chapterNo": ch_no,
                }
            )

    manifest = {
        "version": 1,
        "label": "AIEBOK reading progress",
        "tracks": {
            "onboarding": f"Start here ({stats.progress_onboarding} steps)",
            "books": f"Guided books ({stats.chapters} chapters)",
        },
        "items": items,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT} ({stats.progress_total} trackable items).")


if __name__ == "__main__":
    main()
