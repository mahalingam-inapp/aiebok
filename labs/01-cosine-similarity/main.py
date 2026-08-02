"""Lab 01: cosine similarity from first principles."""
from math import sqrt


def cosine(a: list[float], b: list[float]) -> float:
    if len(a) != len(b):
        raise ValueError("vectors must have equal dimensions")
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = sqrt(sum(x * x for x in a))
    norm_b = sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        raise ValueError("cosine similarity is undefined for a zero vector")
    return dot / (norm_a * norm_b)


if __name__ == "__main__":
    query = [1.0, 1.0, 0.0]
    candidates = {
        "service unavailable": [0.9, 1.0, 0.1],
        "invoice approved": [0.1, 0.0, 1.0],
        "application outage": [1.0, 0.8, 0.0],
    }
    ranked = sorted(
        ((cosine(query, vector), text) for text, vector in candidates.items()),
        reverse=True,
    )
    for score, text in ranked:
        print(f"{score:.3f}  {text}")
