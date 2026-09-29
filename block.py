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

    def getShapeBounds(self):
        #bounding box (minRow, maxRow, minCol, maxCol) of the filled cells since shapeData grids include empty padding rows/cols that vary per block
        shape = self.getCurrentShape()
        rows = [i for i, row in enumerate(shape) if any(row)]
        cols = [j for row in shape for j, cellVal in enumerate(row) if cellVal]
        return min(rows), max(rows), min(cols), max(cols)

    def rotate(self):
        self.rotationIdx = (self.rotationIdx + 1) % len(self.shapeData)
        
    def undoRotate(self):
        self.rotationIdx = (self.rotationIdx - 1) % len(self.shapeData)
    
    def resetPosition(self):
        self.row = 0
        self.col = 3
        self.rotationIdx = 0
    
    def draw(self, screen, cellSize, xOff, yOff):
        shape = self.getCurrentShape()
        
        for i, row in enumerate(shape):
            for j, cellVal in enumerate(row):
                if cellVal == 1:
                    #calculate pixel location
                    xPix = (self.col + j) * cellSize + xOff
                    yPix = (self.row + i) * cellSize + yOff
                    
                    #draw
                    pygame.draw.rect(screen, self.color, (xPix, yPix, cellSize, cellSize))
                    pygame.draw.rect(screen, (255, 255, 255), (xPix, yPix, cellSize, cellSize), 1)