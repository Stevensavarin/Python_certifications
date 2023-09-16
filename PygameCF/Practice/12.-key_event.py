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
    

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                message = "Izquierda"

            print(message)

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                message = "Derecha"

            print(message)

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                message = "Abajo"

            print(message)

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                message = "Arriba"

            print(message)
        
        if event.type == pygame.KEYUP:
            #print("Tecla liberada!")
            pass




    surface.fill(white)
    #surface.blit()
    pygame.display.update()