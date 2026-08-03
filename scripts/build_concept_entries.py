"""Build concept_entries.json from topic_knowledge.py."""
from __future__ import annotations

import json
from pathlib import Path

from topic_knowledge import TOPIC_FACTS, normalize


def main() -> None:
    out = Path(__file__).resolve().parent / "concept_entries.json"
    out.write_text(json.dumps(TOPIC_FACTS, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(TOPIC_FACTS)} concept entries ({len(TOPIC_FACTS)} unique slugs).")


if __name__ == "__main__":
    main()
