"""
2025-12-02

Docstring for state_framework.state_machine

"""
import pygame
from src.events import *
from src.sound_manager import SoundManager
from src.input_manager import InputManager

class StateMachine:

    def __init__(self):
        self.current_state = None

    #Handles all of the events (ex. Key Presses / audio?)
    def handle_events(self, events):
        self.current_state.handle_events(events)



    #Updates animations/motions
    def update(self, dt):
        self.current_state.update(dt)

    #Handles things that need to be drawn on the screen
    def draw(self, screen):
        self.current_state.draw(screen)

    #Changes to the new state
    def change_state(self, new_state):
        #If there is a pre-existing state, exit it first
        if self.current_state:
            self.current_state.leave()

        #Set the new state 
        self.current_state = new_state
        #Enter the new state
        self.current_state.enter()

        #Post State Change event
        try:
            pygame.event.post(pygame.event.Event(CUSTOM, {"system":"state_machine", "action": "changed_state", "new_state":new_state.name}))
        except Exception as e:
            print("Event Err: ", e)

