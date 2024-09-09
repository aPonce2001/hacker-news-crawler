from typing import List, Optional
from fastapi import APIRouter, Depends
from src.api.di import get_news_entries_scraping_service
from src.api.routers.hackers_news_filter_request import HackersNewsFilterRequest
from src.api.routers.hackers_news_response import HackerNewsResponse, HackerNewsResponseAdapter
from src.services.filtering.filtering_builder import FilterBuilder
from src.services.news_entries_scraping.news_entries_scraping_service import NewsEntriesScrapingService
from src.utils.title_word_counter import count_title_words


router = APIRouter(prefix="/hacker-news-entries", tags=["Hacker News"])


@router.get("/")
def get_hackers_news(
    filter_request: Optional[HackersNewsFilterRequest] = None,
    news_entries_scraping_service: NewsEntriesScrapingService = Depends(
        get_news_entries_scraping_service)
) -> List[HackerNewsResponse]:
    entries = news_entries_scraping_service.get_entries()

    if filter_request is None:
        return HackerNewsResponseAdapter.to_hacker_news_responses(entries)

    filtering_builder = FilterBuilder(entries)

    if filter_request == HackersNewsFilterRequest.TITLE_WORDS_GREATER_THAN_FIVE_ORDER_BY_COMMENTS_DESC:
        entries = filtering_builder.where(
            lambda entry: count_title_words(entry.title) > 5
        ).order_by(
            lambda entry: entry.comments_count,
            reverse=True
        ).execute_filter()

    elif filter_request == HackersNewsFilterRequest.TITLE_WORDS_LESS_THAN_OR_EQUALS_TO_FIVE_ORDER_BY_POINTS_DESC:
        entries = filtering_builder.where(
            lambda entry: count_title_words(entry.title) <= 5
        ).order_by(
            lambda entry: entry.points,
            reverse=True
        ).execute_filter()

    return HackerNewsResponseAdapter.to_hacker_news_responses(entries)

