"""Bounded agent state machine with checkpoint, approval, and termination."""
from dataclasses import dataclass, asdict
import json


@dataclass
class State:
    step: str = "plan"
    attempts: int = 0
    approved: bool = False
    done: bool = False


def transition(state):
    if state.attempts >= 5: return State("stopped", state.attempts, state.approved, True)
    if state.step == "plan": return State("draft", state.attempts + 1)
    if state.step == "draft": return State("approval", state.attempts + 1)
    if state.step == "approval" and not state.approved: return State("approval", state.attempts + 1)
    return State("complete", state.attempts + 1, state.approved, True)


state = State()
while not state.done:
    print(json.dumps(asdict(state)))
    if state.step == "approval": state.approved = True
    state = transition(state)
print(json.dumps(asdict(state)))
