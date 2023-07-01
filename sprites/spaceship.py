import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, coordinates):
        super().__init__()

        self.image = pygame.image.load(r"assets\images\bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = coordinates

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.y -= 5

        # удаление пули если она вылетит за экран
        if self.rect.bottom <= 0:
            self.kill()

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, bullets):
        super().__init__()
        self.surface = pygame.display.get_surface()

        self.image = pygame.image.load(r"assets\images\spaceship.png")
        self.rect = self.image.get_rect()

        # расположение корабля
        self.rect.midbottom = self.surface.get_rect().midbottom
        self.rect.y = self.surface.get_height() // 1.2

        self.bullets = bullets
        self.cooldown = 500
        self.last_shot = pygame.time.get_ticks()


    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        key = pygame.key.get_pressed()

        if (key[pygame.K_LEFT] or key[pygame.K_a]) and self.rect.left >= 0:
            self.rect.x -= 5
        elif (key[pygame.K_RIGHT] or key[pygame.K_d]) and self.rect.right <= self.surface.get_width():
            self.rect.x += 5
        elif (key[pygame.K_UP] or key[pygame.K_w]) and self.rect.top >= 0:
            self.rect.y -= 5
        elif (key[pygame.K_DOWN] or key[pygame.K_s]) and self.rect.bottom <= self.surface.get_height():
            self.rect.y += 5

        now = pygame.time.get_ticks()
        if key[pygame.K_SPACE] and now - self.last_shot >= self.cooldown:
            bullet = Bullet(self.rect.midtop)
            self.bullets.add(bullet)
            self.last_shot = now

            # добавление звука выстрела
            shot_sound = pygame.mixer.Sound(r"assets\sounds\laser.wav")
            shot_sound.set_volume(0.3)
            shot_sound.play()