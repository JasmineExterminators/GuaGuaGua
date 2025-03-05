import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

duckImg = pygame.image.load("assets/duck.png")
duckImg = pygame.transform.scale(duckImg, (80, 80))

#GLOBAL VARS
MOVING_SPEED = 100
PIPE_WIDTH = 50
PIPE_TIME = 2
TALLEST_PIPE = int(screen.get_height() * (3/4))

# this is a 2D vector that reps the player's position
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


class Pipe:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def move(self):
        self.rect.x -= MOVING_SPEED * dt

    def draw(self, surface):
        pygame.draw.rect(surface, "green", self.rect)

pipesList = []
pipesListMirror = []
pipeTimer = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    screen.blit(duckImg, (player_pos.x - duckImg.get_width() / 2, player_pos.y - duckImg.get_height() / 2))

    for i in range(len(pipesList)):
        pipesList[i].move()
        pipesList[i].draw(screen)
        pipesListMirror[i].move()
        pipesListMirror[i].draw(screen)

    pipeTimer += dt
    if pipeTimer >= PIPE_TIME:
        pipeTimer = 0
        pipeHeight = random.randint(0, TALLEST_PIPE)
        newPipe = Pipe(screen.get_width(), screen.get_height() - pipeHeight, PIPE_WIDTH, pipeHeight)
        pipesList.append(newPipe)
        mirrorNewPipe = Pipe(screen.get_width(), 0, PIPE_WIDTH, screen.get_height() - pipeHeight - 200)
        pipesListMirror.append(mirrorNewPipe)
    

    # KEYS ======================================
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()