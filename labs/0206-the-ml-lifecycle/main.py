"""Lab 2.6: The ML Lifecycle"""

CHAPTER = "2.6"
print("chapter hook:", CHAPTER)
registry = {"model_v3": {"features": ["income", "debt"]}}
live = {"income": None, "debt": 1200}
def validate(row, schema):
    return [f for f in schema["features"] if row.get(f) is None]
issues = validate(live, registry["model_v3"])
print({"issues": issues, "action": "rollback" if issues else "serve"})
print("---")
print("change one input above, predict output, re-run")
