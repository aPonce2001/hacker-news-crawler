from typing import List

from src.contracts.entries_scraping_service import EntriesScrapingService
from src.models.news_entry import NewsEntry
from src.services.news_entries_scraping.html_entries_parser import HtmlEntriesParser


class MockNewsEntriesScrapingService(EntriesScrapingService):
    def __init__(self, content: str, parser: HtmlEntriesParser) -> None:
        self.__content = content
        self.__parser = parser

    def get_entries(self) -> List[NewsEntry]:
        return self.__parser.parse_entries(content=self.__content)


html_entries_parser = HtmlEntriesParser()


def test_get_entries_1():
    '''Test the get_entries function with a not valid content, that will return an empty list'''
    mock_news_entries_scraping_service = MockNewsEntriesScrapingService(
        content='test',
        parser=html_entries_parser
    )
    assert len(mock_news_entries_scraping_service.get_entries()) == 0


def test_get_entries_2():
    '''Test the get_entries function with a valid content, that will return a list of news entries'''
    mock_news_entries_scraping_service = MockNewsEntriesScrapingService(
        content="""
        <table id="hnmain">
            <tr></tr>
            <tr></tr>
            <tr>
                <td>
                <table>
                    <tr class="athing">
                    <td class="title">
                        <span class="rank">1.</span>
                    </td>
                    <td class="votelinks">
                        <center>
                        <a>
                            <div class="votearrow" title="upvote"></div>
                        </a>
                        </center>
                    </td>
                    <td class="title">
                        <span class="titleline"
                        ><a>Companies need junior devs</a
                        ><span class="sitebit comhead">
                            (<a><span class="sitestr">robinsloan.com</span></a
                            >)
                        </span></span
                        >
                    </td>
                    </tr>
                    <tr>
                    <td colspan="2"></td>
                    <td class="subtext">
                        <span class="subline">
                        <span class="score">89 points</span> by
                        <a>fanf2</a>
                        <span class="age"><a>1 hour ago</a></span>
                        <span></span> | <a>hide</a> |
                        <a>74&nbsp;comments</a>
                        </span>
                    </td>
                    </tr>
                    <tr class="spacer" style="height: 5px"></tr>
                    <tr class="athing">
                    <td class="title">
                        <span class="rank">2.</span>
                    </td>
                    <td class="votelinks">
                        <center>
                        <a>
                            <div class="votearrow" title="upvote"></div>
                        </a>
                        </center>
                    </td>
                    <td class="title">
                        <span class="titleline"
                        ><a>Graphics Tricks from Boomers</a
                        ><span class="sitebit comhead">
                            (<a><span class="sitestr">robinsloan.com</span></a
                            >)
                        </span></span
                        >
                    </td>
                    </tr>
                    <tr>
                    <td colspan="2"></td>
                    <td class="subtext">
                        <span class="subline">
                        <span class="score">19 points</span> by
                        <a>fanf2</a>
                        <span class="age"><a>1 hour ago</a></span>
                        <span></span> | <a>hide</a> |
                        <a>1&nbsp;comment</a>
                        </span>
                    </td>
                    </tr>
                    <tr class="spacer" style="height: 5px"></tr>
                    <tr class="morespace" style="height: 10px"></tr>
                    <tr><div class="morelink"><a href="more">more</a></div></tr>
                </table>
                </td>
            </tr>
            </table>
        """,
        parser=html_entries_parser
    )

    expected_news_entries = [
        NewsEntry(
            number=1,
            title="Companies need junior devs",
            points=89,
            comments_count=74
        ),

        NewsEntry(
            number=2,
            title="Graphics Tricks from Boomers",
            points=19,
            comments_count=1
        ),
    ]

    got_news_entries = mock_news_entries_scraping_service.get_entries()

    assert len(got_news_entries) == 2

    for i, expected_news_entry in enumerate(expected_news_entries):
        expected_entry = expected_news_entries[i]
        assert got_news_entries[i].number == expected_news_entry.number
        assert got_news_entries[i].title == expected_entry.title
        assert got_news_entries[i].points == expected_entry.points
        assert got_news_entries[i].comments_count == expected_entry.comments_count
