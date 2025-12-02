"""
2025-12-02

Docstring for state_framework.state_machine

"""
class StateMachine:

    def __init__(self):
        self.current_state = None

    #Changes to the new state
    def change_state(self, new_state):
        #If there is a pre-existing state, exit it first
        if self.current_state:
            self.current_state.exit()

        #Set the new state 
        self.current_state = new_state
        #Enter the new state
        self.current_state.enter()


    #Updates animations/motions
    def update(self, dt):
        self.current_state.update(dt)

    #Handles all of the events (ex. Key Presses / audio?)
    def handle_events(self, events):
        running = self.current_state.handle_events(events)
        return running

    #Handles things that need to be drawn on the screen
    def draw(self, screen):
        self.current_state.draw(screen)