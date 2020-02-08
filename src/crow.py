import pygame

class crow:
    def __init__(self, x, y, image1,image2):
        pygame.sprite.Sprite(self)
        self.images = [pygame.image.load(image1),pygame.image.load(image2)]
        index = 0;
        self.image = images[index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dir = "Left"
    
    def changeDir(self):
        if self.dir == "left":
            self.dir = "right"
        else:
            self.dir = "left"
        images[0] = pygame.transform.flip(images[0],true,false)
        images[0] = pygame.transform.flip(images[0],true,false)
    
    def update(self)
        if self.dir == "left":
            x -= 5
        else:
            x += 5
        if index == 0:
            index = 1
        else:
            index = 0
            
