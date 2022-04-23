import time
from util import ALGORITHMS, Field, compare_alogrithms, draw, any_in_list, help, print_compared_algorithms
import pygame
from pygame.constants import QUIT
import sys

FPS = 60
SIZE = 500
limit = True

args = sys.argv[1:]

selected_algorithm = [arg for arg in args if not arg.startswith("-")]
if len(selected_algorithm) == 0:
    selected_algorithm = "bubble"
else:
    selected_algorithm = selected_algorithm[0]

if selected_algorithm == "all":
    algo_times = compare_alogrithms()
    for k, v in algo_times.items():
        print(f"{k} sort: {v} seconds")
    exit()

if any_in_list(["-cmp", "--compare"], args):
    print_compared_algorithms()
    quit()

if any_in_list(["-h", "--help"], args):
    quit(help())

if any_in_list(["-nl", "--nolimit"], args):
    limit = False


field = Field(ALGORITHMS[selected_algorithm], size=SIZE)
field.shuffle()

window = pygame.display.set_mode([SIZE, SIZE])
pygame.display.set_caption("Visual Sorting")
clock = pygame.time.Clock()


def render():
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
