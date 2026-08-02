"""Lab 04: a bounded, inspectable agent state machine."""
from dataclasses import dataclass, field


@dataclass
class State:
    goal: str
    step: int = 0
    max_steps: int = 4
    observations: list[str] = field(default_factory=list)
    done: bool = False


def plan(state: State) -> str:
    if not state.observations:
        return "inspect requirements"
    if "requirements inspected" in state.observations and "draft created" not in state.observations:
        return "create draft"
    return "verify result"


def execute(action: str) -> str:
    outcomes = {
        "inspect requirements": "requirements inspected",
        "create draft": "draft created",
        "verify result": "result verified",
    }
    return outcomes[action]


def run(goal: str) -> State:
    state = State(goal=goal)
    while not state.done and state.step < state.max_steps:
        action = plan(state)
        observation = execute(action)
        state.observations.append(observation)
        state.step += 1
        state.done = observation == "result verified"
        print({"step": state.step, "action": action, "observation": observation})
    return state


if __name__ == "__main__":
    final = run("produce a verified draft")
    print("status:", "complete" if final.done else "step limit reached")
