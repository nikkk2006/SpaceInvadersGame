import pygame
import sys
from sprites.space import Space
from sprites.spaceship import Spaceship
from sprites.alien import Alien
from sprites.explosion import Explosion
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
    explosions = pygame.sprite.Group()

    while RUNNING:
        # Частота обновления экрана
        clock.tick(FPS)

        # События
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for alien in aliens.sprites():
            if pygame.sprite.spritecollide(alien, player_bullets, True, pygame.sprite.collide_mask):
                alien.kill()
                explosion = Explosion((0, 0))
                explosion.add(explosions)

                # добавление звука взрыва
                explosion_sound = pygame.mixer.Sound(r"assets\sounds\explosion.wav")
                explosion_sound.set_volume(0.3)
                explosion_sound.play()

        # Рендеринг
        screen.fill(BLACK)
        space.draw(screen)

        for bullet in player_bullets:
            bullet.draw(screen)

        spaceship.draw(screen)

        for alien in aliens:
            alien.draw(screen)

        for explosion in explosions:
            explosion.draw(screen)

        # Обновление спрайтов
        space.update()
        player_bullets.update()
        spaceship.update()
        aliens.update()
        explosions.update()

        # Обновление экрана
        pygame.display.update()


if __name__ == '__main__':
    main()