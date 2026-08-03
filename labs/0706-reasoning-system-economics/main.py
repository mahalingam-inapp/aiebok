"""Lab 7.6: Reasoning-System Economics"""

routes = [
    {"name": "single", "cost": 1, "quality": 0.78},
    {"name": "best3", "cost": 3, "quality": 0.86},
    {"name": "verify", "cost": 5, "quality": 0.91},
]
def pick(uncertainty, budget):
    opts = [r for r in routes if r["cost"] <= budget]
    if uncertainty < 0.3:
        return opts[0]
    return max(opts, key=lambda r: r["quality"])
print(pick(0.25, 4))
print(pick(0.8, 4))
