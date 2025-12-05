import pygame
from pygame import *
import sys

"""
USER EVENTS
There are a max of 8 event types, however you have an endless amount of subtypes and depth

post event:
    pygame.event.post(pygame.event.Event(poison))
"""
#USER EVENTS (pygame has a max of 32 events, pygame uses 23 of them. you have 24-32 accessable. [8] events)
POISON = pygame.USEREVENT + 0 #Event ID 24

PLAYER = pygame.USEREVENT + 1 #Event ID 25

class Player:
    def __init__(self):
        self.health = 100
        self.alive = True

    def __del__(self):
        print("Player Died!")

    def handle_events(self, events): pass

    def update(self, dt):
        if self.health <= 0 and self.alive:
            self.die()

    def draw(self, screen): pass

    def die(self):       
        self.alive = False
        #Send out player died event:
        pygame.event.post(Event(PLAYER, {"subtype": "DIED"}))

    def revive(self):
        self.alive = True
        self.health = 100
        print("Player revived!")



def main():

    pygame.init()
    pygame.display.set_mode((300,300))

    player = Player()
    running = True

    #Create a timer that posts an event:
    timer = pygame.time.set_timer(POISON, 1000)

    while running:
        for event in pygame.event.get():
            #print(f"event recv: ", event)

            if event.type == pygame.QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    player.revive()

            #listen for event
            if event.type == POISON:
                if player.alive:
                    player.health -= 10
                    print("Player Health: ", player.health)

            #Custom event type and subtype
            if event.type == PLAYER:
                if event.subtype == "DIED":
                    print("Player Died!")

        player.update(0)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()


