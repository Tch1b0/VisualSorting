import random
from typing import Iterator


def is_sorted(items: list[int]) -> bool:
    for i in range(0, len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True


def swap(items: list[int], i1: int, i2: int):
    items[i1], items[i2] = items[i2], items[i1]
    return items


def bubble_sort(items: list[int]) -> Iterator[list[int]]:
    while not is_sorted(items):
        for i in range(0, len(items) - 1):
            left = items[i]
            right = items[i+1]

            if right < left:
                swap(items, i, i+1)

        yield items.copy()


def bogo_sort(items: list[int]) -> Iterator[list[int]]:
    while not is_sorted(items):
        random.shuffle(items)
        yield items.copy()


def gnome_sort(items: list[int]) -> Iterator[list[int]]:
    for i, right in enumerate(items):
        if i == 0:
            continue
        n = i
        while n != 0 and items[n - 1] > right:
            swap(items, n, n - 1)
            yield items.copy()
            n -= 1


ALGORITHMS = {
    "bubble": bubble_sort,
    "bogo": bogo_sort,
    "gnome": gnome_sort
}
