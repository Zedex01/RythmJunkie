
""" TODO: """

import pygame
from pygame import *
from src.events import *
from src.states.states import *

class InputManager():
    def __init__(self):
        self.layouts = ["UI", "Gameplay"]
        self.active_layout = "UI"

        #For Special Key Combos
        self.l_shift_down = False
        self.l_ctrl_down = False

    def handle_events(self, events):
        for event in events:
            #print("InputManager handling event: ", event)

            #If there is a quit, exit
            if event.type == QUIT:
                #post quit event
                pygame.event.post(Event(CUSTOM, {SYS:UTIL, ACTION:"quit"}))

            #if event.type == MOUSEWHEEL:
             #   print(event.y)

            # ==== State Based Control Layout ====
            if event.type == CUSTOM:
                if event.system == "state_machine":
                    if event.action == "changed_state":
                        #Switch to gameplay while game is running, else use UI
                        if event.new_state == 'running':
                            self.active_layout == "Gameplay"
                            print("Control layout changed to ", self.active_layout)

                        elif event.new_state != 'running' and self.active_layout != "UI":
                            self.active_layout == "UI"
                            print("Control layout changed to ", self.active_layout)

            #UI Control Events
            if self.active_layout == "UI":
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        pygame.event.post(Event(CUSTOM, {SYS:INPUT, ACTION: "menu-up"}))
                    
                    elif event.key == K_DOWN:
                        pygame.event.post(Event(CUSTOM, {SYS:INPUT, ACTION: "menu-down"}))

                    elif event.key == K_LEFT:
                        pygame.event.post(Event(CUSTOM, {SYS:INPUT, ACTION: "menu-left"}))

                    elif event.key == K_RIGHT:
                        pygame.event.post(Event(CUSTOM, {SYS:INPUT, ACTION: "menu-right"}))

                    elif event.key == K_SPACE or event.key == K_RETURN:
                        pygame.event.post(Event(CUSTOM, {SYS:INPUT, ACTION: "menu-accept"}))

                    elif event.key == K_BACKSPACE or event.key == K_ESCAPE:
                        pygame.event.post(Event(CUSTOM, {SYS:INPUT, ACTION: "menu-back"}))

                    elif event.key == K_LSHIFT:
                        pygame.event.post(Event(CUSTOM, {SYS:INPUT, ACTION:"l_shift_down"}))
                    
                    elif event.key == K_LCTRL:
                        pygame.event.post(Event(CUSTOM, {SYS:INPUT, ACTION:"l_ctrl_down"}))
                    
                    # ==== Volume Controls ====
                    #Keep Track of Ctrl and Shift using states
                    if event.key == K_LSHIFT:
                        if not self.l_shift_down:
                            self.l_shift_down = True
                    elif event.key == K_LCTRL:
                        if not self.l_ctrl_down:
                            self.l_ctrl_down = True

                elif event.type == KEYUP:
                    if event.key == K_LSHIFT:
                        if self.l_shift_down:
                            self.l_shift_down = False
                    elif event.key == K_LCTRL:
                        if self.l_ctrl_down:
                            self.l_ctrl_down = False
                
                #Check Scroll Wheel Events
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4: #Scroll up
                        print("SU")
                        if self.l_shift_down: 
                            pygame.event.post(Event(CUSTOM, {SYS:SOUND, ACTION:"music_volume_up"}))
                        elif self.l_ctrl_down: 
                            pygame.event.post(Event(CUSTOM, {SYS:SOUND, ACTION:"sound_volume_up"}))
                        else:
                            pygame.event.post(Event(CUSTOM, {SYS:SOUND, ACTION:"volume_up"}))

                    elif event.button == 5: #Scroll Down
                        print("SD")
                        if self.l_shift_down: 
                            pygame.event.post(Event(CUSTOM, {SYS:SOUND, ACTION:"music_volume_down"}))
                        elif self.l_ctrl_down: 
                            pygame.event.post(Event(CUSTOM, {SYS:SOUND, ACTION:"sound_volume_down"}))
                        else:
                            pygame.event.post(Event(CUSTOM, {SYS:SOUND, ACTION:"volume_down"}))
                   
            #Gameplay Control Events
            elif self.active_layout == "Gameplay": 
                pass

            # =============================


 # ===================================================

                #if event.type == pygame.KEYDOWN: 
                #if event.key == pygame.K_l:
                #    pygame.event.post(Event(CUSTOM, {"system":"sound", "action":"load_song", "set_id":"1"}))
#
                #if event.key == pygame.K_p:
                #    pygame.event.post(Event(CUSTOM, {"system":"sound", "action":"play_song"}))
#
                #if event.key == pygame.K_s:
                #    pygame.event.post(Event(CUSTOM, {"system":"sound", "action":"stop_song"}))
#
                #if event.key == pygame.K_o:
                #    pygame.event.post(Event(CUSTOM, {"system":"sound", "action":"pause_song"}))
                #
                #if event.key == pygame.K_u:
                #    pygame.event.post(Event(CUSTOM, {"system":"sound", "action":"unpause_song"}))
#
                #if event.key == pygame.K_z or event.key == pygame.K_x:
                #    pygame.event.post(Event(CUSTOM, {"system":"sound", "action":"play_sound", "sound":"hit"}))



    
    def update(self, dt):
        pass

    def volume_event_handler(self, event): pass