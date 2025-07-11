# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initialzing
pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 3
SCORE = 0
COIN_SCORE = 0
SPEEDING_N = 3
ENEMY_SPEED = 2
SCORE_BEFORE_SPEEDING = COIN_SCORE

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.sound = pygame.mixer.Sound("coin.mp3")
        self.weight = 1

    def move(self):
        self.rect.move_ip(0, SPEED // 2)
        if self.rect.bottom > 600:
            self.respawn()

    def respawn(self):
        # self.rect.top = 0
        self.weight = random.randint(1, 3)
        self.rect.center = (
            random.randint(40, SCREEN_WIDTH - 40),
            random.randint(-200, -50),
        )

    def collect(self):
        self.sound.play()
        global COIN_SCORE
        global SCORE_BEFORE_SPEEDING
        COIN_SCORE += self.weight
        if COIN_SCORE - SCORE_BEFORE_SPEEDING >= SPEEDING_N:
            global ENEMY_SPEED
            ENEMY_SPEED += (
                COIN_SCORE - SCORE_BEFORE_SPEEDING
            ) // SPEEDING_N  # increase enemy speed by coin difference
            SCORE_BEFORE_SPEEDING = COIN_SCORE
        self.respawn()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, (SPEED + ENEMY_SPEED) // 2)
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
coins = pygame.sprite.Group()
coins.add(C1)

# Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

running = True

# Game Loop
while running:

    # Cycles through all events occuring
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            running = False

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    coin_scores = font_small.render(str(COIN_SCORE), True, BLACK)
    coin_scores_rect = coin_scores.get_rect()
    coin_scores_rect.topright = (SCREEN_WIDTH - 10, 10)
    DISPLAYSURF.blit(coin_scores, coin_scores_rect)

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("crash.wav").play()
        time.sleep(1)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        running = False

    # To be run if collision occurs between Player and Coins
    if pygame.sprite.spritecollideany(P1, coins):
        for coin in coins:
            coin.collect()

    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.quit()
sys.exit()
