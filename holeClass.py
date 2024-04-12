import pygame
pygame.init()


class Hole(object):
    def __init__(self, pos, radius, win):
        self.pos = pos
        self.radius = radius
        self.win = win
        self.sprite = pygame.draw.circle(self.win, 'gray', self.pos, self.radius)
    
    def draw(self):
        self.sprite = pygame.draw.circle(self.win, 'gray', self.pos, self.radius)
