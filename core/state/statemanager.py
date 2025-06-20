from core.state.state import *
from helper import log_system_state_transitions

class StateManager:
    def __init__(self):
        #app states
        self.app_state = APPSTATE.MAIN_MENU
        self.previous_app_state = None
        
        #game states
        self.game_state = GAMESTATE.PLAYING
        self.previous_game_state = None
        
        #player movement states

        #allowed transition definitions
        self.app_allowed_transitions = {
            APPSTATE.MAIN_MENU: [APPSTATE.IN_GAME,APPSTATE.LOAD_MENU,APPSTATE.QUIT],
            APPSTATE.LOAD_MENU: [APPSTATE.MAIN_MENU,APPSTATE.IN_GAME,APPSTATE.QUIT],
            APPSTATE.IN_GAME: [APPSTATE.MAIN_MENU,APPSTATE.QUIT]
        }

        self.game_allowed_transitions = {
            GAMESTATE.PLAYING: [GAMESTATE.PAUSED],
            GAMESTATE.PAUSED: [GAMESTATE.PLAYING]
        }
    
    def set_app_state(self,new_state):
        if new_state == self.app_state:
            return
        if new_state in self.app_allowed_transitions.get(self.app_state,[]):
            log_system_state_transitions(self.app_state,new_state,"APPSTATE")
            self.set_previous_app_state(self.app_state)
            self.app_state = new_state
            print(self.get_app_state())

    def is_app_state(self,state):
        return self.app_state == state
    
    def get_app_state(self):
        return f"Appstate: {self.app_state}"
    
    def set_previous_app_state(self,state):
        self.previous_app_state = state

    def set_game_state(self,new_state):
        if new_state == self.game_state:
            return
        if new_state in self.game_allowed_transitions.get(self.game_state,[]):
            log_system_state_transitions(self.game_state,new_state,"GAMESTATE")
            self.set_previous_game_state(self.game_state)
            self.game_state = new_state
            print(self.get_game_state())

    def is_game_state(self,state):
        return self.game_state == state
    
    def get_game_state(self):
        return f"Gamestate: {self.game_state}"
    
    def set_previous_game_state(self,state):
        self.previous_game_state = state
    