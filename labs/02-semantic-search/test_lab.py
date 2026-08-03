"""Tests for starter lab 02-semantic-search."""
import subprocess
import sys
from pathlib import Path

from main import DOCUMENTS, embed, search


def test_embed_dimension():
    assert len(embed("hello world")) == 32


def test_search_ranks_outage_first():
    results = search("the application is unavailable")
    assert results
    top_doc = results[0][1].lower()
    assert "unavailable" in top_doc or "outage" in top_doc


def test_search_returns_all_documents_scored():
    results = search("password reset")
    assert len(results) == len(DOCUMENTS)


def test_main_script_runs():
    result = subprocess.run(
        [sys.executable, str(Path(__file__).parent / "main.py")],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip()
