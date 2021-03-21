import pygame
import fishFunctions # imports second file
import fishClass

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fish")
clock = pygame.time.Clock()

#fishFunctions.PlayIntro()

fishbucket = list()

doExit = False

boat = fishClass.fisherman()

for i in range (25):
	fishbucket.append(fishClass.fish())

while not doExit: # GAME LOOOOOOOOOOOOOOOOOOP
	# PHYSICS #############################
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # checks for the x being clicked
			doExit = True # interesting cause you would need to modify the other file to close the game during the intro screen

	for i in range(len(fishbucket)):
		fishbucket[i].movement()
		fishbucket[i].collision()

	boat.movement()

	#RENDERRRRRRRRRRRRRRRRRRRRRRRRRRRRR
	screen.fill((0,0,255))
	pygame.draw.rect(screen, (0x89,0xe9,0xf0), (0,0,800,80))
	for i in range(len(fishbucket)):
		fishbucket[i].draw()
	boat.draw()
	pygame.display.flip()


pygame.quit()