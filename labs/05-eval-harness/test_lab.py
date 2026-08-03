"""Tests for starter lab 05-eval-harness."""
import subprocess
import sys
from pathlib import Path


def test_main_prints_release_gate():
    result = subprocess.run(
        [sys.executable, str(Path(__file__).parent / "main.py")],
        capture_output=True,
        text=True,
    )
    assert "score=" in result.stdout
    assert "release=" in result.stdout
    assert result.stdout.strip()
