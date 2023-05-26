import pygame

from game import *
from settings import *

# General
pygame.init()

# Window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("CosmicClash")


class GameManagement:
    def __init__(self, status="game"):

        # general data
        self.status = status
        self.game = Game(screen)

        self.FPS = 60

    def run(self):
        clock = pygame.time.Clock()
        while True:

            # checking the game status
            if self.status == "game":
                self.game.update()

            pygame.display.update()
            clock.tick(self.FPS)


game = GameManagement()

game.run()
