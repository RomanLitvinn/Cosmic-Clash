import pygame
import sys
from player import Player
from enemy import Enemy
from settings import raw_bg


class Game:
    def __init__(self, surf):

        # game setup
        self.display_surface = surf
        self.back_ground = pygame.transform.scale(raw_bg, (self.display_surface.get_width(), self.display_surface.get_height())).convert()

        pygame.mouse.set_visible(False)

        # player
        self.player = pygame.sprite.GroupSingle(Player(self.display_surface))

        # enemies
        self.enemies = pygame.sprite.Group()
        self.enemies.add(Enemy(self.display_surface, "normal"))

    def controls(self):

        self.player.sprite.move()

        self.player.sprite.shoot()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update(self):

        # screen
        self.display_surface.blit(self.back_ground, (0, 0))

        # player
        self.player.sprite.lasers.draw(self.display_surface)

        self.controls()
        self.player.draw(self.display_surface)

        # enemies
        self.enemies.draw(self.display_surface)
        self.enemies.update()

        pygame.sprite.groupcollide(self.player.sprite.lasers, self.enemies, True, True)  # Check for laser and enemy collision
