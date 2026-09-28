#game.py
import random
from grid import Grid
from blocks import OBlock, TBlock, IBlock, JBlock, LBlock, SBlock, ZBlock

class Game:
    
    def __init__(self):
        self.grid = Grid()
        self.blocks = [OBlock, TBlock, IBlock, JBlock, LBlock, SBlock, ZBlock]
        
        self.nextBlock = self.getRandomBlock()
        self.currentBlock = self.getRandomBlock()
        
        #Holding
        self.holdBlock = None
        self.canHold = True

    def getRandomBlock(self):
        randomClass = random.choice(self.blocks)
        return randomClass()
    
    def spawnBlock(self):
        self.currentBlock = self.nextBlock
        self.nextBlock = self.getRandomBlock()
    
    def moveBlockDown(self):
        self.currentBlock.row += 1
        
        if self.checkCollision():
            self.currentBlock.row -= 1
            self.lockToGrid()
            self.spawnBlock() 

    def checkCollision(self):
        shape = self.currentBlock.getCurrentShape()
        
        for i, row in enumerate(shape):
            for j, cellVal in enumerate(row):
                if cellVal == 0:
                    continue
                
                globalRow = self.currentBlock.row + i
                globalCol = self.currentBlock.col + j
                
                #checks
                if globalRow >= self.grid.ROWS:
                    #hit the ground
                    return True
                if globalCol < 0 or globalCol >= self.grid.COLS:
                    return True
                if self.grid.grid[globalRow][globalCol] != 0:
                    return True
        
        return False
                    
    
    def lockToGrid(self):
        shape = self.currentBlock.getCurrentShape()
        
        for i, row in enumerate(shape):
            for j, cellVal in enumerate(row):
                if cellVal != 0:
                    globalRow = self.currentBlock.row + i
                    globalCol = self.currentBlock.col + j
                    
                    #overwrite 0 with block specific rgb color
                    self.grid.grid[globalRow][globalCol] = self.currentBlock.color
    
    
    #Movement
    def moveLeft(self):
        self.currentBlock.col -= 1
        if self.checkCollision():
            self.currentBlock.col += 1
    
    def moveRight(self):
        self.currentBlock.col += 1
        if self.checkCollision():
            self.currentBlock.col -= 1
    
    def updateScore(self):
        return

    def draw(self, screen):
        self.grid.drawGrid(screen)
        
        self.currentBlock.draw(screen, self.grid.CELL_SIZE, self.grid.X_OFFSET, self.grid.Y_OFFSET)        