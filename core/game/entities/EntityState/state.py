from enum import Enum,auto

class PLAYER_INTENT_STATE(Enum):
    UP = auto()
    LEFT = auto()
    RIGHT = auto()
    DOWN = auto()
    IDLE = auto()   
    ATTACK = auto()
    BLOCK = auto()

class PLAYER_MOVEMENT_STATE(Enum):
    UP = auto()
    LEFT = auto()
    RIGHT = auto()
    DOWN = auto()
    IDLE = auto()
    ATTACK = auto()
    BLOCK = auto()

class PLAYER_STATUS_STATE(Enum):
    HEALTHY = auto()
    POISONED = auto()
    FROZEN = auto()

