from enum import Enum
from typing import Callable, List, Tuple, Union

from src.models.news_entry import NewsEntry


class Operation(Enum):
    SORT = 1,
    FILTER = 2


class FilterBuilder:
    def __init__(self, entries: List[NewsEntry]):
        self.__entries = entries
        self.__operations: List[
            Tuple[
                Union[
                    Callable[[NewsEntry], bool],
                    Tuple[Callable[[NewsEntry], Union[int, float, str]], bool]],

                Operation
            ]
        ] = []

    def where(self, function: Callable[[NewsEntry], bool]):
        self.__operations.append((function, Operation.FILTER))
        return self

    def order_by(self, function: Callable[[NewsEntry], Union[int, float, str]], reverse: bool = False):
        self.__operations.append(((function, reverse), Operation.SORT))
        return self

    def execute_filter(self) -> List[NewsEntry]:

        for function, operation in self.__operations:
            if operation == Operation.SORT:
                sort_function, reverse = function
                self.__entries = list(sorted(self.__entries, key=sort_function, reverse=reverse))
                continue
            if operation == Operation.FILTER:
                self.__entries = list(
                    filter(function, self.__entries))
                continue

        return list(self.__entries)
