from core.game.entities.EntityState.state import *
from core.game.entities.entities import EntityStateManager
class Entities:
    def __init__(self):
        self.state = EntityStateManager()
        self.players = []

        self.neutral_mobs = []
        self.hostile_mobs = []
        self.friendly_mobs = []
        
        self.health_potions = []

        self.keys = []

        self.bronze_coins = []
        self.silver_coins = []
        self.gold_coins = []

        self.damaging_tiles = []
