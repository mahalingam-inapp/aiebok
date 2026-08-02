# Deployment Checklist

## One-time personalization

- [ ] Review the site name, description, repository URL, copyright, and licenses.
- [ ] Replace or retain the included logo and color tokens.
- [ ] Decide whether to use the default GitHub Pages URL or a custom domain.

No repository name or username is hard-coded; the included GitHub Actions deployment works unchanged after push.

## Local release check

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/validate_content.py
mkdocs build --strict
mkdocs serve
```

- [ ] Inspect home, book index, one long chapter, one table, one Mermaid diagram, search, dark mode, and mobile navigation.
- [ ] Run all five starter labs.
- [ ] Confirm no secrets, private data, generated site directory, or virtual environment is committed.

## GitHub Pages

1. Push the repository to the `main` branch on GitHub.
2. Open **Settings → Pages**.
3. Choose **GitHub Actions** as the publishing source.
4. Run or wait for **Deploy MkDocs to GitHub Pages**.
5. Open the deployment URL shown in the workflow summary.

## After deployment

- [ ] Verify search and deep links from a private browser window.
- [ ] Verify the custom domain and HTTPS if configured.
- [ ] Add the public URL to the repository description.
- [ ] Enable Dependabot or schedule dependency review.
- [ ] Open issues for factual corrections and content gaps rather than blocking publication on perfection.
