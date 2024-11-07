import pygame 
from objects import laser
import manager
class Ship():
    def __init__(self,x,y,speed):
        super().__init__()
        image1 = pygame.image.load("images/carrot.jpg")
        image2 = pygame.transform.scale(image1, (60, 60)).convert_alpha()
        playerImg = image2
        self.playerX = x
        self.playerY = y
        self.speed = speed
        self.speed = 5
        
        def get_input(self):
            keys = pygame.key.get_pressed()

            if keys[pygame.K_RIGHT]:
                self.playerX += self.speed
            elif keys[pygame.K_LEFT]:
                self.playerX -= self.speed

            if keys[pygame.K_SPACE] and self.ready:
                self.shoot_laser()
                self.ready = False
                laser.laser_time = pygame.time.get_ticks()
               
        
        def draw(self, x, y):
            manager.window.blit(playerImg, (x, y))

        def update(self):
            playerX
            playerX += self.speed
            if playerX <= 0:
                playerX = 0
            elif playerX >= manager.WINDOW_WIDTH:
                playerX = manager.WINDOW_WIDTH