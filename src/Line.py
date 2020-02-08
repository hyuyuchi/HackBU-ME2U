import pygame
import random

class Line(pygame.sprite.Sprite):

    def __init__(self, x, y, h, w, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale((pygame.image.load(image).convert_alpha()), (h,w))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y

    def update(self, num, numx):
        try:
            if self.rect.x < 1700 and num >= 0:
            
                self.rect.x += 30 
                self.rect.y = (((-1/num) * (self.rect.x-numx) ** 2) - 350) * -1
                '''-1/num*(X-numx)**2 -350'''
                #print(str(self.rect.x) + " , " + str(self.rect.y))

    def reset(self):
        self.rect.x = self.x
        self.rect.y = self.y

