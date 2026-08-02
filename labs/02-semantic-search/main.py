"""Lab 02: an intentionally simple hashing-vector search pipeline."""
from collections import Counter
from hashlib import sha256
from math import sqrt
import re

DOCUMENTS = [
    "Reset a forgotten employee password in the identity portal.",
    "Investigate an unavailable application and service outage.",
    "Submit and approve an expense reimbursement invoice.",
    "Request access to a restricted analytics database.",
]


def tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def embed(text: str, dimensions: int = 32) -> list[float]:
    counts = Counter(tokens(text))
    vector = [0.0] * dimensions
    for token, count in counts.items():
        bucket = int.from_bytes(sha256(token.encode()).digest()[:4], "big") % dimensions
        vector[bucket] += count
    return vector


def cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na, nb = sqrt(sum(x * x for x in a)), sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0


def search(query: str) -> list[tuple[float, str]]:
    q = embed(query)
    return sorted(((cosine(q, embed(doc)), doc) for doc in DOCUMENTS), reverse=True)


if __name__ == "__main__":
    for score, document in search("the application is unavailable"):
        print(f"{score:.3f}  {document}")
