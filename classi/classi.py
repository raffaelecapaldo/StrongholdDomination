import pygame

immagineLord = "immagini/Lord-1-removebg-preview.png"



class Lord(pygame.sprite.Sprite):


    def __init__(self, larghezza, altezza):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(immagineLord)
        self.image = pygame.transform.scale(self.image, (100,134))
        self.image = self.image.convert_alpha()
        self.rect =  self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)


        self.rect.topleft = (larghezza,altezza)
        self.vel_x = 0
        self.vel_y = 0

    def cambia_vel(self, x, y):
        self.vel_x += x
        self.vel_y += y


    def update(self):
        larghezza = 1920
        altezza = 1080
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        # Controllo dei limiti dello schermo
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > larghezza:
            self.rect.right = larghezza
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > altezza:
            self.rect.bottom = altezza


        

