import pygame
pygame.init()


class Meter(object):
    def __init__(self, win, pos):
        self.pos = pos
        self.win = win
        self.sprite = pygame.draw.rect(self.win, 'gray', (250, 475, 18, 18))

    def draw(self, width):
        self.sprite = pygame.draw.rect(self.win, 'gray', ((250 - (width/2)), 475, width, 18))
        pygame.display.update()

    def get_power(self):
        power = 12
        while power < 50:
            pygame.time.Clock().tick(24)
            power += 0.5
            self.draw((power * 8) - (12 * 8))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    return power
        print(power)
        return power
