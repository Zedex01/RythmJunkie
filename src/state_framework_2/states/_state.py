"Abstract/base State Class"
import pygame
from pygame import *

class State():
    def __init__(self, state_machine):
        #Set State Machine Refrence
        self.state_machine = state_machine    
        
        #Set Default Fonts    
        self.font = pygame.font.SysFont("Arial", 48)
        self.small_font = pygame.font.SysFont("Arial", 24)

        self.screen_w = 480
        self.screen_h = 270
        self.surface_padding = 20

        #Surface
        self.surface = pygame.Surface((self.screen_w-2*self.surface_padding, self.screen_h-2*self.surface_padding), pygame.SRCALPHA)

    #Ran on state init
    def enter(self):
        pass

    def leave(self):
        pass

    def handle_events(self, events):
        return True
    
    def update(self, dt):
        pass

    def draw(self, screen):
        pass
