import time
from util import algorithms, utils, field
import pygame
from pygame.constants import QUIT
import sys

limit = True

# /Read args
args = sys.argv[1:]

selected_algorithm = [arg for arg in args if not arg.startswith("-")]
if len(selected_algorithm) == 0:
    selected_algorithm = "bubble"
else:
    selected_algorithm = selected_algorithm[0]

if utils.any_in_list(["-h", "--help"], args):
    quit(utils.help())

if utils.any_in_list(["-nl", "--nolimit"], args):
    limit = False

field = field.Field(algorithms.ALGORITHMS[selected_algorithm])
field.shuffle()

window = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()


def render():
    for event in pygame.event.get():
        if event.type == QUIT:
            quit(pygame.quit())

    window.fill((0, 0, 0))

    utils.draw(window, field.field, field.is_sorted())

    pygame.display.update()
    if limit:
        clock.tick(60)


start = time.time()
for _ in field.sort():
    render()
end = time.time()

print(f"Sorting took {end - start} seconds!")

while True:
    render()
