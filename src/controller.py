import pygame
import sys
import random
import time
import json
from src import Button
from src import Line
from src import Chia
from src import Sian
from src import Crow
from src import Gift

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
        self.theline = Line.Line(150, 600, 10, 10, "assets/Dot.PNG")
        self.chia = Chia.Chia(1400, 435, 221, 365, "assets/Chia_Standing.PNG","assets/Chia_Walking1+3.PNG", "assets/Chia_Walking2.PNG", "assets/Chia_Walking1+3.PNG", "assets/Chia_Walking4.PNG")
        self.sian = Sian.Sian(50, 435, 219, 364, "assets/Sian_Empty.PNG")
        self.empty = True
        self.holding_object = False
        self.score = 0
     


        self.gift = Gift.Gift(150, 600, 60, 60, "assets/LoveLetter.PNG")

        self.hearts = pygame.sprite.Group()
        for i in range(3):
            x = 170 + 50 * i
            y = 13
            self.hearts.add(Button.Button(x, y, 70, 70, "assets/Heart.PNG"))
        self.deadH = pygame.sprite.Group()

 
        self.scorepic10 = Button.Button(200, 93, 40, 40, "assets/0.PNG")
        self.scorepic1 = Button.Button(250, 93, 40, 40, "assets/0.PNG")       
        self.scorepic = pygame.sprite.Group((self.scorepic10,) + (self.scorepic1,))    
        self.numbers = [0]


        #GameOver buttons
        self.endPB = Button.Button(1100, 370, 109, 607, "assets/GameOverScreen_PlayAgainButton.PNG")


        #Timers
        self.happy_timer = 0
        self.happyy = False
        self.walktimer = 0
        self.angry_timer = 0
        self.angryy = False
        self.startwalk = False


        self.endRB = Button.Button(1150, 500, 104, 598, "assets/GameOverScreen_ReturnButton.PNG")
        self.scoreH10 = Button.Button(1270, 247, 35, 35, "assets/0.PNG")
        self.scoreH1 = Button.Button(1305, 247, 35, 35, "assets/0.PNG")       
        self.scoreH = pygame.sprite.Group((self.scoreH10,) + (self.scoreH1,))


#-----------------------------------------------------------------------------------------------------------LOAD SPRITES

        
        self.show = pygame.sprite.Group()
        self.line = pygame.sprite.Group()

        self.score = 0
        self.state = "START"

        self.linestate = "n"
        self.num = 500
        self.numx = 400

    def mainLoop(self):
        if self.state == "START":
            self.startLoop()
        elif self.state == "GAMEOVER":
            self.gameOver()

    def reset(self, image):
        self.theline.reset()
        self.background = pygame.transform.scale((pygame.image.load(image)), (1700,956))
        self.screen.blit(self.background, (0, 0))      
        self.show.draw(self.screen)          
        pygame.display.flip()
#---------------------------------------------------------------------------------------------------------------------------------DIVIDER

    def startLoop(self):
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
    
            if self.state == "GAME":
                self.gameLoop()

#------------------------------------------------------------------------------------------------------------------------------------------DIVIDER

    def fly(self):
        while True:
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   sys.exit()

            self.gift.update(self.num, self.numx)

            fall = pygame.sprite.collide_rect(self.ground, self.gift) or self.gift.rect.x > 1710
            if fall:
                if self.gift.state == "GOOD":
                    hearts = self.hearts.sprites()
                    dead = hearts[-1]
                    self.hearts.remove(dead)
                    self.deadH.add(dead)
                    print(len(self.hearts))
                self.gift.reset()
                self.gameLoop()

            catch = pygame.sprite.collide_rect_ratio(0.5)(self.chia, self.gift)
            if catch:

                if self.gift.state == "GOOD":
                   self.score += 1
                   self.chia.happy(221, 365)
                   self.happyy = True
                   self.startwalk = True

                elif self.gift. state == "BAD":
                   self.chia.angry(221, 365)
                   self.angryy = True

                   hearts = self.hearts.sprites()
                   dead = hearts[-1]
                   self.hearts.remove(dead)
                   self.deadH.add(dead)
                   #print(len(self.hearts))
                else:
                   self.score += 1
                   self.scorepic10.change(self.numbers, self.score//10)
                   self.scorepic1.change(self.numbers, self.score%10)
                   print(self.score//10, self.score%10)

                self.gift.reset()
                self.gameLoop()

            steal = pygame.sprite.collide_rect_ratio(0.5)(self.crow, self.gift)
            if steal:
               if self.gift.state == "GOOD" and self.score > 0:
                  self.score -= 1
               elif self.gift.state == "BAD":
                  self.score +=1
               self.gift.reset()
               self.gameLoop()

            self.crow.update()
            self.show = pygame.sprite.Group((self.ground,) + (self.crow,) + (self.sian,) + (self.gift,) + (self.chia,) + (self.hearts,) + (self.scorepic,))
            self.show.draw(self.screen)
            self.reset("assets/GameScreen.PNG")



    def gameLoop(self):
        pygame.key.set_repeat(1,50)

        while True:
           #exit button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     sys.exit()


            with open("src/data.json", "r") as jsonFile1:
                data1 = json.load(jsonFile1)
            good = data1["GoodObjects"]
            bad = data1["BadObjects"]
            sian = data1["Sian"]
            self.numbers = data1["numbers"]
            allObjects = []
            for i in good:
                allObjects.append(i)
            for j in bad:
                allObjects.append(j)



            if (self.empty == True):
                holds = random.choice(sian)
                self.gift.object(holds, allObjects, sian, good, bad)
                self.sian.hold(219, 364, holds)
                self.holding_object = True
                self.empty = False


            self.show = pygame.sprite.Group((self.ground,) + (self.crow,) + (self.sian,) + (self.chia,) + (self.hearts,) + (self.scorepic,))


            self.reset("assets/GameScreen.PNG")

    
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        self.linestate = "y"
                        self.num += 50
                        self.numx += 15

                        print(self.num, self.numx)
                    if event.key == pygame.K_9:
                        self.linestate = "y"
                        if self.num > 450:
                            self.num -= 50
                            self.numx -= 15
                            print(self.theline.rect.x, self.numx)
                    if event.key == pygame.K_1:
                        sys.exit()
                    if (self.holding_object == True):
                        if event.key == pygame.K_SPACE:
                            self.sian.throw(219, 364)
                            self.holding_object = False

                            self.fly()
                            
		
            if (self.holding_object == False):
                self.sian.empty(219, 364)
                

            if (self.happy_timer<=50 and self.happyy == True):
                self.happy_timer += 1

            if (self.happy_timer>=50):
                if (self.startwalk == True):
                    self.chia.startwalk()
                    self.happyy + False
                    self.startwalk == False
                elif self.walktimer <= random.randrange(5,11):
                    self.walk()
                    self.chia.update()
                    self.walktimer += 1
                elif self.walktimer > random.randrange(5,11):
                    self.chia.default(221, 365)
                    self.empty = True
                    self.walktimer = 0
                    self.happy_timer = 0

            if (self.angry_timer< 50 and self.angryy == True):
                self.angry_timer += 1

            else:
                self.angry_timer = 0
                self.angryy = False
                self.chia.default(221, 365)
                            
            while self.linestate == "y":
                self.theline.update(self.num, self.numx)
                self.line.add((self.theline,))
                self.line.draw(self.screen)
                #self.show.draw(self.screen)             
                pygame.display.flip()
                if self.theline.rect.x >= 1700:
                    self.linestate = "n"



            self.crow.update()
            if (len(self.hearts) == 0):
                self.state = "GAMEOVER"
                self.gameOver()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     sys.exit()

    def restart(self):
        for i in self.deadH:
            self.hearts.add(i)
        self.score = 0
        self.scorepic10.change(self.numbers, self.score//10)
        self.scorepic1.change(self.numbers, self.score%10)
        self.scorepic10.final(200, 93, 40, 40)
        self.scorepic1.final(250, 93, 40, 40)

    def gameOver(self):
        while self.state == "GAMEOVER":

            self.scorepic10.final(1300, 147, 70, 70)
            self.scorepic1.final(1360, 147, 70, 70)

            with open("src/data.json", "r") as jsonFile2:
                data2 = json.load(jsonFile2)
            most = int(data2["high"])
            if self.score > most:
                data2["high"] = self.score
            with open("src/data.json", "w") as jsonFile3:
                json.dump(data2, jsonFile3)
            jsonFile3.close()
            with open("src/data.json", "r") as jsonFile:
                data = json.load(jsonFile)
            highest = data["high"]
            self.scoreH10.change(self.numbers, highest//10)
            self.scoreH1.change(self.numbers, highest%10)

            
            self.show = pygame.sprite.Group((self.endRB,) + (self.endPB,) + (self.scorepic,) + (self.scoreH,))
            self.reset("assets/GameOverScreen_FullDisplay.PNG")

            if pygame.mouse.get_pressed()[0] and self.endRB.rect.collidepoint(pygame.mouse.get_pos()):
                self.restart()
                self.state = "START"
                self.mainLoop()    
            if pygame.mouse.get_pressed()[0] and self.endPB.rect.collidepoint(pygame.mouse.get_pos()):
                self.restart()
                self.gameLoop()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     sys.exit()






























