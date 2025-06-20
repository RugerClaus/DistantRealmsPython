import pygame

from core.ui.font import FontEngine
from core.state.state import APPSTATE

class Debugger:
    def __init__(self,game,state,window):
        self.game = game
        self.state = state
        self.window = window
        self.surface = window.make_surface(window.get_screen().get_width(),window.get_screen().get_height(),True)
        self.rect = self.surface.get_rect()
        self.font = FontEngine("UI").font

    def check_in_game_state(self):
        if self.state.is_app_state(APPSTATE.IN_GAME):
            return True
        
    def create_options(self):
        pass

    def handle_event(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if self.check_in_game_state():
                    print("In game")
                else:
                    print("Not in game")


    def draw(self):
        
        self.surface.fill((0,0,0,0))
        fps = self.font.render(f"FPS: {round(self.window.get_fps())}",False,(255,255,255))
        self.surface.blit(fps,(0,0))

        self.window.blit(self.surface,self.rect)

    def update(self):
        pass