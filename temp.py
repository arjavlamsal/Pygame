import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()

text = pygame.font.Font(None,50)

block = pygame.Surface((200,200))
block.fill('red')

sky_surface = pygame.image.load("graphics/Sky.png")
ground_surface = pygame.image.load("graphics/Ground.png")
text_surface = text.render("HEHEEH", False, "Black")



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(block,(50,50))
    screen.blit(text_surface,(200,200))


    pygame.display.update()
    clock.tick(60)

    