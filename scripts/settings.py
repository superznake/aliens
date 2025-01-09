import pygame


class Settings:
    def __init__(self):

        # screen
        self.fps = 60
        self.fullscreen = False
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 127, 255)

        # controls
        self.right = {pygame.K_RIGHT, pygame.K_d}
        self.left = {pygame.K_LEFT, pygame.K_a}

        # ship
        self.ship_speed = 5

        # bullet
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 3
