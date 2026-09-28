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
    
    def drawGrid(self, screen):
        for i in range(self.ROWS):
            for j in range(self.COLS):
                xPix = j * self.CELL_SIZE + self.X_OFFSET
                yPix = i * self.CELL_SIZE + self.Y_OFFSET
                
                cellVal = self.grid[i][j]
                if (cellVal != 0):
                    pygame.draw.rect(screen, cellVal, (xPix, yPix, self.CELL_SIZE, self.CELL_SIZE))
                
                pygame.draw.rect(screen, (255, 255, 255), (xPix, yPix, self.CELL_SIZE, self.CELL_SIZE), 1)
    
    #Check and clear line
    def isRowFull(self, row):
        #if a single 0 -> row is not full
        for cellVal in self.grid[row]:
            if cellVal == 0:
                return False
        
        return True
    
    def clearRow(self, row):
        for col in range(self.COLS):
            self.grid[row][col] = 0
    
    def moveRowsDown(self, row, dist):
        for col in range(self.COLS):
            #cpy color to new pos
            self.grid[row + dist][col] = self.grid[row][col]
            #erase old pos
            self.grid[row][col] = 0    
    
    def checkFullLines(self):
        completedLines = 0
        
        #reverse for loop
        for row in range(self.ROWS - 1, -1, -1):
            if self.isRowFull(row):
                self.clearRow(row)
                completedLines += 1
            
            #if row isn't full but line nder is cleared -> needs to fall down
            elif completedLines > 0:
                self.moveRowsDown(row, completedLines)
        
        return completedLines
