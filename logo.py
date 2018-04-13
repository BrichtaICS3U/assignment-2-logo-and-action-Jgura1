# ICS3U
# Assignment 2: Logo
# Jesse

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
pygame.init()
Font = pygame.font.SysFont('magnificent', 80)

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (192, 192, 192)
SILVER = (205, 208, 215)

# Set the screen size (please don't change this)
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Logo")

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
    # There should be none for a static image
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(BLACK)

    # Queue different shapes and lines to be drawn
    pygame.draw.ellipse(screen, SILVER, [50, 100, 300, 160], 18)
    pygame.draw.ellipse(screen, SILVER, [87, 104, 220, 70], 18)
    pygame.draw.ellipse(screen, SILVER, [167,125,60, 115],16)

    text = Font.render('TOYOTA', 1, (SILVER))
    screen.blit(text,(90, 295))

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
