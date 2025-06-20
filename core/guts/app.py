import pygame, sys
from core.state.state import APPSTATE
from core.state.statemanager import StateManager
from core.state.mode import APPMODE
from core.state.modemanager import ModeManager
from core.util.debugger import Debugger
from core.guts.input.inputmanager import InputManager
from core.game.game import Game
from core.menus.menu import Menu

class App:
    def __init__(self,window):
        self.window = window
        self.input = InputManager()
        self.state = StateManager()
        self.mode = ModeManager()
        self.menu = Menu(window.get_screen(),self.start_game,self.load_menu,self.quit)
        self.game = Game(self.state,window,self.go_to_menu,self.quit)
        self.debugger = Debugger(self.game,self.state,window)

    def start_game(self):
        self.state.set_app_state(APPSTATE.IN_GAME)

    def load_menu(self):
        pass
    def toggle_debug_mode(self):
        if not self.mode.is_mode(APPMODE.DEBUG):
            self.mode.set_mode(APPMODE.DEBUG)
        else:
            self.mode.set_mode(APPMODE.PRIMARY)
    def quit(self):
        self.state.set_app_state(APPSTATE.QUIT)

    def go_to_menu(self):
        self.state.set_app_state(APPSTATE.MAIN_MENU)
    
    def handle_events(self):
        for event in pygame.event.get():
            self.window.handle_resize(event)

            if event.type == pygame.QUIT:
                self.state.set_app_state(APPSTATE.QUIT)
            
            if self.state.is_app_state(APPSTATE.MAIN_MENU):
                self.menu.handle_event(event)

            elif self.state.is_app_state(APPSTATE.IN_GAME):
                self.game.handle_event(event,self.input)
            
            if self.mode.is_mode(APPMODE.DEBUG):
                self.debugger.handle_event(event)

            command = self.input.handle_event(event)
            if command == "debug":
                self.toggle_debug_mode()
            elif command == "secret":
                print("Kiss me!")

    def run(self):
        while not self.state.is_app_state(APPSTATE.QUIT):
            self.window.fill(0,0,0)
            self.handle_events()
            
            if self.state.is_app_state(APPSTATE.MAIN_MENU):
                self.menu.update()
                self.menu.draw()
            elif self.state.is_app_state(APPSTATE.IN_GAME):
                self.game.run()
            elif self.state.is_app_state(APPSTATE.LOAD_MENU):
                self.menu.update()
                self.menu.draw()
            elif self.state.is_app_state(APPSTATE.QUIT):
                pygame.quit()
                sys.exit()

            
            self.window.timer()
            self.window.update()
    
        