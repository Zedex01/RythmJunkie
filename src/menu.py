import pygame

#https://www.youtube.com/watch?v=bmRFi7-gy5Y

class Menu():
    def __init__(self, game):
        #Get ref to game
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2

        #Is Active?
        self.run_display = True
        
        #Cursor
        #Make cursor a 20,20 square
        self.cursor_rect = pygame.Rect(0,0,20,20) 
         
        #We do not want the cusor right ontop of our selection, 
        #   we want it to be to the left of our text.
        self.offset = - 60

    #Helper Functions
    def draw_cursor(self):
        #Draw the cursor on the screen
        self.game.draw_text("*", 30, self.cursor_rect.x, self.cursor_rect.y + 6 )

    #Update surface
    def blit_screen(self):

        #Draws over the surface
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.update()

        #Reset keys
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.state = "Start"

        #Text Locations
        self.start_x, self.start_y = self.mid_w, self.mid_h + 30
        self.options_x, self.options_y = self.mid_w, self.mid_h + 50
        self.credits_x, self.credits_y = self.mid_w, self.mid_h + 70
        
        #Starting position for cursor
        self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)

    def display_menu(self):
        #Make is true while running
        self.run_display = True

        while self.run_display:
            
            #Check Events
            self.game.check_events()
            
            #Check for various inputs
            self.check_input()

            #Fill the entire surface with black
            self.game.display.fill(self.game.BLACK)
            
            #Draw Text
            self.game.draw_text("Main Menu", 20, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2 - 20)
            self.game.draw_text("Start Game", 20, self.start_x, self.start_y)
            self.game.draw_text("Options", 20, self.options_x, self.options_y)
            self.game.draw_text("Credits", 20, self.credits_x, self.credits_y)

            #Draw Cursor
            self.draw_cursor()
            #render
            self.blit_screen()

            
    def move_cursor(self):
        #print(f"{self.cursor_rect} | {self.state}")

        #Set Cursor position on key presses
        if self.game.DOWN_KEY:
            print("Pressed Down!")
            if self.state == "Start":
                self.cursor_rect.midtop = (self.options_x + self.offset, self.options_y)
                self.state = "Options"
            
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.credits_x + self.offset, self.credits_y)
                self.state = "Credits"
            
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.state = "Start"
        
        if self.game.UP_KEY:
            print("Pressed up!")
            if self.state == "Start":
                self.cursor_rect.midtop = (self.credits_x + self.offset, self.credits_y)
                self.state = "Credits"

            elif self.state == "Options":
                self.cursor_rect.midtop = (self.start_x + self.offset, self.start_y)
                self.state = "Start"

            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.options_x + self.offset, self.options_y)
                self.state = "Options"
        
    def check_input(self):
        self.move_cursor()


        #If the player presses the start key, check which state game is in:
        if self.game.START_KEY:

            #If in start state, launch game
            if self.state == "Start":
                self.game.playing = True

            #If in Options state, open options menu
            elif self.state == "Options":
                #Set new menu
                self.game.curr_menu = self.game.options_menu

                #Stop Current loop
                self.run_display = False

            #If in Credits state, open credits
            elif self.state == "Credits":
                pass

            #Disable current menu:
            self.run_display = False
            

class OptionsMenu(Menu):
    def __init__(self, game):
        super().__init__(game)
        #Init Selection
        self.state = "Volume"

        #Text Positions
        self.title_x, self.title_y = self.mid_w, self.mid_h - 20
        self.vol_x, self.vol_y = self.mid_w, self.mid_h + 20
        self.controls_x, self.controls_y = self.mid_w, self.mid_h + 40

        #Init Cursor Pos:
        self.cursor_rect.midtop = (self.vol_x + self.offset, self.vol_y)

    def display_menu(self):
        self.run_display = True

        while self.run_display:
            #Poll Events
            self.game.check_events()
            #Check player inputs
            self.check_input()

            #Update Graphics
            self.game.display.fill((0,0,0))
            self.game.draw_text("Options", 20, self.title_x, self.title_y)
            self.game.draw_text("Volume", 20, self.vol_x, self.vol_y)
            self.game.draw_text("Controls", 20, self.controls_x, self.controls_y)
            self.draw_cursor()

            self.blit_screen()

    def check_input(self):
        #exit from menu
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False

        #Menu Navigation
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            
            if self.state == "Volume":
                self.state = "Controls"
                self.cursor_rect.midtop = (self.controls_x + self.offset, self.controls_y)
            
            elif self.state == "Controls":
                self.state = "Volume"
                self.cursor_rect.midtop = (self.vol_x + self.offset, self.vol_y)

          

class CreditsMenu(Menu):
    def __init__(self):
        super().__init__()
        #Text Positions
        self.title_x, self.title_y = self.mid_w, self.mid_h - 20
        self.author_x, self.author_y = self.mid_w, self.mid_h + 20

        self.back_x, self.back_y = self.game.DISPLAY_W - 50, self.game.DISPLAY_H - 50


    def display_menu(self):
        pass
        
        
