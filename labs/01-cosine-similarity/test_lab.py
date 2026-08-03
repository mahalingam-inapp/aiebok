"""Tests for starter lab 01-cosine-similarity."""
import subprocess
import sys
from pathlib import Path

import pytest

from main import cosine


def test_identical_direction():
    assert cosine([1.0, 2.0, 3.0], [2.0, 4.0, 6.0]) == pytest.approx(1.0)


def test_orthogonal_vectors():
    assert cosine([1.0, 0.0, 0.0], [0.0, 1.0, 0.0]) == pytest.approx(0.0)


def test_zero_vector_raises():
    with pytest.raises(ValueError, match="zero vector"):
        cosine([0.0, 0.0], [1.0, 1.0])


def test_mismatched_dimensions_raises():
    with pytest.raises(ValueError, match="equal dimensions"):
        cosine([1.0], [1.0, 2.0])


def test_main_script_runs():
    result = subprocess.run(
        [sys.executable, str(Path(__file__).parent / "main.py")],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    lines = result.stdout.strip().splitlines()
    assert len(lines) == 3
    scores = [float(line.split()[0]) for line in lines]
    assert scores == sorted(scores, reverse=True)
