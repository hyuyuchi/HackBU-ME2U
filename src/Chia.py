import pygame
import random
class Chia(pygame.sprite.Sprite):
     def __init__(self, x, y, w=1700, h=956):
         pygame.sprite.Sprite.__init__(self)

         self.image = pygame.transform.scale(pygame.image.load("assets/Chia_Standing.PNG").convert_alpha(),(w,h))
         self.rect = self.image.get_rect()
         self.rect.x = x
         self.rect.y = y
         self.width = w
         self.height = h
         self.direction = "left"



         #walking animation
         self.walking = []
         self.walking.append(pygame.image.load("assets/Chia_Walking1+3.PNG"))
         self.walking.append(pygame.image.load("assets/Chia_Walking2.PNG")
         self.walking.append(pygame.image.load("assets/Chia_Walking1+3.PNG"))
         self.walking.append(pygame.image.load("assets/Chia_Walking4.PNG"))

         self.index = 0



     def default(self)
         self.image = pygame.image.load("assets/Chia_Standing.PNG").convert_alpha


     def happy(self):
         for i in range(3)
             self.image = pygame.image.load("assets/Chia_Happy.PNG").convert_alpha
         self.image = pygame.image.load("assets/Chia_Standing.PNG").convert_alpha

     def angry(self):
         for i in range(3)
             self.image = pygame.image.load("assets/Chia_Angry").convert_alpha

     def walk(self):
         '''
            Controls walking 
         '''
         if self.rect.x >= h/2 and self.rect.x < h:
            self.direction = random.choice(["right","left"])

            if self.direction = "left":
               for i in random.choice([1,2,3,4,5])
                   self.index += 1
                       if self.index > len(self.walking):
                          self.index = 0
                   self.rect.x -= 1
               self.image = pygame.image.load("assets/Chia_Standing.PNG").convert_alpha
               

            if self.direction = "right"
               self.image = self.walking[self.index]
               self.image = pygame.transform.flip(self.walking, True, False)
               for i in random.choice([1,2,3,4,5])
                   self.index += 1
                       if self.index > len(self.walking):
                          self.index = 0
                   self.rect.x += 1
               self.image = pygame.transform.flip(self.walking, True, False)
               self.image = pygame.image.load("assets/Chia_Standing.PNG").convert_alpha
         

         #To prevent going out of range
         elif self.rect.x < h/2
            self.direction = "right"
               for i in random.choice([1,2,3,4,5])
                   self.index += 1
                       if self.index > len(self.walking):
                          self.index = 0
                   self.rect.x += 1
            self.image = pygame.transform.flip(self.walking, True, False)
            self.image = pygame.image.load("assets/Chia_Standing.PNG").convert_alpha

         else self.rect.x > 2:
            if self.direction = "left":
               for i in random.choice([1,2,3,4,5])
                   self.index += 1
                       if self.index > len(self.walking):
                          self.index = 0
                   self.rect.x -= 1
               self.image = pygame.image.load("assets/Chia_Standing.PNG").convert_alpha
         
                    

            
            
            

            

         




         

