import sys
import pygame

pygame.init()

width = 500
height = 500

surface = pygame.display.set_mode((width, height)) #surface
pygame.display.set_caption("Time")

#RGB
red = pygame.Color(255, 0, 0) #0 - 255
white = pygame.Color(255, 255, 255)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    time = pygame.time.get_ticks() // 1000 #Milisegundos - // 1000 para segundos
    print(time)

    surface.fill(white)
    pygame.display.update()