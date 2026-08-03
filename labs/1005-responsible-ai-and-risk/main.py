"""Lab 10.5: Responsible AI and Risk"""

CHAPTER = "10.5"
print("chapter hook:", CHAPTER)
use_cases = [
    {"name": "grammar fix", "impact": "low"},
    {"name": "promotion recommendation", "impact": "high"},
]
for uc in use_cases:
    hitl = uc["impact"] == "high"
    print(uc["name"], "human_review:", hitl)
print("---")
print("change one input above, predict output, re-run")
