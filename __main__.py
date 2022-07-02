import time
from typing_extensions import Never
from util import ALGORITHMS, Field, draw, print_compared_algorithms
import pygame
from pygame.constants import QUIT
import sys

from util.cli import Cli

FPS = 60
SIZE = 500
limit = True

cli = Cli(sys.argv[1:])

selected_algorithm: str = "bubble"


@cli.argument(1, "Select an algorithm")
def select_algorithm(algorithm: str) -> None:
    global selected_algorithm
    selected_algorithm = algorithm


@cli.flag("-cmp", "--compare", "Compare all algorithms")
def compare_algorithms() -> Never:
    print_compared_algorithms()
    quit()


@cli.flag("-h", "--help", "Display help")
def show_help() -> Never:
    print(cli)
    print("\nAvailable algorithms:", *ALGORITHMS.keys(), sep="\n\t")
    quit()


@cli.flag("-nl", "--no-limit", "Remove the limit of the Framerate")
def remove_limit() -> None:
    global limit
    limit = False


cli.execute()

field = Field(ALGORITHMS[selected_algorithm], size=SIZE)
field.shuffle()

window = pygame.display.set_mode([SIZE, SIZE])
pygame.display.set_caption("Visual Sorting")
clock = pygame.time.Clock()


def render() -> None:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit(pygame.quit())

    window.fill((0, 0, 0))

    draw(window, field.field, field.is_sorted())

    pygame.display.update()
    if limit:
        clock.tick(FPS)


start = time.time()
for _ in field.sort():
    render()
end = time.time()

print(f"Sorting took {round(end - start, 3)} seconds!")

while True:
    render()
