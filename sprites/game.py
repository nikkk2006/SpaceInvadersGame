import pygame


class Game(pygame.sprite.Sprite):
    def __init__(self, end_game):
        super().__init__()
        surface = pygame.display.get_surface()

        # работа со шрифтом

        self.font = pygame.font.Font(r'assets\fonts\gamefont.ttf', 20)
        self.image = self.font.render(end_game, True, "white")
        self.rect = self.image.get_rect()
        self.rect.center = (surface.get_width() // 2, surface.get_height() // 2)

    def draw(self, surface):
        surface.blit(self.image, self.rect)