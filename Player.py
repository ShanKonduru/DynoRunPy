import pygame

from consts import consts
from Obstacle import Obstacle

# Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([consts.PLAYER_WIDTH, consts.PLAYER_HEIGHT])
        self.image.fill(consts.RED)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = consts.SCREEN_HEIGHT - consts.PLAYER_HEIGHT - 10
        self.y_velocity = 0
    
    def jump(self):
        if self.rect.y == consts.SCREEN_HEIGHT - consts.PLAYER_HEIGHT - 10:
            self.y_velocity = -10

    def update(self):
        self.y_velocity += 0.5
        self.rect.y += self.y_velocity

        if self.rect.y > consts.SCREEN_HEIGHT - consts.PLAYER_HEIGHT - 10:
            self.rect.y = consts.SCREEN_HEIGHT - consts.PLAYER_HEIGHT - 10
            self.y_velocity = 0
