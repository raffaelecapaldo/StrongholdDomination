import pygame
import math

immagineLord = "immagini/lordnuovo.png"



class Lord(pygame.sprite.Sprite):


    def __init__(self, larghezza, altezza):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(immagineLord)
        self.imageLeft = pygame.transform.scale(self.image, (134,134))
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
        super().__init__()
        self.image = pygame.image.load("immagini/bandito.png")
        self.image = pygame.transform.scale(self.image, (134, 134))
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (larghezza, altezza)  # Posizione iniziale
        self.radius = 20
        self.speed = velocita

    def update(self, lord, enemies):
        self.move_towards(lord, enemies)

    def move_towards(self, personaggio, enemies):
        dx, dy = personaggio.rect.centerx - self.rect.centerx, personaggio.rect.centery - self.rect.centery
        distance = math.hypot(dx, dy)

        if distance > 0:
            dx /= distance
            dy /= distance

            # Prima, evita gli altri nemici
            self.avoid_others(enemies)
            
            # Muovi il nemico verso il personaggio
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed

    def avoid_others(self, enemies):
        avoid_x = 0
        avoid_y = 0
        for other in enemies:
            if other == self:
                continue

            distance = math.hypot(other.rect.x - self.rect.x, other.rect.y - self.rect.y)
            if distance < self.radius * 2:  # Aumenta il raggio di evitamento
                avoid_x += self.rect.x - other.rect.x
                avoid_y += self.rect.y - other.rect.y

        # Normalizza il vettore di evitamento
        if avoid_x != 0 or avoid_y != 0:
            avoid_distance = math.hypot(avoid_x, avoid_y)
            if avoid_distance > 0:  # Evita divisione per zero
                avoid_x /= avoid_distance
                avoid_y /= avoid_distance
                self.rect.x += avoid_x * self.speed * 0.5  # Modifica la velocità di evitamento
                self.rect.y += avoid_y * self.speed * 0.5

    def __init__(self, larghezza, altezza, velocita):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("immagini/bandito.png")
        self.image = pygame.transform.scale(self.image, (134,134))

        self.image = self.image.convert_alpha()
        self.rect =  self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()  # Ottieni il rettangolo dell'immagine
        self.rect.center = (larghezza, altezza)  # Posizione iniziale
        self.radius = 500
        self.speed = velocita
    
    def update(self, lord, enemies):
        self.move_towards(lord, enemies)


        #distanza = math.sqrt(dx ** 2 + dy ** 2)

    def move_towards(self, personaggio, enemies):
        dx, dy = personaggio.rect.centerx - self.rect.centerx, personaggio.rect.centery - self.rect.centery

        distance = math.hypot(dx, dy)

        if distance > 0:
            dx /= distance
            dy /= distance

            # Prima, evita gli altri nemici
            self.avoid_others(enemies)
            
            # Muovi il nemico verso il personaggio
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed

    def avoid_others(self, enemies):
        avoid_x = 0
        avoid_y = 0
        for other in enemies:
            if other == self:
                continue

            distance = math.hypot(other.rect.x - self.rect.x, other.rect.y - self.rect.y)
            if distance < self.radius:
                avoid_x += self.rect.x - other.rect.x
                avoid_y += self.rect.y - other.rect.y

        if avoid_x != 0 or avoid_y != 0:
            avoid_distance = math.hypot(avoid_x, avoid_y)
            if avoid_distance > 0:  # Evita divisione per zero
                avoid_x /= avoid_distance
                avoid_y /= avoid_distance
                self.rect.x += avoid_x * self.speed * 0.5
                self.rect.y += avoid_y * self.speed * 0.5