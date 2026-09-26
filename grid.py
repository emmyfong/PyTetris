#grid.py
import pygame

class Grid:
    ROWS = 20
    COLS = 10     
    
    def __init__(self):
        self.grid = [[0 for _ in range(self.COLS)] for _ in range(self.ROWS)]
    
    def drawGrid(self, screen):
        return
    
    def checkFullLines(self):
        return
    
    def clearLine(self):
        return
    
    def moveRowsDown(self):
        return