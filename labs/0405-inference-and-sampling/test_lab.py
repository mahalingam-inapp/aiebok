"""Tests for lab 4.5."""
import subprocess
import sys
from pathlib import Path


def test_main_exits_zero():
    result = subprocess.run(
        [sys.executable, str(Path(__file__).parent / "main.py")],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip()
