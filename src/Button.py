import pygame

class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, h, w, image):
        pygame.sprite.Sprite.__init__(self)
        self.theimage = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.theimage, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.h = h
        self.w = w

    def change(self, numList, num):
        self.theimage = pygame.image.load(numList[num]).convert_alpha()
        self.image = pygame.transform.scale(self.theimage, (self.w, self.h))

    def final(self, x, y, w, h):
        self.rect.x = x
        self.rect.y = y
        self.image = pygame.transform.scale(self.theimage, (w, h))
        
