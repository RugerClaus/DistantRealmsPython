from enum import Enum,auto

class MASTERSCENES(Enum):
    INTROSCENE = auto()
    TUTORIALSCENE = auto()
    ROAMINGSCENE = auto()

class INTROSCENE(Enum):
    TITLE_CARD_1 = auto()
    TITLE_CARD_2 = auto()
    TITLE_CARD_3 = auto()

class  TUTORIALSCENE(Enum):
    INITIAL_EXPLANATION = auto()
    ONLY_MAN_INTRODUCTION = auto()
