
import pygame
from pygame import *
import json
from pathlib import Path

from src.events import *

"""
Sound manager handles all audio related task
start song, stop song, pause song, resume song
play sound, stop sound, pause sound, resume sound

Win + R:
sndvol.exe - Classic Volume Mixer

General Flow:
    recieve event(s)
        set_volume -> volume

        load_song -> set_id, map_id
        play_song
        pause_song
        stop_song

        load_sound -> sound
        play_sound
        

        
        about 20-25 ms of latency on press to click sound
"""

class SoundManager():
    def __init__(self):

        #Init Audio:
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

        pygame.mixer.set_num_channels(32)

        self.song_playing = False
        self.song_paused = False

        #Get directory that contains all songs
        self.sets = Path(__file__).parent.parent / "data" / "songs"

        #Set hitsound
        self.hit_sound = pygame.mixer.Sound(Path(__file__).parent.parent / "data" / "skins" / "Builtin" / "hit.wav")

        self.master_volume = 1.0


    def handle_events(self, events): 
        for event in events:
            if event.type == CUSTOM:
                if event.system == "sound":
                    #Hit Sounds
                    if event.action == "play_sound":
                        if event.sound == "hit":
                            #Find open audio channel
                            channel = pygame.mixer.find_channel()
                            if channel:
                                #Play hit sound
                                channel.play(self.hit_sound)

                    #Song Control
                    elif event.action == "load_song":
                        self.load_song(event.set_id)

                    elif event.action == "play_song":
                        try:
                            pygame.mixer.music.play()
                        except Exception as e:
                            print("Play Err: ", e)

                    elif event.action == "stop_song":
                        pygame.mixer.music.stop()

                    elif event.action == "pause_song":
                        pygame.mixer.music.pause()

                    elif event.action == "unpause_song":
                        pygame.mixer.music.unpause()

                    #Audio Levels
                    elif event.action == "volume_up":
                        if self.master_volume < 1.00:
                            self.master_volume += 0.05

                    elif event.action == "volume_down":
                        if self.master_volume > 0.00:
                            self.master_volume -= 0.05

    
    def update(self, dt):

        # === Volume Levels ===
        #Check volume is within 0.02 of mixer audio
        if abs(self.master_volume - pygame.mixer.music.get_volume()) >= 0.02:

            #if volume is less than 0, set to 0
            if self.master_volume < 0:
                self.master_volume = 0

            #Set master Volume Level            
            pygame.mixer.music.set_volume(round(self.master_volume, 2))
            print(f"volume: {round(self.master_volume, 2)}")


    def load_song(self, set_id):

        #Search sets dir looking for set id and return set dir
        set_dir = next((d for d in self.sets.iterdir() if d.is_dir() and d.name.startswith(str(set_id))), None)
        
        #build song path
        audio =  set_dir / "audio.mp3"

        try:
            pygame.mixer.music.load(audio)
        except Exception as e:
            print("Song Load Error: ", e)

    def play_sound(self, sound): pass

        

