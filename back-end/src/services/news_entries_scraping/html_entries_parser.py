from typing import List

from bs4 import BeautifulSoup, ResultSet, Tag
from src.models.news_entry import NewsEntry


class HtmlEntriesParser:
    def parse_entries(self, content: str) -> List[NewsEntry]:
        soup = BeautifulSoup(content, "html.parser")
        items: ResultSet[Tag] = soup.select(
            "#hnmain > tr:nth-child(3) > td > table > tr:not(.spacer, .morespace, :has(.morelink))")

        entries: List[NewsEntry] = []

        for i in range(0, len(items), 2):
            number: int = int(items[i].select_one(
                ".title > .rank").get_text().strip().strip("."))
            
            title: str = items[i].select_one(
                ".title > .titleline > a").get_text().strip()

            points_tag = items[i + 1].select_one(".subtext > .subline > .score")
            if points_tag is not None:
                points = int(points_tag.get_text().strip().split(" ")[0])
            else:
                points = 0
            
            comments_tag = items[i + 1].select_one(".subtext > .subline > a:last-child")
            if comments_tag is None:
                comments_count = 0
            else:
                comments_text = comments_tag.get_text().strip()
                comments_count = 0 if comments_text == "discuss" else int(comments_text.split("\xa0")[0])

            new_entry = NewsEntry(
                number=number,
                title=title,
                points=points,
                comments_count=comments_count
            )
            entries.append(new_entry)

        return entries
