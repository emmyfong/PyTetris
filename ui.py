#UI stuff -> score, next block
import pygame

class UI:
    def __init__(self):
        pygame.font.init()
        
        #reusable font
        self.mainFont = pygame.font.SysFont('Consolas', 30, bold=True)
        self.smallFont = pygame.font.SysFont('Consolas', 20)
    
        self.textColor = (255, 255, 255)
        self.boxColor = (255, 255, 255)
    
    def draw(self, screen, game):
        #master UI
        self.drawScore(screen, game)
        self.drawNextBox(screen, game)
        self.drawHoldBox(screen, game)
        
    def drawScore(self, screen, game):
         scoreTitle = self.mainFont.render("SCORE", True, self.textColor)
         screen.blit(scoreTitle, (430, 30))
         
         pygame.draw.rect(screen, self.boxColor, (375, 70, 200, 50), 2)
         
         scoreStr = f"{game.score:09}"
         scoreSurface = self.mainFont.render(scoreStr, True, self.textColor)
         scoreRect = scoreSurface.get_rect(center=(473, 95))
         screen.blit(scoreSurface, scoreRect)        
    
    def drawNextBox(self, screen, game):
        nextTitle = self.mainFont.render("NEXT", True, self.textColor)

        nextRect = nextTitle.get_rect(center=(475, 165))
        screen.blit(nextTitle, nextRect)
        
        pygame.draw.rect(screen, self.boxColor, (375, 190, 200, 150), 2)
        
        if game.nextBlock:
            uiX = 430 - (game.nextBlock.col * game.grid.CELL_SIZE)
            uiY = 235 - (game.nextBlock.row * game.grid.CELL_SIZE)
            
            game.nextBlock.draw(screen, game.grid.CELL_SIZE, uiX, uiY)
    
    def drawHoldBox(self, screen, game):
        holdTitle = self.mainFont.render("HOLD", True, self.textColor)
        holdRect = holdTitle.get_rect(center=(475, 385))
        screen.blit(holdTitle, holdRect)
        
        pygame.draw.rect(screen, self.boxColor, (375, 410, 200, 150), 2)
        
        if game.holdBlock:
            uiX = 430 - (game.holdBlock.col * game.grid.CELL_SIZE)
            uiY = 455 - (game.holdBlock.row * game.grid.CELL_SIZE)
            
            game.holdBlock.draw(screen, game.grid.CELL_SIZE, uiX, uiY)