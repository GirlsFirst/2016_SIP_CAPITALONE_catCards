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


possible_ball_colors = [BLACK, WHITE, GREEN, RED, BLUE, GREY]



# x_speed = random.randint(-10, 10)
# y_speed = random.randint(-10, 10)

# x_location = int(100)
# y_location = int(400)


# ball_size = random.randint(10, 30)
image_list = ["WIZ.png", "WIZ2.png"]
class character():
    def __init__(self,image,width,height,X,Y):
        #super()._init_()
        #self.image=pygame.surface([width,height])
        self.image=pygame.image.load (image)
        self.rect=self.image.get_rect()
        self.width=width
        self.height=height
        self.x=X
        self.y=Y
    def draw(self):
        # self.draw.rect(screen, BLACK, [self.x,self.y, self.width, self.height], 2)
        screen.blit(self.image,self.rect)
        
cat= character(image_list[1],120,140,70,100)
#foe= character("wiz2.0.png",120,140,600,100)
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
    if count == 1:
        cat.image = image_list[1]
        count =2
    elif count == 2:
        cat.image = image_list[0]
        count = 1
    # --- Drawing code should go here

    pygame.draw.line(screen,BLACK,[0,SCREEN_HEIGHT/2],[900,SCREEN_HEIGHT/2],1)
    # ball_color = BLUE # This is outside because of variable scoping.


    # pygame.draw.circle(screen, ball_color, [x_location, y_location], ball_size)


    # if x_location >= SCREEN_WIDTH - ball_size or x_location < ball_size:
        # x_speed = x_speed * -1

    # if y_location >= SCREEN_HEIGHT - ball_size or y_location < ball_size:
        # y_speed = y_speed * -1


    # x_location += x_speed
    # y_location += y_speed

    cat.draw()
    #foe.draw()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
