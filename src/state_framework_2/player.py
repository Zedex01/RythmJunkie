"""
Basic 2-D Player Control Class
"""

import pygame, math
from pygame import *

class Player():
    def __init__(self, state_machine):
        #Set initital Position
        self.pos = Vector2(480/2, 270/2)
        self.last_pos = self.pos.copy()

        self.mv_scale = 200
        self.mv_velocity = Vector2(0,0)

        #Set all keys to false
        self.reset_keys()


    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.mv_up = True
                if event.key == pygame.K_DOWN:
                    self.mv_down = True
                if event.key == pygame.K_LEFT:
                    self.mv_left = True
                if event.key == pygame.K_RIGHT:
                    self.mv_right = True
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.mv_up = False
                if event.key == pygame.K_DOWN:
                    self.mv_down = False
                if event.key == pygame.K_LEFT:
                    self.mv_left = False
                if event.key == pygame.K_RIGHT:
                    self.mv_right = False

    def update(self, dt):
        #Store last position
        self.last_pos = self.pos.copy()
        
        #Reset Values
        self.mv_velocity = Vector2(0,0)
        mv_vel_normalized = Vector2(0,0)

        #Apply velocity based on keys
        if self.mv_up:
            self.mv_velocity.y = -1
        if self.mv_down:
            self.mv_velocity.y = 1
        if self.mv_left:
            self.mv_velocity.x = -1
        if self.mv_right:
            self.mv_velocity.x = 1

        #Check if velocity is not Zero
        if self.mv_velocity.length_squared() > 0:
            #Normalize motion
            self.mv_velocity.normalize_ip()

        #Update position
        self.pos += self.mv_velocity*self.mv_scale*dt

    def draw(self, screen):
        #Fill Screen with Black
        screen.fill((50,50,50))

        #Render Player
        player_rect = pygame.Rect(self.pos.x, self.pos.y, 10, 10)

        #Draw Player
        pygame.draw.rect(screen, (255,255,255),player_rect, 0)


# === Methods ===
    def reset_keys(self):
        self.mv_up, self.mv_down, self.mv_left, self.mv_right = False, False, False, False

