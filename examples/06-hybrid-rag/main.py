"""Fuse lexical and vector-like rankings with reciprocal rank fusion."""
LEXICAL = ["doc-expense", "doc-leave", "doc-security"]
VECTOR = ["doc-leave", "doc-expense", "doc-onboarding"]


def reciprocal_rank_fusion(rankings, k=60):
    scores = {}
    for ranking in rankings:
        for rank, document in enumerate(ranking, start=1):
            scores[document] = scores.get(document, 0.0) + 1 / (k + rank)
    return sorted(scores.items(), key=lambda item: item[1], reverse=True)


for document, score in reciprocal_rank_fusion([LEXICAL, VECTOR]):
    print(f"{score:.5f} {document}")
