import pygame
import sys
from sprites.space import Space
from sprites.spaceship import Spaceship
from sprites.alien import generateAliens
from sprites.explosion import Explosion
from sprites.health import HealthBar
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
    spaceships = pygame.sprite.GroupSingle()
    spaceships.add(spaceship)
    health_bar = HealthBar(spaceship.health)
    aliens = pygame.sprite.Group()
    alien_bullets = pygame.sprite.Group()
    generateAliens(aliens, alien_bullets)
    explosions = pygame.sprite.Group()

    while RUNNING:
        # Частота обновления экрана
        clock.tick(FPS)

        # События
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # коллизия пришельцев с пулями игрока
        for alien in aliens.sprites():
            if pygame.sprite.spritecollide(alien, player_bullets, True, pygame.sprite.collide_mask):
                alien.kill()
                explosion = Explosion(alien.rect.center)
                explosions.add(explosion)

                # добавление звука взрыва
                explosion_sound = pygame.mixer.Sound(r"assets\sounds\explosion.wav")
                explosion_sound.set_volume(0.3)
                explosion_sound.play()

        # коллизия игрока и пуль пришельцев
        for spaceship in spaceships.sprites():
            if pygame.sprite.spritecollide(spaceship, alien_bullets, True, pygame.sprite.collide_mask):
                spaceship.health -= 1
                health_bar.hearts.pop()
                explosion = Explosion(spaceship.rect.center)
                explosions.add(explosion)

                if spaceship.health < 1:

                    # добавление звука взрыва
                    explosion_sound = pygame.mixer.Sound(r"assets\sounds\explosion.wav")
                    explosion_sound.set_volume(0.3)
                    explosion_sound.play()
                    spaceship.kill()
                else:
                    damage_sound = pygame.mixer.Sound(r"assets\sounds\damage.wav")
                    damage_sound.play()


        # Рендеринг
        screen.fill(BLACK)
        space.draw(screen)

        for bullet in player_bullets:
            bullet.draw(screen)

        for spaceship in spaceships:
            spaceship.draw(screen)

        health_bar.draw(screen)

        for alien in aliens:
            alien.draw(screen)

        for alien_bullet in alien_bullets:
            alien_bullet.draw(screen)

        for explosion in explosions:
            explosion.draw(screen)

        # Обновление спрайтов
        space.update()
        player_bullets.update()
        spaceships.update()
        aliens.update()
        alien_bullets.update()
        explosions.update()

        # Обновление экрана
        pygame.display.update()


if __name__ == '__main__':
    main()