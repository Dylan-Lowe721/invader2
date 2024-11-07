import objects.images
import pygame
import manager  
class movable(objects.images.still):
    def __init__(self, x, y,width,height,image_to_use,speed):
        super().__init__(x, y,width,height,image_to_use)
        self.speed = speed
        
    def key_press(self):
        key_input = pygame.key.get_pressed()
        self.newX = (key_input[pygame.K_LEFT] * -self.speed) + (key_input[pygame.K_RIGHT] * self.speed)
        self.newY = (key_input[pygame.K_UP] * -self.speed) + (key_input[pygame.K_DOWN] * self.speed)
        
        self.rect.x += self.newX
        
        
    def back(self):
        self.rect.x -= self.newX
        self.rect.y -= self.newY
        

        
        

        
    
        
        
    
        
    
        
                