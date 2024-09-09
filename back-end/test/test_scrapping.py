from src.services.news_entries_scraping.html_entries_parser import HtmlEntriesParser
from src.services.news_entries_scraping.news_entries_scraping_service import NewsEntriesScrapingService


html_entries_parser = HtmlEntriesParser()
news_entries_scraping_service = NewsEntriesScrapingService(
    url='https://news.ycombinator.com/',
    parser=html_entries_parser
)


def test_get_entries_1():
    '''Test the get_entries function with the url of Hacker News should return 30 entries'''
    assert len(news_entries_scraping_service.get_entries()) == 30