import sys
import pygame

pygame.init()

width = 600
height = 600

surface = pygame.display.set_mode((width, height)) #surface
pygame.display.set_caption("Mover imagen")

#RGB
white = pygame.Color(255, 255, 255)
red = (134, 45, 83)

font = pygame.font.Font("freesansbold.ttf", 48)
image = pygame.image.load("Practice/images/medium_circle.png")
rect = image.get_rect()
rect.center = (width // 2, height // 2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    rect.center = pygame.mouse.get_pos() #Tupla -> (x,y)

    surface.fill(white)
    surface.blit(image, rect)

    pygame.display.update()