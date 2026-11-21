# AIEBOK

An open, mobile-friendly **AI Engineering Body of Knowledge** built with Markdown, MkDocs Material, and GitHub Pages.

Choose a [learning path](docs/getting-started/learning-paths/index.md) or browse the [course catalog](docs/courses/index.md). Lectures are grouped into sections within each course.

## Start locally

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
mkdocs serve
```

Open <http://127.0.0.1:8000>. Learners can find a suggested first session in [Your First 30 Minutes](docs/getting-started/first-30-minutes.md).

To publish, push to a GitHub repository, open **Settings → Pages**, and choose **GitHub Actions**. No username, repository name, backend, or secrets are required.

## What is included

<!-- site-stats:readme:start -->
- 14 role-based learning paths, 29 courses, and 142 lectures
- 23 downloadable course workbooks and 5 starter notebooks
- 20 knowledge-area maps
- 361 concept cards, 100 patterns, 25 architecture studios
- 13 build guides · 26 cloud capability guides
- 5 runnable starter labs (+ 78 chapter labs in the repo)
- Content templates and editorial quality system
- Link/configuration validation and GitHub Pages deployment
- A roadmap for growing the body of knowledge without turning it into an LMS
<!-- site-stats:readme:end -->

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
python scripts/generate_learning_paths.py
python scripts/generate_interactive_workbook.py
python scripts/generate_site_stats.py
python scripts/learning_cards.py
python scripts/generate_spec_driven.py
python scripts/validate_content.py
python scripts/audit_book_coverage.py
node scripts/check_interactive_workbook.js
mkdocs build --strict
```

After installing the notebook requirements, run `python scripts/check_notebooks.py` to validate and execute every workbook and starter notebook.

## GitHub Pages hosting

The published site is **static HTML only** (MkDocs → GitHub Actions → Pages). Nothing executes on the server at request time.

| Need | Where |
|---|---|
| Read docs, search, concept cards | Hosted site |
| Lecture slide decks | **Open slide deck** on each lecture page |
| Course workbooks | [Jupyter Notebooks](docs/labs/notebooks/index.md) in the site |
| Offline interactive workbook | [HarborLink](docs/labs/interactive-workbook.md) under Labs |
| Starter lab notebooks | <a href="https://github.com/mahalingam-inapp/aiebok/tree/main/labs" target="_blank" rel="noopener"><code>labs/*/lab.ipynb</code></a> in the repo — start at **Labs → Hands-on Start** on the site |
| Python labs | Local machine, Codespaces, or Dev Container (`.devcontainer/`) |

MkDocs generates the standalone HTML decks from the curriculum catalogs during each build. Open a deck from its lecture and use the onscreen controls or arrow keys to advance. The decks share local CSS and JavaScript.

## Dev Container / Codespaces

Open the repo in GitHub Codespaces or a VS Code Dev Container to install Jupyter and MkDocs automatically. For local notebook use, run `python -m pip install -r requirements-notebooks.txt` in the active virtual environment.

```bash
jupyter lab docs/assets/notebooks/01-foundations-of-intelligence.ipynb
```

## License

Code samples are MIT licensed. Written content is CC BY 4.0. See `LICENSE` and `LICENSE-CONTENT`.
