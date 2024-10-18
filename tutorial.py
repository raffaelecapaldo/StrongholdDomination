import pygame
import sys
from classi import classi

# Inizializza Pygame
pygame.init()

# Costanti
# Background del menu
larghezza_schermo, altezza_schermo = (1920, 1080)
bg = pygame.image.load("Immagini/sfondo menu.jpg")
bg = pygame.transform.scale(bg, (larghezza_schermo,altezza_schermo))
font = pygame.font.Font(None, 100)
font_titolo = pygame.font.Font(None, 150)
# Definisci le dimensioni della finestra


# Crea una finestra di gioco
schermo = pygame.display.set_mode((larghezza_schermo, altezza_schermo))

COLORE_NERO = (0, 0, 0)
COLORE_BIANCO = (255, 255, 255)

# Stato del gioco
stato = "menu"


  

def mostra_tutorial():
    schermo.fill(COLORE_NERO)
    font = pygame.font.Font(None, 36)
    testo = [
        "Tutorial:",
        "Usa le frecce per muovere la palla.",
        "Premi 'Esc' per tornare al menu.",
    ]
    for i, linea in enumerate(testo):
        testo_render = font.render(linea, True, COLORE_BIANCO)
        schermo.blit(testo_render, (100, 100 + i * 40))
    
    pygame.display.flip()

while True:
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

    elif stato == "tutorial":
        mostra_tutorial()
    elif stato == "gioco":

        schermo.fill(COLORE_NERO)

        # Aggiorna lo schermo
        pygame.display.flip()