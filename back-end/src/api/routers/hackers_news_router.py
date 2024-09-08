from typing import List
from fastapi import APIRouter, Depends
from src.api.di import get_news_entries_scraping_service
from src.api.routers.hackers_news_response import HackerNewsResponse, HackerNewsResponseAdapter
from src.services.news_entries_scraping.news_entries_scraping_service import NewsEntriesScrapingService


router = APIRouter(prefix="/hacker-news-entries", tags=["Hacker News"])


@router.get("/")
def get_hackers_news(news_entries_scraping_service: NewsEntriesScrapingService = Depends(get_news_entries_scraping_service)) -> List[HackerNewsResponse]:
    return HackerNewsResponseAdapter.to_hacker_news_responses(
        news_entries_scraping_service.get_entries()
    )
