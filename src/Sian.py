import pygame
import random
class Sian(pygame.sprite.Sprite):
     def __init__(self, x, y, w, h, image):
         pygame.sprite.Sprite.__init__(self)

         self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(),(h,w))
         self.rect = self.image.get_rect()
         self.rect.x = x
         self.rect.y = y
         self.width = w
         self.height = h
         self.direction = "right"


     def hold(self, w, h, holds):
         self.image = pygame.transform.scale(pygame.image.load(holds).convert_alpha(),(w,h))

     def throw(self, w, h):
         self.image = pygame.transform.scale(pygame.image.load("assets/Sian_Throw.PNG").convert_alpha(),(w,h))


     def empty(self, w, h):
         self.image = pygame.transform.scale(pygame.image.load("assets/Sian_Empty.PNG").convert_alpha(),(h,w))

