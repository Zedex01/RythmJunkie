"Abstract/base State Class"
import pygame
from pygame import *

from pathlib import Path

class State():
    def __init__(self, state_machine):
        self.name = None
        #For tracking currently highlighted button
        self.curr_btn = None

        #Set State Machine Refrence
        self.state_machine = state_machine    
        
        #Set Default Fonts    
        #self.font = pygame.font.SysFont("Arial", 48)
        #self.small_font = pygame.font.SysFont("Arial", 24)
        #self.super_small_font = pygame.font.SysFont("Arial", 12)

        #ubuntu_font = self.state_machine.ubuntu

        self.font = self.state_machine.font
        self.small_font = self.state_machine.small_font
        self.super_small_font = self.state_machine.super_small_font

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
