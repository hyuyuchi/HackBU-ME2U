import pygame
import random

class GoodObject(pygame.sprite.Sprite):

    def __init__(self, x, y, h, w, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale((pygame.image.load(image).convert_alpha()), (h,w))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y

    def update(self, num, numx):
        self.
