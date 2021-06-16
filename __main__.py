from field import Field
import pygame
from pygame.constants import QUIT
import utils
import random
import sys

try:
    arg = sys.argv[1]
except:
    arg = "bubble"

if arg == "-h" or arg == "--help": quit(utils.help())
algorithm = utils.ALGORITHMS[arg]

field = Field(algorithm)
field.shuffle()

window = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit(pygame.quit())

    window.fill((0, 0, 0))
    
    field.sort(steps=1)
    utils.draw(window, field.field, field.is_sorted())

    pygame.display.update()
    clock.tick(60)