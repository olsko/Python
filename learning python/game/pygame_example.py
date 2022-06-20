import pygame
import random
# Anticinating pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

# Changing title
pygame.display.set_caption("Space invaders")
# Backround image
backround = pygame.image.load("space_backround.png")

# Icon
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
# Player logic
player_img = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0
def player(x, y):
    screen.blit(player_img, (x, y))

#Enemy logic
enemy_img = pygame.image.load("enemy.png")
enemyX = random.randint(1, 800)
enemyY = 10
enemyX_change = 0.2
enemyY_change = 64
def enemy(x, y):
    screen.blit(enemy_img, (x, y))

#Bullet logic
bullet_img = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

# Game loop
running = True
while running:
    
    screen.fill((0, 0, 0))

    screen.blit(backround, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # If a keystroke is preesed check if right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE  :
                fire_bullet(playerX, bulletY)
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    if enemyX <= 0:
        enemyX_change = 0.2
        enemyY += enemyY_change
    if enemyX >= 736:
        enemyX_change = -0.2
        enemyY += enemyY_change
    #Bullet movement
    if bullet_state is "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change
    playerX += playerX_change
    enemyX += enemyX_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
    