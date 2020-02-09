import pygame
import random
class Chia(pygame.sprite.Sprite):
     def __init__(self, x, y, w, h, image, image1, image2, image3, image4):
         pygame.sprite.Sprite.__init__(self)

         self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(), (w,h))
         self.image1 = pygame.transform.scale(pygame.image.load(image1).convert_alpha(), (w,h))
         self.image2 = pygame.transform.scale(pygame.image.load(image2).convert_alpha(), (w,h))
         self.image3 = pygame.transform.scale(pygame.image.load(image3).convert_alpha(), (w,h))
         self.image4 = pygame.transform.scale(pygame.image.load(image4).convert_alpha(), (w,h))
         self.rect = self.image.get_rect()
         self.rect.x = x
         self.rect.y = y
         self.width = w
         self.height = h
         self.direction = "left"



         #walking animation
         '''self.walking = ["assets/Chia_Walking1+3.PNG", "assets/Chia_Walking2.PNG", "assets/Chia_Walking1+3.PNG", "assets/Chia_Walking4.PNG"]
         self.walking.append(pygame.transform.scale(pygame.image.load("assets/Chia_Walking1+3.PNG").convert_alpha(),(w,h)))
         self.walking.append(pygame.transform.scale(pygame.image.load("assets/Chia_Walking2.PNG").convert_alpha(),(w,h)))
         self.walking.append(pygame.transform.scale(pygame.image.load("assets/Chia_Walking1+3.PNG").convert_alpha(),(w,h)))
         self.walking.append(pygame.transform.scale(pygame.image.load("assets/Chia_Walking4.PNG").convert_alpha(),(w,h)))'''

         
     
         self.index = 0

     def changeDirection(self):
         if self.rect.x >= (1700/2)+100 and self.rect.x < 1700-100:
            self.direction = random.choice(["right","left"])
         elif (self.rect.x < (1700/2)+100):
            self.direction = "right"
         elif self.rect.x > 1700-100:
            self.direction = "left"

     def default(self, w, h):
         self.image = pygame.transform.scale(pygame.image.load("assets/Chia_Standing.PNG").convert_alpha(),(w,h))


     def happy(self, w, h):
             self.image = pygame.transform.scale(pygame.image.load("assets/Chia_Happy.PNG").convert_alpha(),(w,h))

     def angry(self, w, h):
             self.image = pygame.transform.scale(pygame.image.load("assets/Chia_Angry.PNG").convert_alpha(),(w,h))


     def startwalk (self):
         self.image == self.image1

     def walk(self):
         self.changeDirection()
         if self.image == self.image1:
            self.image = self.image2

         elif self.image == self.image2:
            self.image = self.image3

         elif self.image == self.image3:
            self.image = self.image4

         elif self.image == self.image4:
            self.image = self.image1

     def update (self):
         if self.direction == "left":
            self.rect.x -= 10

         else:
            self.rect.x += 10

        

            



     ''' def walk(self, w, h):


         if self.rect.x >= (1700/2)+100 and self.rect.x < 1700-100:
            self.direction = random.choice(["right","left"])


            if (self.direction == "left"):
               for i in range(random.randrange(50, 101)):
                   self.index += 1
                   if self.index >= len(self.walking):
                      self.index = 0
                   self.image = pygame.transform.scale(pygame.image.load(self.walking[self.index]).convert_alpha(),(w,h))
                   self.rect.x -= 5
               self.image = pygame.transform.scale(pygame.image.load("assets/Chia_Standing.PNG").convert_alpha(),(w,h))
               

            if (self.direction == "right"):
               self.image = pygame.transform.flip(pygame.image.load(self.walking[self.index]).convert_alpha(), True, False)
               for i in range(random.randrange(50, 101)):
                   self.index += 5
                   if self.index >= len(self.walking):
                      self.index = 0
                   self.image = pygame.transform.scale(pygame.image.load(self.walking[self.index]).convert_alpha(),(w,h))
                   self.rect.x += 5
               self.image = pygame.transform.scale(pygame.image.load("assets/Chia_Standing.PNG").convert_alpha(),(w,h))

         #To prevent going out of range
         elif (self.rect.x < (1700/2)+100):
            self.direction = "right"
            self.image = pygame.transform.flip(pygame.image.load(self.walking[self.index]).convert_alpha(),(w,h))
            for i in range(random.randrange(50, 101)):
                self.index += 5
                if self.index >= len(self.walking):
                   self.index = 0
                self.image = pygame.transform.scale(pygame.image.load(self.walking[self.index]).convert_alpha(),(w,h))
                self.rect.x += 5
            self.image = pygame.transform.scale(pygame.image.load("assets/Chia_Standing.PNG").convert_alpha(),(w,h))

         elif self.rect.x > 1700-100:
            self.direction = "left"
            for i in range(random.randrange(5,11)):
                self.index += 5
                if self.index >= len(self.walking):
                   self.index = 0
                self.image = pygame.transform.scale(pygame.image.load(self.walking[self.index]).convert_alpha(), True, False)
                self.rect.x -= 5
            self.image = pygame.transform.scale(pygame.image.load("assets/Chia_Standing.PNG").convert_alpha(),(w,h))'''

   
         
                    

            
            
            

            

         




         

