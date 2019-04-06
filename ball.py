import pygame
import math
import Game
class ball:
#
    def __init__(self, surface, color, pos, radius, width=0):
        self.surface = Game.screen
        self.color = (255,255,0)
        self.pos = (0,0)
        self.radius = 10
    #
    def draw_ball_frame(self):
        return pygame.draw.circle(surface, color, pos, radius, width)
    #
    def draw_ball_loop(self, draw_ball_frame):
        self.draw_ball_frame = draw_ball_frame()