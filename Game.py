#-------------------------------------------------------------------------------
#@Author Jason A. Zinn
#@Date April 6th, 2019
# Python Implementation of Classic Arcade Game Pong
#-------------------------------------------------------------------------------
import pygame
from pygame.locals import *
import math
#-------------------------------------------------------------------------------
# Global Variables
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Functions
#-------------------------------------------------------------------------------
class Game():
    MAX_HEIGHT = 512
    MAX_WIDTH = 512
    def __init__(self):
        pass
    def start(self):
        pass
    def game_loop(self):
        # Initialize Screen
        pygame.init()
        screen = pygame.display.set_mode((self.MAX_HEIGHT, self.MAX_WIDTH))
        pygame.display.set_caption(" | Pong |")
        # Fill Background
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((255,55,255))
        # Display some text
        font = pygame.font.Font(None,36)
        text = font.render("Hello There", 1, (10,10,10))
        textpos = text.get_rect()
        textpos.centerx = background.get_rect().centerx
        background.blit(text, textpos)
        # Blit? everything to the screen
        screen.blit(background, (0,0))
        pygame.display.flip()
        # Event loop
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return








#-------------------------------------------------------------------------------
# Main Function
#-------------------------------------------------------------------------------
def main():
    pass
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    Pong = Game()
    Pong.game_loop()
