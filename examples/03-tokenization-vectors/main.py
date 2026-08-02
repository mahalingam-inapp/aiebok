"""Toy tokenization, TF-IDF vectors, and cosine ranking."""
from collections import Counter
from math import log, sqrt
import re

DOCS = ["application service outage", "expense invoice approval", "reset user password"]


def tokenize(text): return re.findall(r"[a-z0-9]+", text.lower())
vocabulary = sorted(set().union(*(tokenize(d) for d in DOCS)))
document_frequency = {t: sum(t in tokenize(d) for d in DOCS) for t in vocabulary}


def vector(text):
    counts = Counter(tokenize(text))
    return [counts[t] * (log((1 + len(DOCS)) / (1 + document_frequency[t])) + 1) for t in vocabulary]


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b)); na = sqrt(sum(x*x for x in a)); nb = sqrt(sum(y*y for y in b))
    return dot / (na * nb) if na and nb else 0.0


query = vector("service unavailable outage")
for score, doc in sorted(((cosine(query, vector(d)), d) for d in DOCS), reverse=True):
    print(f"{score:.3f} {doc}")
