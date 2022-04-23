import time
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


def any_in_list(search_items, target_items):
    return any([x in search_items for x in target_items])


def help():
    algos = ""
    for algorithm in ALGORITHMS.keys():
        algos += f"\n\t{algorithm}"
    algos += "\n"
    print(
        "\nUsage: python VisualSorting [optional algorithm] [...options]\n",
        "\nAvailable algorithms:",
        algos,
        "\nAvailable flags:",
        "\n\t-nl --nolimit\tRemove the fps limit",
        "\n\t-cmp --compare\t Compare all algorithms",
        "\n\t-h  --help\tGet all available arguments\n"
    )


def compare_alogrithms() -> dict[str, float]:
    algorithm_times: dict[str, float] = {}
    all_algorithms = ALGORITHMS.copy()
    for k, v in all_algorithms.items():
        if k in ["bogo"]:
            continue
        start = time.time()
        field = Field(v, size=500)
        field.shuffle()
        field.sort_now()
        end = time.time()
        algorithm_times[k] = end - start

    return algorithm_times


def print_compared_algorithms() -> None:
    algo_times = compare_alogrithms()
    name_length = max(len(k) for k in algo_times.keys())
    for k, v in algo_times.items():
        print(f"{' '*(name_length-len(k))}{k} sort: {round(v, 3)} seconds")
