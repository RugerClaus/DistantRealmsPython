import pygame

from core.state.state import GAMESTATE
from core.menus.pause import Pause
#from core.game.entities.entities import Entities
#from core.game.entities.EntityState.state import *
from core.game.camera.camera import Camera
from core.game.entities.player import Player

class Game:
    def __init__(self,state,window,menu_callback,quit_callback):
        self.state = state
        self.window = window
        self.menu_callback = menu_callback
        self.quit_callback = quit_callback
        self.pause_menu = Pause(window,self.toggle_pause,self.quit_to_menu,self.quit)
        #self.entity_manager = Entities()
        #self.entity_manager.players.append(Player())
        self.camera = Camera(self.window.get_screen().get_width,self.window.get_screen().get_height())

    def main(self):
        self.window.default_fill()

    def toggle_pause(self):
        if not self.state.is_game_state(GAMESTATE.PAUSED):
            self.state.set_game_state(GAMESTATE.PAUSED)
        else:
            self.state.set_game_state(GAMESTATE.PLAYING)


    def handle_event(self,event,input):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.toggle_pause()
            if self.state.is_game_state(GAMESTATE.PAUSED):
                if event.key == pygame.K_9:
                    self.quit_to_menu()

        if self.state.is_game_state(GAMESTATE.PAUSED):
            self.pause_menu.handle_event(event)
        
        elif self.state.is_game_state(GAMESTATE.PLAYING):
            for player in self.entity_manager.players:
                player.handle_event(event)

    def draw(self):
        if self.state.is_game_state(GAMESTATE.PLAYING):
            self.main()
        if self.state.is_game_state(GAMESTATE.PAUSED):
            self.pause_menu.update()
            self.pause_menu.draw()

    def update(self):
        for player in self.entity_manager.players:
            self.camera.update(player)

    def run(self):
        self.update()
        self.draw()

    def quit_to_menu(self):
        self.reset()
        self.menu_callback()

    def quit(self):
        self.quit_callback()
    
    def reset(self):
        self.state.set_game_state(GAMESTATE.PLAYING)