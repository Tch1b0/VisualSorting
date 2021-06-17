from util import algorithms, utils, field
import pygame
from pygame.constants import QUIT
import sys

limit = True

# /Read args
args = sys.argv

try:
    arg = args[1]
    if arg.startswith("-"): raise Exception() # Go to except block
except:
    arg = "bubble"

if "-h" in args or "--help" in args: quit(utils.help())
if "-nl" in args or "--nolimit" in args: limit = False

try:
    algorithm = algorithms.ALGORITHMS[arg]
except KeyError:
    quit(utils.help())
# Read args/

field = field.Field(algorithm)
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

    pygame.display.update()           # Update the window
    if limit: clock.tick(60)          # Run a maximum of 60 times a second