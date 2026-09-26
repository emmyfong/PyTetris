#App state and game entry -> keyboard input

import pygame
from grid import Grid

# pygame setup
pygame.init()
screen = pygame.display.set_mode((650, 650))
clock = pygame.time.Clock()
running = True

grid = Grid()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #background color
    screen.fill("black")

    grid.drawGrid(screen)

    #render game
    pygame.display.flip()

    clock.tick(60)

pygame.quit()