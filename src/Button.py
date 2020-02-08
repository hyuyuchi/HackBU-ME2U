import pygame

class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, h, w, image):
        pygame.sprite.Sprite.__init__(self)
        theimage = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(theimage, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
