#App state and game entry -> keyboard input

import pygame
from game import Game
from ui import UI

# pygame setup
pygame.init()
screen = pygame.display.set_mode((650, 650))
clock = pygame.time.Clock()
running = True

#initialie the game
game = Game()
uiManager = UI()

DAS = 170  #Time to hold before auto-shifting starts
ARR = 50   #Time between shifts once DAS is active

# Key states and timers
leftHeld = False
rightHeld = False
downHeld = False

leftTimer = 0
rightTimer = 0
downTimer = 0

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
            #Track continuous keys
            if event.key == pygame.K_LEFT:
                game.moveLeft()
                leftHeld = True
                leftTimer = 0
            if event.key == pygame.K_RIGHT:
                game.moveRight()
                rightHeld = True
                rightTimer = 0
            if event.key == pygame.K_DOWN:
                game.moveBlockDown()
                downHeld = True
                downTimer = 0
                
            #Single shot actions    
            if event.key == pygame.K_UP:
                game.rotateBlock()
            if event.key == pygame.K_SPACE:
                game.dropBlock()
            if event.key == pygame.K_c:
                game.hold()
                
        #moment keys are released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                leftHeld = False
            if event.key == pygame.K_RIGHT:
                rightHeld = False
            if event.key == pygame.K_DOWN:
                downHeld = False
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game.gameOver and event.button == 1:
                mousePos = pygame.mouse.get_pos()
                
                if uiManager.playAgainRect and uiManager.playAgainRect.collidepoint(mousePos):
                    game.reset()
                
                elif uiManager.exitRect and uiManager.exitRect.collidepoint(mousePos):
                    running = False


    dt = clock.tick(30)
    if leftHeld:
        leftTimer += dt
        if leftTimer >= DAS:
            game.moveLeft()
            leftTimer -= ARR
    if rightHeld:
        rightTimer += dt
        if rightTimer >= DAS:
            game.moveRight()
            rightTimer -= ARR
    if downHeld:
        downTimer += dt
        if downTimer >= DAS:
            game.moveBlockDown()
            downTimer -= ARR
    
    #background color
    screen.fill("black")
    game.draw(screen)
    uiManager.draw(screen, game)

    #render game
    pygame.display.flip()

pygame.quit()