"""Tests for starter lab 03-basic-rag."""
import subprocess
import sys
from pathlib import Path

from main import answer, retrieve


def test_retrieve_finds_expense_passage():
    hits = retrieve("How soon must I submit an expense claim?")
    assert hits[0][0] > 0
    assert hits[0][1] == "expenses"


def test_answer_includes_citation():
    text = answer("How soon must I submit an expense claim?")
    assert "[expenses]" in text
    assert "30 days" in text


def test_abstention_without_evidence():
    text = answer("What is the company's stock price?")
    assert "do not have relevant evidence" in text.lower()


def test_main_script_runs():
    result = subprocess.run(
        [sys.executable, str(Path(__file__).parent / "main.py")],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "Answer:" in result.stdout
