import pygame
import random
class Sian(pygame.sprite.Sprite):
     def __init__(self, x, y, h, w, image, direction):
         pygame.sprite.Sprite.__init__(self)

         self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha()),(h,w))
         self.rect = image.rect.get_rect()

         #objects

         self.object.
         self.rect.x = x
         self.rect.y = y
         self.height = h
         self.width = w
         self.direction = "right"

     def hold (self):
         hold = random.choice(["assets/Bouquet", "assets/Choco", "assets/GiftBoxGreen","assets/GiftBoxPink","assets/LoveLetter","assets/Ring", "assets/DeadMouse", "assets/PaperBall", "assets/Rock"])
         self.image = pygame.image.load(hold).convert_alpha())

     def throw(self):
             self.image = pygame.image.load("assets/Sian_Throw").convert_alpha())


     def empty(self):
         self.image = pygame.image.load("assets/Sian_Throw").convert_alpha())

