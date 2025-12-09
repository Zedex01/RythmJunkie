"""
States classes

"""
import pygame, json
from pygame import *
from src.states._state import State
from src.player import Player
from src.note import Note
from src.button import Button

from src.events import *

""" 
Main Entry point, 
3 Options
 - play, credits, exit

    Play -> Song Select State
    Credits -> Credits State
    Exit  -> Quit Game

SPACE and ENTER can be used inter-changeably
ESCAPE and BACKSPACE can be used inter-changeably

ARROWS to navigate buttons (WASD?)

 """

class Main(State):
    def __init__(self, state_machine):
        super().__init__(state_machine)

        self.name = "main"

        #List of all buttons
        self.btns = ["Play", "Credits", "Exit"]

        #Set default button
        self.curr_btn = 0
        self.last_btn = len(self.btns) - 1

        self.play_btn = Button("Play", (100,35), (30,80))
        self.credits_btn = Button("Credits", (100,35), (30,120))
        self.exit_btn = Button("Exit", (100,35), (30,160))

    def handle_events(self, events) -> bool:
        for event in events:
            if event.type == CUSTOM:
                if event.system == INPUT:
                    #if the menu-up event is called, move 1 button up
                    if event.action == "menu-up":
                        if self.curr_btn <= 0:
                            self.curr_btn = self.last_btn
                        else:
                            self.curr_btn -= 1   
                    #if the menudown event is grabbed, move 1 button down
                    elif event.action == "menu-down":
                        if self.curr_btn >= self.last_btn:
                            self.curr_btn = 0
                        else:
                            self.curr_btn += 1 

                    #If the accept key is pressed, check which button is selected and perform action
                    elif event.action == "menu-accept":
                        if self.btns[self.curr_btn] == "Play":
                            self.state_machine.change_state(SongSelect(self.state_machine))

                        elif self.btns[self.curr_btn] == "Credits":
                            self.state_machine.change_state(Credits(self.state_machine))

                        elif self.btns[self.curr_btn] == "Exit":
                            pygame.event.post(Event(CUSTOM, {SYS:UTIL, ACTION:"quit"}))

        self.play_btn.handle_events(events)

    def update(self, dt):
    #Apply changes to button states
        if self.btns[self.curr_btn] == "Play":
            self.play_btn.set_state("selected")
        else:
            self.play_btn.set_state("default")

        if self.btns[self.curr_btn] == "Credits":
            self.credits_btn.set_state("selected")
        else:
            self.credits_btn.set_state("default")

        if self.btns[self.curr_btn] == "Exit":
            self.exit_btn.set_state("selected")
        else:
            self.exit_btn.set_state("default")

    #Update buttons
        self.play_btn.update(dt)
        self.credits_btn.update(dt)
        self.exit_btn.update(dt)

    def draw(self, screen):
        #Fill screen grey
        screen.fill((50,50,50))

        #Render Text
        title_text = self.font.render("Rythm Junkie!!!", True, (255,255,255))
        #prompt_text = self.small_font.render("Press G to Start", True, (255,255,255))
        play_button = self.small_font.render("Play", True, (255,255,255))
        credits_button = self.small_font.render("Credits", True, (255,255,255))
        exit_button = self.small_font.render("Exit", True, (255,255,255))

        #Position Text
        screen.blit(title_text, (20,20))
        self.play_btn.draw(screen)
        self.credits_btn.draw(screen)
        self.exit_btn.draw(screen)
        #screen.blit(play_button, (40,60))
        #screen.blit(credits_button, (40,100))
        #screen.blit(exit_button, (40,140))

class Credits(State):
    """
    Credits page, contains a back button in bottom left
    surface with long explination, creator, inspiration, mentions etc
    """
    def __init__(self, state_machine):
        super().__init__(state_machine)
        self.name = "credits"

        #textbox
        self.text_box = pygame.Surface((self.screen_w*0.6,self.screen_h*0.5), SRCALPHA)

    def handle_events(self, events):
        for event in events:
            #pressing back returns to main
            if event.type == CUSTOM:
                if event.system == INPUT:
                    if event.action == "menu-back":
                        self.state_machine.change_state(Main(self.state_machine))
        return True

    def update(self, dt): pass

    def draw(self, screen): 
        screen.fill((50,50,50))

        # ==== Text Box ====
        self.text_box.fill((0,0,0,0))

        #Draw BG:
        pygame.draw.rect(self.text_box, (75,75,75), self.text_box.get_rect(), border_radius=12)
        #Draw Border:
        pygame.draw.rect(self.text_box, (150,150,150), self.text_box.get_rect(), width=3, border_radius=12)


        # === Text ===

        title_text = self.font.render("Credits", True, (255,255,255))
        content = " This is a sample multiline text\nHere is the start of line 2.\nThree!"
        content_text = self.super_small_font.render(content, True, (255,255,255))
        screen.blit(title_text, (20,20))
        self.text_box.blit(content_text, (20,20))

        #Set rect of textbox at center of screen
        self.text_box_rect = self.text_box.get_rect(center=screen.get_rect().center)
        
        #draw textbox on screen
        screen.blit(self.text_box, self.text_box_rect)

class SongSelect(State):
    """
    Docstring for SongSelect

    Allows Navigation of various songs, move left and right to scroll through songs, shows visual and audio preview

    Functions:
        - Left/Right
        - Start
        - Back

        Settings ???

    """

    def __init__(self, state_machine):
        super().__init__(state_machine)
        
        #Send out a request for the currently active set when loading the state
        pygame.event.post(Event(CUSTOM, {SYS:SET, ACTION:"request_active_set"}))

        #Set Track info to None
        self.track_artist, self.track_name = None, None

        self.set_root = None

        #Get paths
        self.data_dir = self.state_machine.data_dir
        ui_path = self.data_dir / "skins" / "Builtin" / "SongSelect.png"
        self.ui_bg = pygame.image.load(ui_path)


    def handle_events(self, events):
        #Itterate through all events
        for event in events:

            #Check for custom events
            if event.type == CUSTOM:

                #Check for events from the input manager
                if event.system == INPUT:
                    if event.action == "menu-left": 
                        pygame.event.post(Event(CUSTOM, {SYS:SET, ACTION:"change_left"}))

                    elif event.action == "menu-right": 
                        pygame.event.post(Event(CUSTOM, {SYS:SET, ACTION:"change_right"}))

                    elif event.action == "menu-accept":  pass
                       
                    elif event.action == "menu-back":
                        #return to main menu
                        self.state_machine.change_state(Main(self.state_machine))

                #Anytime there is a change to the active set update!
                if event.system == SET:
                    if event.action == "active_set" or event.action == "new_active_set":
                        self.set_root = event.set_path
                        self.update_set()



    def update(self, dt):
        pass


    def draw(self, screen):
        screen.fill((50,50,50))

        #get screen size dynamically
        width, height = screen.get_size()

        #get center of screen
        screen_cx, screen_cy = screen.get_rect().center

        #BackgroundSurface
        bg_surface = pygame.Surface((width, height), SRCALPHA)

        #UI Surface
        self.ui_bg = pygame.transform.scale(self.ui_bg, (width, height))
        screen.blit(self.ui_bg, (0,0))

        #AlbumSurface

        #Text_Surface
        song_name_surface = pygame.Surface((width*0.27, height*0.15), SRCALPHA)
        song_name_surface.fill((0,0,0,0))
        song_name_surface_rect = song_name_surface.get_rect() #Def pos will be 0, 0

        #Set pos on screen
        song_name_surface_rect.center = screen_cx, height*0.14
        screen.blit(song_name_surface, song_name_surface_rect)
        
        if self.set_root:
        #song_name
            song_text = self.small_font.render(self.track_name, True, (0,0,0))
            artist_text = self.super_small_font.render(self.track_artist, True, (0,0,0))
            song_text_rect = song_text.get_rect() #Gets Size
            artist_text_rect = artist_text.get_rect() #Gets Size
            song_text_rect.center = song_name_surface_rect.centerx, song_name_surface_rect.centery - (height*0.025)
            artist_text_rect.center = song_name_surface_rect.centerx, song_name_surface_rect.centery + (height*0.025)
            screen.blit(song_text, song_text_rect)
            screen.blit(artist_text, artist_text_rect)

        #artist_name

        #Button Surface

        #make surface
        set_name_surface = pygame.Surface((width*0.6,height*0.2), SRCALPHA)
        
        #make surface rect
        set_name_surface_rect = set_name_surface.get_rect(center=(screen.get_rect().center[0], height*0.2))


    def update_set(self):
        chart = self.set_root / "0.json"

        #Get info:
        with chart.open("r", encoding="utf-8") as f:
            track = json.load(f)

        self.track_name = track["song"]
        self.track_artist = track["artist"]   



class Settings(State):
    def handle_events(self, events) -> bool:

        for event in events:

            #Check if the 'X' is pressed on window
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                #Check which key was pressed:

                #if 'Esc' key was pressed:
                if event.key == pygame.K_ESCAPE:
                    
                    #Lazy import to prevent circular import
                    from states.states import Main
                    self.state_machine.change_state(Main(self.state_machine))

        return True

    def draw(self, screen):
        #Fill screen Green
        screen.fill((50,255,50))

        #Render Text
        title_text = self.font.render("Settings", True, (255,255,255))
        prompt_text = self.small_font.render("Press Esc to go back.", True, (255,255,255))

        #Position Text
        screen.blit(title_text, (50,50))
        screen.blit(prompt_text, (50,120))

class Controls(State):
    pass

# ====== Game States ======
class Running(State):
    def __init__(self, state_machine):
        super().__init__(state_machine)
        self.name = "running"

        #Spawn player
        self.player = Player(self.state_machine)

        #Spawn Note
        self.note = Note(Vector2(480, 100))

    def enter(self):
        #reset Keys
        self.player.reset_keys()

    def handle_events(self, events):
        #Handle Player Events
        self.player.handle_events(events)

        for event in events:
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:                  
                #If escape is pressed, pause the game!
                if event.key == pygame.K_ESCAPE:
                    #Pass to pause both the current game state and the state machine
                    self.state_machine.change_state(Pause(self.state_machine, self))
        
        return True  

    def update(self, dt):
        self.player.update(dt)   
        self.note.update(dt)

    def draw(self, screen):
        self.player.draw(screen)
        self.note.draw(screen)       
                    
class Pause(State):
    def __init__(self, state_machine, running_state):
        super().__init__(state_machine)
        #Get passed the current instance of the running state
        self.running_state = running_state
        self.name = "pause"

    def handle_events(self, events):
        for event in events:
            #If 'X' is clicked, close
            if event.type == pygame.QUIT:
                return False

            #If a key is pressed...
            if event.type == pygame.KEYDOWN:

                #If Escape is pressed...
                if event.key == pygame.K_ESCAPE:
                    #Return to gameplay...
                    self.state_machine.change_state(self.running_state)
        return True
    
    def draw(self, screen):
        #Clear the screen
        screen.fill((0,0,0))

        #Draw Current Game state as Background
        self.running_state.draw(screen)

        #Set Surface to have slight opacity
        self.surface.fill((0, 0, 0, 40))

        #render text
        title_text = self.font.render("Paused", True, (255,255,255))
        prompt_text = self.small_font.render("Press ESC to return to game.", True, (255,255,255))

        #Blit to surface
        self.surface.blit(title_text, (50,50))
        self.surface.blit(prompt_text, (50,120))

        #Blit to screen
        screen.blit(self.surface, (self.surface_padding,self.surface_padding))



