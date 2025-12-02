import pygame
from states.state import State

#inherit from abstract class 'State'
class MainMenu(State):

    def enter(self):
        pass

    def leave(self):
        pass

    def handle_events(self, events) -> bool:

        for event in events:

            #Check if the 'X' is pressed on window
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                #Check which key was pressed:

                #if 'g' key was pressed:
                if event.key == pygame.K_g:
                    
                    #Lazy import to prevent circular import
                    from states.game import Game
                    self.state_machine.change_state(Game(self.state_machine))

        return True
    
    def update(self, dt):
        pass

    def draw(self, screen):
        #Fill screen red
        screen.fill((255,50,50))

        #Render Text
        title_text = self.font.render("Main Menu", True, (255,255,255))
        prompt_text = self.small_font.render("Press G to Start", True, (255,255,255))

        #Position Text
        screen.blit(title_text, (50,50))
        screen.blit(prompt_text, (50,120))