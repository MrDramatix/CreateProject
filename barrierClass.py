import pygame
pygame.init()


class Barrier(object):
    def __init__(self, pos, width, height, win):
        self.pos = pos
        self.width = width
        self.height = height
        self.win = win

    def draw(self):
        pygame.draw.rect(self.win, 'chocolate4', (self.pos.x, self.pos.y, self.width, self.height))
