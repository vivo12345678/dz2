import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 32)

class Player:
    alive = True
    SPEED_PER_SEC = 200
    frame = 0
    def __init__(self, pos):
        self.pos = pygame.Vector2(pos)
        self.speed = int(self.SPEED_PER_SEC)

        a = pygame.image.load(".\pipo-enemy047a.png")
        b = pygame.image.load(".\pipo-enemy047a2.png")
        self.anim = [a, b]

        self.animation_timer = 0
        self.anim_frame_speed = 0.5

    def move(self, keys, dt):
        if keys[pygame.K_LEFT]:
            self.pos.x -= 400 * dt
        if keys[pygame.K_RIGHT]:
            self.pos.x += 400 * dt
        if keys[pygame.K_UP]:
            self.pos.y -= 400 * dt
        if keys[pygame.K_DOWN]:
            self.pos.y += 400 * dt

    def draw_me(self, screen, dt):
        frame = self.get_animation_frame(dt)

        blit_pos = (
            self.pos.x - frame.get_width() // 2,
            self.pos.y - frame.get_height() // 2
        )

        screen.blit(frame, blit_pos)

    def get_animation_frame(self, dt):
        self.animation_timer += dt

        if self.animation_timer >= self.anim_frame_speed:
            self.frame += 1

            if self.frame == len(self.anim):
                self.frame = 0

            self.animation_timer = 0

        return self.anim[self.frame]

class Enemy:
    def __init__(self, image):
        self.image = pygame.transform.scale(image, (100, 40))
        self.respawn()

    def respawn(self):
        self.pos = pygame.Vector2(random.randint(1, 800),random.randint(1, 600))

    def draw(self, screen):
        screen.blit(self.image, self.pos)


class MovingSquare:
    def __init__(self):
        self.pos = pygame.Vector2(random.randint(1, 800),random.randint(1, 600))
        self.speed = pygame.Vector2(random.choice([-1, 1]) * 200,random.choice([-1, 1]) * 200)
        self.size = 40

    def update(self, dt):
        self.pos += self.speed * dt

        if self.pos.x <= 0 or self.pos.x >= 800 - self.size:
            self.speed.x *= -1
        if self.pos.y <= 0 or self.pos.y >= 600 - self.size:
            self.speed.y *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0),(self.pos.x, self.pos.y, self.size, self.size))


player_img = pygame.image.load('./f.png')
enemy_img = pygame.image.load('./d.png')

player = Player((400, 500))
enemy = Enemy(enemy_img)
square = MovingSquare()

coin = 0
running = True


while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys, dt)

    square.update(dt)

    if player.pos.distance_to(enemy.pos) < 40:
        enemy.respawn()
        coin += 1

    if player.pos.distance_to(square.pos) < 40:
        running = False
    if coin>= 10:
        running= False
    text_surface = font.render(f'10/{coin}', True, (255, 255, 255))

    screen.fill((0, 0, 0))
    player.draw_me(screen,dt)
    enemy.draw(screen)
    square.draw(screen)
    screen.blit(text_surface, (50, 100))

    pygame.display.flip()