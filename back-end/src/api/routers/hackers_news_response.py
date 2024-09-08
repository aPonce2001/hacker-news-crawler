from typing import List
from src.models.news_entry import NewsEntry

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel


class HackerNewsResponse(BaseModel):
    number: int = Field(..., alias="number")
    title: str = Field(..., alias="title")
    points: int = Field(..., alias="points")
    comments_count: int = Field(..., alias="commentsCount")


class HackerNewsResponseAdapter:
    @staticmethod
    def to_hacker_news_response(news_entry: NewsEntry) -> HackerNewsResponse:
        data = {
            "number": news_entry.number,
            "title": news_entry.title,
            "points": news_entry.points,
            "commentsCount": news_entry.comments_count
        }

        return HackerNewsResponse(**data)

    @staticmethod
    def to_hacker_news_responses(news_entries: List[NewsEntry]) -> List[HackerNewsResponse]:
        return [HackerNewsResponseAdapter.to_hacker_news_response(news_entry) for news_entry in news_entries]
