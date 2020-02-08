import pygame
import sys
import random
import time
from src import Button
from src import Line
#from src import Chia
from src import Sian

class Controller:

    def __init__(self, width=1700, height=956):

        #screen
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()


        #start buttons
        self.startPB = Button.Button(595, 500, 123, 465, "assets/StartScreen_PlayButton.png")
        self.startHB = Button.Button(595, 635, 123, 465, "assets/StartScreen_HelpButton.png")
        self.startQB = Button.Button(595, 760, 123, 465, "assets/StartScreen_QuitButton.png")


        #instruction buttons
        self.insrXB = Button.Button(35, 40, 120, 120, "assets/InstructionScreen_ExitButton.PNG")
        self.insrNB = Button.Button(1538, 810, 138, 138, "assets/InstructionScreen_RightButton.PNG")
        self.insrLeftB = Button.Button(35, 810, 138, 138, "assets/InstructionScreen_LeftButton.PNG")
                 

        #game screen
        self.ground = Button.Button(0, 55, 900, 1700, "assets/GameScreen_Ground.PNG")

#______________________________________________________________________________LOAD SPRITES

        #self.chia = Chia.Chia(1800, 200)
        self.sian = Sian.Sian(300, 300, "assets/Sian_Empty.PNG")

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
        while True:
            while self.state == "START":

                #exit button
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()


                if pygame.mouse.get_pressed()[0] and self.startPB.rect.collidepoint(pygame.mouse.get_pos()):
                    self.state = "GAME"
    
                if pygame.mouse.get_pressed()[0] and self.startHB.rect.collidepoint(pygame.mouse.get_pos()):
                    self.state = "INSTRUCTION_1"
    
                if pygame.mouse.get_pressed()[0] and self.startQB.rect.collidepoint(pygame.mouse.get_pos()):
                    sys.exit()



                self.show = pygame.sprite.Group((self.startPB,) + (self.startHB,) + (self.startQB,))
                self.reset("assets/StartScreen_FullDisplay.png")


            while self.state == "INSTRUCTION_1":
                #exit button
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
    
                if self.insrXB.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.state = "START"

                if self.insrNB.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.state = "INSTRUCTION_2"
                    time.sleep(0.3)

                self.show = pygame.sprite.Group((self.insrXB,) + (self.insrNB,))
                self.reset("assets/InstructionScreen_PG1.PNG")


            while self.state == "INSTRUCTION_2":
               #exit button
                for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       sys.exit()

                if self.insrXB.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.state = "START"

                if self.insrNB.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.state = "INSTRUCTION_3"
                    time.sleep(0.3)

                if self.insrLeftB.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                   self.state = "INSTRUCTION_1"
                   time.sleep(0.3)


                self.show = pygame.sprite.Group((self.insrXB,) + (self.insrNB,) + (self.insrLeftB,))
                self.reset("assets/InstructionScreen_PG2.PNG")



            while self.state == "INSTRUCTION_3":
               #exit button
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                if self.insrXB.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.state = "START"

                if self.insrNB.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.state = "INSTRUCTION_4"
                    time.sleep(0.3)

                if self.insrLeftB.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.state = "INSTRUCTION_2"
                    time.sleep(0.3)


                self.show = pygame.sprite.Group((self.insrXB,) + (self.insrNB,) + (self.insrLeftB,))
                self.reset("assets/InstructionScreen_PG3.PNG")

            while self.state == "INSTRUCTION_4":
                #exit button
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                if self.insrXB.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.state = "START"

                if self.insrNB.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.state = "INSTRUCTION_5"
                    time.sleep(0.3)

                if self.insrLeftB.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.state = "INSTRUCTION_3"
                    time.sleep(0.3)


                self.show = pygame.sprite.Group((self.insrXB,) + (self.insrNB,) + (self.insrLeftB,))
                self.reset("assets/InstructionScreen_PG4.PNG")

            while self.state == "INSTRUCTION_5":
                #exit button
                for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       sys.exit()

                if self.insrXB.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.state = "START"

                if self.insrLeftB.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    self.state = "INSTRUCTION_4"
                    time.sleep(0.3)

                self.show = pygame.sprite.Group((self.insrXB,) + (self.insrLeftB,))
                self.reset("assets/InstructionScreen_PG5.PNG")

            #===============================================================================================================================================================


            while self.state == "GAME":
               #exit button
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                      sys.exit()


               self.sian.empty
               self.sian.hold
            
               self.show = pygame.sprite.Group((self.ground,))
               self.reset("assets/GameScreen.PNG")
    







































