"""Lab 9.6: Experiments, Adoption, and Value"""

CHAPTER = "9.6"
print("chapter hook:", CHAPTER)
metrics = {"time_saved": 0.15, "compliance_errors": 0.02, "slice_EU_success": -0.05}
gates = {"compliance_errors_max": 0.01, "slice_min_success": 0.0}
blocked = metrics["compliance_errors"] > gates["compliance_errors_max"]
blocked |= metrics["slice_EU_success"] < gates["slice_min_success"]
print({"blocked": blocked, "reason": "compliance or slice harm"})
print("---")
print("change one input above, predict output, re-run")
