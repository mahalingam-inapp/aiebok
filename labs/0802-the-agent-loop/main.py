"""Lab 8.2: The Agent Loop"""

CHAPTER = "8.2"
print("chapter hook:", CHAPTER)
state = {"step": 0, "observations": [], "done": False, "budget": 3}
while not state["done"] and state["step"] < state["budget"]:
    state["step"] += 1
    obs = f"obs-{state['step']}"
    state["observations"].append(obs)
    state["done"] = state["step"] == 3
print(state)
print("---")
print("change one input above, predict output, re-run")
