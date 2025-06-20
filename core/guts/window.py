import pygame
class Window:
    def __init__(self):
        pygame.init()
        self.default_width = 1200
        self.default_height = 800
        self.color = (255,0,0)
        self.width = self.default_width
        self.height = self.default_height
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.set_screen()
        
    def set_screen(self):
        self.screen = pygame.display.set_mode((self.width,self.height),pygame.RESIZABLE | pygame.SCALED)
    
    def handle_resize(self,e):
        if e.type == pygame.VIDEORESIZE:
            (self.width,self.height) = e.size
            self.set_screen()
    
    def timer(self):
        self.clock.tick(self.fps)
    
    def default_fill(self):
        self.screen.fill(self.color)

    def fill(self,r,g,b):
        self.screen.fill((r,g,b))
    
    def blit(self,surface,destination):
        self.screen.blit(surface,destination)

    def get_screen(self):
        return self.screen
    
    def make_surface(self, width, height, alpha=False):
        flags = pygame.SRCALPHA if alpha else 0
        return pygame.Surface((width, height), flags)

    def update(self):
        pygame.display.flip()

    def get_fps(self):
        return self.clock.get_fps()