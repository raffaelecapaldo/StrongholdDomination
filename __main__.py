import pygame
import sys
from classi import classi
#per i monitor dei portatili che hanno il desktop scalato
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

#SETTAGGIO FINESTRA

pygame.init()
# Definisci le dimensioni della finestra
larghezza_schermo, altezza_schermo = (1920, 1080)

# Crea una finestra di gioco
screen = pygame.display.set_mode((larghezza_schermo, altezza_schermo))

# Sfondo del gioco
bg = pygame.image.load("Immagini/sfondo menu.jpg")
bg = pygame.transform.scale(bg, (1920,1080))
font = pygame.font.Font(None, 100)
font_titolo = pygame.font.Font(None, 150)

orologio = pygame.time.Clock()
risoluzione = (1920,1080)
schermo = pygame.display.set_mode(risoluzione)
pygame.display.set_caption('Stronghold Domination')
orologio.tick(60)
lord = classi.Lord(960,540)
castello = classi.Edificio(0,0,"Immagini/Castello_1-removebg-preview.png")
bandito = classi.Nemico(700,700, 2)
bandito2 = classi.Nemico(1300,1000, 2)

COLORE_PRATO = (141,200,103)

vel_lord_x = 2
vel_lord_y = 2

#VALUTE GIOCO
oro = 5
spade = 5
contatore_oro = font_titolo.render('Oro: ' + str(oro), True, 'white')
contatore_spade = font_titolo.render('Spade: ' + str(spade), True, 'white')


#BOTTONI
clessidra = pygame.image.load("Immagini/clessidra.png")
clessidra_rect = clessidra.get_rect()
clessidra_rect.topleft = (1800, 10)
clessidra_grigia = clessidra.copy()
clessidra_grigia.fill((100, 100, 100), special_flags=pygame.BLEND_RGB_MULT)

ACCRESCI_VALUTA  = pygame.USEREVENT + 1
pygame.time.set_timer(ACCRESCI_VALUTA, 10000)
RIPRISTINA_VELOCITA = pygame.USEREVENT + 2


slow_speed = False




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
            text_start = font.render('START', True, "white")
            text_exit = font.render('EXIT', True, "white")

            # Definiamo i nostri bottoni
            start_button = pygame.Rect(810, 400, 250, 80)
            exit_button = pygame.Rect(830, 640, 190, 80)

            # Riempi la finestra con l'immagine di sfondo
            schermo.blit(bg, (0,0))

            # Disegna rettangoli sullo schermo
            pygame.draw.rect(schermo, "blue", start_button, 1, 1)
            pygame.draw.rect(schermo, "blue", exit_button, 1, 1)

            # Posiziona il testo nel rettangolo
            schermo.blit(text_start, (820, 410))  
            schermo.blit(text_exit, (840, 650))
            schermo.blit(titolo_gioco,(400,140))

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
    contatore_oro = font_titolo.render('Oro: ' + str(oro), True, 'white')
    contatore_spade = font_titolo.render('Spade: ' + str(spade), True, 'white')
    schermo.blit(contatore_oro,(10,30))
    schermo.blit(contatore_spade,(10,70))

    gruppoNemici = pygame.sprite.Group()
    gruppoNemici.add(bandito, bandito2)
    gruppoNemici.draw(schermo)
    gruppoNemici.update(lord)
    if slow_speed or oro < 4:
    # Se slow_speed è attivo, mostra la clessidra grigia
        schermo.blit(clessidra_grigia, clessidra_rect.topleft)
    else:
    # Altrimenti, mostra la clessidra normale
        schermo.blit(clessidra, clessidra_rect.topleft)
        schermo.blit(clessidra, (1800,10))




    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if event.type == ACCRESCI_VALUTA:
            oro+=1
            spade+=1
            contatore_oro = font_titolo.render('Oro: ' + str(oro), True, 'white')
            contatore_spade = font_titolo.render('Spade: ' + str(spade), True, 'white')
            schermo.blit(contatore_oro,(10,30))
            schermo.blit(contatore_spade,(10,70))
        
        if event.type == RIPRISTINA_VELOCITA:
    # Ripristina la velocità dei nemici al valore originale
            for nemici in gruppoNemici:
             nemici.velocita = 2
    # Ferma il timer (impostando a 0)
            pygame.time.set_timer(RIPRISTINA_VELOCITA, 0)
            slow_speed = False

        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if clessidra_rect.collidepoint(mouse_pos):
                    if oro >= 4 and slow_speed == False:
                        oro-=4
                        slow_speed = True
                        for nemici in gruppoNemici:
                            nemici.velocita -=1
                        pygame.time.set_timer(RIPRISTINA_VELOCITA, 5000)

        





        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                
                game_state = "menu"
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