"""Lab 11.1: Choosing Adaptation"""

CHAPTER = "11.1"
print("chapter hook:", CHAPTER)
scenarios = [
    ("new policy fact", "RAG"),
    ("consistent tone", "prompt/SFT"),
    ("live database count", "tool"),
]
for need, fix in scenarios:
    print({"need": need, "intervention": fix})
print("---")
print("change one input above, predict output, re-run")
