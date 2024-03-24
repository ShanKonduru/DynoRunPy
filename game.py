import pygame
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

# Player dimensions
PLAYER_WIDTH = 20
PLAYER_HEIGHT = 50
PLAYER_SPEED = 15

# Obstacle dimensions
OBSTACLE_WIDTH = 20
OBSTACLE_HEIGHT = 20
OBSTACLE_SPEED = 5

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dinosaur Game")

# Clock
clock = pygame.time.Clock()

# Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - PLAYER_HEIGHT - 10
        self.y_velocity = 0

    def jump(self):
        if self.rect.y == SCREEN_HEIGHT - PLAYER_HEIGHT - 10:
            self.y_velocity = -10

    def update(self):
        self.y_velocity += 0.5
        self.rect.y += self.y_velocity

        if self.rect.y > SCREEN_HEIGHT - PLAYER_HEIGHT - 10:
            self.rect.y = SCREEN_HEIGHT - PLAYER_HEIGHT - 10
            self.y_velocity = 0

# Obstacle
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, width):
        super().__init__()
        self.image = pygame.Surface([width, OBSTACLE_HEIGHT])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = SCREEN_HEIGHT - OBSTACLE_HEIGHT - 10
        self.speed = OBSTACLE_SPEED

    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < -self.rect.width:
            self.kill()

# Groups
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
running = True
spawn_timer = 0
spawn_interval = 60  # Spawn obstacle every second

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.jump()

    screen.fill(WHITE)

    # Spawn obstacles
    spawn_timer += 1
    if spawn_timer == spawn_interval:
        spawn_timer = 0
        obstacle_width = random.randint(20, 100)
        obstacle = Obstacle(SCREEN_WIDTH, obstacle_width)
        obstacles.add(obstacle)
        all_sprites.add(obstacle)

    # Check for collisions
    hits = pygame.sprite.spritecollide(player, obstacles, False)
    if hits:
        running = False

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
