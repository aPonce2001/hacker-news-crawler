from src.utils.title_word_counter import count_title_words


def test_count_title_words_1():
    assert count_title_words("Hello, World!") == 2


def test_count_title_words_2():
    assert count_title_words("This is - a self-explained example") == 5


def test_count_title_words_3():
    assert count_title_words("A                 B ") == 2


def test_count_title_words_4():
    assert count_title_words("   ") == 0


def test_count_title_words_5():
    assert count_title_words("   Leading and trailing spaces   ") == 4


def test_count_title_words_6():
    assert count_title_words("Multiple!!! punctuation??? marks.") == 3

def test_count_title_words_7():
    assert count_title_words("á é") == 2