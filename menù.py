import pygame
import sys
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

pygame.init()
# Definisci le dimensioni della finestra
larghezza_schermo, altezza_schermo = (1920, 1080)

# Crea una finestra di gioco
screen = pygame.display.set_mode((larghezza_schermo, altezza_schermo))


# Background del menu
bg = pygame.image.load("Immagini/sfondo menu.jpg")
bg =  pygame.transform.scale(bg, (larghezza_schermo,altezza_schermo))



# Imposta il titolo della finestra
pygame.display.set_caption("Menu")

# Crea un oggetto Clock per gestire il frame rate
orologio = pygame.time.Clock()

# Imposta il frame rate desiderato (ad esempio 60 FPS)
frame_rate = 60

font = pygame.font.Font(None, 36)
font_titolo = pygame.font.Font(None, 60)
def main_menu():
    while True:
        # Gestione degli eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if start_button.collidepoint(mouse_pos):
                    start_game()

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
            screen.blit(bg, (0,0))

            # Disegna rettangoli sullo schermo
            pygame.draw.rect(screen, "blue", start_button, 1, 1)
            pygame.draw.rect(screen, "blue", exit_button, 1, 1)

            # Posiziona il testo nel rettangolo
            screen.blit(text_start, (310, 210))  
            screen.blit(text_exit, (310, 350))
            screen.blit(titolo_gioco,(100,100))

            pygame.display.update()


def start_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            screen.fill("blue")        
        

        # Aggiorna il display
        pygame.display.update()

        # Limita il frame rate al valore specificato
        orologio.tick(frame_rate)



if __name__ == "__main__":
    main_menu()
