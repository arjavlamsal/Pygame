import pygame

pygame.init() # Initializing pygame to lead all its components into the program

width = 400
height = 800
screen = pygame.display.set_mode((width,height)) # Setting screen resolution (Should pass a tuple as resolution)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    # Draw all our elements
    # Update everything

    pygame.display.update() # Updates pygame.display.set_mode((width,height)) so the window keeps on running

