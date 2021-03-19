import pygame
import random
#import fishFunctions

screen = pygame.display.set_mode((800, 600))
class fish():
    """contains fish and their associated variables"""
    def __init__(self):
        self.xpos = random.randrange(0, 500)
        self.ypos = random.randrange(0, 500)
        self.xVel = 0
        self.yVel = 0
        self.color = [
            random.randrange(0, 100),
            random.randrange(100, 255),
            random.randrange(50, 200)
        ]  # generates random color
        self.isDead = False
        self.onHook = False
        self.direction = 1  #0 = left # 1 = right
        self.ticker = random.randrange(0,100)

    def movement(self):  # generates random numbers between -3 and 3
        self.xVel = random.randrange(-3, 4)
        self.xpos += self.xVel

        self.yVel = random.randrange(-3, 4)
        self.ypos += self.yVel
        if self.xVel > 0:
            self.direction = 0
        else:
            self.direction = 1

    def printinfo(self):
        #print("Current xpos: ", self.xpos)
        #print("Current ypos: ", self.ypos)
        #print("Current x velocity :", self.xVel)
        #print("Current y velocity :", self.yVel)
        #print("Current color is: ", end='')
        #for i in range(0, 3):
        #    print(self.color[i], " ", end='')

        pygame.draw.ellipse(screen, self.color, (self.xpos, self.ypos, 30, 20))
        if self.direction == 0:
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.xpos + 5, self.ypos + 5), 3)
            pygame.draw.polygon(screen, self.color,
                                ((self.xpos + 25, self.ypos + 10),
                                 (self.xpos + 30, self.ypos),
                                 (self.xpos + 30, self.ypos + 20)))
        elif self.direction == 1:
            pygame.draw.circle(screen, (0, 0, 0),
                               (self.xpos + 25, self.ypos + 5), 3)
            pygame.draw.polygon(screen, self.color,
                                ((self.xpos, self.ypos),
                                 (self.xpos, self.ypos + 20),
                                 (self.xpos + 5, self.ypos + 5)))
    def distance(self,foodx,foody):
        dist = math.sqrt((foodx-self.xpos)*(foodx-self.xpos)+(foody-self.ypos)*(foody-self.ypos))
        print(dist)

