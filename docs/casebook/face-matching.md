# The errors a face-matching average hides

## What researchers measured

In 2019, NIST published a comparison of demographic effects in face-matching algorithms. Results depended on the algorithm, the task, and the image data. The authors found demographic differences in error rates in most of the algorithms evaluated. They distinguish one-to-one verification from one-to-many identification, where the operational meaning of a false match differs. [NIST Face Recognition Vendor Test, Part 3](https://www.nist.gov/publications/face-recognition-vendor-test-part-3-demographic-effects)

## Follow the mistake to the person who bears it

A false rejection at a building entrance can mean a worker is late because they must find someone to verify their identity. A false acceptance raises another concern for the building operator. Teams should decide which outcome they are optimizing for and inspect how often each failure occurs under actual operating conditions. Sensor quality, camera placement, and fallback staffing can change what people experience even if the model stays the same.

The following are **illustrative** counts from two entrances with different capture conditions.

| Entrance | Valid attempts | Valid attempts rejected | Rejection rate |
|---|---:|---:|---:|
| Main entry | 900 | 9 | 1% |
| Side entry | 100 | 10 | 10% |
| Combined | 1,000 | 19 | 1.9% |

The aggregate is dominated by the main entrance. A policy based only on 1.9% could understate the experience of workers using the side entrance. The table also gives no evidence about false acceptance.

What evidence would you ask for before changing the threshold? Check sample sizes, image conditions, and false acceptance by entrance, then test a staffed alternative. Record the time a rejected worker spends recovering access. That is an outcome the model metrics omit.

[Machine Learning Systems](../books/02-machine-learning-systems/index.md) · [Evaluation, Safety, and Governance](../books/10-evaluation-safety-and-governance/index.md) · [Casebook](index.md)
