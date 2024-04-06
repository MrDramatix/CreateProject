import pygame
import math


class Arrow(object):
    def __init__(self, sprite, win, x_pos, y_pos, width, height, angle):
        self.sprite = sprite
        self.win = win
        self.xPos = x_pos
        self.yPos = y_pos
        self.angle = angle
        self.width = width
        self.height = height
        self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height))

    def find_true_pos(self):
        img_center = [self.width / 2 + self.xPos, self.height / 2 + self.yPos]
        return img_center

    def point_to_mouse(self, win, origin, pivot):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        x_dis = mouse_x - pivot[0]
        y_dis = mouse_y - pivot[1]
        angle = math.degrees(math.atan2(x_dis, y_dis))
