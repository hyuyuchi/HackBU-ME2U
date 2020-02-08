import pygame
import sys
import random
from src import Button

class Controller:

    def __init__(self, width=1700, height=956):

        #screen
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()


        #start buttons
        self.startPB = Button.Button(571, 490, 123, 465, "assets/StartScreen_PlayButton.png")
        





                 




















        self.show = pygame.sprite.Group()

        self.state = "START"

    def mainLoop(self):
        while self.state == "START":
            self.gameLoop()


    def reset(self, image):
        #self.theline.reset()
        self.background = pygame.transform.scale((pygame.image.load(image)), (1700,956))
        self.screen.blit(self.background, (0, 0))      
        self.show.draw(self.screen)          
        pygame.display.flip()



    def gameLoop(self):
        pygame.key.set_repeat(1,10)

        while self.state == "START":

            #exit button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()




            if pygame.mouse.get_pressed()[0] and self.startPB.rect.collidepoint(pygame.mouse.get_pos()):
                self.state = "INSTRUCTION_1"





            self.show = pygame.sprite.Group((self.startPB,))
            self.reset("assets/StartScreen_FullDisplay.png")


        while self.state == "INSTRUCTION_1":
            #exit button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


            self.show = pygame.sprite.Group()
            self.reset("assets/InstructionScreen_PG1.PNG")





















































