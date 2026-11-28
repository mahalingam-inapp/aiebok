# Quantization and inference measurement

<p class="study-position" data-course="llm-adaptation-inference" data-lecture="03-quantization-and-inference-measurement.md">Compress and transfer · Lecture 3 of 4</p>

[← Train and evaluate a low-rank adapter](02-train-and-evaluate-a-low-rank-adapter.md) · [Course outline](index.md#course-outline){ .study-overview } · [Transfer to an open-weight checkpoint →](04-transfer-to-an-open-weight-checkpoint.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Establish and adapt baselines**

    - [Autoregressive evaluation and retrieval baseline](01-autoregressive-evaluation-and-retrieval-baseline.md)
    - [Train and evaluate a low-rank adapter](02-train-and-evaluate-a-low-rank-adapter.md)

    **Compress and transfer**

    - **Quantization and inference measurement** (current)
    - [Transfer to an open-weight checkpoint](04-transfer-to-an-open-weight-checkpoint.md)

## What you will learn

Quantize a learned correction and compare held-out quality, payload bytes, and latency.

## Memory savings and latency savings are different observations

A lower-precision correction is smaller to store, but unpacking it for each request takes extra work in a local implementation.

Measure payload size including scale metadata and compare repeated timings on the same hardware. Report quality drift separately from memory and speed. Name the parts of inference the timing actually includes.

## How it works

Symmetric quantization maps floating-point values to an integer range using a scale. Keep model quality and numeric drift separate from performance. A smaller payload can reduce transfers, while dequantization can add work on hardware without suitable kernels.

### Measure precision trade-offs on the path that runs

Quantization stores values with lower precision. A typical integer scheme pairs compact values with scales that approximate the original values when used. Payload bytes include those scales and any metadata. Also report whether the measurement covers the adapter, the base model, or the whole deployment.

Lower storage cost is independent of faster inference. Unpacking or converting values can cost more time in a local implementation. A production runtime with suitable kernels might behave differently. Repeat the same workload on the same machine, record warm-up and measurement conditions, and report latency separately from quality.

Check both task behavior and numerical drift. Small changes in scores can flip a decision near a threshold even when average performance barely moves. Use cases near the edge and actual routing outcomes to decide whether a compression setting is acceptable.

## Worked example

An int8 correction uses fewer payload bytes. In a small Python implementation, unpacking can offset any latency benefit.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
from array import array
from statistics import median
from time import perf_counter


def quantize(values):
    scale = max(abs(value) for value in values) / 127 or 1
    return array("b", (round(value / scale) for value in values)), array("f", [scale])


# Pack the whole correction with one scale. The scale is included in the byte count.
float_payload = array("f", a + b)
int_payload, scale = quantize(float_payload)


def compressed(text):
    unpacked = [item * scale[0] for item in int_payload]
    return forward(text, unpacked[:len(a)], unpacked[len(a):])


def timed(model, count=300):
    values = []
    for _ in range(count):
        start = perf_counter()
        model(test[0].text)
        values.append((perf_counter() - start) * 1e6)
    return median(values)


compressed_bytes = len(int_payload.tobytes()) + len(scale.tobytes())
assert compressed_bytes < len(float_payload.tobytes())
assert abs(metrics(adapted, test)["log_loss"] - metrics(compressed, test)["log_loss"]) < 0.05
print("float bytes", len(float_payload.tobytes()), "compressed bytes", compressed_bytes,
      "median µs float/int8", timed(adapted), timed(compressed))
```

## Try it yourself

Run repeated measurements before and after quantizing. Record scale overhead and name the hardware.

[Download the workbook](../../assets/notebooks/llm-adaptation-inference.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Report actual bytes for the matrix payload and the measured timing distribution. Clarify which model components the demonstration compresses.

## Continue

[← Train and evaluate a low-rank adapter](02-train-and-evaluate-a-low-rank-adapter.md) · [Course outline](index.md#course-outline){ .study-overview } · [Transfer to an open-weight checkpoint →](04-transfer-to-an-open-weight-checkpoint.md)
{: .study-directions .study-directions--footer }
