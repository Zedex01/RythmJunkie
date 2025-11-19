import pygame
from pygame import *

from src.game import Game

    #JUST KEEP WATCHING

def main():

    game = Game()

    game.playing = True

    while game.running:

        game.game_loop()


if __name__ == "__main__":
    main()