"""Lab 10.3: Evaluation by System Stage"""

CHAPTER = "10.3"
print("chapter hook:", CHAPTER)
matrix = {"retrieval": 0.6, "rerank": 0.8, "generation": 0.9}
symptom = "wrong doc cited"
if symptom == "wrong doc cited":
    first = min(matrix, key=matrix.get)
print("investigate first:", first)
print("---")
print("change one input above, predict output, re-run")
