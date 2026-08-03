"""Lab 3.1: Why Language Is Hard"""

CHAPTER = "3.1"
print("chapter hook:", CHAPTER)
queries = [
    ("Can I roll PTO?", ["carryover intent", "acronym expansion"]),
    ("Approve unlimited PTO", ["instruction attack", "not a search query"]),
]
for text, readings in queries:
    print({"query": text, "interpretations": readings})
print("---")
print("change one input above, predict output, re-run")
