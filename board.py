import vector
import Game
import pygame
import math
class board:
    # constructor
    def __init__(self, color, vector, height, width):
        self.color = (255,255,0)
        self.vector = vector
        self.height = 10
        self.width = 2 
    # functions
    def draw_board_frame(self):
        pygame.draw.rect(Game.screen, color, vector)
    #
    def draw_board_loop(self, draw_frame):
        self.draw_frame = draw_frame

        
