"""Tests for starter lab 04-agent-loop."""
import subprocess
import sys
from pathlib import Path

from main import State, execute, plan, run


def test_agent_completes_default_goal():
    state = run("produce a verified draft", verbose=False)
    assert state.done
    assert state.observations[-1] == "result verified"


def test_agent_stops_before_completion_when_step_limit_reached():
    s = State(goal="produce a verified draft", max_steps=1)
    action = plan(s)
    s.observations.append(execute(action))
    s.step = 1
    assert not s.done
    assert s.observations == ["requirements inspected"]


def test_main_script_runs():
    result = subprocess.run(
        [sys.executable, str(Path(__file__).parent / "main.py")],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "status:" in result.stdout
