
import pygame
from pygame import *
import json
from pathlib import Path

from note import Note

from states._state import State
from state_machines import Core

"""
Song manager has to handle note spawning, audio syncing, pausing??


"""

class SongManager():
    def __init__(self, song_name):

        self.playing = False
        self.paused = False
        self.resume = False

        #Get main path
        root = Path(__file__).parent

        #Get song dir path
        songs = root / "data" / "songs"
        
        file_name = song_name + ".json"

        #build song path
        song = songs / song_name / file_name


        #Grab song info
        with open(song, "r") as f:
            chart = json.load(f)

        #Pull the notes into a list
        notes = chart["notes"]

        print(notes)

    def __del__(self): pass

    def handle_events(self, events): pass
    
    def update(self, dt):
        #if the game is paused, pause music
        if self.paused:
            pygame.mixer.music.pause()

        #if the game is being resumed, unpause music
        elif not self.paused and self.resume:
            pygame.mixer.music.unpause()
            self.resume = False


    def draw(self, screen):pass

    def spawn_note(self): pass

# ==== Testing state ====
class TestEnv(State):
    
    def __init__(self, state_machine):
        super().__init__(state_machine)

        #Create Song Manager
        song_name = "song1-artist1"
        song_manager = SongManager(song_name)

    def enter(self): pass
    def leave(self): pass
    def handle_events(self, events): pass
    def update(self, dt): pass
    def draw(self, screen): pass




if __name__ == "__main__":
    
    #Env for testing:

    #Initialize Audio:
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

    pygame.init()
    pygame.display.set_caption("Audio Test")
    screen = pygame.display.set_mode((480, 270))
    clock = pygame.time.Clock()
    dt = 0.01

    core = Core()
    core.change_state(TestEnv(core))
    running = True

    while running:

        events = pygame.event.get()

        running = core.handle_events(events)
        core.update(dt)
        core.draw(screen)      
        pygame.display.flip()      

        dt = clock.tick(60)  / 1000
        dt = max(0.001, min(0.1, dt))

    pygame.quit()

