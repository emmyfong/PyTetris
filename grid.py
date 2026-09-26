#grid.py
import pygame

class Grid:
    ROWS = 20
    COLS = 10
    CELL_SIZE = 30
    X_OFFSET = 20
    Y_OFFSET = 25     
    
    def __init__(self):
        self.grid = [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.grid[5][5] = 1
        self.grid[5][6] = 1
    
    def drawGrid(self, screen):
        for i in range(self.ROWS):
            for j in range(self.COLS):
                xPix = j * self.CELL_SIZE + self.X_OFFSET
                yPix = i * self.CELL_SIZE + self.Y_OFFSET
                
                if (self.grid[i][j] == 1):
                    pygame.draw.rect(screen, (0, 0, 255), (xPix, yPix, self.CELL_SIZE, self.CELL_SIZE))
                
                pygame.draw.rect(screen, (255, 255, 255), (xPix, yPix, self.CELL_SIZE, self.CELL_SIZE), 1)
    
    def checkFullLines(self):
        return
    
    def clearLine(self):
        return
    
    def moveRowsDown(self):
        return