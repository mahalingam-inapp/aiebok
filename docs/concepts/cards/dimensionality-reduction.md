# Dimensionality Reduction

**Purpose:** Reference card for **dimensionality reduction** used across AIEBOK books and knowledge areas.

## Core explanation

Dimensionality reduction projects high-dimensional data to fewer dimensions for visualization, compression, or denoising—PCA, t-SNE, UMAP. Preserved geometry depends on the method.

## Example

PCA on ticket embeddings for dashboard visualization may linearly mix topics; UMAP preserves local neighborhoods differently.

## Evidence of understanding

Compare reconstruction error (PCA) or neighborhood preservation metrics on a fixed sample.

## Trade-offs

No mechanism is universal. Compare dimensionality reduction against a simpler baseline on normal, boundary, and adversarial cases before adding operational complexity.

## Related study

- Search guided books for chapters tagged with this concept
- Run the matching chapter lab under `labs/` when available
- Cross-check the [question index](../../reference/question-index.md)
