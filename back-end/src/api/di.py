from src.services.news_entries_scraping.html_entries_parser import HtmlEntriesParser
from src.services.news_entries_scraping.news_entries_scraping_service import NewsEntriesScrapingService


html_entries_parser = HtmlEntriesParser()
news_entries_scraping_service = NewsEntriesScrapingService(
    url='https://news.ycombinator.com/',
    parser=html_entries_parser
)

def get_news_entries_scraping_service() -> NewsEntriesScrapingService:
    return news_entries_scraping_service