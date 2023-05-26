import pygame
from settings import raw_player, raw_laser


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()

        self.screen = screen

        # player
        self.image = pygame.transform.scale(raw_player, (screen.get_width()*0.125, screen.get_height()*0.1)).convert_alpha()
        self.rect = self.image.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))

        # laser
        self.lasers = pygame.sprite.Group()
        self.shooting = False

    def move(self):
        self.rect.center = pygame.mouse.get_pos()
        if self.rect.bottom >= self.screen.get_height():
            self.rect.bottom = self.screen.get_height()
        if self.rect.top <= self.screen.get_height()/2.5:
            self.rect.top = self.screen.get_height()/2.5

        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.screen.get_width():
            self.rect.right = self.screen.get_width()

    def shoot(self):
        if pygame.mouse.get_pressed()[0] and not self.shooting:
            self.shooting = True

            laser_width = self.screen.get_width() * 0.01125
            laser_height = self.screen.get_height() * 0.0675
            laser_speed = self.screen.get_height() * 0.03
            self.lasers.add(Laser((laser_width, laser_height), self.rect.center, laser_speed))
        if not pygame.mouse.get_pressed()[0]:
            self.shooting = False
        self.lasers.update()


class Laser(pygame.sprite.Sprite):
    def __init__(self, size, pos, speed):
        super().__init__()

        self.image = pygame.transform.scale(raw_laser, size).convert_alpha()
        self.rect = self.image.get_rect(center=pos)

        self.speed = speed

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom <= 0:
            self.kill()
