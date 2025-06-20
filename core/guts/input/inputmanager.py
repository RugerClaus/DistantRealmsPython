import pygame
from core.guts.input.iostream import IOSTREAM

class InputManager:
    def __init__(self):
        self.iostream = IOSTREAM()
        self.current_keys = set()
        self.released_keys = set()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.current_keys.add(event.key)
            return self.iostream.update(event)
        elif event.type == pygame.KEYUP:
            self.current_keys.discard(event.key)
            self.released_keys.add(event.key)
        return None

    def is_pressed(self, key):
        return key in self.current_keys

    def was_released(self, key):
        return key in self.released_keys

    def clear_released(self):
        self.released_keys.clear()
