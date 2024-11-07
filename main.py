#dylan lowe
#september 23rd 2024
#space invaders project



import pygame,sys
import manager
import interfaces.game

pygame.init()

#Setup of Starting objects
window = pygame.display.set_mode((manager.WINDOW_WIDTH,manager.WINDOW_HEIGHT), pygame.HWSURFACE)
pygame.display.set_caption("void incursion")

while True:
    interfaces.game.output(window)
    
    if manager.level == -1:
        pygame.quit()
        sys.exit()  