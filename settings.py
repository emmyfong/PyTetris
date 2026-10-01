#Game settings
from enum import Enum

class Color(Enum):
    CYAN = (21, 204, 209)
    YELLOW = (237, 234, 4)
    PURPLE = (166, 0, 247)
    BLUE = (13, 64, 216)
    ORANGE = (226, 116, 17)
    GREEN = (47, 230, 23)
    RED = (232, 18, 18)

#Points awarded for clearing N lines in a single move
SCORE_VALUES = {
    1: 40,
    2: 100,
    3: 300,
    4: 1200,
}
