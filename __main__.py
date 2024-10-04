import pygame
import sys
from classi import classi

#SETTAGGIO FINESTRA

pygame.init()

orologio = pygame.time.Clock()
risoluzione = (1920,1080)
schermo = pygame.display.set_mode(risoluzione)
pygame.display.set_caption('Stronghold Domination')
orologio.tick(60)
lord = classi.Lord(960,540)

COLORE_PRATO = (141,200,103)

vel_lord_x = 0.35
vel_lord_y = 0.35

running = True

while running:
    schermo.fill(COLORE_PRATO)
    gruppoLord = pygame.sprite.Group()
    gruppoLord.add(lord)
    gruppoLord.draw(schermo)
    gruppoLord.update()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_LEFT:
                lord.cambia_vel(-1*vel_lord_x, 0)
                print("test")
            if event.key == pygame.K_RIGHT:
                lord.cambia_vel(vel_lord_x, 0)
            if event.key == pygame.K_UP:
                lord.cambia_vel(0, -1*vel_lord_y)
            if event.key == pygame.K_DOWN:
                lord.cambia_vel(0, vel_lord_y)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                lord.cambia_vel(vel_lord_x, 0)
            if event.key == pygame.K_RIGHT:
                lord.cambia_vel(-1*vel_lord_x, 0)
            if event.key == pygame.K_UP:
                lord.cambia_vel(0, vel_lord_y)
            if event.key == pygame.K_DOWN:
                lord.cambia_vel(0, -1*vel_lord_y)