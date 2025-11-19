import pygame
from pygame import *

from src.game import Game

    #JUST KEEP WATCHING

def main():

    game = Game()


    while game.running:
        #Displays whatever the current menu is
        game.curr_menu.display_menu()
        
        #Run game loop
        game.game_loop()


if __name__ == "__main__":
    main()