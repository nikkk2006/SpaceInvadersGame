import pygame


class Space(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.display.get_surface()

        self.image = pygame.image.load(r"assets\images\space.png")
        self.rect = self.image.get_rect()

        self.image_1 = pygame.image.load(r"assets\images\space.png")
        self.rect_1 = self.image.get_rect()
        self.rect_1.bottom = self.rect.top

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.image_1, self.rect_1)

    def update(self):
        self.rect.y += 1
        self.rect_1.y += 1

        # условие выхода за пределы экрана
        if self.rect.top >= self.surface.get_height():
            self.rect.bottom = self.rect_1.top
        elif self.rect_1.top >= self.surface.get_height():
            self.rect_1.bottom = self.rect.top

