"""Shared content model for additional courses and their lectures."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Lecture:
    title: str
    outcome: str
    explanation: str
    example: str
    practice: str
    answer: str


@dataclass(frozen=True)
class Course:
    slug: str
    title: str
    goal: str
    entry: str
    project: str
    standard: str
    sections: tuple[tuple[str, tuple[Lecture, ...]], ...]
    workbook: bool = False
    resources: tuple[tuple[str, str], ...] = ()
