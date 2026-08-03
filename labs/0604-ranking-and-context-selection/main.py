"""Lab 6.4: Ranking and Context Selection"""

rank_a = ["doc-leave", "doc-expense", "doc-security"]
rank_b = ["doc-expense", "doc-leave", "doc-onboarding"]
def rrf(lists, k=60):
    scores = {}
    for ranking in lists:
        for rank, doc in enumerate(ranking, 1):
            scores[doc] = scores.get(doc, 0) + 1/(k+rank)
    return sorted(scores.items(), key=lambda x: -x[1])
print("rrf top2:", rrf([rank_a, rank_b])[:2])
