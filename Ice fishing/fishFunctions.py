
import pygame
import time

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fish")


#print(pygame.font.get_fonts()) #uncomment this to see what font options you have

def PlayIntro():
    font = pygame.font.SysFont('freesans.ttf', 38) #pick the font

    #this fades the first sentence from white to black
    for x in range(255):
        screen.fill((255, 255, 255))
        text = font.render('Once there was a young man', True, (255-x,255-x,255-x), (255,255,255))
        screen.blit(text, (200,200))
        pygame.display.flip()
        time.sleep(20 / 1000)
    #this fades the second sentence from white to black
    for x in range(255):
        screen.fill((255, 255, 255))
        text = font.render('Once there was a young man', True, (0,0,0), (255,255,255))
        text2 = font.render('that wanted to go ice fishing...', True, (255-x,255-x,255-x), (255,255,255))
        screen.blit(text, (200,200))
        screen.blit(text2, (250,300))
        pygame.display.flip()
        time.sleep(20 / 1000)
    #this fades both from black to white
    for x in range(255):
        screen.fill((255, 255, 255))
        text = font.render('Once there was a young man', True, (0+x,0+x,0+x), (255,255,255))
        text2 = font.render('that wanted to go ice fishing...', True, (0+x,0+x,0+x), (255,255,255))
        screen.blit(text, (200,200))
        screen.blit(text2, (250,300))
        pygame.display.flip()
        time.sleep(10 / 1000)
    for x in range(255):
        screen.fill((255-x, 255-x, 255))
        pygame.display.flip()
        time.sleep(10/1000)