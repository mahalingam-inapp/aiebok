# Chunking

**Purpose:** Split documents into retrieval-sized units while preserving semantic boundaries, provenance, and access metadata.

**Prerequisites:** Document ingestion, embeddings, retrieval basics.

## Why chunking exists

Models and retrievers operate on bounded context. Whole documents rarely fit; arbitrary splits destroy sentences, tables, and section structure. Chunking determines what evidence retrieval can ever surface.

## Core intuition

A chunk is a **retrieval atom**: it should be small enough to rank precisely and large enough to answer typical questions. Parent–child schemes store small search units linked to larger reading units for generation.

## Mechanics

1. Parse structure: headings, paragraphs, tables, lists, code blocks.
2. Choose strategy: fixed token windows, semantic boundaries, or layout-aware splits.
3. Attach metadata: source ID, section title, page, ACL, version, timestamps.
4. Index chunks; optionally index parent sections for context expansion after retrieval.
5. Evaluate recall with realistic queries—not average chunk length alone.

## Engineering checklist

- Measure retrieval recall before tuning generation prompts.
- Preserve table and list integrity; split mid-row breaks grounding.
- Align chunk boundaries with authorization boundaries in multi-tenant systems.
- Re-chunk and re-index when ingestion rules or embedding models change.

## Trade-offs

Smaller chunks improve precision but lose broader context; larger chunks improve context but dilute relevance signals. Hybrid parent–child designs add storage and join complexity.

## Common misconceptions

- Chunk size defaults from vector DB docs are not universal optima.
- OCR text without layout metadata often chunks poorly.
- More chunks always means better answers—only if retrieval selects the right ones.

## Evolution lens

Yesterday: whole-document keyword search. Today: structure-aware chunking with metadata and parent links. Tomorrow: learned segmentation and multimodal units. The durable principle is retrieval atoms aligned to questions and provenance.
