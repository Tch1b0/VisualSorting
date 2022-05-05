import random
from typing import Iterator


def is_sorted(items: list[int]) -> bool:
    """
    checks whether the list is sorted
    """
    for i in range(0, len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True


def swap(items: list, i1: int, i2: int):
    """
    swaps two items in a list
    """
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
            n -= 1
        yield items.copy()


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


def insertion_sort(items: list[int]) -> Iterator[list[int]]:
    for i, item in enumerate(items):
        for j in range(0, i):
            if items[j] > item:
                items.pop(i)
                items.insert(j, item)
                break
        yield items.copy()
    yield items.copy()


def selection_sort(items: list[int]) -> Iterator[list[int]]:
    for i in range(0, len(items)):
        lowest_val: int = None
        lowest_index: int = None

        for j in range(i, len(items)):
            if lowest_val is None or items[j] < lowest_val:
                lowest_val = items[j]
                lowest_index = j

        swap(items, i, lowest_index)
        yield items.copy()


ALGORITHMS = {k.split("_")[0]: v for k, v in locals().items()
              if k.endswith("_sort") and callable(v)}
