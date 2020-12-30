import pygame, sys

import time

from pygame.locals import *

from mainGame import *

import pandas as pd

'''anything go with rect use the form (left, top, width, height)'''
pygame.init()

#from this is the define for game statistics
FPS = 60
fpsClock = pygame.time.Clock()
gMoney = 0

#access to database
database = pd.ExcelFile("../database.xlsx")
data = pd.read_excel(database, 0, header=None)

#windows statics
WINDOWSIZE = (1280,720) #window size
pygame.display.set_caption('Racing bet 888') #set Caption for title bar
menuSound = pygame.mixer.Sound('../soundFX/menu.wav') #open sound
DISPLAYSURFACE = pygame.display.set_mode(WINDOWSIZE) #create surface for mainmenu
loginscreen = pygame.image.load('../image/loginscreen.png')
changeSet = pygame.image.load('../image/changeSet.png')
donate = pygame.image.load('../image/donateRaiseRacingGame.png')

#define the set image
set0 = '../image/set0.png'
set1 = '../image/set1.png'
set2 = '../image/set2.png'
set3 = '../image/set3.png'
set4 = '../image/set4.png'
set5 = '../image/set5.png'
setIndex = [set0, set1, set2, set3, set4, set5]
characterSet = 0
loginSound = pygame.mixer.Sound("../soundFX/loginsound.wav")
loginScreen = pygame.image.load("../image/loginscreen.png")

font = pygame.font.SysFont(None, 20, bold=True, italic=False) #set font for drawing
userNameFont = pygame.font.SysFont(None, 25, bold=True, italic=True)
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


def loginscreen():
    running = True
    clicked = False
    loginSound.play(-1)
    show = True
    inputUserName = ""
    inputPassword = ""
    censoredPassword = ""
    typingUserName = False
    typingPassword = False
    pushLoginButtn = False
    while running:
        DISPLAYSURFACE = pygame.display.set_mode(WINDOWSIZE)
        DISPLAYSURFACE.blit(loginScreen, (0, 0))
        DISPLAYSURFACE.blit(donate, (1080, 0))
        draw_text('DONATE TO HELP THE DEVELOPMENT', font, (255,255,255), DISPLAYSURFACE, 1000, 200)
        userNameArea = pygame.Rect(40, 320, 375, 37)
        passwordArea = pygame.Rect(40, 397, 374, 40)
        loginButton = pygame.Rect(312, 460, 99, 32)
        dx, dy = pygame.mouse.get_pos()

        if show:
            draw_text('Now Playing: NIVIRO - Demons (No Copyright Sound)', font, (255,255,255), DISPLAYSURFACE, 1, 705)
        show = not show

        if userNameArea.collidepoint(dx, dy):
            pygame.draw.rect(DISPLAYSURFACE, (0, 255, 0), userNameArea, 3)
            if clicked:
                typingUserName = True
                typingPassword = False
                print(inputUserName)
        if passwordArea.collidepoint(dx, dy):
            pygame.draw.rect(DISPLAYSURFACE, (0, 255, 0), passwordArea, 3)
            if clicked:
                typingPassword = True
                typingUserName = False
                print(inputPassword)
        if loginButton.collidepoint(dx, dy):
            pygame.draw.rect(DISPLAYSURFACE, (0, 255, 0), loginButton, 3)
            if clicked:
                TypingPassword = False
                TypingUserName = False
                pushLoginButtn = True


        clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if inputUserName == "" or inputPassword == "":
                        pushLoginButtn = False
                    else:
                        running = False
                        username = inputUserName
                        password = inputPassword
                else:
                    if typingUserName and not typingPassword:
                        if event.key == K_BACKSPACE:
                            inputUserName = inputUserName[0:-1]
                        else:
                            inputUserName += event.unicode
                    elif typingPassword and not typingUserName:
                        if event.key == K_BACKSPACE:
                            inputPassword = inputPassword[0:-1]
                            censoredPassword = censoredPassword[0:-1]
                        else:
                            inputPassword += event.unicode
                            censoredPassword += '*'
            if pushLoginButtn:
                if inputUserName == "" or inputPassword == "":
                    pushLoginButtn = False
                else:
                    running = False
                    username = inputUserName
                    password = inputPassword

            draw_text(inputUserName, font, (0,0,0), DISPLAYSURFACE, 45, 330)
            draw_text(censoredPassword, font, (0,0,0), DISPLAYSURFACE, 45, 407)
        fpsClock.tick(FPS)
        pygame.display.update()
    loginSound.stop()
    return username, password


#running main menu
def mainMenu(money, characterSet, username):
    Running = True #check if running
    clicked = False #get clicked
    show = True #music description info
    menuSound.play(-1) #playing background music
    while Running:
        #define the display
        MAINMENUSCREEN = pygame.image.load(setIndex[characterSet])
        MAINMENUSCREEN = pygame.transform.scale(MAINMENUSCREEN, WINDOWSIZE)
        DISPLAYSURFACE.blit(MAINMENUSCREEN, (0,0)) #draw background
        displayUserNameArea = (250, 87, 190, 43)
        moneyArea = (600, 605, 250, 62)
        pygame.draw.rect(DISPLAYSURFACE, (255,255,255), displayUserNameArea)
        pygame.draw.rect(DISPLAYSURFACE, (255,255,255), moneyArea)
        pygame.draw.rect(DISPLAYSURFACE, (255, 0, 0), moneyArea, 3)
        draw_text(username, userNameFont, (255, 0, 255), DISPLAYSURFACE, 260, 100)
        draw_text(str(money), mediumfont, (255,0,0), DISPLAYSURFACE, 700, 630)

        #define the bet button
        bet1Button = pygame.Rect(5, 298, 200, 153)
        bet2Button = pygame.Rect(210, 298, 200, 153)
        bet3Button = pygame.Rect(410, 298, 200, 153)
        bet4Button = pygame.Rect(610, 298, 200, 153)
        bet5Button = pygame.Rect(810, 298, 280, 153)
        bet6Button = pygame.Rect(1010, 298, 280, 153)

        #show the music description
        if show:
            draw_text('Now Playing: Linko - Goodbye (No Copyright Sound)', font, (255,255,0), DISPLAYSURFACE, 500, 705)
        show = not show

        #define the Buttons used in main menu
        exitButton = pygame.Rect(58, 42, 82, 67)
        helpButton = pygame.Rect(55, 580, 110, 100)
        miniGameButton = pygame.Rect(212, 575, 100, 100)
        changeSetButton = pygame.Rect(360, 580, 110, 100)
        shopButton = pygame.Rect(888, 582, 93, 95)
        gameButton = pygame.Rect(1050, 580, 210, 100)
        playButton = pygame.Rect(1075, 465, 120, 45)
        changeNameButton = pygame.Rect(1075, 515, 120, 40)
        logOutButton = pygame.Rect(1213, 5, 68, 68)

        #GET MOUSE CLICK
        dx, dy = pygame.mouse.get_pos() #get clicked

        #if mouse click execute
        if characterSet == 2:
            frame = (0,0,0)
        else:
            frame = (255,255,255)
        if exitButton.collidepoint(dx, dy):
            if clicked:
                exitConfirmScreen()
        if helpButton.collidepoint(dx, dy):
            pygame.draw.rect(DISPLAYSURFACE, frame, helpButton, 3)
            if clicked:
                helpScreen()
        if miniGameButton.collidepoint(dx, dy):
            pygame.draw.rect(DISPLAYSURFACE, frame, miniGameButton, 3)
            if clicked:
                money = miniGameScreen(money)
        if changeSetButton.collidepoint(dx, dy):
            pygame.draw.rect(DISPLAYSURFACE, frame, changeSetButton, 3)
            if clicked:
                characterSet = changeSetScreen(characterSet)
        if shopButton.collidepoint(dx, dy):
            pygame.draw.rect(DISPLAYSURFACE, frame, shopButton, 3)
            if clicked:
                money = shopScreen(money)
        if gameButton.collidepoint(dx, dy):
            pygame.draw.rect(DISPLAYSURFACE, frame, gameButton, 3)
            if clicked:
                if characterSet == 0:
                    characterSet = 1
                money = runGame(2, characterSet, money)
                menuSound.play(-1)
        if logOutButton.collidepoint(dx, dy):
            if clicked:
                menuSound.stop()
                loginscreen()

        #not code yet
        clicked = False

    #checking exit game or input mouse click
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True

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
    clicked = False
    while running:
        DISPLAYSURFACE.blit(changeSet, (0,0))

        draw_text('Your current set is: ' + str(selectedSet), font, (0,0,0), DISPLAYSURFACE, 500, 200)

        if clicked:
            running = False

        set1Button = pygame.Rect(5, 298, 200, 153)
        set2Button = pygame.Rect(230, 298, 200, 153)
        set3Button = pygame.Rect(465, 298, 200, 153)
        set4Button = pygame.Rect(710, 298, 200, 153)
        set5Button = pygame.Rect(950, 298, 280, 153)

        dx, dy = pygame.mouse.get_pos()

        if set1Button.collidepoint(dx, dy):
            pygame.draw.rect(DISPLAYSURFACE, (0,0,0), set1Button, 3)
            if clicked:
                selectedSet = 1
        if set2Button.collidepoint(dx, dy):
            pygame.draw.rect(DISPLAYSURFACE, (0,0,0), set2Button, 3)
            if clicked:
                selectedSet = 2
        if set3Button.collidepoint(dx, dy):
            pygame.draw.rect(DISPLAYSURFACE, (0,0,0), set3Button, 3)
            if clicked:
                selectedSet = 3
        if set4Button.collidepoint(dx, dy):
            pygame.draw.rect(DISPLAYSURFACE, (0,0,0), set4Button, 3)
            if clicked:
                selectedSet = 4
        if set5Button.collidepoint(dx, dy):
            pygame.draw.rect(DISPLAYSURFACE, (0,0,0), set5Button, 3)
            if clicked:
                selectedSet = 5

        clicked = False

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
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True

        fpsClock.tick(FPS)
        pygame.display.update()
    return selectedSet

dontHavemoney = 'YOU DON\'T HAVE ENOUGH MONEY'

def shopScreen(money):
    running = True
    while running:
        DISPLAYSURFACE.fill((0, 0, 0))
        draw_text('Nothing at this time', bigfont, (255, 255, 255), DISPLAYSURFACE, 470, 300)
        draw_text('Money at this time is: ' + str(money), mediumfont, (255, 255, 255), DISPLAYSURFACE, 490, 350)
        draw_text('Press ESC Key to return Main Menu', font, (255,255,255), DISPLAYSURFACE, 490, 200)
        draw_text('Press 1 to 5 to buy', font, (255, 255, 255), DISPLAYSURFACE, 550, 400)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == ord('1'):
                    if money < 100:
                        draw_text(dontHavemoney, bigfont, (255, 255, 255), DISPLAYSURFACE, 400, 500)
                    else:
                        money -= 100
                if event.key == ord('2'):
                    if money < 200:
                        draw_text(dontHavemoney, bigfont, (255, 255, 255), DISPLAYSURFACE, 400, 500)
                    else:
                        money -= 200
                if event.key == ord('3'):
                    if money < 300:
                        draw_text(dontHavemoney, bigfont, (255, 255, 255), DISPLAYSURFACE, 400, 500)
                    else:
                        money -= 300
                if event.key == ord('4'):
                    if money < 400:
                        draw_text(dontHavemoney, bigfont, (255, 255, 255), DISPLAYSURFACE, 400, 500)
                    else:
                        money -= 400
                if event.key == ord('5'):
                    if money < 500:
                        draw_text(dontHavemoney, bigfont, (255, 255, 255), DISPLAYSURFACE, 400, 500)
                    else:
                        money -= 500
                if event.key == K_ESCAPE:
                    running = False
        fpsClock.tick(FPS)
        pygame.display.update()
    return money


def drawGameMenuSub(set):
    if set == 1:
        textColor = (0,0,0)
        buttonColor = (255,255,255)
    else:
        textColor = (255, 255, 255)
        buttonColor = (0, 0, 0)
    playButton = pygame.Rect(1075, 470, 120, 40)
    changeNameButton = pygame.Rect(1075, 515, 120, 40)
    pygame.draw.rect(DISPLAYSURFACE, buttonColor, playButton)
    pygame.draw.rect(DISPLAYSURFACE, buttonColor, changeNameButton)
    draw_text('PLAY', font, textColor, DISPLAYSURFACE, 1115, 485)
    draw_text('CHANGE NAME', font, textColor, DISPLAYSURFACE, 1080, 530)


def changeNameScreen():
    pass


def main():
    username, password = loginscreen()
    mainMenu(gMoney, characterSet, username)


if __name__ == "__main__":
    main()

# end of file
