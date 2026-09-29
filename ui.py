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
        
        self.playAgainRect = None
        self.exitRect = None
    
    def draw(self, screen, game):
        #master UI
        self.drawScore(screen, game)
        self.drawNextBox(screen, game)
        self.drawHoldBox(screen, game)
        self.drawGameOver(screen, game)

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

        boxRect = pygame.Rect(375, 190, 200, 150)
        pygame.draw.rect(screen, self.boxColor, boxRect, 2)

        if game.nextBlock:
            self.drawCenteredBlock(screen, game.nextBlock, game.grid.CELL_SIZE, boxRect.center)

    def drawHoldBox(self, screen, game):
        holdTitle = self.mainFont.render("HOLD", True, self.textColor)
        holdRect = holdTitle.get_rect(center=(475, 385))
        screen.blit(holdTitle, holdRect)

        boxRect = pygame.Rect(375, 410, 200, 150)
        pygame.draw.rect(screen, self.boxColor, boxRect, 2)

        if game.holdBlock:
            self.drawCenteredBlock(screen, game.holdBlock, game.grid.CELL_SIZE, boxRect.center)

    def drawCenteredBlock(self, screen, block, cellSize, boxCenter):
        #center the block's actual filled cells (not its full shapeData grid) in the box
        minRow, maxRow, minCol, maxCol = block.getShapeBounds()
        widthPx = (maxCol - minCol + 1) * cellSize
        heightPx = (maxRow - minRow + 1) * cellSize

        boundingLeft = (block.col + minCol) * cellSize
        boundingTop = (block.row + minRow) * cellSize

        xOff = boxCenter[0] - widthPx / 2 - boundingLeft
        yOff = boxCenter[1] - heightPx / 2 - boundingTop

        block.draw(screen, cellSize, xOff, yOff)

    def drawGameOver(self, screen, game):
        if not game.gameOver:
            return

        gridRect = pygame.Rect(
            game.grid.X_OFFSET, game.grid.Y_OFFSET,
            game.grid.COLS * game.grid.CELL_SIZE, game.grid.ROWS * game.grid.CELL_SIZE
        )

        overlay = pygame.Surface(gridRect.size, pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, gridRect.topleft)

        gameOverText = self.mainFont.render("GAME OVER", True, (255, 0, 0))
        screen.blit(gameOverText, gameOverText.get_rect(center=gridRect.center))
        
        #play again button
        self.playAgainRect = pygame.Rect(0, 0, 160, 40)
        self.playAgainRect.center = (gridRect.centerx, gridRect.centery + 20)
        
        pygame.draw.rect(screen, (255, 255, 255), self.playAgainRect, border_radius=5)
        
        playText = self.smallFont.render("PLAY AGAIN", True, (0, 0 ,0))
        screen.blit(playText, playText.get_rect(center=self.playAgainRect.center))
        
        #exit button
        self.exitRect = pygame.Rect(0, 0, 160, 40)
        self.exitRect.center = (gridRect.centerx, gridRect.centery + 80)
        pygame.draw.rect(screen, (255, 255, 255), self.exitRect, border_radius=5)
        
        exitText = self.smallFont.render("QUIT", True, (0, 0, 0))
        screen.blit(exitText, exitText.get_rect(center=self.exitRect.center))