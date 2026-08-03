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
python scripts/generate_cloud_guides.py
python scripts/generate_lessons.py
python scripts/generate_reference_views.py
python scripts/generate_featured_concepts.py
python scripts/generate_lab_notebooks.py
python scripts/generate_pdf.py
python scripts/generate_progress_manifest.py
python scripts/validate_content.py
python scripts/audit_book_coverage.py
mkdocs build --strict
```

## GitHub Pages hosting

The published site is **static HTML only** (MkDocs → GitHub Actions → Pages). Nothing executes on the server at request time.

| Need | Where |
|---|---|
| Read docs, search, concept cards | Hosted site |
| Print full sections | **Reference → Print & Offline** (print-site plugin) |
| Offline summary PDF | [aiebok-companion.pdf](docs/assets/aiebok-companion.pdf) (built in CI) |
| Starter lab notebooks | <a href="https://github.com/mahalingam-inapp/aiebok/tree/main/labs" target="_blank" rel="noopener"><code>labs/*/lab.ipynb</code></a> in the repo — start at **Labs → Hands-on Start** on the site |
| Python labs | Local machine, Codespaces, or Dev Container (`.devcontainer/`) |

## Dev Container / Codespaces

Open the repo in GitHub Codespaces or VS Code Dev Containers for Python 3.12, Jupyter, and MkDocs preinstalled:

```bash
mkdocs serve
jupyter lab labs/01-cosine-similarity/lab.ipynb
```

## License

Code samples are MIT licensed. Written content is CC BY 4.0. See `LICENSE` and `LICENSE-CONTENT`.
