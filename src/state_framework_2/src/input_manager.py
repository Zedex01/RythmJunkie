
""" TODO: """

import pygame
from src.events import *
from src.states.states import *

class InputManager():
    def __init__(self):
        self.layouts = ["UI", "Gameplay"]
        self.active_layout = "UI"

    def handle_events(self, events):
        for event in events:

            #If there is a quit, exit
            if event.type == pygame.QUIT:
                return False
            
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

            #Gameplay Control Events
            if self.active_layout == "Gameplay":
                if event.type == KEYDOWN:
                    pass



            if event.type == CUSTOM:
                
                # ==== State Based Control Layout ====
                if event.system == "state_machine":
                    if event.action == "changed_state":
                        #Switch to gameplay while game is running, else use UI
                        if event.new_state == 'running':
                            self.active_layout == "Gameplay"
                            print("Control layout changed to ", self.active_layout)

                        elif event.new_state != 'running' and self.active_layout != "UI":
                            self.active_layout == "UI"
                            print("Control layout changed to ", self.active_layout)

                # =============================

                if event.system == INPUT:
                    pass
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4: #Scroll up
                    pygame.event.post(Event(CUSTOM, {SYS:SOUND, ACTION: "volume_up"}))
                if event.button == 5: #Scroll Down
                    pygame.event.post(Event(CUSTOM, {SYS:SOUND, ACTION: "volume_down"}))
                    

            if event.type == pygame.KEYDOWN:

                # ================== DEBUG ===================
                                #Temp for DEBUG
                if event.key == pygame.K_l:
                    pygame.event.post(Event(CUSTOM, {"system":"sound", "action":"load_song", "set_id":"1"}))

                if event.key == pygame.K_p:
                    pygame.event.post(Event(CUSTOM, {"system":"sound", "action":"play_song"}))

                if event.key == pygame.K_s:
                    pygame.event.post(Event(CUSTOM, {"system":"sound", "action":"stop_song"}))

                if event.key == pygame.K_o:
                    pygame.event.post(Event(CUSTOM, {"system":"sound", "action":"pause_song"}))
                
                if event.key == pygame.K_u:
                    pygame.event.post(Event(CUSTOM, {"system":"sound", "action":"unpause_song"}))

                if event.key == pygame.K_z or event.key == pygame.K_x:
                    pygame.event.post(Event(CUSTOM, {"system":"sound", "action":"play_sound", "sound":"hit"}))





        return True
