"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)



pygame.init()




# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Cat cards")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



wiz_list = ["WIZ.png", "WIZ2.png"]
foe_list=["foe.png","foe2.png"]
class character():
	def __init__(self,image):
		#super()._init_()
		#self.image=pygame.surface([width,height])
		self.image=pygame.image.load (image)
		self.rect=self.image.get_rect()
		# self.width=width
		# self.height=height
		# self.rect.x=X
		# self.rect.y=Y
	def draw(self, image,X,Y):
		self.image=pygame.image.load (image)
		self.rect=self.image.get_rect()
		self.rect.x=X
		self.rect.y=Y
		# self.draw.rect(screen, BLACK, [self.x,self.y, self.width, self.height], 2)
		screen.blit(self.image,self.rect)

cat= character(wiz_list[0])
foe= character(foe_list[0])
count =1

# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True


	# --- Game logic should go here

	# --- Screen-clearing code goes here

	# Here, we clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.

	# If you want a background image, replace this clear with blit'ing the
	# background image.
	screen.fill(WHITE)
	#
	if count < 30:
		cat.image = wiz_list[1]
		foe.image= foe_list[1]
		count +=1
	elif count < 60:
		cat.image = wiz_list[0]
		foe.image= foe_list[0]
		count += 1
	if count == 59:
		count = 1

	# --- Drawing code should go here

	pygame.draw.line(screen,BLACK,[0,SCREEN_HEIGHT/2],[900,SCREEN_HEIGHT/2],1)

	cat.draw(cat.image,-50,60)
	foe.draw(foe.image,500,50)

	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
