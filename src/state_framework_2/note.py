"""
Note Object.

on hit, plays audio clip, item disappears
"""
import pygame
from pygame import *

class Note():
    def __init__(self, start_pos):
        
        #Current position of the note
        self.pos = start_pos

        #Position of where the hit happens
        self.hit_pos = Vector2(0,40)

        #Time when the note should be hit, set by song
        self.hit_time = 3.45

        #Travel Speed, set by song
        self.speed = 1

    #Ran when ref to the object is deleted
    def __del__(self):
        #Play Audio??
        #If good hit, play one sound
        #Else, play other
        pass

    def handle_events(self, events):
        #Check for hit??
        pass

    def update(self, dt):
        #apply Movement
        if self.pos.x > 0:
            self.pos.x -= 20*dt

    
    def draw(self, screen):
        #Render Note
        note_rect = pygame.Rect(self.pos.x, self.pos.y, 10, 10)

        #Draw Note
        pygame.draw.rect(screen, (255,255,255),note_rect, 0)