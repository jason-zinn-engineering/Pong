import vector
import Game
import pygame
class board:
    # variables
    HEIGHT = 10
    WIDTH = 2
    
    # constructor
    def __init__(self, vector):
        screen = pygame.display.get_surfacE()
        self.area = screen.get_rect()

        
    # functions
    def draw_board(self, color):
        pygame.draw.rect(Game.screen, color, vector)
        
