from typing import List
from src.models.news_entry import NewsEntry
from src.services.filtering.filtering_builder import FilterBuilder
from src.utils.title_word_counter import count_title_words


def has_the_same_order_by_number(entries: List[NewsEntry], other_entries: List[NewsEntry]) -> bool:
    print(entries, other_entries)

    if len(entries) != len(other_entries):
        return False

    for i in range(len(entries)):
        if entries[i].number != other_entries[i].number:
            return False

    return True


def test_filtering_builder_1() -> None:
    entries = [
        NewsEntry(
            number=1,
            title="News 1",
            points=100,
            comments_count=10
        ),
        NewsEntry(
            number=2,
            title="News 2",
            points=200,
            comments_count=20
        ),
        NewsEntry(
            number=3,
            title="News 3",
            points=300,
            comments_count=30
        )
    ]

    builder = FilterBuilder(entries=entries)

    filtered_entries = builder.where(
        lambda entry: entry.title == "News 2"
    ).execute_filter()

    expected_entries = [entries[1]]

    assert has_the_same_order_by_number(filtered_entries, expected_entries)


def test_filtering_builder_filter_long_titles_order_by_comments() -> None:
    entries = [
        NewsEntry(number=1, title="This title has more than five words",
                  points=100, comments_count=30),

        NewsEntry(number=2, title="Short title",
                  points=200, comments_count=20),

        NewsEntry(number=3, title="Another long title with more than five words",
                  points=150, comments_count=10),

        NewsEntry(number=4, title="A title with exactly five words",
                  points=300, comments_count=25),
                  
        NewsEntry(number=5, title="Shorter", points=250, comments_count=15),
    ]

    builder = FilterBuilder(entries=entries)

    filtered_entries = builder.where(
        lambda entry: count_title_words(entry.title) > 5
    ).order_by(
        lambda entry: entry.comments_count,
        reverse=True
    ).execute_filter()

    expected_entries = [
        entries[0],  # Title with more than five words and most comments
        entries[3],  # Title with exactly five words and fewer comments
        entries[2],  # Another long title with fewer comments
    ]

    assert has_the_same_order_by_number(filtered_entries, expected_entries)


def test_filtering_builder_filter_short_titles_order_by_points() -> None:
    entries = [
        NewsEntry(number=1, title="This title has more than five words",
                  points=100, comments_count=30),

        NewsEntry(number=2, title="Short title",
                  points=200, comments_count=20),

        NewsEntry(number=3, title="Another long title with more than five words",
                  points=150, comments_count=10),

        NewsEntry(number=4, title="Title with exactly five words",
                  points=300, comments_count=25),

        NewsEntry(number=5, title="Shorter", points=250, comments_count=15),
    ]

    builder = FilterBuilder(entries=entries)

    filtered_entries = builder.where(
        lambda entry: count_title_words(entry.title) <= 5
    ).order_by(
        lambda entry: entry.points,
        reverse=True
    ).execute_filter()

    expected_entries = [
        entries[3],  # Short title with highest points
        entries[4],  # Short title with lower points
        entries[1],  # Short title with even lower points
    ]

    assert has_the_same_order_by_number(filtered_entries, expected_entries)
