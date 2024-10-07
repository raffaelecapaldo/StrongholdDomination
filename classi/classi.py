import pygame
import math

immagineLord = "immagini/Lord-1-removebg-preview.png"



class Lord(pygame.sprite.Sprite):


    def __init__(self, larghezza, altezza):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(immagineLord)
        self.imageLeft = pygame.transform.scale(self.image, (100,134))
        self.image = self.imageLeft

        self.image = self.image.convert_alpha()
        self.rect =  self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.imageRight = pygame.transform.flip(self.image, True, False)
        
        self.isLeft = True
        self.isRight = False



        self.rect.topleft = (larghezza,altezza)
        self.vel_x = 0
        self.vel_y = 0

        #usato float per memorizzare posizione con virgola mobile, in modo da renderlo più lento
        #e riconvertito in int dopo perché pygame nel rendering con rect richiede numeri interi
        self.pos_x = float(larghezza)
        self.pos_y = float(altezza)

    def cambia_vel(self, x, y):
        self.vel_x += float(x)
        self.vel_y += float(y)


    def update(self):
        larghezza = 1920
        altezza = 1080
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.rect.x += int(self.vel_x)
        self.rect.y += int(self.vel_y)
        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)
        # Controllo dei limiti dello schermo
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > larghezza:
            self.rect.right = larghezza
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > altezza:
            self.rect.bottom = altezza

class Edificio(pygame.sprite.Sprite):


    def __init__(self, larghezza, altezza, immagine_edificio):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(immagine_edificio)
        #self.imageLeft = pygame.transform.scale(self.image, (100,134))

        self.image = self.image.convert_alpha()
        self.rect =  self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


        self.rect.topleft = (larghezza,altezza)


class Nemico(pygame.sprite.Sprite):
    def __init__(self, larghezza, altezza, velocita):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("immagini/bandito.png")
        self.image = pygame.transform.scale(self.image, (134,134))

        self.image = self.image.convert_alpha()
        self.rect =  self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.velocita = velocita


        self.rect.topleft = (larghezza,altezza)


        #distanza = math.sqrt(dx ** 2 + dy ** 2)

    def update(self, personaggio):
        dx, dy = personaggio.rect.centerx - self.rect.centerx, personaggio.rect.centery - self.rect.centery
        distanza = math.hypot(dx, dy)
        
        if distanza > 0:
            dx, dy = dx / distanza, dy / distanza 
            self.rect.x += dx * self.velocita
            self.rect.y += dy * self.velocita

