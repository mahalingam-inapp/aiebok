"""Lab 9.5: Human-Centered AI UX"""

CHAPTER = "9.5"
print("chapter hook:", CHAPTER)
risk = "high"
ux = {"preview": True, "approval": risk == "high", "undo_sec": 30 if risk == "high" else 0}
print(ux)
print("inspect step", 1)
print("---")
print("change one input above, predict output, re-run")
