#App state and game entry -> keyboard input

import pygame
from grid import Grid

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

grid = Grid()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("cornflowerblue")

    # RENDER YOUR GAME HERE
    pygame.display.flip()

    clock.tick(60)
    
    grid.drawGrid()

pygame.quit()