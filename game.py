#game.py
import random
from grid import Grid
from blocks import OBlock, TBlock, IBlock, JBlock, LBlock, SBlock, ZBlock

class Game:
    
    def __init__(self):
        self.grid = Grid()
        self.blocks = [OBlock, TBlock, IBlock, JBlock, LBlock, SBlock, ZBlock]
        
        self.bag = []
        
        self.nextBlock = self.getRandomBlock()
        self.currentBlock = self.getRandomBlock()
        
        #Holding
        self.holdBlock = None
        self.canHold = True
        
        self.score = 0
        self.gameOver = False

    def reset(self):
        self.grid = Grid()
        self.bag = []
        self.nextBlock = self.getRandomBlock()
        self.currentBlock = self.getRandomBlock()
        self.holdBlock = None
        self.canHold = True
        self.score = 0
        self.gameOver = False

    def getRandomBlock(self):
        if not self.bag:
            #get current bag and shuffle the blocks
            self.bag = self.bag.copy()
            random.shuffle(self.bag)
        
        randomClass = self.bag.pop()
        return randomClass()

    def spawnBlock(self):
        self.currentBlock = self.nextBlock
        self.nextBlock = self.getRandomBlock()

        #no room for the new block -> stack topped out
        if self.checkCollision():
            self.gameOver = True

    def moveBlockDown(self):
        if self.gameOver:
            return

        self.currentBlock.row += 1
        
        if self.checkCollision():
            self.currentBlock.row -= 1
            self.lockToGrid()
            
            linesCleared = self.grid.checkFullLines()
            if linesCleared > 0:
                self.updateScore(linesCleared)
            
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
        
        self.canHold = True
    
    
    #Movement
    def moveLeft(self):
        if self.gameOver:
            return

        self.currentBlock.col -= 1
        if self.checkCollision():
            self.currentBlock.col += 1

    def moveRight(self):
        if self.gameOver:
            return

        self.currentBlock.col += 1
        if self.checkCollision():
            self.currentBlock.col -= 1

    #Block Rotation
    def rotateBlock(self):
        if self.gameOver:
            return

        self.currentBlock.rotate()

        if self.checkCollision():
            self.currentBlock.undoRotate()

    def dropBlock(self):
        if self.gameOver:
            return

        while True:
            self.currentBlock.row += 1
            if self.checkCollision():
                self.currentBlock.row -= 1
                self.lockToGrid()
                
                #update score
                linesCleared = self.grid.checkFullLines()
                if linesCleared > 0:
                    self.updateScore(linesCleared)
                
                self.spawnBlock()
                break
        
        self.canHold = True
    
    def hold(self):
        if self.gameOver or not self.canHold:
            return

        #First time holding block
        if self.holdBlock is None:
            self.holdBlock = self.currentBlock
            self.spawnBlock()
        
        #already holding something -> swap
        else:
            self.currentBlock, self.holdBlock = self.holdBlock, self.currentBlock
            self.currentBlock.resetPosition()
        
        self.holdBlock.resetPosition()
        self.canHold = False
    
    def updateScore(self, linesCleared):
        if linesCleared == 1:
            self.score += 40
        elif linesCleared == 2:
            self.score += 100
        elif linesCleared == 3:
            self.score += 300
        elif linesCleared == 4:
            self.score += 1200

    def draw(self, screen):
        self.grid.drawGrid(screen)
        
        self.currentBlock.draw(screen, self.grid.CELL_SIZE, self.grid.X_OFFSET, self.grid.Y_OFFSET)        