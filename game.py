
import pygame
import random
from consts import consts
from Obstacle import Obstacle
from Player import Player

# Initialize pygame
pygame.init()

# Initialize screen
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))
pygame.display.set_caption("Dinosaur Game")

# Clock
clock = pygame.time.Clock()

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

    screen.fill(consts.WHITE)

    # Spawn obstacles
    spawn_timer += 1
    if spawn_timer == spawn_interval:
        spawn_timer = 0
        obstacle_width = random.randint(20, 100)
        obstacle = Obstacle(consts.SCREEN_WIDTH, obstacle_width)
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
