import pygame
import math

import arrowClass
import playerClass

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Game")
win.fill((0, 120, 0))
clock = pygame.time.Clock()

ball = playerClass.Player(pygame.image.load('res/ballsprite.png'),
                          218, 218, 0, 0, 64, 64, 0, 20)

arrow = arrowClass.Arrow(pygame.image.load('res/arrowsprite.png'),
                         win, ball.xPos, ball.yPos, 64, 256, 0)

arrow_pivot_point = [arrow.find_true_pos()[0], arrow.find_true_pos()[1] - (arrow.height/2) + 10]

run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 120, 0))
    ball.draw(win)
    ballcenter = ball.find_true_pos()

    # END OF LOOP HERE
    pygame.display.update()

pygame.quit()
