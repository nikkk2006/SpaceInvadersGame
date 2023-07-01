import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, coordinates):
        super().__init__()

        self.images = [r"assets\images\exp{}.png".format(i) for i in range(1, 6)]
        self.index = 0
        self.image = pygame.image.load(self.images[self.index])
        self.rect = self.image.get_rect()
        self.rect.center = coordinates
        self.step = 0

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.step += 1

        if self.step % 3 == 0:
            self.index += 1
            self.image = pygame.image.load(self.images[self.index])

            if self.index >= len(self.images) - 1:
                self.kill()

            self.step = 0