import pygame

from states.state import State

class PauseMenu(State):

    def enter(self):
        pass

    def leave(self):
        pass
    
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
                    from states.game import Game #Lazy import prevents circular import
                    self.state_machine.change_state(Game(self.state_machine))
        return True

    def update(self, dt):
        pass
    
    def draw(self, screen):
        #Clear the screen
        screen.fill((71,4,21))

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
