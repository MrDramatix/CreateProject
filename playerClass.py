import pygame
pygame.init()


class Player(object):
    def __init__(self, sprite, x_pos, y_pos, x_rot, y_rot, width, height, vel, radius):
        self.sprite = sprite
        self.xPos = x_pos
        self.yPos = y_pos
        self.xRot = x_rot
        self.yRot = y_rot
        self.vel = vel
        self.radius = radius
        self.width = width
        self.height = height

    def draw(self, win):
        self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height))
        win.blit(self.sprite, (self.xPos, self.yPos))

    def find_true_pos(self):
        img_center = [self.width/2 + self.xPos, self.height/2 + self.yPos]
        return img_center
