import pygame


class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.display.get_surface()

        self.image = pygame.image.load(r"assets\images\spaceship.png")
        self.rect = self.image.get_rect()

        # расположение корабля
        self.rect.midbottom = self.surface.get_rect().midbottom
        self.rect.y = self.surface.get_height() // 1.2


    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        key = pygame.key.get_pressed()

        if (key[pygame.K_LEFT] or key[pygame.K_a]) and self.rect.left >= 0:
            self.rect.x -= 3
        elif (key[pygame.K_RIGHT] or key[pygame.K_d]) and self.rect.right <= self.surface.get_width():
            self.rect.x += 3