"""Expose the ordered curriculum to the Material learning templates."""

from dataclasses import dataclass
from pathlib import Path
import sys

from mkdocs.utils import get_relative_url

scripts = str(Path(__file__).resolve().parent)
if scripts not in sys.path:
    sys.path.insert(0, scripts)

from applied_courses import APPLIED_COURSES
from course_catalog import PATHS, SPECIALIST_PATHS, TECHNICAL_COURSES
from generate_books import BOOKS, chapter_filename, course_slug
from generate_learning_paths import lecture_filename
from no_code_courses import NO_CODE_COURSES


@dataclass(frozen=True)
class Entry:
    title: str
    uri: str
    description: str
    category: str
    detail: str
    sections: tuple = ()


def course_entries():
    for category, courses, time in (
        ("No code", NO_CODE_COURSES, "About 2 hours"),
        ("Project practicums", APPLIED_COURSES, "3–4 hours"),
    ):
        for course in courses:
            uri = f"courses/{course.slug}"
            sections = []
            number = 0
            for title, lectures in course.sections:
                lessons = []
                for lecture in lectures:
                    number += 1
                    lessons.append((lecture.title, f"{uri}/{lecture_filename(number, lecture)}"))
                sections.append((title, tuple(lessons)))
            yield Entry(course.title, f"{uri}/index.md", course.goal, category,
                        f"{number} lectures · {time}", tuple(sections))

    for number, (book, course) in enumerate(zip(BOOKS, TECHNICAL_COURSES, strict=True), 1):
        uri = f"books/{course_slug(number, book['title'])}"
        lessons = tuple((chapter[0], f"{uri}/{chapter_filename(index, chapter[0])}")
                        for index, chapter in enumerate(book["chapters"], 1))
        sections = tuple((title, lessons[index * 2:index * 2 + 2])
                         for index, title in enumerate(course.sections))
        yield Entry(book["title"], f"{uri}/index.md", book["goal"], "Technical core",
                    f"{len(lessons)} lectures · 10–12 hours", sections)


def path_entries():
    for path in PATHS:
        category = "Specialist paths" if path in SPECIALIST_PATHS else "Core paths"
        yield Entry(path.title, f"getting-started/learning-paths/{path.slug}.md", path.audience,
                    category, f"{path.level} · {len(path.courses)} courses")


COURSES = tuple(course_entries())
PATH_CATALOG = "getting-started/learning-paths/index.md"
COURSE_CATALOG = "courses/index.md"
CATALOGS = {
    COURSE_CATALOG: {"title": "Courses", "noun": "course", "entries": COURSES,
                     "description": "Choose a course to study on its own, or follow a learning path for your role.",
                     "browse": (PATH_CATALOG, "Browse learning paths"),
                     "resources": (("labs/notebooks/index.md", "Notebook downloads and setup"),
                                   ("casebook/index.md", "Real-world casebook"))},
    PATH_CATALOG: {"title": "Learning paths", "noun": "learning path", "entries": tuple(path_entries()),
                   "description": "Choose your role or specialty, then take the courses in order.",
                   "browse": (COURSE_CATALOG, "Browse courses"),
                   "resources": (("editorial/learning-path-coverage.md", "Learning path coverage"),
                                 ("editorial/textbook-audit.md", "Textbook content audit"))},
}
COURSE_PAGES = {
    uri: course
    for course in COURSES
    for uri in (course.uri, *(uri for _, lessons in course.sections for _, uri in lessons))
}
PATH_PAGES = {entry.uri for entry in CATALOGS[PATH_CATALOG]["entries"]}
PAGE_URLS = {}


def on_files(files, **kwargs):
    PAGE_URLS.clear()
    PAGE_URLS.update((file.src_uri, file.url) for file in files.documentation_pages())


def on_page_content(html, *, page, **kwargs):
    uri = page.file.src_uri
    if uri not in COURSE_PAGES and uri not in PATH_PAGES and not page.is_homepage:
        return html
    intro, heading, rest = html.partition("<h2")
    if not heading:
        return html
    return f'<header class="learning-intro">{intro}</header>\n{heading}{rest}'


def on_page_context(context, *, page, **kwargs):
    uri = page.file.src_uri
    catalog = CATALOGS.get(uri)
    course = COURSE_PAGES.get(uri)
    if not (catalog or course or uri in PATH_PAGES or page.is_homepage):
        return context

    def url(target):
        return get_relative_url(PAGE_URLS[target], page.url)

    layout = {"kind": "landing", "courses_url": url(COURSE_CATALOG), "paths_url": url(PATH_CATALOG)}
    if catalog:
        layout.update(catalog)
        layout["kind"] = "catalog"
        layout["entries"] = [(item, url(item.uri)) for item in catalog["entries"]]
        layout["categories"] = tuple(dict.fromkeys(item.category for item in catalog["entries"]))
        layout["browse_url"] = url(catalog["browse"][0])
        layout["resources"] = [(url(location), label) for location, label in catalog["resources"]]
    elif course:
        layout["kind"] = "lesson" if uri != course.uri else "course"
        layout["course"] = course
        layout["course_url"] = url(course.uri)
        layout["sections"] = [(title, [(label, location, url(location)) for label, location in lessons])
                              for title, lessons in course.sections]
        layout["current"] = uri
        layout["total"] = sum(len(lessons) for _, lessons in course.sections)
    context["learning_layout"] = layout
    return context
