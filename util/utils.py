import pygame

from util import algorithms

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
                i,       # From x
                500-val,  # From y
                1,       # width
                500      # height
            )
        )
        i += 1


def any_in_list(search_items, target_items):
    return any([x in search_items for x in target_items])


def help():
    algos = ""
    for algorithm in algorithms.ALGORITHMS.keys():
        algos += f"\n\t{algorithm}"
    algos += "\n"
    print(
        "\nUsage: python VisualSorting [optional algorithm] [...options]\n",
        "\nAvailable algorithms:",
        algos,
        "\nAvailable flags:",
        "\n\t-nl --nolimit\tRemove the fps limit",
        "\n\t-h  --help\tGet all available arguments\n"
    )
