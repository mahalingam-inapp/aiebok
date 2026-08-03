"""Lab 4.6: Model Families and Selection"""

tasks = {"lookup": 0.95, "cite": 0.88, "route": 0.91}
models = {"small-instruct": 0.01, "large-reason": 0.08}
def route(task, risk):
    if risk == "low" and tasks[task] > 0.9:
        return "small-instruct"
    return "large-reason"
for risk in ("low", "high"):
    print({"risk": risk, "model": route("lookup", risk), "cost_per_1k": models[route("lookup", risk)]})
