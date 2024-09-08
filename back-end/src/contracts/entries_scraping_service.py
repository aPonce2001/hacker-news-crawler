from abc import ABC, abstractmethod
from typing import List

from src.models.news_entry import NewsEntry


class EntriesScrapingService(ABC):
    @abstractmethod
    def get_entries(self) -> List[NewsEntry]:
        ...
