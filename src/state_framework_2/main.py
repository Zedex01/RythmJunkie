import pygame
from pygame import *

from src.events import *
from src.state_machines import Core

#States
from src.states.states import Main

def main():
    #Init game
    pygame.init()
    #Set window title
    pygame.display.set_caption("Rhythm Junkie!!!")

    screen = pygame.display.set_mode((640, 360), pygame.RESIZABLE)

    clock = pygame.time.Clock()
    dt = 0.01

    running = True

    #Create the main state machine
    core = Core()
    #Set inital state
    core.change_state(Main(core))

    while running:

        events = pygame.event.get()
        
        core.handle_events(events)
        core.update(dt)
        core.draw(screen) 

        #Check for a quit event
        for event in events:
            if event.type == CUSTOM:
                if event.system == UTIL:
                    if event.action == "quit":
                        running = False     

        pygame.display.flip()      

        dt = clock.tick(60)  / 1000
        dt = max(0.001, min(0.1, dt))



    pygame.quit()

if __name__ == "__main__":
    main()