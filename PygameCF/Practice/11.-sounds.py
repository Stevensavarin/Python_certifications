import sys
import pygame

pygame.init()

width = 500
height = 500

surface = pygame.display.set_mode((width, height)) #surface
pygame.display.set_caption("Sonido de fondo")

#RGB
white = pygame.Color(255, 255, 255)

pygame.mixer.music.load("Practice/sounds/Haggstrom.mp3")
pygame.mixer.music.set_volume(1.0) # Float 0.0 - 1.0
pygame.mixer.music.play(2, 0.0) #time to start, minute to start
# la canción no para de sonar -1

#pygame.mixer.music.rewind() # Rebobinar
#pygame.mixer.music.pause() # Pausar
#pygame.mixer.music.stop() # Detener por completo
#pygame.mixer.music.fadeout(20000) # bajar la cancion gradualmente

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    surface.fill(white)
    #surface.blit()
    pygame.display.update()