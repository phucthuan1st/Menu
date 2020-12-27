import pygame, sys
from pygame.locals import *
import time
import tkinter
from tkinter import *

from mainGame import runGame

'''anything go with rect use the form (left, top, width, height)'''

pygame.init()
#from this is the define for game statistics
FPS = 60
fpsClock = pygame.time.Clock()

WINDOWSIZE = (1280,720) #window size

pygame.display.set_caption('Racing bet 888') #set Caption for title bar

MAINMENUSCREEN = pygame.image.load('..\image\mainmenu.png')
MAINMENUSCREEN = pygame.transform.scale(MAINMENUSCREEN, WINDOWSIZE) #create background image

menuSound = pygame.mixer.Sound('..\soundFX\menu.wav') #open sound

DISPLAYSURFACE = pygame.display.set_mode(WINDOWSIZE) #create surface for mainmenu
gMoney = 0
characterSet = None

#define font using 
font = pygame.font.SysFont(None, 20, bold=True, italic=False) #set font for drawing
mediumfont = pygame.font.SysFont(None, 30, bold = True, italic = False)
bigfont = pygame.font.SysFont(None, 40, bold = True, italic = False)

#end define the game statistics
#------------------------------------------------------------------------------------------------#

#drawing text on screen
def draw_text(text, font, color, surface, x, y): 
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)
    return 1

#running main menu
def mainMenu(money, characterSet):
    Running = True
    clicked = False
    toggleMenuSub = False
    global IsPlaying

    while Running:
        #menuSound.play(-1) #repeat sound
        DISPLAYSURFACE.blit(MAINMENUSCREEN, (0,0)) #draw background
        draw_text(str(money), mediumfont, (255,0,0), DISPLAYSURFACE, 700, 630)
        draw_text('YOUR CURRENT SET IS: ' + str(characterSet), font, (0,0,0), DISPLAYSURFACE, 550, 200)
        #define the Buttons
        exitButton = pygame.Rect(40, 20, 100, 65)
        helpButton = pygame.Rect(55, 580, 110, 100)
        miniGameButton = pygame.Rect(200, 580, 110, 100)
        changeSetButton = pygame.Rect(350, 580, 110, 100)
        shopButton = pygame.Rect(885, 580, 90, 95)
        gameButton = pygame.Rect(1050, 580, 210, 100)
        playButton = pygame.Rect(1075, 470, 120, 40)
        changeNameButton = pygame.Rect(1075, 515, 120, 40)

        #GET MOUSE CLICK
        dx, dy = pygame.mouse.get_pos() #get clicked

        #if mouse click execute
        if exitButton.collidepoint(dx, dy):
            if clicked:
                exitConfirmScreen()
        if helpButton.collidepoint(dx, dy):
            if clicked:
                helpScreen()
        if miniGameButton.collidepoint(dx, dy):
            if clicked:
                money = miniGameScreen(money)
        if changeSetButton.collidepoint(dx, dy):
            if clicked:
                characterSet = changeSetScreen(characterSet)
        if shopButton.collidepoint(dx, dy):
            if clicked:
                money = shopScreen(money)
        if gameButton.collidepoint(dx, dy):
            if clicked:
                toggleMenuSub = not toggleMenuSub
        if playButton.collidepoint(dx, dy):
            IsPlaying = True
            if clicked and toggleMenuSub:
                 draw_text('PRESSED', mediumfont, (0,0,0), DISPLAYSURFACE, 500, 500)
                 runGame()
        if changeNameButton.collidepoint(dx, dy):
            if clicked and toggleMenuSub:
                draw_text('PRESSED', mediumfont, (0,0,0), DISPLAYSURFACE, 500, 500)
        clicked = False

    #checking exit game or input mouse click
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
    #if menusub is on then draw it                
        if toggleMenuSub:
            drawGameMenuSub()

    #update screen every frame of loop
        fpsClock.tick(FPS)
        pygame.display.update() #update screen every execution
    return Running #return the running status to main

def exitConfirmScreen():
    running = True
    clicked = False
    while running:
        DISPLAYSURFACE.fill((0,0,0))
        draw_text('Confirm Exit?', bigfont, (255,255,255), DISPLAYSURFACE, 500, 200)
        dx, dy = pygame.mouse.get_pos()

        #define and draw yes/no buttons
        yesButton = pygame.Rect(480, 300, 50, 50)
        noButton = pygame.Rect(680, 300, 50, 50)
        pygame.draw.rect(DISPLAYSURFACE, (255,255,255), yesButton)
        draw_text('Yes', font, (0,0,0), DISPLAYSURFACE, 490, 320)
        pygame.draw.rect(DISPLAYSURFACE, (255,255,255), noButton)
        draw_text('No', font, (0,0,0), DISPLAYSURFACE, 695, 320)

        if yesButton.collidepoint(dx,dy):
            if clicked:
                pygame.exit()
                sys.exit()
        elif noButton.collidepoint(dx,dy):
            if clicked:
                running = False

        clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        fpsClock.tick(FPS)
        pygame.display.update()
    return running

def drawHelp():
    draw_text('HELP', bigfont, (255,255,255), DISPLAYSURFACE, 620, 20)
    draw_text('Welcome to Racing Bet Game', mediumfont, (255,255,255), DISPLAYSURFACE, 500, 50)
    draw_text('Nothing to see here at this time', font, (255,255,255), DISPLAYSURFACE, 550, 100)
    draw_text('Press ESC Key to return Main Menu', font, (255,255,255), DISPLAYSURFACE, 530, 120)

def helpScreen():
    running = True
    while running:
        DISPLAYSURFACE.fill((0,0,0))
        drawHelp()
        #check event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        fpsClock.tick(FPS)
        pygame.display.update()

def miniGameScreen(money):
    running = True
    while running:
        DISPLAYSURFACE.fill((0,0,0))
        draw_text('Nothing to see at this time', bigfont, (255,255,255), DISPLAYSURFACE, 450, 300)
        money = miniGameEvent(money)
        draw_text('Money at this time is: ' + str(money), mediumfont, (255,255,255), DISPLAYSURFACE, 500, 400)
        draw_text('Press ESC Key to return Main Menu', font, (255,255,255), DISPLAYSURFACE, 530, 120)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        fpsClock.tick(FPS)
        pygame.display.update()
    return money

def miniGameEvent(money):
    money += 10
    return money

def changeSetScreen(selectedSet):
    running = True
    while running:
        DISPLAYSURFACE.fill((0,0,0))
        draw_text('CHOSE YOUR FAVORITE SET: ', bigfont, (255,255,255), DISPLAYSURFACE, 400, 50)
        draw_text('YOUR CURRENT SET IS: ' + str(selectedSet), mediumfont, (255,255,255), DISPLAYSURFACE, 450, 100) 
        draw_text('Press 1 to 5 to choose set', mediumfont, (255,255,255), DISPLAYSURFACE, 480, 150)
        draw_text('Press ESC Key to return Main Menu', mediumfont, (255,255,255), DISPLAYSURFACE, 415, 200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == ord('1'):
                    selectedSet = 1
                if event.key == ord('2'):
                    selectedSet = 2
                if event.key == ord('3'):
                    selectedSet = 3
                if event.key == ord('4'):
                    selectedSet = 4
                if event.key == ord('5'):
                    selectedSet = 5
                if event.key == K_ESCAPE:
                    running = False

        fpsClock.tick(FPS)
        pygame.display.update()
    return selectedSet

def shopScreen(money):
    running = True
    while running:
        DISPLAYSURFACE.fill((0,0,0))
        draw_text('Nothing at this time', bigfont, (255,255,255), DISPLAYSURFACE, 470, 300)
        draw_text('Money at this time is: ' + str(money), mediumfont, (255,255,255), DISPLAYSURFACE, 490, 350)
        draw_text('Press ESC Key to return Main Menu', font, (255,255,255), DISPLAYSURFACE, 490, 200)
        draw_text('Press 1 to 5 to buy', font, (255,255,255), DISPLAYSURFACE, 550, 400)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == ord('1'):
                    if money < 100:
                        draw_text('YOU DON\'T HAVE ENOUGHT MONEY', bigfont, (255,255,255), DISPLAYSURFACE, 400, 500)
                    else:
                        money -= 100
                if event.key == ord('2'):
                    if money < 200:
                        draw_text('YOU DON\'T HAVE ENOUGHT MONEY', bigfont, (255,255,255), DISPLAYSURFACE, 400, 500)
                    else: 
                        money -= 200
                if event.key == ord('3'):
                    if money < 300:
                        draw_text('YOU DON\'T HAVE ENOUGHT MONEY', bigfont, (255,255,255), DISPLAYSURFACE, 400, 500)
                    else:
                        money -= 300
                if event.key == ord('4'):
                    if money < 400:
                        draw_text('YOU DON\'T HAVE ENOUGHT MONEY', bigfont, (255,255,255), DISPLAYSURFACE, 400, 500)
                    else: 
                        money -= 400
                if event.key == ord('5'):
                    if money < 500:
                        draw_text('YOU DON\'T HAVE ENOUGHT MONEY', bigfont, (255,255,255), DISPLAYSURFACE, 400, 500)
                    else: 
                        money -= 500                       
                if event.key == K_ESCAPE:
                    running = False
        fpsClock.tick(FPS)
        pygame.display.update()
    return money

def drawGameMenuSub():
    subMenuArea = pygame.Rect(1060, 460, 150, 100)
    pygame.draw.rect(DISPLAYSURFACE, (255,255,255), subMenuArea)
    playButton = pygame.Rect(1075, 470, 120, 40)
    changeNameButton = pygame.Rect(1075, 515, 120, 40)
    pygame.draw.rect(DISPLAYSURFACE, (0,0,0), playButton, 3)
    pygame.draw.rect(DISPLAYSURFACE, (0,0,0), changeNameButton, 3)
    draw_text('PLAY', font, (0,0,0), DISPLAYSURFACE, 1115, 485)
    draw_text('CHANGE NAME', font, (0,0,0), DISPLAYSURFACE, 1080, 530)

def playScreen():
    pass

def changeNameScreen():
    pass

# Global Variables
IsPlaying = False
def main():
    Running = True
    while Running:
        Running = mainMenu(gMoney, characterSet)

if __name__ == "__main__":
    main()
#end of file