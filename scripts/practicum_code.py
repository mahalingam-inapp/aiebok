"""The executable lecture cells shared by course pages and notebooks."""

from pathlib import Path

EXAMPLES = Path(__file__).resolve().parent / "practicum_examples"


def lecture_cells(course):
    if not course.workbook:
        return ()
    cells = tuple(cell.strip() for cell in (EXAMPLES / f"{course.slug}.py").read_text(encoding="utf-8").split("\n# %%\n"))
    expected = sum(len(lectures) for _, lectures in course.sections)
    if len(cells) != expected or not all(cells):
        raise ValueError(f"{course.slug} needs one nonempty code cell per lecture.")
    return cells
