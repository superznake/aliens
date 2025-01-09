import pygame


class Settings:
    def __init__(self):

        # screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 127, 255)

        # controls
        self.right = {pygame.K_RIGHT, pygame.K_d}
        self.left = {pygame.K_LEFT, pygame.K_a}

        # ship
        self.ship_speed = 5
