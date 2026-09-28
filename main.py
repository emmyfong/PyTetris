#App state and game entry -> keyboard input

import pygame
from game import Game

# pygame setup
pygame.init()
pygame.key.set_repeat(300, 50)
screen = pygame.display.set_mode((650, 650))
clock = pygame.time.Clock()
running = True

#initialie the game
game = Game()

#custom even for gravity timer
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 500)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == GAME_UPDATE:
            game.moveBlockDown()
    
        #movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.moveLeft()
            if event.key == pygame.K_RIGHT:
                game.moveRight()
            if event.key == pygame.K_DOWN:
                game.moveDown()
            if event.key == pygame.K_UP:
                game.rotateBlock()

    #background color
    screen.fill("black")

    game.draw(screen)

    #render game
    pygame.display.flip()
    clock.tick(60)

pygame.quit()