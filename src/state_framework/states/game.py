import pygame
from states.state import State



class Game(State):

    def enter(self):
        pass

    def exit(self):
        pass

    def handle_events(self, events):
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
                    
        return True
    
    def update(self, dt):
        pass

    def draw(self, screen):
        #Fill screen red
        screen.fill((0,50,50))