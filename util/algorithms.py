import random
from typing import Iterator
from numpy import block

from pkg_resources import yield_lines


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


def own_sort(items: list[int]) -> Iterator[list[int]]:
    for i in range(2, len(items) + 1):
        block_size = int(len(items)/i)
        blocks: list[list[int]] = []
        for j in range(0, int(len(items)/block_size) + 1):
            blocks.append(items[j*block_size:(j*block_size)+block_size])
        for j in range(0, len(blocks) - 1):
            if sum(blocks[j]) > sum(blocks[j + 1]):
                swap(blocks, j, j + 1)

        new_items = []
        for b in blocks:
            for i in b:
                new_items.append(i)
        items = new_items
        yield items.copy()


ALGORITHMS = {
    "bubble": bubble_sort,
    "bogo": bogo_sort,
    "gnome": gnome_sort,
    "own": own_sort
}

if __name__ == "__main__":
    _items = [x for x in range(1, 500 + 1)]
    random.shuffle(_items)
    for items in own_sort(_items.copy()):
        assert len(
            items) == 500, f"len(items) != 500; len(items) == {len(items)}"
