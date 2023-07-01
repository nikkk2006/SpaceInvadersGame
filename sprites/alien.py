import pygame
from random import choice


class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        images = [r"assets\images\alien{}.png".format(i) for i in range(1, 6)]
        self.image = pygame.image.load(choice(images))
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
