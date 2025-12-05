"""
Contains State Machines

"""
#import abstract class

import pygame
from pathlib import Path 


from src._state_machine import StateMachine


class Core(StateMachine):
    def __init__(self):
        super().__init__()
    
        #Set fonts and stuff here for glboalb use?? Screen Szie 
        fonts = Path(__file__).parent.parent / "data" / "assets" / "fonts"
        
        rubik_dirt = fonts / "Rubik_Dirt" / "RubikDirt-Regular.ttf"
        ubuntu = fonts / "Ubuntu" / "Ubuntu-Regular.ttf"

        self.font = pygame.font.Font(ubuntu, 48)
        self.small_font = pygame.font.Font(ubuntu, 24)
        self.super_small_font = pygame.font.Font(ubuntu,12)

        

class GameStateMachine(StateMachine):
    def __init__(self):
        super().__init__()

        self.running = True
