import pygame


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, health):
        super().__init__()
        surface = pygame.display.get_surface()

        self.hearts = []
        x = 35
        for _ in range(health):
            self.image = pygame.image.load(r"assets\images\heart.png")
            self.rect = self.image.get_rect()
            self.rect.topright = (surface.get_width() - 10 - x, 10)
            x += 35

            self.hearts.append((self.image, self.rect))

    def draw(self, surface):
        surface.blits(self.hearts)