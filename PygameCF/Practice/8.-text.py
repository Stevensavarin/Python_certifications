import sys
import pygame

pygame.init()

width = 500
height = 500

surface = pygame.display.set_mode((width, height)) #surface
pygame.display.set_caption("Text")

#RGB
red = pygame.Color(255, 0, 0) #0 - 255
white = pygame.Color(255, 255, 255)

#1.-Obtener una fuente
font = pygame.font.Font("Practice/roboto/Roboto-Thin.ttf", 48) #str, tamaño

#2.-Crear el texto
text = font.render("Hola mundo!", True, red ) #texto, bool, color -> surface
rect = text.get_rect()
rect.center = (width // 2, height // 2)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    surface.fill(white)
    surface.blit(text, rect)
    pygame.display.update()