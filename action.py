
# ICS3U
# Assignment 2: Action
# <Jesse Guram>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
# Don't forget to import your class
import pygame, random
from ball import Ball
pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (237, 35, 35)
BLUE = (66, 134, 244)
YELLOW = (255, 242, 0)

speed = 1
colorList = [RED, WHITE, GREEN, BLUE, YELLOW]

# Set the screen size
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Animation")

all_balls_list = pygame.sprite.Group()

for i in range (10):
    myBall = Ball(colorList[random.randint(0, 4)], 20, 20, random.randint(20, 80)) 
    myBall.rect.x = random.randint(0, 400)
    myBall.rect.y = random.randint(0, 400)
    all_balls_list.add(myBall)





# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # --- Game logic goes here
    for ball in all_balls_list:
        ball.moveDown(speed)
        if ball.rect.y > SCREENHEIGHT:
            ball.changeSpeed(random.randint(50,100))
            ball.repaint(random.choice(colorList))
            ball.rect.y = -200
            ball.rect.x = random.randint(0, 400)


    
    # There should be none for a static image
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(BLUE)
    all_balls_list.draw(screen)

    # Queue different shapes and lines to be drawn
    # pygame.draw.rect(screen, RED, [55, 200, 100, 70], 0)
    # pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    # pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
