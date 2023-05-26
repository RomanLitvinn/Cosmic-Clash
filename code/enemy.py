import pygame
from random import choice, uniform
from settings import raw_small_enemy, raw_normal_enemy, raw_big_enemy


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen, ship_type="normal"):
        super().__init__()

        # ship settings
        self.screen = screen

        if ship_type == "small":
            image = pygame.transform.scale(raw_small_enemy, (int(self.screen.get_width() * 0.1), int(self.screen.get_height() * 0.07))).convert_alpha()
            self.basic_speed = self.screen.get_height() * 0.01
        elif ship_type == "normal":
            image = pygame.transform.scale(raw_normal_enemy, (int(self.screen.get_width() * 0.125), int(self.screen.get_height() * 0.1))).convert_alpha()
            self.basic_speed = self.screen.get_height() * 0.006
        elif ship_type == "big":
            image = pygame.transform.scale(raw_big_enemy, (int(self.screen.get_width() * 0.135), int(self.screen.get_height() * 0.135))).convert_alpha()
            self.basic_speed = self.screen.get_height() * 0.005

        self.image = image
        self.rect = self.image.get_rect(center=(400, 100))

        self.speed = self.basic_speed
        self.direction = pygame.math.Vector2(choice([-1, 1]), choice([-1, 1]))

    def movement(self):
        self.rect.x += self.speed*self.direction.x
        self.rect.y += self.speed * self.direction.y

        if self.rect.top <= 0:
            self.direction.y = 1
        if self.rect.bottom >= self.screen.get_height() / 2.5:
            self.direction.y = -1

        if self.rect.left <= 0:
            self.direction.x = 1
            self.speed = uniform(self.basic_speed * 0.8, self.basic_speed * 1.8)
        if self.rect.right >= self.screen.get_width():
            self.direction.x = -1
            self.speed = uniform(self.basic_speed * 0.8, self.basic_speed * 1.8)

    def update(self):
        self.movement()
