import pygame
import random
class Chia(pygame.sprite.Sprite):
     def __init__(self, x, y, w, h, image):
         pygame.sprite.Sprite.__init__(self)

         self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(),(w,h))
         self.rect = self.image.get_rect()
         self.rect.x = x
         self.rect.y = y
         self.width = w
         self.height = h
         self.direction = "left"



         #walking animation
         self.walking = []
         self.walking.append(pygame.transform.scale(pygame.image.load("assets/Chia_Walking1+3.PNG").convert_alpha(),(w,h)))
         self.walking.append(pygame.transform.scale(pygame.image.load("assets/Chia_Walking2.PNG").convert_alpha(),(w,h)))
         self.walking.append(pygame.transform.scale(pygame.image.load("assets/Chia_Walking1+3.PNG").convert_alpha(),(w,h)))
         self.walking.append(pygame.transform.scale(pygame.image.load("assets/Chia_Walking4.PNG").convert_alpha(),(w,h)))

         self.index = 0



     def default(self, w, h)
         self.image = pygame.transform.scale(pygame.image.load("assets/Chia_Standing.PNG").convert_alpha(),(w,h))


     def happy(self, w, h):
         for i in range(3)
             self.image = pygame.transform.scale(pygame.image.load("assets/Chia_Happy.PNG").convert_alpha(),(w,h))
         self.image = pygame.transform.scale(pygame.image.load("assets/Chia_Standing.PNG").convert_alpha(),(w,h))

     def angry(self, w, h):
         for i in range(3)
             self.image = pygame.transform.scale(pygame.image.load("assets/Chia_Angry.PNG").convert_alpha(),(w,h))

     def walk(self, w, h):
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
               self.image = pygame.transform.scale(pygame.image.load("assets/Chia_Standing.PNG").convert_alpha(),(w,h))
               

            if self.direction = "right"
               self.image = self.walking[self.index]
               self.image = pygame.transform.flip(self.walking, True, False)
               for i in random.choice([1,2,3,4,5])
                   self.index += 1
                       if self.index > len(self.walking):
                          self.index = 0
                   self.rect.x += 1
               self.image = pygame.transform.flip(self.walking, True, False)
               self.image = pygame.transform.scale(pygame.image.load("assets/Chia_Standing.PNG").convert_alpha(),(w,h))

         #To prevent going out of range
         elif self.rect.x < h/2
            self.direction = "right"
               for i in random.choice([1,2,3,4,5])
                   self.index += 1
                       if self.index > len(self.walking):
                          self.index = 0
                   self.rect.x += 1
            self.image = pygame.transform.flip(self.walking, True, False)
            self.image = pygame.transform.scale(pygame.image.load("assets/Chia_Standing.PNG").convert_alpha(),(w,h))

         else self.rect.x > 2:
            if self.direction = "left":
               for i in random.choice([1,2,3,4,5])
                   self.index += 1
                       if self.index > len(self.walking):
                          self.index = 0
                   self.rect.x -= 1
               self.image = pygame.transform.scale(pygame.image.load("assets/Chia_Standing.PNG").convert_alpha(),(w,h))
         
                    

            
            
            

            

         




         

