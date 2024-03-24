import pygame
import random
from consts import consts

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, width):
        super().__init__()
        self.image = pygame.Surface([width, consts.OBSTACLE_HEIGHT])
        self.image.fill(consts.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = consts.SCREEN_HEIGHT - consts.OBSTACLE_HEIGHT - 10
        self.speed = self.getObstacleSpeed()

    def getObstacleSpeed(self):
        return random.randrange(consts.OBSTACLE_SPEED-3, consts.OBSTACLE_SPEED+3)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < -self.rect.width:
            self.kill()
