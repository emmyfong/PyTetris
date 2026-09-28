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
        return random.choice(self.blocks)
    
    def spawnBlock(self):
        self.currentBlock = self.nextBlock
        self.nextBlock = self.getRandomBlock()

    def checkCollision(self, grid):
        return
    
    def lockToGrid(self):
        return
    
    def updateScore(self):
        return