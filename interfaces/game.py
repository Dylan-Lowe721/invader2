#Name:
#Date:
#Basic PyGame Setup Code
import pygame,sys
import math
import random
import pygame
import manager
from objects.user import Ship

pygame.init()

# Game Setup
fps = 60
fpsClock = pygame.time.Clock()
window = manager.window
WINDOW_WIDTH = manager.WINDOW_WIDTH
WINDOW_HEIGHT = manager.WINDOW_HEIGHT

#Setup of Starting objects
#creating window


#changing name and icon
pygame.display.set_caption("void incursion")
icon = pygame.image.load('images/carrot.jpg')
pygame.display.set_icon(icon)

#creating objects and such
background = pygame.image.load('images/bg.png')
guy = Ship(600, 400, 2)


def output(window):
    def display():
        window.fill((255,255,255)) #White background
        #object_draw_name=pygame.draw.rect(window,(COLOR_CODE),(locX,locY,sizeX,sizeY))
    
    
    # Player


# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('images/zellyasko.jpg'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load('images/laser.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.SysFont('Consolas', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.SysFont('Consolas', 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    window.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    window.blit(over_text, (200, 250))


def enemy(x, y, i):
    window.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    window.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#Game Loop
run = True
while run:
    # Background Image
    window.blit(background, (0, 0))
    guy.draw(window)    
    
    for event in pygame.event.get():
        #ship.draw_player()
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
            
        #moving player left and right 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # Get the current x cordinate of the spaceship
                    bulletX = guy.playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

   

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    show_score(textX, testY)
    pygame.display.update()
    for event in pygame.event.get():
        # if user  QUIT then the screen will close
            if event.type == pygame.QUIT:
                
    
        
                pygame.display.update() #update the display
    fpsClock.tick(fps) #speed of redraw










