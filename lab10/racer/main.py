# Imports
import pygame, sys
from pygame.locals import *
import random, time
from db import create_tables, get_or_create_user, save_state

pygame.init()
FPS = 60
clock = pygame.time.Clock()

# screen
W, H = 400, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Game")

# fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, (0, 0, 0))

# assets
background = pygame.image.load("AnimatedStreet.png")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

LEVELS = {
    1: {"speed": 3},
    2: {"speed": 4},
    3: {"speed": 5},
}


# ---------- Sprite Classes ----------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect(center=(160, 520))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[K_RIGHT] and self.rect.right < W:
            self.rect.x += 5


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.respawn()

    def respawn(self):
        self.rect.center = (random.randint(40, W - 40), 0)

    def move(self, speed):
        self.rect.y += speed
        if self.rect.top > H:
            self.rect.y = 0
            global SCORE
            SCORE += 1


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.rect = self.image.get_rect()
        self.sound = pygame.mixer.Sound("coin.mp3")
        self.weight = 1
        self.respawn()

    def respawn(self):
        self.weight = random.randint(1, 3)
        self.rect.center = (random.randint(40, W - 40), random.randint(-200, -50))

    def move(self, speed):
        self.rect.y += speed
        if self.rect.top > H:
            self.respawn()

    def collect(self):
        self.sound.play()
        global COIN_SCORE, SCORE_BEFORE_SPEEDING, ENEMY_SPEED
        COIN_SCORE += self.weight
        if COIN_SCORE - SCORE_BEFORE_SPEEDING >= SPEEDING_N:
            ENEMY_SPEED += (COIN_SCORE - SCORE_BEFORE_SPEEDING) // SPEEDING_N
            SCORE_BEFORE_SPEEDING = COIN_SCORE
        self.respawn()


# ---------- Main ----------


def main():
    # DB init and user login
    create_tables()
    username = input("Enter your username: ").strip()
    user_id, level = get_or_create_user(username)
    print(f"Welcome {username}, starting at level {level}")
    params = LEVELS.get(level, LEVELS[1])
    base_speed = params["speed"]

    global SCORE, COIN_SCORE, SPEEDING_N, ENEMY_SPEED, SCORE_BEFORE_SPEEDING
    SCORE = 0
    COIN_SCORE = 0
    SPEED = base_speed
    SPEEDING_N = 3
    ENEMY_SPEED = 2
    SCORE_BEFORE_SPEEDING = 0

    # create sprites
    player = Player()
    enemies = pygame.sprite.Group(Enemy())
    coins = pygame.sprite.Group(Coin())
    all_sprites = pygame.sprite.Group(player, *enemies, *coins)

    paused = False

    INC_SPEED = pygame.USEREVENT + 1
    pygame.time.set_timer(INC_SPEED, 1000)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == INC_SPEED and not paused:
                SPEED += 0.5
            if event.type == KEYDOWN:
                if event.key == K_p:
                    paused = not paused
                if paused and event.key == K_s:
                    # save state
                    state = {
                        "player_pos": [player.rect.x, player.rect.y],
                        "enemies": [[e.rect.x, e.rect.y] for e in enemies],
                        "coins": [[c.rect.x, c.rect.y, c.weight] for c in coins],
                    }
                    save_state(user_id, SCORE, COIN_SCORE, level, state)
                    print("Game saved.")

        if not paused:
            screen.blit(background, (0, 0))
            # move and draw
            for sprite in all_sprites:
                if isinstance(sprite, Enemy):
                    sprite.move((SPEED + ENEMY_SPEED) // 2)
                elif isinstance(sprite, Coin):
                    sprite.move(SPEED // 2)
                else:
                    sprite.move()
                screen.blit(sprite.image, sprite.rect)

            # collisions
            if pygame.sprite.spritecollideany(player, enemies):
                pygame.mixer.Sound("crash.wav").play()
                time.sleep(1)
                screen.fill(RED)
                screen.blit(game_over, (30, 250))
                pygame.display.update()
                time.sleep(2)
                running = False

            if pygame.sprite.spritecollideany(player, coins):
                for coin in coins:
                    if pygame.sprite.collide_rect(player, coin):
                        coin.collect()

            # HUD
            screen.blit(font_small.render(f"Score:{SCORE}", True, BLACK), (10, 10))
            cs = font_small.render(f"Coins:{COIN_SCORE}", True, BLACK)
            screen.blit(cs, cs.get_rect(topright=(W - 10, 10)))

        else:
            # paused overlay
            overlay = font_small.render(
                "Paused - press P to resume, S to save", True, BLACK
            )
            screen.blit(overlay, (20, H // 2))

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
