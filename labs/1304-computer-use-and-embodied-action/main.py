"""Lab 13.4: Computer Use and Embodied Action"""

CHAPTER = "13.4"
print("chapter hook:", CHAPTER)
actions = [
    {"type": "click_semantic", "target": "Submit enrollment", "risk": "high"},
    {"type": "click_xy", "x": 120, "y": 400, "risk": "high"},
]
for a in actions:
    needs_confirm = a["risk"] == "high"
    print(a["type"], "confirm:", needs_confirm)
print("---")
print("change one input above, predict output, re-run")
