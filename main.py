import pygame
from sys import exit # To close the game efficiently

pygame.init() # Initializing pygame to lead all its components into the program

width = 800
height = 400
screen = pygame.display.set_mode((width,height)) # Setting screen resolution (Should pass a tuple as resolution)
pygame.display

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Polar opposite of 'pygame.init()'; uninitializes everything.
            exit() # to exit program as an error occurs as pygame.display,update() still has to run in the main loop.
    
    # Draw all our elements
    # Update everything

    pygame.display.update() # Updates pygame.display.set_mode((width,height)) so the window keeps on running


