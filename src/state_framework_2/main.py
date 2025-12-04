import pygame
from pygame import *

from src.state_machines import Core

#States
from src.states.states import Main

def main():
    #Init game
    pygame.init()
    #Set window title
    pygame.display.set_caption("Rythm Junkie!!!")
    #Init Audio:
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

    screen = pygame.display.set_mode((480, 270))

    clock = pygame.time.Clock()
    dt = 0.01

    running = True

    #Create the main state machine
    core = Core()
    #Set inital state
    core.change_state(Main(core))

    while running:

        events = pygame.event.get()

        running = core.handle_events(events)
        core.update(dt)
        core.draw(screen)      

        pygame.display.flip()      

        dt = clock.tick(60)  / 1000
        dt = max(0.001, min(0.1, dt))

    pygame.quit()

if __name__ == "__main__":
    main()