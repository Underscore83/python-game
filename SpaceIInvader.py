import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("character.png")
pygame.display.set_icon(icon)

# Load background color
background_color = (0, 10, 30)


player_img = pygame.image.load("character.png")
player_x = 370
player_y = 480
player_x_change = 0

# Resize the image if it’s too big
player_img = pygame.transform.scale(player_img, (50, 50))

# Enemy
enemy_img = pygame.image.load("Flappy2.png")
enemy_x = random.randint(0, 735)
enemy_y = random.randint(50, 150)
enemy_x_change = 0.5
enemy_y_change = 10

# Resize the image if it’s too big
enemy_img = pygame.transform.scale(enemy_img, (50, 50))

# Bullet
# Ready - not visible | Fire - moving
bullet_img = pygame.image.load("ball.gif")
bullet_x = 0
bullet_y = 480
bullet_y_change = 2.5
bullet_state = "ready"

# Resize the image if it’s too big
bullet_img = pygame.transform.scale(bullet_img, (50, 50))

# Score
score = 0
font = pygame.font.SysFont("comicsansms", 24)


def show_score(x, y):
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (x, y))

# Functions
def player(x, y):
    screen.blit(player_img, (x, y))

def enemy(x, y):
    screen.blit(enemy_img, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 6, y + 5))

def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2)
    return distance < 27

# Game Loop
running = True
while running:
    screen.fill(background_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Keystroke check
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -1
            if event.key == pygame.K_RIGHT:
                player_x_change = 1
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player_x_change = 0
                
                
   # Player movement
    player_x += player_x_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # Enemy movement
    enemy_x += enemy_x_change
    if enemy_x <= 0:
        enemy_x_change = 0.5
        enemy_y += enemy_y_change
    elif enemy_x >= 736:
        enemy_x_change = -0.5
        enemy_y += enemy_y_change

    # Bullet movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    # Collision detection
    if is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
        bullet_y = 480
        bullet_state = "ready"
        score += 1
        enemy_x = random.randint(0, 735)
        enemy_y = random.randint(50, 150)

    # Draw everything
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    show_score(10, 10)

    pygame.display.update()

pygame.quit()
 