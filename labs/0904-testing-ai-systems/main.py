"""Lab 9.4: Testing AI Systems"""

CHAPTER = "9.4"
print("chapter hook:", CHAPTER)
layers = ["unit", "contract", "scenario", "eval", "adversarial"]
catch_abstain = {"unit": False, "contract": False, "scenario": True, "eval": True, "adversarial": False}
for layer in layers:
    print(layer, "catches_abstain:", catch_abstain[layer])
print("---")
print("change one input above, predict output, re-run")
