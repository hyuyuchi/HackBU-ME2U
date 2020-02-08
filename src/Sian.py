import pygame
import random
class Sian(pygame.sprite.Sprite):
     def __init__(self, x, y, image, w=1700, h=956):
         pygame.sprite.Sprite.__init__(self)

         self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(),(w,h))
         self.rect = self.image.get_rect()
         self.rect.x = x
         self.rect.y = y
         self.width = w
         self.height = h
         self.direction = "right"


     def hold (self):
         holds = random.choice(["assets/Bouquet.PNG", "assets/Choco.PNG", "assets/GiftBoxGreen.PNG","assets/GiftBoxPink.PNG","assets/LoveLetter.PNG","assets/Ring.PNG", "assets/DeadMouse.PNG", "assets/PaperBall.PNG", "assets/Rock.PNG"])
         self.image = pygame.image.load(holds).convert_alpha()

     def throw(self):
             self.image = pygame.image.load("assets/Sian_Throw.PNG").convert_alpha()


     def empty(self):
         self.image = pygame.image.load("assets/Sian_Throw.PNG").convert_alpha()

