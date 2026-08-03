# AIEBOK

An open, mobile-friendly **AI Engineering Body of Knowledge** built with Markdown, MkDocs Material, and GitHub Pages.

## Start locally

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
mkdocs serve
```

Open <http://127.0.0.1:8000>. See `docs/getting-started/first-30-minutes.md` for the guided setup.

To publish, push to a GitHub repository, open **Settings → Pages**, and choose **GitHub Actions**. No username, repository name, backend, or secrets are required.

## What is included

- A complete 19-knowledge-area curriculum plan
- Starter concept, pattern, architecture, cloud, paper, and lab pages
- Five runnable, dependency-light Python labs
- Content templates and an editorial quality system
- Link/configuration validation and GitHub Pages deployment
- A roadmap for growing the body of knowledge without turning it into an LMS

## Validate and build

```bash
python scripts/build_concept_entries.py
python scripts/generate_expansion.py
python scripts/generate_books.py
python scripts/generate_maturity_content.py
python scripts/validate_content.py
python scripts/audit_book_coverage.py
mkdocs build --strict
```

## License

Code samples are MIT licensed. Written content is CC BY 4.0. See `LICENSE` and `LICENSE-CONTENT`.
