"""Lab 3.4: From Sparse Features to Embeddings"""

docs = {"a": "remote office allowance for home equipment", "b": "expense report submission deadline"}
query_terms = set("work from home equipment stipend".split())
def tfidf_score(q, doc):
    doc_terms = doc.lower().split()
    overlap = len(q & set(doc_terms))
    return overlap / (len(doc_terms) + 1)
scores = {k: tfidf_score(query_terms, v) for k, v in docs.items()}
print("ranking:", sorted(scores.items(), key=lambda x: -x[1]))
