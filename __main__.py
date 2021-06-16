import pygame
from pygame.constants import QUIT
import utils
import random

items = [i for i in range(500)]
random.shuffle(items)

window = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit(pygame.quit())

    window.fill((0, 0, 0))

    items = utils.bubble_sort(items)
    utils.draw(window, items)

    pygame.display.update()
    clock.tick(60)