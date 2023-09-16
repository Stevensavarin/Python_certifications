import sys
import pygame

pygame.init()

width = 500
height = 500

surface = pygame.display.set_mode((width, height)) #surface
pygame.display.set_caption("Teclado")

#RGB
white = pygame.Color(255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        print("Arriba")

    if pressed[pygame.K_a]:
        print("Izquierda")

    if pressed[pygame.K_s]:
        print("Abajo")

    if pressed[pygame.K_d]:
        print("Derecha")

    surface.fill(white)
    #surface.blit()
    pygame.display.update()