"""Lab 13.3: Image and Video Generation"""

CHAPTER = "13.3"
print("chapter hook:", CHAPTER)
rubric = {"brand_match": 0.9, "safety": 1.0, "provenance": 1.0, "aesthetic": 0.85}
gates = {"safety": 1.0, "provenance": 1.0}
release = all(rubric[k] >= gates[k] for k in gates)
print({"release": release, "scores": rubric})
print("---")
print("change one input above, predict output, re-run")
