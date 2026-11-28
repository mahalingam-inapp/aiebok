# Measure selective risk and cost

<p class="study-position" data-course="model-selection-and-adaptation" data-lecture="03-measure-selective-risk-and-cost.md">Choose a threshold and package evidence · Lecture 3 of 4</p>

[← Fit and compare a supervised baseline](02-fit-and-compare-a-supervised-baseline.md) · [Course outline](index.md#course-outline){ .study-overview } · [Version a model artifact and regression gate →](04-version-a-model-artifact-and-regression-gate.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Prepare data and learn a baseline**

    - [Group-aware splits and dataset lineage](01-group-aware-splits-and-dataset-lineage.md)
    - [Fit and compare a supervised baseline](02-fit-and-compare-a-supervised-baseline.md)

    **Choose a threshold and package evidence**

    - **Measure selective risk and cost** (current)
    - [Version a model artifact and regression gate](04-version-a-model-artifact-and-regression-gate.md)

## What you will learn

Pick an abstention threshold on validation and report coverage and accuracy on test.

## A better accepted score may cost more

A stricter threshold improves accuracy among answered cases and doubles the cases sent to the help desk.

Report accepted error, coverage, and review workload together. Choose the threshold on validation using an explicit error and handoff cost, then report results on held-out cases once.

## How it works

A selective classifier can hand uncertain cases to a person. Accuracy among answered cases can look high if the system answers very little, so report coverage alongside it. Use independently estimated costs for mistakes and reviews. Choose the threshold with validation data and freeze it before evaluating test.

### A decision threshold changes who does the work

A system can route high-confidence requests and send the rest to staff. Define **coverage** as the fraction of requests handled automatically and **selective risk** as the error rate on those accepted requests. Moving the threshold trades speed and queue volume against the number of incorrect automatic routes.

Imagine one setting accepts 80 of 100 requests and misroutes 8. Another accepts 60 and misroutes 3. Selective risk drops from 10% to 5%, while review volume doubles from 20 to 40. A recommendation needs operational costs as well as acceptance accuracy. Some wrong routes may be more costly than a manual review.

Select the threshold using validation data and a cost assumption appropriate to the workload. Report the final result on the held-out test, including uncertainty and per-group counts. Recheck that confidence estimates are usable on new traffic before assuming a threshold chosen from one set transfers to another.

## Worked example

If one mistaken route costs four minutes and a review costs one, a threshold may be valuable even when accuracy changes little. A small sample can only illustrate the trade-off.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
from collections import defaultdict


def evaluate(records, predictor, threshold, review_cost=1, error_cost=4):
    summary = defaultdict(Counter)
    for row in records:
        predicted, confidence = predictor(row.text)
        outcome = "handoff" if confidence < threshold else ("correct" if predicted == row.label else "wrong")
        summary["all"][outcome] += 1
        summary[row.slice][outcome] += 1
    result = {}
    for key, counts in summary.items():
        accepted = counts["correct"] + counts["wrong"]
        result[key] = {
            "n": counts.total(), "wrong_accepted": counts["wrong"], "handoffs": counts["handoff"],
            "coverage": accepted / counts.total(),
            "accepted_accuracy": counts["correct"] / accepted if accepted else None,
            "cost": review_cost * counts["handoff"] + error_cost * counts["wrong"],
        }
    return result


def trained(text):
    return predict(model, text)


thresholds = (0.5, 0.65, 0.8, 0.9)
validation = {t: evaluate(splits["validation"], trained, t)["all"] for t in thresholds}
threshold = min(thresholds, key=lambda t: (validation[t]["cost"], -validation[t]["coverage"], t))
baseline = evaluate(splits["test"], lambda text: (majority, 1), 0)
report = evaluate(splits["test"], trained, threshold)
print("Validation", validation)
print("Frozen threshold", threshold, "baseline", baseline, "test", report)
assert report["all"]["n"] == len(splits["test"])
assert report["all"]["cost"] < baseline["all"]["cost"]
```

## Try it yourself

Compare the tested thresholds. Increase review cost and see which threshold you would choose on validation.

[Download the workbook](../../assets/notebooks/model-selection-and-adaptation.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Report accepted count, wrong accepted count, and handoffs on each slice. Explain any change through its expected operating cost.

## Continue

[← Fit and compare a supervised baseline](02-fit-and-compare-a-supervised-baseline.md) · [Course outline](index.md#course-outline){ .study-overview } · [Version a model artifact and regression gate →](04-version-a-model-artifact-and-regression-gate.md)
{: .study-directions .study-directions--footer }
