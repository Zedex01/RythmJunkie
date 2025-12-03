"""
States classes

"""
import pygame
from pygame import *
from states._state import State
from player import Player
from note import Note

class Main(State):
    def handle_events(self, events) -> bool:

        for event in events:

            #Check if the 'X' is pressed on window
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                #Check which key was pressed:

                #if 'g' key was pressed:
                if event.key == pygame.K_g:
                    self.state_machine.change_state(Running(self.state_machine))
                
                #Switch to settings menu on 's' press
                if event.key == pygame.K_s:
                    from states.states import Settings
                    self.state_machine.change_state(Settings(self.state_machine))
        return True

    def draw(self, screen):
        #Fill screen red
        screen.fill((255,50,50))

        #Render Text
        title_text = self.font.render("Main Menu", True, (255,255,255))
        prompt_text = self.small_font.render("Press G to Start", True, (255,255,255))

        #Position Text
        screen.blit(title_text, (50,50))
        screen.blit(prompt_text, (50,120))

class Settings(State):
    def handle_events(self, events) -> bool:

        for event in events:

            #Check if the 'X' is pressed on window
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                #Check which key was pressed:

                #if 'Esc' key was pressed:
                if event.key == pygame.K_ESCAPE:
                    
                    #Lazy import to prevent circular import
                    from states.states import Main
                    self.state_machine.change_state(Main(self.state_machine))

        return True

    def draw(self, screen):
        #Fill screen Green
        screen.fill((50,255,50))

        #Render Text
        title_text = self.font.render("Settings", True, (255,255,255))
        prompt_text = self.small_font.render("Press Esc to go back.", True, (255,255,255))

        #Position Text
        screen.blit(title_text, (50,50))
        screen.blit(prompt_text, (50,120))

class Controls(State):
    pass

# ====== Game States ======
class Running(State):
    def __init__(self, state_machine):
        super().__init__(state_machine)

        #Spawn player
        self.player = Player(self.state_machine)

        #Spawn Note
        self.note = Note(Vector2(480, 100))

    def enter(self):
        #reset Keys
        self.player.reset_keys()

    def handle_events(self, events):
        #Handle Player Events
        self.player.handle_events(events)

        for event in events:
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:                  
                #If escape is pressed, pause the game!
                if event.key == pygame.K_ESCAPE:
                    #Pass to pause both the current game state and the state machine
                    self.state_machine.change_state(Pause(self.state_machine, self))
        
        return True  

    def update(self, dt):
        self.player.update(dt)   
        self.note.update(dt)

    def draw(self, screen):
        self.player.draw(screen)
        self.note.draw(screen)       
                    
class Pause(State):
    def __init__(self, state_machine, running_state):
        super().__init__(state_machine)
        #Get passed the current instance of the running state
        self.running_state = running_state

    def handle_events(self, events):
        for event in events:
            #If 'X' is clicked, close
            if event.type == pygame.QUIT:
                return False

            #If a key is pressed...
            if event.type == pygame.KEYDOWN:

                #If Escape is pressed...
                if event.key == pygame.K_ESCAPE:
                    #Return to gameplay...
                    self.state_machine.change_state(self.running_state)
        return True
    
    def draw(self, screen):
        #Clear the screen
        screen.fill((0,0,0))

        #Draw Current Game state as Background
        self.running_state.draw(screen)

        #Set Surface to have slight opacity
        self.surface.fill((0, 0, 0, 40))

        #render text
        title_text = self.font.render("Paused", True, (255,255,255))
        prompt_text = self.small_font.render("Press ESC to return to game.", True, (255,255,255))

        #Blit to surface
        self.surface.blit(title_text, (50,50))
        self.surface.blit(prompt_text, (50,120))

        #Blit to screen
        screen.blit(self.surface, (self.surface_padding,self.surface_padding))
