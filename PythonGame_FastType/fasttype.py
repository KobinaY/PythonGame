from tkinter import *
import random
import math
#from PIL import ImageTk, Image
import time
import sys
import imghdr
#import os
#import winsound #uncomment this line to play sound on windows computer
from random_word import RandomWords

#Key variables
game_WIDTH = 800
game_HEIGHT = 600
a = ""
b = ""
c = ""
t = ""
userW = ""
gstart = False
gameOv = False
point = 0
posl = 80
posr = 80
posd = 80
dsP = 0
tLeft = 20 # Time left

window = Tk()
canvas = Canvas(window, bg = "black",width = game_WIDTH, height = 600)
canvas.pack()

#wordList = open('words1.txt', 'r',encoding='utf-8', errors='ignore')
#words = [line.split(',') for line in wordList.readlines()]

#Array of word that are randomly picked and displayed
words = ['apple', 'earth', 'ear', 'planet', 'python', 'a', 'b', 'c', 'd', 'success', 'smile',
         'joker', 'wind', 'fire','Awesome', 'Science', 'books', 'pen','Universe','COPPER', 'unite',
         'UNITY','decisive','BRANCH','copper','unfasten','doll','wistful','sophisticated','magnificent'
         ,'rabid','education','numerous','plantation','embarrassed','wacky','dust','teeny-tiny','FAX'
         ,'influence','scientific','supply','mate','spring','gabby','title','release','scare','pine',
         'rule','toys','distinct','present','cloth','mitten','How fast can you type']

#Random words from using package random-word
words2 = RandomWords()

        





#Random word picker and color
rndw = random.choice(words)
rndw2 = words2.get_random_word()
color = ("#%06x" % random.randint(1, 0xFFFFFF))
color1 = ("#%06x" % random.randint(1, 0xFFFFFF))

def startGame():
        global words
        global words2 
        #print(words)
        count = 0
        global posl
        

        window.bind("<Key>", userInput)
        
 
        canvas.update()
        createfast(canvas)
        createype(canvas)
        createload(canvas)
        moveLeftRight()
                
        #window.mainloop()

def moveLeftRight():
        global posl
        global posr
        posl += 10
        posr += 10
        canvas.delete(ALL)
        createfast(canvas)
        createype(canvas)
        createload(canvas)
        delay = 100
        if posl < 500:
         canvas.after(delay,moveLeftRight)
         print(posl,posr)
         
        
        if (posl == 500):
                gstart = True
                canvas.configure(background = "white")
                canvas.delete(ALL)
                loadGUI()
                
        
                
        
               
                
def loadGUI():
        canvas.delete(ALL)
        word(rndw2,point,tLeft)
        #window.bind("<Key>", userInput)
        #if(event.char in rndw):
                #print("Its in there")
        gameTime()
        
def createfast(canvas):
    canvas.create_text((game_WIDTH / 2) - posl, game_HEIGHT / 2,fill="orange",font="Sanrif 70 italic bold",
                        text="FAST")
def createype(canvas):
    canvas.create_text((game_WIDTH / 2) + posr, game_HEIGHT / 2,fill="white",font="Sanrif 70  bold",
                        text="YPE")
def createload(canvas):
    canvas.create_text((game_WIDTH / 2) + posd, (game_HEIGHT / 2) + 70 ,fill="white",font="Sanrif 20 italic ",
                        text="Loading ....")
def word(rndw,point,tLeft):
        a = canvas.create_rectangle(0,100,game_WIDTH, 40, fill = "black" )
        b = canvas.create_text(80, 70, fill = "green", font = "Sanrif 25",text = "SCORE : ")
        b = canvas.create_text(600, 70, fill = "yellow", font = "Sanrif 25",text = "Time ")
        b = canvas.create_text(400, 70, fill = "yellow", font = "Sanrif 15",text = "Level 1")
        b1 = canvas.create_text(190, 70, fill = "white", font = "Sanrif 25",text = point)
        canvas.create_text((game_WIDTH / 2), game_HEIGHT / 4,fill = "red",font="Sanrif 13 ",
                        text = "Type the word below")
        canvas.create_text((game_WIDTH / 2), game_HEIGHT / 2,fill= color,font="Sanrif 50 ",
                        text = rndw)
        canvas.create_oval(650,10,790,150,fill = "black" , outline ="yellow")
        t = canvas.create_text(720, 75, fill = "yellow", font = "Sanrif 70",text = tLeft)
        
        img = PhotoImage("keyphoto.jpg")
        canvas.create_image(0,0, image = img)

        
        #b = canvas.create_image(0,0, anchor= CENTER, image=img)
        
#Reload game interface
def playAgain():
        canvas.delete(ALL)
        canvas.configure(background = "white")
        global tLeft
        global dsP
        global userW
        global gameOv
        tLeft += 21
        point = 0
        dsP = 0
        userW = ""
        loadGUI()

#End program        
def quitGame():
        window.destroy()

#Count down timer
def gameTime():
        
        global tLeft
        global dsP
        global rndw2
        global point
        global gameOv
        tLeft -= 1
        canvas.delete(ALL)
        word(rndw2,point,tLeft)
        print("Time Left: ",tLeft)
        if (tLeft > 0):
                canvas.after(1000,gameTime)
        if(tLeft == 0):
                canvas.delete(ALL)
                gameOv = True
                print("GAME OVER")
                gameOver()
                point = 0
                
                        
                
#Game Over interceptor                        
def gameOver():
        canvas.delete(ALL)
        canvas.configure(background = "black")
        canvas.create_text((game_WIDTH / 2), game_HEIGHT / 2,fill="orange",font="Sanrif 90 ",
                        text = "GAME OVER")
        b = canvas.create_text((game_WIDTH/ 2) - 50, 100, fill = "yellow", font = "Sanrif 35 ",text = "SCORED : ")
        b1 = canvas.create_text((game_WIDTH / 2) + 125, 100, fill = "white", font = "Sanrif 35 bold",text = point)
        b2 = canvas.create_text((game_WIDTH / 2), 500, fill = "White", font = "Sanrif 20", text = "PLAY AGAIN?")
        canvas.create_text((game_WIDTH / 2), 550, fill = "White", font = "Sanrif 20", text = "enter :  Y = Play or N = Quit ")
        

        

#Keyboard input handler
def userInput(event):
        global rndw2
        global userW
        global point
        global tLeft
        global gameOv
        global color
        global Letes
        print("Word length : ",len(rndw2))
        
        if(gameOv == False):
                if(event.char in rndw2.lower() and (len(userW) != len(rndw2))):
                        userW += event.char
                        print(event.char)
                        point += 1
                        canvas.delete(ALL)
                        word(rndw2,point,tLeft)
                        print("user typed :",userW)
                elif(event.char in userW ):
                        point += 0
                elif(event.char not in rndw2.lower()):
                        userW += event.char
                        print("You typed : ",userW)
                        point -= 1
                        canvas.delete(ALL)
                        word(rndw2,point,tLeft)
                if(userW.lower() == rndw2.lower()):
                        #Uncomment line below to play sound on windows computer
                        #winsound.PlaySound("shooting.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
                        canvas.delete(ALL)
                        #rndw = random.choice(words)
                        rndw2 = words2.get_random_word()
                        color = ("#%06x" % random.randint(1, 0xFFFFFF))
                        color1 = ("#%06x" % random.randint(1, 0xFFFFFF))
                        #canvas.configure(background = color1)
                        userW = ""
                        point += 20
                        print("Point is 100")
                        word(rndw2,point,tLeft)
                elif(len(userW) == len(rndw2)):
                        gameOv = True
                        print("GAME OVER")
                        gameOver()
                        tLeft = 1
                
        
        elif(gameOv == True):
                Yes = "Yy"
                No = "Nn"
                print("Time left :",tLeft)
                if(event.char in Yes):
                        gameOv = False
                        playAgain()
                else:
                        if(event.char in No):
                                quitGame()       
                         
                         
        
                

startGame()




