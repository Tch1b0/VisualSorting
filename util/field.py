import random
from typing import Callable, Iterator


class Field:
    def __init__(self, algorithm: Callable[[list[int]], Iterator[list[int]]], size=500) -> None:
        self.field = [i for i in range(size)]
        self.algorithm = algorithm

    def shuffle(self) -> None:
        random.shuffle(self.field)

    def is_sorted(self) -> bool:
        for i in range(0, len(self.field) - 1):
            x, y = self.field[i], self.field[i+1]
            if x > y:
                return False
        return True

    def sort(self) -> Iterator[list[int]]:
        for items in self.algorithm(self.field.copy()):
            self.field = items.copy()
            yield items
