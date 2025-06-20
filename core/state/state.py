from enum import Enum,auto

class APPSTATE(Enum):
    MAIN_MENU = auto()
    LOAD_MENU = auto()
    IN_GAME = auto()
    QUIT = auto()

class GAMESTATE(Enum):
    PAUSED = auto()
    PLAYING = auto()
    GAME_OVER = auto()