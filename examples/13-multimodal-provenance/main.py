"""Preserve provenance while combining extracted multimodal evidence."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Evidence:
    content: str
    source: str
    page: int
    modality: str
    confidence: float


items = [
    Evidence("Revenue: 12M", "report.pdf", 3, "table", .98),
    Evidence("Revenue increased", "report.pdf", 4, "chart", .82),
]
usable = [item for item in items if item.confidence >= .90]
for item in usable:
    print(f"{item.content} [{item.source}#page={item.page}; modality={item.modality}]")
