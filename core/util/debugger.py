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
        text_color = (255,255,255)
        self.surface.fill((0,0,0,0))
        surface_width = self.surface.get_width()
        fps = self.font.render(f"FPS: {round(self.window.get_fps())}",False,text_color)
        line_spacing = fps.get_height()

        appstate = self.font.render(f"Appstate: {str(self.state.app_state)}",False,text_color)



        self.surface.blit(fps,(0,0))
        self.surface.blit(appstate,(0,line_spacing*1))

        if self.check_in_game_state():
            game_state = self.font.render(f"Gamestate: {str(self.state.game_state)}",False,text_color)
            Layer_1_Scene = self.font.render(f"Scene: {self.game.scene.get_scene()}",False,text_color)
            
            self.surface.blit(Layer_1_Scene,(surface_width//2+surface_width//20,0))
            self.surface.blit(game_state,(surface_width//2+surface_width//20,line_spacing*1))

        self.window.blit(self.surface,self.rect)

    def update(self):
        pass