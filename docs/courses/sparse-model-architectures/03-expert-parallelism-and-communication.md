# Expert parallelism and communication

<p class="study-position" data-course="sparse-model-architectures" data-lecture="03-expert-parallelism-and-communication.md">Size the system and workload · Lecture 3 of 4</p>

[← Expert capacity and load balancing](02-expert-capacity-and-load-balancing.md) · [Course outline](index.md#course-outline){ .study-overview } · [Hybrid backbones and architecture selection →](04-hybrid-backbones-and-architecture-selection.md)
{: .study-directions }

??? note "Jump to a lecture"

    **Route tokens through experts**

    - [Token routing and top-k experts](01-token-routing-and-top-k-experts.md)
    - [Expert capacity and load balancing](02-expert-capacity-and-load-balancing.md)

    **Size the system and workload**

    - **Expert parallelism and communication** (current)
    - [Hybrid backbones and architecture selection](04-hybrid-backbones-and-architecture-selection.md)

## What you will learn

Account for expert dispatch and return traffic alongside local computation and queueing.

## Follow the activation across devices

The sparsest candidate reduces expert FLOPs in a spreadsheet. Its busiest expert lives across a slow link from the device handling most inputs.

Estimate the outgoing and return payload. Mark the synchronization cost and collective startup as unknown. Watch the busiest rank before attributing a latency miss to the model math.

## How it works

Expert parallelism distributes expert weights across devices. A token whose chosen expert is remote must send an activation and receive the transformed activation. Traffic depends on the routing distribution, placement, shared replication, and message layout. A simplified byte count excludes collective startup, padding and synchronization, so it cannot predict latency by itself.

### Placement belongs in the latency budget
Split weight memory from communication. Replicating a popular expert may reduce load on one rank at the cost of memory elsewhere. Measure collective time, maximum rank load, per-device memory, and throughput with fixed sequence lengths and concurrency. A low average rank load can coexist with a straggler because the step must wait for the slowest participants. Compare a placement change with the same routed workload to isolate its effect.

## Worked example

For 64 remote assignments of width 4096 at two bytes per number, dispatch and return together move 1 MiB of activation payload under the simple accounting model.

### Follow the example

**Given:** Rank 0 sends 64 tokens to an expert on rank 1. Each token has 4,096 two-byte elements.

**Walkthrough:** The send is 512 KiB and the return is another 512 KiB. Time the transfer and the slowest rank separately. Payload alone leaves the collective and queueing costs unknown.

## Follow the code

Run this cell after the preceding cells in the course workbook. Read the inputs and checks before running it. Use the practice below to change one assumption and compare the result.

```python
def remote_bytes(assignments, placements, width, element_bytes):
    remote = sum(source_rank != placements[expert] for source_rank, expert in assignments)
    return remote * width * element_bytes * 2


traffic = [(0, 0)] * 64 + [(1, 1)] * 8
for placement in ((0, 1), (1, 0)):
    print("payload bytes", remote_bytes(traffic, placement, 4096, 2))
assert remote_bytes([(0, 0)] * 64, (1,), 4096, 2) == 1024 ** 2
```

## Try it yourself

Place the busiest expert on another device and inspect how remote assignment traffic changes. Record one measurement that the byte model lacks.

[Download the workbook](../../assets/notebooks/sparse-model-architectures.ipynb){ download } and run through **Lecture 03** in order. See [Jupyter setup](../../labs/notebooks/index.md#set-up-jupyter) if needed.

??? success "Compare your answer"
    Ownership and routing together determine traffic. Use a serving profiler to measure dispatch time, device utilization, and the slowest rank before choosing an expert layout.

## Continue

[← Expert capacity and load balancing](02-expert-capacity-and-load-balancing.md) · [Course outline](index.md#course-outline){ .study-overview } · [Hybrid backbones and architecture selection →](04-hybrid-backbones-and-architecture-selection.md)
{: .study-directions .study-directions--footer }
