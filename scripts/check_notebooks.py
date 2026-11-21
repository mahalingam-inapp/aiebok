"""Validate and execute the starter notebooks and downloadable course workbooks."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from tempfile import TemporaryDirectory

from nbclient import NotebookClient
from nbformat import read, validate

from applied_courses import APPLIED_COURSES
from generate_books import BOOKS, course_slug
from generate_lab_notebooks import COURSE_NOTEBOOKS, LABS, ROOT, STARTER_LABS


def execute(notebook: Path, directory: Path) -> None:
    document = read(notebook, as_version=4)
    validate(document)
    NotebookClient(
        document,
        timeout=60,
        kernel_name="python3",
        resources={"metadata": {"path": str(directory)}},
    ).execute()


def check(job: tuple[Path, Path]) -> None:
    notebook, directory = job
    try:
        execute(notebook, directory)
    except Exception as error:
        raise RuntimeError(f"{notebook.relative_to(ROOT)} failed from {directory}") from error
    print(f"Passed {notebook.relative_to(ROOT)} from {directory.name}", flush=True)


def main() -> None:
    slugs = [course_slug(number, book["title"]) for number, book in enumerate(BOOKS, 1)]
    slugs.extend(course.slug for course in APPLIED_COURSES)
    courses = [COURSE_NOTEBOOKS / f"{slug}.ipynb" for slug in slugs]
    if set(courses) != set(COURSE_NOTEBOOKS.glob("*.ipynb")):
        raise ValueError("Expected exactly one identified workbook for every technical course.")
    starters = [LABS / slug / "lab.ipynb" for slug, *_ in STARTER_LABS]
    with TemporaryDirectory(prefix="aiebok-notebooks-") as scratch:
        jobs = [(path, Path(scratch)) for path in courses]
        jobs.extend((path, directory) for path in starters for directory in (ROOT, path.parent))
        with ThreadPoolExecutor(max_workers=4) as pool:
            list(pool.map(check, jobs))
    print(f"Verified {len(courses)} course workbooks and {len(starters)} starter notebooks.")


if __name__ == "__main__":
    main()
