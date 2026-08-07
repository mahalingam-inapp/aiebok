# Spec-Driven AI Feature

## Context

Write executable specs before model integration.

## Solution

Examples define acceptance; tests drive implementation.

## Consequences

Aligns PM, eng, and evals. Upfront writing cost.

## Do not use when

Exploratory research spikes.

## Tooling

### OpenSpec workflow

```bash
npm install -g @fission-ai/openspec@latest
openspec init
```

```text
/opsx:explore        # clarify problem before artifacts
/opsx:propose        # generate proposal + delta specs + tasks
/opsx:apply          # implement against tasks.md
/opsx:archive        # merge specs into openspec/specs/
```

### Cursor workflow

```bash
cursor .
```

Use **Plan** mode with the feature brief and acceptance YAML in context. Require a green pytest run before merge:

```bash
python -m pytest -q
```

### Sample acceptance file

```yaml
# specs/feature-x.yaml
feature: invoice_extractor
cases:
  - name: valid_pdf
    input: fixtures/invoice_clean.pdf
    expect_schema: invoice/v1
    expect_status: ok
  - name: missing_vendor
    input: fixtures/invoice_partial.pdf
    expect_status: structured_error
    expect_code: MISSING_VENDOR
```

See [spec-driven workflow](../getting-started/spec-driven-workflow.md).
