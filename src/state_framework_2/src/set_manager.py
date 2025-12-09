import pygame
from pygame import *

from pathlib import Path

from src.events import *

import random as r

#For Errors:
import tkinter.messagebox as m

"""
Docstring for state_framework_2.src.set_manager

Recieves calls for set change.
outline:


broadcasts a set change and updates everything that needs to know:
    sends out:
        Song Name
        Artist Name
        Map Name
        Set_id
        Map_id

        #By default, set map_id to zero, unless otherwise specified

        
        Format

        [<set_id> <set_name>]:set_str
            |_ <map_id> <map_name>
        
"""

class SetManager():
    def __init__(self):

        #Active set(id)
        self.set_id: int = None
        self.map_id: int = None

        self.set_root: Path = None

        #contains a list of all sets
        self.sets: list = []
        self.set_index: int = None
        self.sets_last_index: int = None

        #TODO add exe support
        self.sets_root = Path(__file__).parent.parent / "data" / "songs"

        #Update all sets
        self._update_sets()

        #Pick random set at startup
        self._change_set(r.randint(0, self.sets_last_index))

        #play song
        #pygame.event.post(Event(CUSTOM, {SYS:SOUND, ACTION:"play_song"}))


    def handle_events(self, events):
        for event in events:
            if event.type == CUSTOM:
                if event.system == SET:
                    #Rotates left through list
                    if event.action == "change_left": 
                        #Decrement within bounds
                        if self.set_index > 0:
                            self.set_index -= 1
                        else:
                            self.set_index = self.sets_last_index

                        self._change_set(self.sets[self.set_index])

                    #Rotates Right through list
                    if event.action == "change_right":
                        #Increment within bounds
                        if self.set_index < self.sets_last_index:
                            self.set_index += 1
                        else:
                            self.set_index = 0

                        self._change_set(self.sets[self.set_index])

                    #TODO: Implement specific song
                    if event.action == "change_to":
                        if event.set_id:#
                            pass

                    #re-grabs all the sets from the songs folder (useful after adding new maps while playing)
                    if event.action == "refresh":
                        self._update_sets

                    #For any state entrys that need to know the current set, the can may a request to echo the active set
                    if event.action == "request_active_set":
                        pygame.event.post(Event(CUSTOM, {SYS:SET, ACTION:"active_set", "set_path":self.set_root}))



    #Updates the current list of sets avaliable
    def _update_sets(self): 
        #clear the list
        self.sets = []

        #itter through all sets and add them to list.
        for set in self.sets_root.iterdir():
            self.sets.append(set)
        #set the final index of sets
        self.sets_last_index = len(self.sets) - 1

    #Change Active set
    def _change_set(self, set_root):
        
        if not isinstance(set_root, Path):
            if type(set_root) is int:
                for set in self.sets:
                    if set.name.startswith(str(set_root)+" "):
                        set_root = set

            else:
                m.showerror("Error", f"Unknown type: {type(set_root)}")
                exit()

        self.set_root = set_root

        #Get the index of the new set
        self.set_index = self.sets.index(self.set_root)

        #Send out event containing the set root whenever there is a change to the song!
        pygame.event.post(Event(CUSTOM, {SYS:SET, ACTION:"new_active_set", "set_path":self.set_root}))
        pygame.event.post(Event(CUSTOM, {SYS:SOUND, ACTION:"play_song"}))


    def _change_map(self, map_id): pass

    

       

