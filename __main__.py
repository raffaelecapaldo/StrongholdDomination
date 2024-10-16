import pygame
import sys
from classi import classi
#per i monitor dei portatili che hanno il desktop scalato
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

#SETTAGGIO FINESTRA

pygame.init()
bg = pygame.image.load("Immagini/sfondo menu.jpg")
bg = pygame.transform.scale(bg, (1920,1080))
font = pygame.font.Font(None, 36)
font_titolo = pygame.font.Font(None, 60)

orologio = pygame.time.Clock()
risoluzione = (1920,1080)
schermo = pygame.display.set_mode(risoluzione)
pygame.display.set_caption('Stronghold Domination')
orologio.tick(60)
lord = classi.Lord(960,540)
castello = classi.Edificio(0,0,"Immagini/Castello_1-removebg-preview.png")


COLORE_PRATO = (141,200,103)

vel_lord_x = 2
vel_lord_y = 2
enemy_sprites = pygame.sprite.Group()
enemy_sprites.add(classi.Nemico(100, 100, 2))  # Usa il percorso dell'immagine del nemico
enemy_sprites.add(classi.Nemico(200, 200, 2))
enemy_sprites.add(classi.Nemico(300, 300, 2))

running = True
game_state = "menu"
while running:
 if game_state == "menu":
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if start_button.collidepoint(mouse_pos):
                    game_state = "play"



                if exit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()
            # Creazione della schermata iniziale
            titolo_gioco = font_titolo.render('StrongHold Domination', True, 'white')
            text_start = font.render('Inizia', True, "white")
            text_exit = font.render('Esci', True, "white")

            # Definiamo i nostri bottoni
            start_button = pygame.Rect(300, 200, 200, 50)
            exit_button = pygame.Rect(300, 340, 200, 50)
                    
            # Riempi la finestra con l'immagine di sfondo
            schermo.blit(bg, (0,0))

            # Disegna rettangoli sullo schermo
            pygame.draw.rect(schermo, "blue", start_button, 1, 1)
            pygame.draw.rect(schermo, "blue", exit_button, 1, 1)

            # Posiziona il testo nel rettangolo
            schermo.blit(text_start, (310, 210))  
            schermo.blit(text_exit, (310, 350))
            schermo.blit(titolo_gioco,(100,100))

            pygame.display.update()
 elif game_state == "play":

    schermo.fill(COLORE_PRATO)
    gruppoLord = pygame.sprite.Group()
    gruppoLord.add(lord)
    gruppoLord.draw(schermo)
    gruppoLord.update()
    gruppoCastello = pygame.sprite.Group()
    gruppoCastello.add(castello)
    gruppoCastello.draw(schermo)
    gruppoCastello.update()


        # Muovi e disegna nemici
    for enemy in enemy_sprites:
            enemy.update(lord, enemy_sprites)  # Aggiorna posizione nemici seguendo il lord

    enemy_sprites.draw(schermo)  # Disegna i nemici sullo schermo

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
                if lord.isRight:
                    lord.image = lord.imageLeft
                    lord.isRight = False
                    lord.isLeft = True
            if event.key == pygame.K_RIGHT:
                lord.cambia_vel(vel_lord_x, 0)
                if lord.isLeft:
                    lord.image = lord.imageRight
                    lord.isRight = True
                    lord.isLeft = False

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