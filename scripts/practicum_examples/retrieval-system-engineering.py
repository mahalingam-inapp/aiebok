from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Passage:
    document: str
    revision: int
    effective: int
    audience: str
    text: str
    chunk: int = 1

    @property
    def source(self):
        prefix = f"{self.document}@{self.revision}"
        return prefix if self.chunk == 1 else f"{prefix}#{self.chunk}"


corpus = (
    Passage("leave", 1, 1, "public", "vacation leave limit 10 days"),
    Passage("leave", 2, 3, "public", "vacation leave limit 15 days"),
    Passage("leave", 3, 8, "public", "vacation leave limit 18 days"),
    Passage("travel", 1, 1, "public", "travel policy for boarding and rail. keep the receipt"),
    Passage("equipment", 1, 1, "public", "board replacement and circuit equipment"),
    Passage("payroll", 1, 1, "finance", "payroll adjustments and tax forms"),
)


def visible(records, role, as_of):
    latest = {}
    for row in records:
        if row.effective <= as_of and (row.document not in latest or row.revision > latest[row.document].revision):
            latest[row.document] = row
    return [
        replace(row, text=sentence.strip(), chunk=chunk)
        for row in latest.values() if row.audience in {"public", role}
        for chunk, sentence in enumerate(row.text.split("."), 1) if sentence.strip()
    ]


eligible = visible(corpus, "employee", 6)
assert {row.source for row in eligible} == {"leave@2", "travel@1", "travel@1#2", "equipment@1"}

# %%
from math import sqrt
import re


def tokens(text):
    return set(re.findall(r"[a-z]+", text.lower()))


concepts = (
    {"vacation", "leave", "holidays"},
    {"travel", "boarding", "rail", "journey", "board"},
    {"board", "equipment", "circuit"},
    {"payroll", "tax", "adjustments"},
)


def vector(text):
    terms = tokens(text)
    return tuple(len(terms & concept) for concept in concepts)


def similarity(left, right):
    norm = sqrt(sum(v * v for v in left) * sum(v * v for v in right))
    return sum(a * b for a, b in zip(left, right)) / norm if norm else 0


def ranked(query, rows, score):
    scores = [(score(query, row.text), row.source) for row in rows]
    return [source for value, source in sorted(scores, key=lambda pair: (-pair[0], pair[1])) if value > 0]


def lexical(query, rows):
    return ranked(query, rows, lambda a, b: len(tokens(a) & tokens(b)))


def dense(query, rows):
    return ranked(query, rows, lambda a, b: similarity(vector(a), vector(b)))


assert lexical("holidays", eligible) == []
assert dense("holidays", eligible)[0] == "leave@2"

# %%
from collections import defaultdict


def fused_scores(query, rows, k):
    scores = defaultdict(float)
    for ranking in (lexical(query, rows), dense(query, rows)):
        for position, source in enumerate(ranking, 1):
            scores[source] += 1 / (k + position)
    return scores


def fusion(query, rows):
    scores = fused_scores(query, rows, k=20)
    return sorted(scores, key=lambda source: (-scores[source], source))


def hybrid(query, rows, k=20, rerank_weight=0.30):
    scores = fused_scores(query, rows, k)
    by_source = {row.source: row for row in rows}
    return sorted(scores, key=lambda source: (
        -(scores[source] + rerank_weight * similarity(vector(query), vector(by_source[source].text))), source
    ))


cases = (("holidays", "employee", "leave@2"), ("board journey", "employee", "travel@1"),
         ("circuit", "employee", "equipment@1"), ("payroll", "finance", "payroll@1"),
         ("payroll", "employee", None), ("astronomy", "employee", None))


def evaluate(method):
    positions, clean = [], 0
    for query, role, wanted in cases:
        ranking = method(query, visible(corpus, role, 6))
        if wanted is None:
            clean += not ranking
        else:
            positions.append(ranking.index(wanted) + 1 if wanted in ranking else None)
    return {"recall@2": sum(pos is not None and pos <= 2 for pos in positions) / len(positions),
            "MRR": sum(1 / pos for pos in positions if pos) / len(positions), "no_evidence": clean}


for method in (lexical, dense, fusion, hybrid):
    print(method.__name__, evaluate(method))
assert evaluate(hybrid)["recall@2"] > evaluate(lexical)["recall@2"]
assert evaluate(hybrid)["MRR"] > evaluate(fusion)["MRR"]
assert evaluate(hybrid)["no_evidence"] == 2

# %%
def verify_quote(source, quote, retrieved_sources, eligible_rows):
    evidence = {row.source: row.text for row in eligible_rows if row.source in retrieved_sources}
    if source in evidence and quote.strip() and quote in evidence[source]:
        return quote, source
    return None


hits = hybrid("holidays", eligible)
assert verify_quote("leave@2", "15 days", hits, eligible) == ("15 days", "leave@2")
assert verify_quote("leave@1", "10 days", hits, eligible) is None
assert verify_quote("leave@2", "20 days", hits, eligible) is None
assert verify_quote("payroll@1", "tax forms", hits + ["payroll@1"], eligible) is None
assert verify_quote("leave@2", "15 days", hits, visible(corpus, "employee", 8)) is None
