# Your First 30 Minutes

## 1. Install

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`.

## 2. Preview

```bash
mkdocs serve
```

Open <http://127.0.0.1:8000>. Changes to Markdown refresh automatically.

## 3. Personalize (optional)

The site deploys without repository-specific configuration. Update the name, description, copyright, logo, and colors if desired. Add `site_url` only when you have chosen the final public URL.

## 4. Validate

```bash
python scripts/validate_content.py
mkdocs build --strict
```

## 5. Publish

1. Create a GitHub repository named `aiebok`.
2. Push this repository to its `main` branch.
3. In **Settings → Pages**, select **GitHub Actions** as the source.
4. The included workflow builds and deploys the site on each push to `main`.

!!! tip "Custom domain"
    Configure the domain in GitHub Pages, then add the final HTTPS address as `site_url` for canonical metadata and sitemap URLs.
