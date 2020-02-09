import pygame
import random
class Sian(pygame.sprite.Sprite):
     def __init__(self, x, y, w, h, image):
         pygame.sprite.Sprite.__init__(self)

         self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(),(w,h))
         self.rect = self.image.get_rect()
         self.rect.x = x
         self.rect.y = y
         self.width = w
         self.height = h
         self.direction = "right"


     def hold(self, w=1700, h=956):
         holds = random.choice(["assets/Sian_Bouquet.PNG", "assets/Sian_Choco.PNG", "assets/Sian_GiftBoxGreen.PNG","assets/Sian GiftBoxPink.PNG","assets/Sian_LoveLetter.PNG","assets/Sian_Ring.PNG", "assets/Sian_DeadMouse.PNG", "assets/Sian_PaperBall.PNG", "assets/Sian_Rock.PNG"])
         self.image = pygame.transform.scale(pygame.image.load(holds).convert_alpha(),(w,h))

     def throw(self,w=1700, h=956):
             self.image = pygame.transform.scale(pygame.image.load("assets/Sian_Throw.PNG").convert_alpha(),(w,h))


     def empty(self,w=1700, h=956):
         self.image = pygame.transform.scale(pygame.image.load("assets/Sian_Empty.PNG").convert_alpha(),(w,h))

