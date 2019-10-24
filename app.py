###Import###
import pygame as pg
from pygame.locals import *
import random as rd

###Init###
pg.init()


###Variables###
_continue = True

table = [["","",""],
         ["","",""],
         ["","",""]]

IsPlayer1 = True
actual_sign = ""

l = 1920
L = 1080

window = pg.display.set_mode((l,L))

points = [0,0]
winner = ""

###Images###
ImgPlaceVoid = pg.image.load("#")
ImgPlaceX = pg.image.load("#").convert_alpha()
ImgPlaceO = pg.image.load("#").convert_alpha()
ImgTable = pg.image.load("#")

###Font###
#A Faire

###Definitions###
def WinnerTest():
    if points[0] == 3:
        winner = "P1"
        _continue = False

    elif points[1] == 3:
        winner = "P2"
        _continue = False

    return winner, _continue

def VoidTable():
    pass

def PrintSymbol(symbol = "C"):
    pass

###Start of the project###
while _continue:

    #Winner verification
    WinnerTest()

    # Events gestion
    for event in pg.event.get():
        if event.type == QUIT:
            _continue = False

        elif event.type == KEYDOWN:
            #Escape
            if event.key in [K_ESCAPE]:
                _continue = False

#Quit the game
pg.quit()