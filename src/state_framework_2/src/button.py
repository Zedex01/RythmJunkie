import pygame
from pygame import *

from pathlib import Path


"""
 Main purposes is to handle the creation / drawing of the button, no need to handle inputs directly???
 TODO: 
  - Add Mouse Hit Detection
  - Let anchor be center
"""

class Button():
    def __init__(self, text: str, size: tuple, pos: tuple, callback_function = None):
        self.text = text
        self.pos = pos
        self.size_default = Vector2(size)
        self.size = self.size_default
        self.size_selected = self.size* 1.05

        self.rect = pygame.Rect(pos, size)
        
        self.surface = pygame.Surface(size, SRCALPHA)

        self.states = ["default", "selected", "pressed", "disabled"]
        self.state, self.last_state = "default", "default"

        fonts = Path(__file__).parent.parent / "data" / "assets" / "fonts"
        
        rubik_dirt = fonts / "Rubik_Dirt" / "RubikDirt-Regular.ttf"
        ubuntu = fonts / "Ubuntu" / "Ubuntu-Regular.ttf"

        self.font = pygame.font.Font(ubuntu, 48)
        self.small_font = pygame.font.Font(ubuntu, 24)
        self.super_small_font = pygame.font.Font(ubuntu,12)

    def handle_events(self, events): 
        #get cursor location
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            print("On ", self.text)



    def update(self, dt): 
        if self.state is not self.last_state:
            if self.state == "default":
                self.surface = pygame.Surface(self.size_default, SRCALPHA)
                self.last_state = self.state

            if self.state == "selected":
                self.surface = pygame.Surface(self.size_selected, SRCALPHA)
                self.last_state = self.state


    def draw(self, screen): 
        self.surface.fill((64,64,64,0))
        #Rounded Button
        pygame.draw.rect(self.surface, (64,64,64), self.surface.get_rect(), border_radius=8)
        #Border:
        pygame.draw.rect(self.surface, (150,150,150), self.surface.get_rect(), width=2, border_radius=8)
        #Render Text 
        button_text = self.small_font.render(self.text, True, (255,255,255))
        #find center of surface and button
        text_rect = button_text.get_rect(center=self.surface.get_rect().center)
        
        #place the text in the middle of the surface
        self.surface.blit(button_text, text_rect)
        
        #Draw on screen
        screen.blit(self.surface, self.pos)

    def set_state(self, new_state: str) -> bool:
        if new_state not in self.states:
            return False
        
        self.last_state = self.state
        self.state = new_state
        return True