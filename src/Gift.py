import pygame
import random

class Gift(pygame.sprite.Sprite):

    def __init__(self, x, y, h, w, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale((pygame.image.load(image).convert_alpha()), (h,w))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.h = h
        self.w = w

    def update(self, num, numx):

        self.rect.x += 30
        self.rect.y = (((-1/num) * (self.rect.x-numx-250) ** 2) - 250) * -1

    def reset(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def object(self, image):
        self.image = pygame.transform.scale((pygame.image.load(image).convert_alpha()), (self.h,self.w))

