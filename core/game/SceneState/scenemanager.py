from helper import log_scene_transitions
from core.game.SceneState.scene import MASTERSCENES

class SceneManager:
    def __init__(self):
        self.scene = MASTERSCENES.INTROSCENE
        self.previous_scene = None
        
        self.allowed_transitions = {
            MASTERSCENES.INTROSCENE: [MASTERSCENES.TUTORIALSCENE,MASTERSCENES.ROAMINGSCENE],
            MASTERSCENES.TUTORIALSCENE: [MASTERSCENES.ROAMINGSCENE,MASTERSCENES.INTROSCENE],
            MASTERSCENES.ROAMINGSCENE: [MASTERSCENES.TUTORIALSCENE,MASTERSCENES.INTROSCENE],
        }

    def set_scene(self,new_scene):
        if self.scene == new_scene:
            return
        if new_scene in self.allowed_transitions.get(self.scene,[]):
            log_scene_transitions(self.scene,new_scene,MASTERSCENES)
            self.set_previous_scene()
            self.scene = new_scene

    def set_previous_scene(self):
        self.previous_scene = self.scene

    def is_scene(self,scene):
        return self.scene == scene
    
    def get_scene(self):
        return self.scene