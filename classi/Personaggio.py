import pygame

class Personaggio(pygame.sprite.Sprite):


    def __init__(self, larghezza, altezza, immagine):
        pygame.sprite.Sprite.__init__(self)
        self.immagine = pygame.image.load(immagine)
        self.immagine = pygame.transform.scale(self.immagine, (100,100))
        self.immagine = self.immagine.convert_alpha()
        self.rect =  self.immagine.get_rect()
        self.mask = pygame.mask.from_surface(self.immagine)


        self.rect.topleft = (larghezza,altezza)