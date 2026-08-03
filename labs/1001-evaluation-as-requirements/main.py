"""Lab 10.1: Evaluation as Requirements"""

CHAPTER = "10.1"
print("chapter hook:", CHAPTER)
cases = [
    {"id": 1, "input": "reset password", "must": "link to policy"},
    {"id": 2, "input": "delete tenant", "must": "require approval"},
]
for case in cases:
    print(case["id"], case["must"])
print("---")
print("change one input above, predict output, re-run")
