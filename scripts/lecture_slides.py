"""Publish HTML lecture decks from the same catalogs as the written curriculum."""
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
import posixpath
import re
import sys

from jinja2 import Environment, FileSystemLoader
from mkdocs.structure.files import File
from mkdocs.utils import get_relative_url

SCRIPTS = Path(__file__).resolve().parent
# MkDocs loads hooks by filename. The curriculum imports use this directory as their root.
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from applied_courses import APPLIED_COURSES
from chapter_catalog import get_knowledge_check, get_worked_example
from generate_books import BOOKS, WORKED_SCENARIOS, chapter_filename, course_slug
from generate_learning_paths import lecture_filename
from no_code_courses import NO_CODE_COURSES
from topic_knowledge import get_topic_entry


@dataclass(frozen=True)
class Slide:
    title: str
    text: str = ""
    terms: tuple[tuple[str, str], ...] = ()
    questions: tuple[str, ...] = ()
    answers: tuple[str, ...] = ()


@dataclass(frozen=True)
class Deck:
    lecture: str
    course: str
    slides: tuple[Slide, ...]


def build_decks():
    for book_no, book in enumerate(BOOKS, 1):
        directory = course_slug(book_no, book["title"])
        for number, chapter in enumerate(book["chapters"], 1):
            title, summary, topics, practice, principle = chapter
            example = get_worked_example(book_no, number, title, summary, topics, WORKED_SCENARIOS[book_no - 1])
            fields = dict(re.findall(r"^\*\*([^\n]+?):\*\* (.+)$", example, re.MULTILINE))
            concepts = [(name, get_topic_entry(name)[0]) for name in topics]
            *questions, answer = get_knowledge_check(book_no, number, topics)
            answers = tuple(re.split(r"\s*Q\d+:\s*", answer.removeprefix("Q1: ")))
            yield Deck(f"books/{directory}/{chapter_filename(number, title)}", book["title"], (
                Slide(title, principle),
                Slide("What you’ll learn", summary),
                *(Slide(concepts[start][0][:1].upper() + concepts[start][0][1:],
                        concepts[start][1], tuple(concepts[start + 1:start + 2]))
                  for start in range(0, len(concepts), 2)),
                Slide("Worked example", fields["Situation"], (
                    ("Baseline", fields["Baseline"]), ("Application", fields["Application"]),
                )),
                Slide("How to evaluate it", terms=(
                    ("Test cases", fields["Test cases"]), ("Measurement", fields["Measurement"]),
                )),
                Slide("Practice", practice, questions=(fields["Design question"],)),
                Slide("Knowledge check", questions=tuple(questions), answers=answers),
            ))

    for course in (*NO_CODE_COURSES, *APPLIED_COURSES):
        lectures = (lecture for _, group in course.sections for lecture in group)
        for number, lecture in enumerate(lectures, 1):
            yield Deck(f"courses/{course.slug}/{lecture_filename(number, lecture)}", course.title, (
                Slide(lecture.title, lecture.outcome),
                Slide("How it works", lecture.explanation),
                Slide("Worked example", lecture.example),
                Slide("Try it yourself", lecture.practice, answers=(lecture.answer,)),
            ))


def deck_path(lecture):
    return PurePosixPath("slides", lecture).with_suffix(".html").as_posix()


def on_files(files, *, config):
    template = Environment(
        loader=FileSystemLoader(SCRIPTS.parent / "templates"), autoescape=True
    ).get_template("lecture-deck.html")

    for deck in build_decks():
        lecture = files.get_file_from_path(deck.lecture)
        if lecture is None:
            raise ValueError(f"Missing lecture for deck: {deck.lecture}")
        path = deck_path(deck.lecture)
        if files.get_file_from_path(path) is not None:
            raise ValueError(f"Duplicate slide deck destination: {path}")

        def relative(url):
            return get_relative_url(url, path)

        files.append(File.generated(config, path, content=template.render(
            deck=deck,
            lecture_url=relative(lecture.url),
            css=relative("assets/slides/deck.css"),
            script=relative("assets/slides/deck.js"),
        )))
    return files


def on_page_markdown(markdown, *, page, config, files):
    deck = files.get_file_from_path(deck_path(page.file.src_uri))
    if deck is None:
        return markdown
    href = posixpath.relpath(deck.src_uri, posixpath.dirname(page.file.src_uri))
    heading, _, body = markdown.partition("\n")
    return f"{heading}\n\n[Open slide deck]({href}){{ .md-button }}\n{body}"
