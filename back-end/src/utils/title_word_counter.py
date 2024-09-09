from re import sub


def count_title_words(title: str) -> int:
    normalized_title = sub(r'[^\w\s]', '', title)
    return len(normalized_title.split())
