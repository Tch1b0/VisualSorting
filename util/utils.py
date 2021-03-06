import time
from typing import Any
import pygame

from util import Field, ALGORITHMS

RED = (0xfc, 0x00, 0x00)
GREEN = (0x00, 0xfc, 0x00)


def draw(screen, items: list, solved=False):
    if solved == True:
        color = GREEN
    else:
        color = RED

    i = 1
    for val in items:
        pygame.draw.rect(
            screen,
            color,
            (
                i,               # From x
                len(items)-val,  # From y
                1,               # Width
                len(items)       # Height
            )
        )
        i += 1


def any_in_list(search_items: list[Any], target_items: list[Any]) -> bool:
    return any([x in search_items for x in target_items])


def compare_alogrithms() -> dict[str, float]:
    algorithm_times: dict[str, float] = {}
    all_algorithms = ALGORITHMS.copy()
    for k, v in all_algorithms.items():
        if k in ["bogo"]:
            continue
        start = time.time()
        field = Field(v, size=500)
        field.shuffle()
        field.sort_instantly()
        end = time.time()
        algorithm_times[k] = end - start

    return algorithm_times


def print_compared_algorithms() -> None:
    algo_times = sorted(compare_alogrithms().items(), key=lambda x: x[1])
    name_length = max(len(k) for k, _ in algo_times)
    for i, [k, v] in enumerate(algo_times):
        print(f"{i+1}. {' '*(name_length-len(k))}{k} sort: {round(v, 3)} seconds")
