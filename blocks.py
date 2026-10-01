#define blocks
from block import Block
from settings import Color

class OBlock(Block):
    def __init__(self):
        super().__init__() #runs setup from parent block
        self.color = Color.YELLOW.value
        self.shapeData = [
            [[1, 1],
            [1, 1]]
        ]

class TBlock(Block):
    def __init__(self):
        super().__init__()
        self.color = Color.PURPLE.value
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
        self.color = Color.CYAN.value
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
        self.color = Color.BLUE.value
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
        self.color = Color.ORANGE.value
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
        self.color = Color.GREEN.value
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
        self.color = Color.RED.value
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