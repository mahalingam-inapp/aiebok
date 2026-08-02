"""Policy-based model routing with risk and fallback controls."""
MODELS = {
    "small": {"quality": 0.75, "cost": 1},
    "large": {"quality": 0.93, "cost": 8},
}


def route(task):
    if task["risk"] == "high" or task["complexity"] > 0.7: return "large"
    return "small"


for task in ({"risk": "low", "complexity": .2}, {"risk": "high", "complexity": .3}):
    model = route(task)
    print(task, "->", model, MODELS[model])
