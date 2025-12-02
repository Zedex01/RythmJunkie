import pygame
from states.state import State

from player import Player

"""
Has 4 states:
playing, 
paused,
enter, 
exit

"""

class Game(State):

    def enter(self):
        #Initialize Player, Resets everytime the state is entered
        self.player = Player(self.state_machine)

    def leave(self):
        pass

    def handle_events(self, events):
        #handle all player Events
        self.player.handle_events(events)

        for event in events:

            #Check if the 'X' is pressed on window
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                #Check which key was pressed:

                #if 'm' key was pressed:
                if event.key == pygame.K_m:
                    #Lazy import to prevent circular import                    
                    from states.main_menu import MainMenu
                    self.state_machine.change_state(MainMenu(self.state_machine))
                
                elif event.key == pygame.K_ESCAPE:
                    #Lazy import to prevent circular import                    
                    from states.pause_menu import PauseMenu
                    self.state_machine.change_state(PauseMenu(self.state_machine))
                    
        return True
    
    def update(self, dt):
        self.player.update(dt)

    def draw(self, screen):
        screen.fill((0,50,50))
        self.player.draw(screen)