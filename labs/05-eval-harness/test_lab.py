"""Tests for starter lab 05-eval-harness."""
import subprocess
import sys
from pathlib import Path

from main import CASES, candidate, contains_expected, main


def test_candidate_answers_known_questions():
    assert "paris" in candidate("capital of France").lower()
    assert candidate("2 + 2") == "4"


def test_contains_expected_is_case_insensitive():
    assert contains_expected("Paris is the capital", "paris")


def test_safety_slice_present():
    assert any(case.slice == "safety" for case in CASES)


def test_main_prints_release_gate():
    result = subprocess.run(
        [sys.executable, str(Path(__file__).parent / "main.py")],
        capture_output=True,
        text=True,
    )
    assert "score=" in result.stdout
    assert "release=" in result.stdout
    assert result.stdout.strip()


def test_release_passes_on_default_cases(capsys):
    assert main() == 0
