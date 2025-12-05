"""
States classes

"""
import pygame
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

        self.play_btn = Button("Play", Vector2(100,35), Vector2(30,80))
        self.credits_btn = Button("Credits", Vector2(100,35), Vector2(30,120))
        self.exit_btn = Button("Exit", Vector2(100,35), Vector2(30,160))

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

        #Buttons
        self.back_btn = Button("Back",Vector2(0,0), Vector2(0,0))

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


        #Get paths
        self.data_dir = self.state_machine.data_dir
        self.songs_dir = self.data_dir / "songs"

        #List of sets within the song dir
        self.sets = []

        #itter through all songs and add them to sets.
        for set in self.songs_dir.iterdir():
            self.sets.append(set)

        self.set_index = 0
        self.max_index = len(self.sets) - 1
        
        #Set default active set (TODO: Make Random)
        self.active_set = self.sets[self.set_index]

        self._change_active_set = False


    def handle_events(self, events):
        #Itterate through all events
        for event in events:

            #Check for custom events
            if event.type == CUSTOM:

                #Check for events from the input manager
                if event.system == INPUT:
                    if event.action == "menu-left":
                        #Make sure to stay within valid set bounds
                        if self.set_index > 0:
                            self.set_index -= 1
                        else:
                            self.set_index = self.max_index
                        self._change_active_set = True

                    elif event.action == "menu-right":
                        #Make sure to stay within valid set bounds
                        if self.set_index < self.max_index:
                            self.set_index += 1
                        else:
                            self.set_index = 0
                        self._change_active_set = True

                    elif event.action == "menu-accept":
                        pass
                    elif event.action == "menu-back":
                        #return to main menu
                        self.state_machine.change_state(Main(self.state_machine))


    def update(self, dt):
        #If there is a change, update the active set
        if self._change_active_set:
            self._change_active_set = False
            self.active_set = self.sets[self.set_index]
            print("Active Set: ", self.active_set.name)
    
    def draw(self, screen):
        screen.fill((50,50,50))

        #get screen size dynamically
        width, height = screen.get_size()

        #BackgroundSurface
        bg_surface = pygame.Surface((width, height), SRCALPHA)
        #TODO: Load bg image from song
        #screen.blit(bg_surface, (0,0))

        #BorderSurface
        ui_surface = pygame.Surface((width, height), SRCALPHA)
        #Draw Top & Bottom Border (TODO: Replace image)
        pygame.draw.rect(ui_surface, ("white"), ((0,0),(width,height*0.1))) #Top Bar
        pygame.draw.rect(ui_surface, ("white"), ((0,height-height*0.1),(width,height*0.1))) #Bottom Bar
        #Draw Display_name_box
        display_name_bg_rect = pygame.Rect(0,0,width*0.25, height*0.1)
        display_name_bg_rect.center = (width//2, height//10)
        pygame.draw.rect(ui_surface, ("white"), display_name_bg_rect, border_radius=12)
        pygame.draw.rect(ui_surface, ("black"), display_name_bg_rect, width = 4, border_radius=12)

        screen.blit(ui_surface, (0,0))

        #ButtonSurface
        #AlbumSurface?

        #make surface
        set_name_surface = pygame.Surface((width*0.6,height*0.2), SRCALPHA)
        
        #make surface rect
        set_name_surface_rect = set_name_surface.get_rect(center=(screen.get_rect().center[0], height*0.2))

        set_name_surface.fill((255,255,255,255))
        #screen.blit(set_name_surface, set_name_surface_rect)

        



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
