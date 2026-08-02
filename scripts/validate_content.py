"""Small dependency-free checks that complement `mkdocs build --strict`."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
errors: list[str] = []

for path in sorted(DOCS.rglob("*.md")):
    text = path.read_text(encoding="utf-8")
    if not re.search(r"^#\s+\S", text, flags=re.MULTILINE):
        errors.append(f"{path.relative_to(ROOT)}: missing H1")
    if "TODO" in text or "TBD" in text:
        errors.append(f"{path.relative_to(ROOT)}: contains TODO/TBD")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean = target.split("#", 1)[0]
        if not clean:
            continue
        resolved = (path.parent / clean).resolve()
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken link {target}")

if errors:
    print("Content validation failed:")
    print("\n".join(f"- {item}" for item in errors))
    sys.exit(1)

count = len(list(DOCS.rglob("*.md")))
print(f"Content validation passed for {count} Markdown files.")
