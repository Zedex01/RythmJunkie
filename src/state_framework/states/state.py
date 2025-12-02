"Abstract/base State Class"

class State():
    def __init__(self, state_machine):
        self.state_machine = state_machine

    #Ran on state init
    def enter(self):
        pass

    def exit(self):
        pass

    def handle_events(self, events):
        return True
    
    def update(self, dt):
        pass

    def draw(self, screen):
        pass
