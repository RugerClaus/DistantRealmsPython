
class GameSceneHandling:
    def __init__(self,game_surface):
        self.surface = game_surface

    def introscene(self):
        self.surface.fill((255,0,0))

    def tutorial_scene(self):
        self.surface.fill((0,255,0))
    
    def roaming_scene(self):
        self.surface.fill((0,0,255))