# Version a model artifact and regression gate

<p class="study-position" data-course="model-selection-and-adaptation" data-lecture="04-version-a-model-artifact-and-regression-gate.md">Choose a threshold and package evidence · Lecture 4 of 4</p>

[← Measure selective risk and cost](03-measure-selective-risk-and-cost.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions }

??? note "Jump to a lecture"

    **Prepare data and learn a baseline**

    - [Group-aware splits and dataset lineage](01-group-aware-splits-and-dataset-lineage.md)
    - [Fit and compare a supervised baseline](02-fit-and-compare-a-supervised-baseline.md)

    **Choose a threshold and package evidence**

    - [Measure selective risk and cost](03-measure-selective-risk-and-cost.md)
    - **Version a model artifact and regression gate** (current)

## What you will learn

Serialize a fitted model, reload it, and gate release using both quality and coverage.

## Save what the operator will actually run

The model artifact reloads correctly. Another team loads it with a different threshold because that setting was stored in a notebook cell.

Version parameters, preprocessing, threshold, and split evidence together. Run an artifact round trip and a gate check so the deployed decision matches the one that reviewers evaluated.

## How it works

Persist parameters, label order, model configuration, and dataset lineage. Check loaded predictions against the in-memory result. Gate on meaningful evidence and inspect slice sample counts before trusting a pass. Changing parameters or the decision threshold should produce a new artifact and reevaluation.

### A release includes the decision rule

Saving only model weights is insufficient if another environment uses different tokenization, a different threshold, or a different label order. Package the estimator with input normalization, output mapping, version identifiers, and the operating point that was evaluated.

Make a known-case round trip. Save the artifact, reload it through the same interface as serving, and compare predictions and fallback outcomes on a narrow fixture. Include a request at or close to the threshold. That case can reveal small version differences that a simple serialization check will miss.

Tie each release to a replayable evaluation record. Declare which failing slice would block deployment, and which previously approved artifact can be restored. After switching versions, verify the result through the serving route. An unchanged file hash confirms you loaded an object, while the round trip checks that people still receive the intended decision.

## Worked example

A new model achieves better accepted accuracy by deferring half the traffic. A minimum coverage requirement surfaces the extra operational burden.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
import json
from pathlib import Path
from tempfile import TemporaryDirectory

artifact = {"dataset": dataset_version, "model_version": "nb-v1", "threshold": threshold, "parameters": model}
with TemporaryDirectory() as directory:
    artifact_path = Path(directory) / "classifier.json"
    artifact_path.write_text(json.dumps(artifact), encoding="utf-8")
    restored = json.loads(artifact_path.read_text(encoding="utf-8"))

for row in splits["test"]:
    assert predict(restored["parameters"], row.text) == trained(row.text)

overall = report["all"]
release = (
    overall["coverage"] >= 0.5
    and overall["accepted_accuracy"] is not None
    and overall["accepted_accuracy"] >= 0.8
    and overall["cost"] < baseline["all"]["cost"]
)
print("Release decision for this fixture", "pass" if release else "hold", restored["model_version"])
```

## Try it yourself

Round-trip the model. Tighten the coverage requirement and observe when the gate changes.

[Download the workbook](../../assets/notebooks/model-selection-and-adaptation.ipynb){ download } and run through **Lecture 04** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Round-trip results should match exactly. Record a keep, revise, or release decision with the evaluated version and the reason.

## Continue

[← Measure selective risk and cost](03-measure-selective-risk-and-cost.md) · [Course outline](index.md#course-outline){ .study-overview } · [Course project →](index.md#course-project)
{: .study-directions .study-directions--footer }
