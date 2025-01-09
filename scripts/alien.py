import pygame

from pygame.sprite import Sprite
from pathlib import *


class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        img_path = Path.cwd().parent / "assets" / "images" / "alien.png"
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(
            self.image, (ai_game.screen.get_width() / 15, ai_game.screen.get_height() / 15))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
