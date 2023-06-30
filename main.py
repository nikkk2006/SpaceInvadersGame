import pygame
pygame.init()


def main():
    # Константы
    WIDTH = 600
    HEIGHT = 700
    FPS = 60
    RUNNING = True

    # Создание окна
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()

    # Спрайты

    while RUNNING:
        # Частота обновления экрана
        clock.tick(FPS)

        # События
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Рендеринг
        screen.fill((0, 0, 0))

        # Обновление спрайтов

        # Обновление экрана
        pygame.display.update()


if __name__ == '__main__':
    main()