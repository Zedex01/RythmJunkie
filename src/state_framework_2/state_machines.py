"""
Contains State Machines

"""
#import abstract class
from _state_machine import StateMachine

class Core(StateMachine):
    pass

class GameStateMachine(StateMachine):
    def __init__(self):
        super().__init__()

        self.running = True
