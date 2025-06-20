
from core.game.entities.EntityState.statemanager import EntityStateManager

class Entity():
    def __init__(self):
        self.location = ()
        self.frames = None
        self.state = EntityStateManager()
        
    