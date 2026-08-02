"""Lab 03: observable retrieval/context/generation stages without an LLM API."""
from pathlib import Path
import re

PASSAGES = [
    ("leave", "Employees receive 20 days of annual leave per calendar year."),
    ("expenses", "Expense claims must be submitted within 30 days of purchase."),
    ("security", "Suspected credential exposure must be reported immediately."),
]


def words(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def retrieve(question: str, k: int = 2) -> list[tuple[int, str, str]]:
    q = words(question)
    scored = [(len(q & words(text)), source, text) for source, text in PASSAGES]
    return sorted(scored, reverse=True)[:k]


def answer(question: str) -> str:
    evidence = [item for item in retrieve(question) if item[0] > 0]
    if not evidence:
        return "I do not have relevant evidence to answer that question."
    citations = " ".join(f"[{source}]" for _, source, _ in evidence)
    context = " ".join(text for _, _, text in evidence)
    return f"Evidence: {context} {citations}"


if __name__ == "__main__":
    question = "How soon must I submit an expense claim?"
    print("Question:", question)
    print("Retrieved:", retrieve(question))
    print("Answer:", answer(question))
