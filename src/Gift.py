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
        self.imageNum = 0
        self.state = "GOOD"



    def update(self, num, numx):

        self.rect.x += 30
        self.rect.y = (((-1/num) * (self.rect.x-numx-220) ** 2) - 200) * -1

    def reset(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def object(self, image, objects, sian, good, bad):

        for i in range(len(sian)):
            if sian[i] == image:
                self.imageNum = i
        theimage = objects[self.imageNum]
        self.image = pygame.transform.scale((pygame.image.load(theimage).convert_alpha()), (self.h,self.w))
        if theimage in good:
            self.state = "GOOD"
        elif theimage in bad:
            self.state = "BAD"
        print(self.state)
