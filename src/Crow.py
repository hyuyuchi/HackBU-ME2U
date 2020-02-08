import pygame

class Crow(pygame.sprite.Sprite):
    def __init__(self, x, y, h, w, image1, image2):
        pygame.sprite.Sprite.__init__(self)

        '''self.images = [pygame.image.load(image1).convert_alpha(), pygame.image.load(image2).convert_alpha()]
        self.index = 0;
        self.image = [image1, image2]
        self.rect = self.image.get_rect()'''

        self.image1 = pygame.transform.scale(pygame.image.load(image1).convert_alpha(), (w,h))
        self.image2 = pygame.transform.scale(pygame.image.load(image2).convert_alpha(), (w,h))
        self.image = self.image1
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.dir = "left"
    
    def changeDir(self):
        '''if self.dir == "left":
            self.dir = "right"
        else:
            self.dir = "left"
        self.images[0] = pygame.transform.flip(images[0],true,false)
        self.images[1] = pygame.transform.flip(images[1],true,false)'''

        if self.rect.x < -30:
            self.dir = "right"
            self.image1 = pygame.transform.flip(self.image1, True, False)
            self.image2 = pygame.transform.flip(self.image2, True, False)
        if self.rect.x > 1700:
            self.dir = "left"
            self.image1 = pygame.transform.flip(self.image1, True, False)
            self.image2 = pygame.transform.flip(self.image2, True, False)
    
    def update(self):

        self.changeDir()


        if self.image == self.image1:
            self.image = self.image2
        else:
            self.image = self.image1



        if self.dir == "left":
            self.rect.x -= 10
        else:
            self.rect.x += 10
        '''if index == 0:
            index = 1
        else:
            index = 0'''
            
