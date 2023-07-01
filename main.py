import pygame
import sys
from sprites.space import Space
from sprites.spaceship import Spaceship
from sprites.alien import Alien
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
    player_bullets = pygame.sprite.Group()
    spaceship = Spaceship(player_bullets)
    aliens = pygame.sprite.Group()
    alien = Alien()
    alien.add(aliens)

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

        for bullet in player_bullets:
            bullet.draw(screen)

        spaceship.draw(screen)

        for alien in aliens:
            alien.draw(screen)

        # Обновление спрайтов
        space.update()
        player_bullets.update()
        spaceship.update()
        aliens.update()

        # Обновление экрана
        pygame.display.update()


if __name__ == '__main__':
    main()