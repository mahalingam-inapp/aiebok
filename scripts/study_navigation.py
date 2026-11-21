"""Shared lecture navigation for technical books and applied courses."""
from html import escape


def lecture_progress(course: str, filename: str, section: str, number: int, total: int) -> str:
    detail = escape(f"{section} · Lecture {number} of {total}")
    return f'<p class="study-position" data-course="{escape(course)}" data-lecture="{escape(filename)}">{detail}</p>'


def directions(titles: list[tuple[str, str]], number: int, *, footer: bool = False) -> str:
    previous = ""
    if number > 1:
        title, filename = titles[number - 2]
        previous = f"[← {title}]({filename})"
    if number < len(titles):
        title, filename = titles[number]
        following = f"[{title} →]({filename})"
    else:
        following = "[Course project →](index.md#course-project)"
    overview = "[Course outline](index.md#course-outline){ .study-overview }"
    links = " · ".join(link for link in (previous, overview, following) if link)
    return f"{links}\n{{: .study-directions{' .study-directions--footer' if footer else ''} }}"


def lecture_outline(groups: list[tuple[str, list[tuple[str, str]]]], filename: str) -> str:
    rows = ['??? note "Jump to a lecture"', ""]
    for title, lectures in groups:
        rows.append(f"    **{title}**")
        rows.append("")
        for label, path in lectures:
            rows.append(f"    - **{label}** (current)" if path == filename else f"    - [{label}]({path})")
        rows.append("")
    return "\n".join(rows).rstrip()


def start_course(course: str, filename: str) -> str:
    return f'[Start the first lecture]({filename}){{ .md-button .md-button--primary .study-start data-course="{course}" }}'


def outline_link(label: str, filename: str) -> str:
    return f'[{label}]({filename}){{ .study-lecture data-lecture="{filename}" }}'
