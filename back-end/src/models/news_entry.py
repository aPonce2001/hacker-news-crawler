from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class NewsEntry:
    number: int
    title: str
    points: int
    comments_count: int
