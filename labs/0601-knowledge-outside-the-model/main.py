"""Lab 6.1: Knowledge Outside the Model"""

CHAPTER = "6.1"
print("chapter hook:", CHAPTER)
requirements = [
    ("cite exact page", "RAG"),
    ("friendly tone", "prompt/finetune"),
    ("live headcount", "SQL tool"),
]
for req, mechanism in requirements:
    print({"requirement": req, "mechanism": mechanism})
print("---")
print("change one input above, predict output, re-run")
