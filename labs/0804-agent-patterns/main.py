"""Lab 8.4: Agent Patterns"""

patterns = {
    "monolith": {"calls": 1, "latency": 1.0},
    "planner_executor": {"calls": 3, "latency": 1.6},
    "supervisor_worker": {"calls": 5, "latency": 2.1},
}
task_risk = "high"
choice = "supervisor_worker" if task_risk == "high" else "planner_executor"
print({"pattern": choice, **patterns[choice]})
