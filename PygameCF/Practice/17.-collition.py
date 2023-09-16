import sys
import pygame

pygame.init()

width = 600
height = 600

surface = pygame.display.set_mode((width, height)) #surface
pygame.display.set_caption("Colisión")

#RGB
white = pygame.Color(255, 255, 255)
red = (134, 45, 83)
green = (52, 157, 89)
blue = (59, 87, 181)

rect1 = pygame.Rect(0, 0, 100, 80)
rect1.center = (width // 2, height // 2)

rect2 = pygame.Rect(0, 0, 100, 80)

font = pygame.font.Font("freesansbold.ttf", 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    surface.fill(white)

    rect2.center = pygame.mouse.get_pos()

    pygame.draw.rect(surface, green, rect1)
    pygame.draw.rect(surface, red, rect2)

    message = ""

    if rect1.colliderect(rect2):
        sound = pygame.mixer.Sound("Practice/sounds/coin.wav")
        sound.play()
        
        message = "Existe una colisión"

    text = font.render(message, True, blue)
    rect3 = text.get_rect()
    rect3.midtop = (width // 2, 50)
    
    surface.blit(text, rect3)

    pygame.display.update()