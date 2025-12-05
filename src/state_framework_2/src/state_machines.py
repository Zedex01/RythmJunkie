"""
Contains State Machines

"""
#import abstract class

import pygame
from pathlib import Path 

from src._state_machine import StateMachine
from src.sound_manager import SoundManager
from src.input_manager import InputManager
from src.events import *


class Core(StateMachine):
    def __init__(self):
        super().__init__()
        
    
        #Set fonts and stuff here for glboalb use?? Screen Szie 
        fonts = Path(__file__).parent.parent / "data" / "assets" / "fonts"
        rubik_dirt = fonts / "Rubik_Dirt" / "RubikDirt-Regular.ttf"
        ubuntu = fonts / "Ubuntu" / "Ubuntu-Regular.ttf"

        self.data_dir = Path(__file__).parent.parent / "data"

        self.font = pygame.font.Font(ubuntu, 48)
        self.small_font = pygame.font.Font(ubuntu, 24)
        self.super_small_font = pygame.font.Font(ubuntu,12)

        self.sound_manager = SoundManager(self)
        self.input_manager = InputManager()

    def handle_events(self, events):
        super().handle_events(events)
        
        self.sound_manager.handle_events(events=events)
        self.input_manager.handle_events(events=events)
        

    def update(self, dt):
        super().update(dt)

        self.sound_manager.update(dt)
        self.input_manager.update(dt)

    def draw(self, screen):
        super().draw(screen)



        
