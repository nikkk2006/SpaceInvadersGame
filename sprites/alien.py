import pygame
from random import choice


class Alien(pygame.sprite.Sprite):
    def __init__(self, coordinates):
        super().__init__()

        images = [r"assets\images\alien{}.png".format(i) for i in range(1, 6)]
        self.image = pygame.image.load(choice(images))
        self.rect = self.image.get_rect()
        self.rect.center = coordinates

        self.step = 1
        self.steps = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.step
        self.steps += abs(self.step)

        if self.steps >= 50:
            self.step *= -1
            self.steps *= -1

def generateAliens(group):
    for column in range(1, 6):
        for row in range(1, 5):
            x = 100 * column
            y = 75 * row

            alien = Alien((x, y))
            group.add(alien)
