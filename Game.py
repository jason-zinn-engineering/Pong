#-------------------------------------------------------------------------------
#@Author Jason A. Zinn
#@Date April 6th, 2019
# Python Implementation of Classic Arcade Game Pong
#-------------------------------------------------------------------------------
import pygame
from pygame.locals import *
import math
import board
import player
#

index = 0

class Game():
   
    def __init__(self):
        self.MAX_HEIGHT = 512
        self.MAX_WIDTH = 512
        self.screen = pygame.display.set_mode((self.MAX_HEIGHT, self.MAX_WIDTH))
        #self.player1 = player("left")
        #self.player2 = player("right")
    
    def game_loop(self):
        # Initialize Screen
        pygame.init()
        pygame.display.set_caption(" | Pong |")
        # Fill Background
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill((255,55,255))
        # Display some text
        font = pygame.font.Font(None,36)
        text = font.render("Hello There", 1, (10,10,10))
        textpos = text.get_rect()
        textpos.centerx = background.get_rect().centerx
        background.blit(text, textpos)
        # Blit? everything to the screen
        self.screen.blit(background, (0,0))
        pygame.display.flip()
        # Event loop
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                

#-------------------------------------------------------------------------------
if __name__ == "__main__":
    Pong = Game()
    Pong.game_loop()
