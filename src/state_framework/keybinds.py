import pygame

class Keybinds:
    def __init__(self):
        #Default Controls:
        self.bindings = {
            "jump": pygame.K_SPACE,
            "shoot": pygame.K_z,
            "pause": pygame.K_ESCAPE,
        }

        #Predefined control schemes?

    #Change an existing binding
    def set_binding(self, action, key):
        self.bindings[action] = key

    #get key for action
    def get_binding(self, action):
        return self.bindings.get(action)