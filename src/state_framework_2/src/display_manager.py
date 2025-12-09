import pygame
from pygame import *

from src.events import *

"""
Display Manager!

Handles resolution changes and screen resizing


resolutions:
640x360
960x540
1280x720
1600x900
1920x1080
????
FullScreen

"""

RESOLUTIONS = [
        (640, 360),
        (960, 540),
        (1280, 720),
        (1600, 900),
        (1920, 1080)
    ]


class DisplayManager():
    def __init__(self):

        self.new_resolution = None
        self._change_resolution = False

    def handle_events(self, events):
        for event in events:
            if event.type == CUSTOM:
                if event.system == DISP:
                    if event.action == "change_res":
                        #split res into tuple, cast both str values into int values, cast full list to tuple
                        self.new_resolution = tuple([int(value) for value in event.res.split("x")])
                        self._change_resolution = True
                        

    def update(self, dt):
        pass


    def draw(self, screen):
        if self._change_resolution:
            self._change_resolution = False
            pygame.display.set_mode(self.new_resolution)