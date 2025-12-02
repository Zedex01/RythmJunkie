"""
Handles all states within the game

things like holding the dt when paused so the games persists
"""
from state_machine import StateMachine

class GameStateMachine(StateMachine):

    def __init__(self, state_machine):
        super().__init__(self, state_machine)

        self.paused = False
    
    #Overwrite update to allow for game persistance while paused
    def update(self):
        #if the game is paused, does not updated
        if not self.paused:
            self.change_state.update(dt)
