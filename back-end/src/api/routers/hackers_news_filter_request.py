from enum import Enum


class HackersNewsFilterRequest(str, Enum):
    TITLE_WORDS_GREATER_THAN_FIVE_ORDER_BY_COMMENTS_DESC = "title_words_greater_than_five_order_by_comments_desc"
    TITLE_WORDS_LESS_THAN_OR_EQUALS_TO_FIVE_ORDER_BY_POINTS_DESC = "title_words_less_than_or_equals_to_five_order_by_points_desc"