import pygame
import random
#import fishFunctions

screen = pygame.display.set_mode((800, 600))
class fish():
	"""contains fish and their associated variables"""
	def __init__(self):
		self.xpos = random.randrange(100, 700 - 30)
		self.ypos = random.randrange(200, 700)
		self.xVel = random.randrange(-4,4)
		self.yVel = random.randrange(-4,4)
		self.color = [
			random.randrange(0, 100),
			random.randrange(100, 255),
			random.randrange(50, 200)
		]  # generates random color
		self.isDead = False
		self.onHook = False
		self.direction = 1
		self.ticker = random.randrange(0,100)

	def movement(self):  
		self.ticker+=1
		if self.ticker > 200:
			self.xVel = random.randrange(-3,2)
			self.yVel = random.randrange(-3,2)
			self.ticker = 0

		self.xpos += self.xVel

		self.ypos += self.yVel
		if self.xVel < 0:
			self.direction = 0
		else:
			self.direction = 1

	def draw(self):

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

	def collision(self):
		if self.xpos > 800 - 30 or self.xpos < 0:
			self.xVel *= -1
		if self.ypos < 100 or self.ypos > 600 - 20:
			self.yVel *= -1
		if self.ypos < 90:
			self.ypos = 130
		if self.ypos > 590:
			self.ypos = 560
		if self.xpos < 0:
			self.xpos = 20
		if self.xpos > 800:
			self.xpos = 760

class fisherman():
	def __init__(self):
		self.xpos = 50
		self.ypos = 50
		self.xVel = 0
		self.stringLength = 20
	def draw(self):
		pygame.draw.circle(screen, (230,230,50), (self.xpos + 60,self.ypos), 20)
		pygame.draw.ellipse(screen, (0xC6,0x86,0x42), (self.xpos+50, self.ypos-30, 20,20),)
		pygame.draw.rect(screen, (150,40,40), (self.xpos,self.ypos,70,30))
		pygame.draw.circle(screen, (0,0,0), (self.xpos + 65, self.ypos -22), 2)
		pygame.draw.circle(screen, (0,0,0), (self.xpos + 60, self.ypos -22), 2)
		pygame.draw.ellipse(screen, (230,230,50), (self.xpos+50, self.ypos-35, 20,10))
		pygame.draw.polygon(screen, (150,40,40), ((self.xpos,self.ypos), (self.xpos,self.ypos+30),(self.xpos-15,self.ypos)))
		pygame.draw.polygon(screen, (150,40,40), ((self.xpos+70,self.ypos), (self.xpos+70,self.ypos+30),(self.xpos+85,self.ypos)))
		
	def movement(self):
		keypressed = False
		self.xpos += self.xVel

		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]:
			self.xVel = -2
			keypressed = True
		if keys[pygame.K_d]:
			self.xVel = 2
			keypressed = True
		if keypressed == False:
			self.xVel = 0
		
		
