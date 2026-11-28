"""Publish HTML lecture decks from the same catalogs as the written curriculum."""
from dataclasses import dataclass
from functools import cache
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
from catalog_helpers import title_from_slug
from concept_card_enrichments import card_enrichment
from chapter_catalog import get_knowledge_check, get_worked_example
from generate_books import BOOKS, WORKED_SCENARIOS, chapter_filename, course_slug
from generate_learning_paths import lecture_filename
from lecture_cases import CASES
from no_code_courses import NO_CODE_COURSES
from topic_knowledge import TOPIC_FACTS, get_topic_entry, normalize
from worked_lecture_traces import TRACE_PAIRS


@dataclass(frozen=True)
class Slide:
    title: str
    text: str = ""
    terms: tuple[tuple[str, str], ...] = ()
    questions: tuple[str, ...] = ()
    answers: tuple[str, ...] = ()
    topic: str = ""


@dataclass(frozen=True)
class Deck:
    lecture: str
    course: str
    slides: tuple[Slide, ...]
    is_reference: bool = False


CONCEPT_INDEX = "concept-decks/index.md"
CARD_LINK = re.compile(r"\[([^]\n]+)\]\(((?:\.\./)*(?:concepts/)?cards/[a-z0-9-]+\.md)\)")


def case_slide(course, number):
    moment = CASES[course].moments[number - 1]
    return Slide(moment.title, moment.scene, answers=(moment.reasoning,))


def build_decks():
    for book_no, book in enumerate(BOOKS, 1):
        directory = course_slug(book_no, book["title"])
        for number, chapter in enumerate(book["chapters"], 1):
            title, summary, topics, practice, principle = chapter
            example = get_worked_example(book_no, number, title, summary, topics, WORKED_SCENARIOS[book_no - 1])
            fields = dict(re.findall(r"^\*\*([^\n]+?):\*\* (.+)$", example, re.MULTILINE))
            *questions, answer = get_knowledge_check(book_no, number, topics)
            answers = tuple(re.split(r"\s*Q\d+:\s*", answer.removeprefix("Q1: ")))
            yield Deck(f"books/{directory}/{chapter_filename(number, title)}", book["title"], (
                Slide(title, principle),
                Slide("What you’ll learn", summary),
                case_slide(book_no, number),
                *(concept_slide(topic) for topic in topics),
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
        traces = TRACE_PAIRS.get(course.slug)
        for number, lecture in enumerate(lectures, 1):
            trace = traces[number - 1] if traces else None
            worked = Slide("Worked example", lecture.example)
            if trace:
                worked = Slide("Follow the example", trace[0], terms=(("Result", trace[1]),))
            yield Deck(f"courses/{course.slug}/{lecture_filename(number, lecture)}", course.title, (
                Slide(lecture.title, lecture.outcome),
                case_slide(course.slug, number),
                Slide("How it works", lecture.explanation),
                worked,
                Slide("Try it yourself", lecture.practice, answers=(lecture.answer,)),
            ))


def deck_path(lecture):
    return PurePosixPath("slides", lecture).with_suffix(".html").as_posix()


def concept_slide(topic):
    key = normalize(topic)
    explanation, example, evidence = get_topic_entry(key)
    title = topic.capitalize() if topic.islower() else topic
    return Slide(title, explanation, (("Example", example), ("What to check", evidence)), topic=key)


def reference_path(key):
    return f"slides/concepts/{key}.html"


@cache
def deck_collection():
    lectures = tuple(build_decks())
    references = {}
    for deck in lectures:
        for slide in deck.slides:
            if slide.topic:
                references.setdefault(slide.topic, (slide.title, deck_path(deck.lecture), deck.course))
    supplements = []
    for key in sorted(TOPIC_FACTS.keys() - references.keys()):
        definition, example, evidence = get_topic_entry(key)
        extra = card_enrichment(key)
        title = title_from_slug(key)
        references[key] = (title, reference_path(key), "Reference deck")
        course = extra.get("course")
        source = f"courses/{course}/index.md" if course else CONCEPT_INDEX
        supplements.append((key, Deck(source, "Concept reference", (
            Slide(title, definition, topic=key),
            Slide("Worked example", example, terms=(("What to check", evidence),)),
            Slide("Design and failure", extra["when_to_use"], terms=(
                ("Limits", extra["when_not"]),
                ("Watch for", extra["failure_modes"][0]),
            )),
        ), is_reference=True)))
    return lectures, tuple(supplements), references


def on_files(files, *, config):
    template = Environment(
        loader=FileSystemLoader(SCRIPTS.parent / "templates"), autoescape=True
    ).get_template("lecture-deck.html")
    lectures, supplements, _ = deck_collection()
    decks = [(deck_path(deck.lecture), deck) for deck in lectures]
    decks.extend((reference_path(key), deck) for key, deck in supplements)
    for path, deck in decks:
        lecture = files.get_file_from_path(deck.lecture)
        if lecture is None:
            raise ValueError(f"Missing page for deck: {deck.lecture}")
        if files.get_file_from_path(path) is not None:
            raise ValueError(f"Duplicate slide deck destination: {path}")

        def relative(url):
            return get_relative_url(url, path)

        files.append(File.generated(config, path, content=template.render(
            deck=deck,
            lecture_url=relative(lecture.url),
            concept_url=relative(files.get_file_from_path(CONCEPT_INDEX).url),
            css=relative("assets/slides/deck.css"),
            script=relative("assets/slides/deck.js"),
        )))
    return files


def concept_directory(page):
    _, _, references = deck_collection()
    template = Environment(loader=FileSystemLoader(SCRIPTS.parent / "templates"),
                           autoescape=True).get_template("concept-deck-directory.html")
    entries = [
        (title, source, get_relative_url(destination, page.url) + f"#concept-{key}")
        for key, (title, destination, source) in sorted(references.items())
    ]
    return template.render(entries=entries)


def on_page_markdown(markdown, *, page, config, files):
    uri = page.file.src_uri
    if uri == CONCEPT_INDEX:
        return markdown + "\n\n" + concept_directory(page)

    lectures, _, concepts = deck_collection()
    directory = posixpath.dirname(uri)
    key = PurePosixPath(uri).stem
    if uri.startswith("concepts/cards/") and key in concepts:
        href = posixpath.relpath(concepts[key][1], directory)
        heading, _, body = markdown.partition("\n")
        markdown = (f"{heading}\n\n[Open concept slide]({href}#concept-{key})"
                    f"{{ .md-button .md-button--primary }}\n{body}")

    own = next((item for item in lectures if item.lecture == uri), None)
    local_topics = {slide.topic for slide in own.slides} if own else set()

    def concept_link(match):
        label, target = match.groups()
        target = posixpath.normpath(posixpath.join(directory, target))
        if target == "concepts/cards/index.md":
            return f"[Concept decks]({posixpath.relpath(CONCEPT_INDEX, directory)})"
        target_key = PurePosixPath(target).stem
        if not target.startswith("concepts/cards/") or target_key not in concepts:
            return match.group(0)
        # Prefer the concept in the lecture the reader opened, when it has its own slide.
        destination = deck_path(uri) if target_key in local_topics else concepts[target_key][1]
        href = posixpath.relpath(destination, directory)
        return f"[{label.removesuffix(' concept card')}]({href}#concept-{target_key})"

    markdown = CARD_LINK.sub(concept_link, markdown)

    deck = files.get_file_from_path(deck_path(uri))
    if deck is None:
        return markdown
    href = posixpath.relpath(deck.src_uri, posixpath.dirname(uri))
    heading, _, body = markdown.partition("\n")
    return f"{heading}\n\n[Open slide deck]({href}){{ .md-button }}\n{body}"
