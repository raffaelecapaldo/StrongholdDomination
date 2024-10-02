import pygame
import sys

#SETTAGGIO FINESTRA

pygame.init()

orologio = pygame.time.Clock()
risoluzione = (800,600)
schermo = pygame.display.set_mode(risoluzione)
pygame.display.set_caption('Stronghold Domination')
orologio.tick(60)  


running = True

while running:
    schermo.fill("white")
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()