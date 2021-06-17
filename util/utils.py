import pygame

RED = (250, 0, 0)
GREEN = (0, 250, 0)

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
                500-val, # From y
                1,       # width
                500      # height
                )   
        )
        i += 1

def help():
    print(
        "\nUsage: python VisualSorting [optional algorithm] [...options]\n",
        "\nAvailable algorithms:",
        "\n\tbubble",
        "\n\tbogo",
        "\n\tgnome\n",
        "\nAvailable flags:",
        "\n\t-nl --nolimit\tRemove the fps limit",
        "\n\t-h  --help\tGet all available arguments\n"
        )