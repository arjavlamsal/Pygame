import pygame
from sys import exit # To close the game efficiently

pygame.init() # Initializing pygame to lead all its components into the program

width = 800
height = 400
screen = pygame.display.set_mode((width,height)) # Setting screen resolution (Should pass a tuple as resolution)

pygame.display.set_caption('Runner') # Title of the game on window

clock = pygame.time.Clock() # This is for the framerate (Don't want too much or too less both cause problems)

test_font = pygame.font.Font("font/Pixeltype.ttf", 50) #Adding font(None or location of ttf file), # pygame.font.Font(font_type, font_size)

## For displaying blocks
# test_surface = pygame.Surface((100,200)) # Creating a regular surface.
# test_surface.fill('Red') # coloring the surface with .fill('color_name')
## Any type of graphical import is going to be a new surface.

# For displaying images
sky_surface = pygame.image.load("graphics/Sky.png")
ground_surface = pygame.image.load("graphics/Ground.png")
text_surface = test_font.render("My game", False, "Black")
snail_surface = pygame.image.load("graphics/snail/snail1.png")

snail_1_position = 600

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Polar opposite of 'pygame.init()'; uninitializes everything.
            exit() # to exit program as an error occurs as pygame.display,update() still has to run in the main loop.
    
    # Draw all our elements (Draws in order this first and the image after this on top of that)
    """ surface.blit(surface_to_place, position_tuple)| 
    block image transfer (blit)-(fancy way of saying putting one surface onto another surface)
    position(0,0 means 0 from top, 0 from left) """
    
    screen.blit(sky_surface,(0,0))  
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    screen.blit(snail_surface,(snail_1_position,250))

    snail_1_position -= 4 # Moving the snail to the left of the screen


    
    
    # Update everything
    pygame.display.update() # Updates pygame.display.set_mode((width,height)) so the window keeps on running
    clock.tick(60) # This while loop will run 60 times per second for 60 refreshes of elements on screen = 60fps


