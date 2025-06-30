from helper import log_scene_transitions
from core.game.SceneState.scene import INTROSCENE

class TitleSceneManager:
    def __init__(self):
        self.scene = INTROSCENE.TITLE_CARD_1
        self.previous_scene = None
        self.allowed_transitions = {
            INTROSCENE.TITLE_CARD_1: [INTROSCENE.TITLE_CARD_2],
            INTROSCENE.TITLE_CARD_2: [INTROSCENE.TITLE_CARD_3]
        }

    def set_scene(self,new_scene):
        if new_scene == self.scene:
            return
        if new_scene in self.allowed_transitions.get(self.scene,[]):
            log_scene_transitions(self.scene,new_scene,INTROSCENE)
            self.set_previous_scene(self.scene)
            self.scene = new_scene

    def set_previous_scene(self,scene):
        self.previous_scene = scene

    def get_scene(self):
        return f"Scene: {self.scene}"