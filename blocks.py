#define blocks
from block import Block

class OBlock(Block):
    def __init__(self):
        super().__init__() #runs setup from parent block
        self.color = (255, 255, 0)
        self.shapeData = [
            [[1, 1],
            [1, 1]]
        ]

class TBlock(Block):
    def __init__(self):
        super().__init__()
        self.color = (128, 0, 128)
        self.shapeData = [
            [[0, 1, 0],
            [1, 1, 1],
            [0, 0, 0]],

            [[0, 1, 0],
            [0, 1, 1],
            [0, 1, 0]],

            [[0, 0, 0],
            [1, 1, 1],
            [0, 1, 0]],

            [[0, 1, 0],
            [1, 1, 0],
            [0, 1, 0]],
        ]

class IBlock(Block):
    def __init__(self):
        super().__init__()
        self.color = (0, 255, 255)
        self.shapeData = [
            [[0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]],

            [[0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0]],

            [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0]],

            [[0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0]],
        ]

class JBlock(Block):
    def __init__(self):
        super().__init__()
        self.color = (0, 0, 255)
        self.shapeData = [
            [[1, 0, 0],
            [1, 1, 1],
            [0, 0, 0]],

            [[0, 1, 1],
            [0, 1, 0],
            [0, 1, 0]],

            [[0, 0, 0],
            [1, 1, 1],
            [0, 0, 1]],

            [[0, 1, 0],
            [0, 1, 0],
            [1, 1, 0]],
        ]

class LBlock(Block):
    def __init__(self):
        super().__init__()
        self.color = (255, 165, 0)
        self.shapeData = [
            [[0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]],

            [[0, 1, 0],
            [0, 1, 0],
            [0, 1, 1]],

            [[0, 0, 0],
            [1, 1, 1],
            [1, 0, 0]],

            [[1, 1, 0],
            [0, 1, 0],
            [0, 1, 0]],
        ]

class SBlock(Block):
    def __init__(self):
        super().__init__()
        self.color = (0, 255, 0)
        self.shapeData = [
            [[0, 1, 1],
            [1, 1, 0],
            [0, 0, 0]],

            [[0, 1, 0],
            [0, 1, 1],
            [0, 0, 1]],

            [[0, 0, 0],
            [0, 1, 1],
            [1, 1, 0]],

            [[1, 0, 0],
            [1, 1, 0],
            [0, 1, 0]],
        ]

class ZBlock(Block):
    def __init__(self):
        super().__init__()
        self.color = (255, 0, 0)
        self.shapeData = [
            [[1, 1, 0],
            [0, 1, 1],
            [0, 0, 0]],

            [[0, 0, 1],
            [0, 1, 1],
            [0, 1, 0]],

            [[0, 0, 0],
            [1, 1, 0],
            [0, 1, 1]],

            [[0, 1, 0],
            [1, 1, 0],
            [1, 0, 0]],
        ]