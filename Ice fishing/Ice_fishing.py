import pygame
import fishFunctions # imports second file
from fishClass import fish

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fish")
clock = pygame.time.Clock()

#fishFunctions.PlayIntro()

doExit = False

fishie = fish()

while not doExit: # GAME LOOOOOOOOOOOOOOOOOOP
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # checks for the x being clicked
            doExit = True # interesting cause you would need to modify the other file to close the game during the intro screen


    #RENDERRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    screen.fill((0,0,255))
    fishie.printinfo()
    pygame.display.flip()


pygame.quit()