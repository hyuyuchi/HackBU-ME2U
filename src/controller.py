import pygame
import sys
import random
import time
from src import Button
from src import Line
from src import Crow
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
        self.ground = Button.Button(0, 793, 163, 1700, "assets/GameScreen_Ground.PNG")
        self.crow = Crow.Crow(35, 200, 128, 163, "assets/Crow1.PNG", "assets/Crow2.PNG")
        self.theline = Line.Line(50, 600, 10, 10, "assets/Dot.PNG")








        self.show = pygame.sprite.Group()
        self.line = pygame.sprite.Group()

        self.state = "START"

        self.linestate = "n"
        self.num = 200
        self.numx = 500

    def mainLoop(self):
        while self.state == "START":
            self.gameLoop()


    def reset(self, image):
        self.theline.reset()
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

            #===========================================================================================================================================================
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

            #===========================================================================================================================================================


            while self.state == "GAME":
               #exit button
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()


                self.crow.update()
            
                self.show = pygame.sprite.Group((self.ground,) + (self.crow,))
                self.reset("assets/GameScreen.PNG")
    
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_0:
                            self.reset("assets/GameScreen.PNG")
                            self.theline.reset()
                            self.linestate = "y"
                            self.num += 50
                            self.numx += 8
                            print(self.num, self.numx)
                        if event.key == pygame.K_9:
                            self.reset("assets/GameScreen.PNG")
                            self.theline.reset()
                            self.linestate = "y"
                            self.numx -= 8
                            if self.num > 0:
                                self.num -= 50
                            print(self.num, self.numx)

                while self.linestate == "y":
                    self.theline.update(self.num, self.numx)
                    self.line.add((self.theline,))
                    self.line.draw(self.screen)
                    self.show.draw(self.screen)             
                    pygame.display.flip()
                    if self.theline.rect.x >= 1670:
                        self.linestate = "n"
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()





































