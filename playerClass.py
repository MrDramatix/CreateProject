import pygame
import math

pygame.init()


class Player(object):
    def __init__(self, x_pos, y_pos, radius, hole, wall, win):
        self.xPos = x_pos
        self.yPos = y_pos
        self.radius = radius
        self.hole = hole
        self.wall = wall
        self.win = win
        self.sprite = pygame.draw.circle(self.win, "white", (self.xPos, self.yPos), self.radius)
        self.finish = False

    def draw(self):
        self.sprite = pygame.draw.circle(self.win, "white", (self.xPos, self.yPos), self.radius)

    def check_with_hole(self, ballpos):
        dist = math.hypot(self.hole.pos.x - ballpos.x, self.hole.pos.y - ballpos.y)
        if dist <= self.hole.radius:
            print("in hole")
            return True
        else:
            return False

    def edge_collision(self, ballpos, angle):
        if ballpos.x >= 450:
            return angle * -1 - math.pi
        elif ballpos.x <= 50:
            return angle * -1 - math.pi
        elif ballpos.y <= 50:
            return -angle
        elif ballpos.y >= 450:
            return -angle
        else:
            return angle

    def launch(self, speed):
        mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())
        origin = pygame.math.Vector2(self.xPos, self.yPos)
        angle = math.atan2(mouse_pos.y - origin.y, mouse_pos.x - origin.x)
        clock = pygame.time.Clock()
        while speed > 0:
            clock.tick(24)
            self.win.fill((0, 120, 0))
            friction = 1
            speed -= friction
            if speed < 0:
                speed = 0
            new_x = origin.x + (speed * math.cos(angle))
            new_y = origin.y + (speed * math.sin(angle))
            self.sprite = pygame.draw.circle(self.win, "white", (new_x, new_y), self.radius)
            self.hole.draw()
            origin = pygame.math.Vector2(new_x, new_y)
            pygame.display.update()
            if self.check_with_hole(origin):
                self.finish = True
                break
            angle = self.edge_collision(origin, angle)
            print(angle)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
        self.xPos = origin.x
        self.yPos = origin.y
