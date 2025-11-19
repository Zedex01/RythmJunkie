import pygame
from pygame import *

from src.menu import *


class Game:
    def __init__(self):
        #Initialize
        pygame.init()
        pygame.display.set_caption("Rythm Junkie!!!")

        #Set basic states
        self.running, self.playing = True, False

        #init menu keys
        self.reset_keys()

        #Window Size
        self.DISPLAY_W , self.DISPLAY_H = 480, 270

        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))

        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))

        self.font_name = pygame.font.get_default_font()

        self.BLACK, self.WHITE = (0,0,0), (255,255,255)

        self.clock = pygame.time.Clock()

        self.dt = 0.01

        #Set the current menu to be main_menu
        self.main_menu = MainMenu(self)
        self.options_menu = OptionsMenu(self)

        self.curr_menu = self.main_menu

    def check_events(self):
        
        #check every event that occurs
        for event in pygame.event.get():

            #Check for clicking the X button
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            
            #Check if a key is being pressed down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
    
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def game_loop(self):

        #Event loop:
        while self.playing:
            self.check_events()
            
            if self.START_KEY:
                self.playing = False

            self.reset_keys()
                      
            #Set Canvas to all black
            self.display.fill(self.BLACK)    

            self.draw_text("Thanks for playing", 20, self.DISPLAY_W/2, self.DISPLAY_H/2)

            #Align display with window
            self.window.blit(self.display, (0,0))    
            pygame.display.update()

            #Update Display:
            #pygame.display.flip()

            dt = self.clock.tick(60)  / 1000
            dt = max(0.001, min(0.1, dt))

        pygame.QUIT

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect() #x, y, Width, Height
        text_rect.center = (x, y) #Center text relative to x,y

        #blit over the window?
        self.display.blit(text_surface, text_rect)
