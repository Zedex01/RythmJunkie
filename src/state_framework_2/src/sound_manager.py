
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
        
        about 20-25 ms of latency on press to click sound

        Songs:
         - play on game load, persistant between menus
         - Changing song in song select changes the displayed song

        Sounds:

"""

class SoundManager():
    def __init__(self, state_machine):
        self.state_machine = state_machine

        #Init Audio:
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
        pygame.mixer.set_num_channels(32) #Setup 32 Channels

        #Receive data path from core
        self.data_dir = self.state_machine.data_dir
        self.songs_dir = self.data_dir / "songs"

        #Set hitsound
        self.hit_sound = pygame.mixer.Sound(self.data_dir / "skins" / "Builtin" / "hit.wav")

        #Set default Volumes 
        # (TODO: read and write to settings.json)
        self.volume = 1.0
        self.music_volume = 1.0
        self.sound_volume = 1.0

        #Flag to indicate volume change
        self._change = False

    def handle_events(self, events: list) -> None: 
        for event in events:
            if event.type == CUSTOM:
                if event.system == SOUND:
                    #Hit Sounds
                    if event.action == "play_sound":
                        if event.sound == "hit":
                            #Find open audio channel
                            channel = pygame.mixer.find_channel()
                            if channel:
                                #Play hit sound
                                channel.play(self.hit_sound)

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

                    #Volume Levels
                    #Master
                    elif event.action == "volume_up":
                        if self.volume < 1.0:
                            self.volume += 0.05
                            #Apply upper bound
                            if self.volume > 1.0:
                                self.volume = 1.0
                    elif event.action == "volume_down":
                        if self.volume > 0.0:
                            self.volume -= 0.05
                            #Apply lower bound
                            if self.volume < 0.0:
                                self.volume = 0.0
                            
                    #Music
                    elif event.action == "music_volume_up":
                        if self.music_volume < 1.00:
                            self.music_volume += 0.05
                    elif event.action == "music_volume_down":
                        if self.music_volume > 0.00:
                            self.music_volume -= 0.05
                    #Sound
                    elif event.action == "sound_volume_up":
                        if self.sound_volume < 1.00:
                            self.sound_volume += 0.05
                    elif event.action == "sound_volume_down":
                        if self.sound_volume > 0.00:
                            self.sound_volume -= 0.05

                if event.system == SET:
                    #recv event for a new set, load the song.
                    if event.action == "new_active_set":
                        self.load_song(event.set_path)


    def update(self, dt):
        # === Volume Levels ===
        #Check volume is within 0.02 of mixer audio
        if abs(self.music_volume * self.volume - pygame.mixer.music.get_volume()) >= 0.02:
            #if volume is less than 0, set to 0
            if self.music_volume < 0:
                self.music_volume = 0

            #Set Volume Level:           
            pygame.mixer.music.set_volume(round(self.music_volume * self.volume, 2))
            self.change = True

        #See if the current sound volume of the channel matches the float value
        if abs(self.sound_volume * self.volume - pygame.mixer.Channel(0).get_volume()) >= 0.02:
            #Set min Volume to 0
            if self.sound_volume < 0:
                self.sound_volume = 0

            #Set sound volume Level:       
            new_sound_volume = round(self.sound_volume * self.volume, 2)  
            for i in range(pygame.mixer.get_num_channels()):
                pygame.mixer.Channel(i).set_volume(new_sound_volume)
            self._change = True

        if self._change:
            self._change = False
            print("Master: ", round(self.volume, 2))
            print("Music: ", round(self.music_volume, 2))
            print("Sound: ", round(self.sound_volume, 2)) 
            
    def load_song(self, set_path: Path) -> None:
        #build song path
        audio =  set_path / "audio.mp3"

        #TODO: Update to allow other maps
        chart = set_path / "0.json"

        #Get info:
        with chart.open("r", encoding="utf-8") as f:
            track = json.load(f)

        t_name = track["song"]
        t_artist = track["artist"]       

        try:
            pygame.mixer.music.load(str(audio))
            print(f"loaded {t_name} by {t_artist}.")

        except Exception as e:
            print("Song Load Error: ", e)

    def play_sound(self, sound): pass

        

