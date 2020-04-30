from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class SearchDrama:
    id: int
    title: str
    cover_url: str
    ranking: Optional[int]
    score: Optional[float]
    description: str


@dataclass
class SearchResult:
    url: str
    dramas: List[SearchDrama]
    timestamp: datetime = datetime.now()

    def is_empty(self):
        return self.count() == 0

    def count(self):
        return len(self.dramas)
