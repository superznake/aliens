import pygame

from pathlib import *


class Ship:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        img_path = Path.cwd().parent / "assets" / "images" / "ship.png"
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(
            self.image, (ai_game.screen.get_width()/15, ai_game.screen.get_height()/15))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.center_ship()

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)