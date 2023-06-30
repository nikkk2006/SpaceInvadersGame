import pygame
import sys
from sprites.space import Space
pygame.init()


def main():
    # Константы
    WIDTH = 600
    HEIGHT = 700
    FPS = 60
    RUNNING = True
    BLACK = (0, 0, 0)

    # Создание окна
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()

    # Спрайты
    space = Space()

    while RUNNING:
        # Частота обновления экрана
        clock.tick(FPS)

        # События
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Рендеринг
        screen.fill(BLACK)
        space.draw(screen)

        # Обновление спрайтов
        space.update()

        # Обновление экрана
        pygame.display.update()


if __name__ == '__main__':
    main()