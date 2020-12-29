#--------------------------#
import sys
import pygame
from pygame import *
#--------------------------#
import xlrd
from xlrd import *
#--------------------------#
import xlwt
from xlwt import *


pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()

WINDOWSIZE = (1280, 720)  # window size

pygame.display.set_caption('LOGIN')
loginSound = pygame.mixer.Sound('..\soundFX\menu.wav')
icon = pygame.image.load("../image/racing.png")
pygame.display.set_icon(icon)
loginScreen = pygame.image.load('..\image\loginscreen.png')

def loginscreen():
    running = True
    while running:
        DISPLAYSURFACE = pygame.display.set_mode(WINDOWSIZE)
        DISPLAYSURFACE.blit(loginScreen, (0,0))
        userNameArea = pygame.Rect(40, 320, 375, 40)

        dx, dy = pygame.mouse.get_pos()

        if userNameArea.collidepoint(dx,dy):
            pygame.draw.rect(loginScreen, (0,255,0), userNameArea, 3)

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
                    running = False

        fpsClock.tick(FPS)
        pygame.display.update()

loginscreen()