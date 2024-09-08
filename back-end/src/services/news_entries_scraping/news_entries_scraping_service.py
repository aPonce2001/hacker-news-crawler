from typing import List
from requests import get as get_request

from src.contracts.entries_scraping_service import EntriesScrapingService
from src.models.news_entry import NewsEntry
from src.services.news_entries_scraping.html_entries_parser import HtmlEntriesParser


class NewsEntriesScrapingService(EntriesScrapingService):
    def __init__(self, url: str, parser: HtmlEntriesParser) -> None:
        self.__url = url
        self.__parser = parser

    def get_entries(self) -> List[NewsEntry]:
        response = get_request(self.__url).text
        return self.__parser.parse_entries(response)
