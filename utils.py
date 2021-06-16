import pygame

RED = (250, 0, 0)

def draw(screen, vals):
    i = 1
    for val in vals:
        pygame.draw.rect(
            screen,
            RED,
            (
                i,       # From x 
                500-val, # From y
                1,       # width
                500      # height
                )   
        )
        i += 1

def bubble_sort(items):

    for i in range(1, len(items) - 1):

        left = items[i]
        right = items[i+1]

        if right < left:
            items[i] = right
            items[i+1] = left

    return items