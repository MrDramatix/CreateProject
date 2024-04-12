import pygame

import playerClass
import powerbarClass
import holeClass
import barrierClass

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Game")
win.fill((0, 120, 0))
clock = pygame.time.Clock()

# Code from "Coding With Russ" Start
text_font = pygame.font.SysFont('Arial', 30)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    win.blit(img, (x, y))
# Code from "Coding With Russ" End


hole = holeClass.Hole(pygame.math.Vector2(250, 100), 25, win)
wall = barrierClass.Barrier(pygame.math.Vector2(250, 250), 200, 50, win)
ball = playerClass.Player(250, 250, 18, hole, wall, win)
meter = powerbarClass.Meter(win, pygame.math.Vector2())

run = True
while run:
    clock.tick(24)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            ball.launch(meter.get_power())

    win.fill((0, 120, 0))
    ball.draw()
    hole.draw()

    if ball.finish:
        draw_text("You Win!", text_font, (0, 0, 0), 250, 250)

    # END OF LOOP HERE
    pygame.display.update()

pygame.quit()
