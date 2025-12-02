import pygame
from pygame import *

from state_machine import StateMachine

#States
from states.main_menu import MainMenu

def main():

    #init game
    pygame.init()
    pygame.display.set_caption("Rythm Junkie!!!")

    screen = pygame.display.set_mode((480, 270))

    clock = pygame.time.Clock()
    dt = 0.01

    running = True

    #Create the main state machine
    state_machine = StateMachine()
    #Set inital state
    state_machine.change_state(MainMenu(state_machine))

    while running:

        events = pygame.event.get()

        running = state_machine.handle_events(events)
        state_machine.update(dt)
        state_machine.draw(screen)      

        pygame.display.flip()      

        dt = clock.tick(60)  / 1000
        dt = max(0.001, min(0.1, dt))

        print(running)

    pygame.quit()


if __name__ == "__main__":
    main()