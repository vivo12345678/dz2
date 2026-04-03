import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
enemy = pygame.Vector2(random.randint(1, 800), random.randint(1, 600))
player = pygame.Vector2(400, 500)
enemy_square = pygame.Vector2(random.randint(1, 800), random.randint(1, 600))
square_speed = pygame.Vector2(random.choice([-1, 1]) * 200, random.choice([-1, 1]) * 200)
coin = 0
running = True
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= 400 * dt
    if keys[pygame.K_UP]: player.y -= 400 * dt
    if keys[pygame.K_RIGHT]: player.x += 400 * dt
    if keys[pygame.K_DOWN]: player.y += 400 * dt
    if player.distance_to(enemy) < 40:
        enemy = pygame.Vector2(random.randint(1, 800), random.randint(1, 600))
        coin = coin+1
        print(coin)
    enemy_square += square_speed * dt

    if enemy_square.x <= 0 or enemy_square.x >= 780:
        square_speed.x *= -1
    if enemy_square.y <= 0 or enemy_square.y >= 580:
        square_speed.y *= -1

    if player.distance_to(enemy_square) < 40:
        running = False
#wefghj
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (0,200,0), player, 20)
    pygame.draw.circle(screen, (255,255,0), enemy, 20)
    pygame.draw.rect(screen, (255, 0, 0), (enemy_square.x, enemy_square.y, 30, 30))
    pygame.display.flip()
