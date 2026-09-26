#block.py
import pygame

class Block:
    def __init__(self):
        self.shapeData = []
        self.color = (0, 0, 0)
        
        #state tracking stuff
        self.rotationIdx = 0
        self.row = 0
        self.col = 3
    
    def getCurrentShape(self):
        #return the current shape's 2d array for current rotation
        return self.shapeData[self.rotationIdx]
    
    def rotate(self):
        self.rotationIdx = (self.rotationIdx + 1) % len(self.shapeData)
    
    def draw(self, screen, cellSize, xOff, yOff):
        shape = self.getCurrentShape()
        
        for i, row in enumerate(shape):
            for j, cellVal in enumerate(row):
                if cellVal == 1:
                    #calculate pixel location
                    xPix = (self.col + j) * cellSize + xOff
                    yPix = (self.row + i) * cellSize + yOff
                    
                    #draw
                    pygame.draw.rect(screen, (0, 0, 255), (xPix, yPix, cellSize, cellSize))
                    pygame.draw.rect(screen, (255, 255, 255), (xPix, yPix, cellSize, cellSize), 1)