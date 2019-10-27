### Import ###
import pygame as pg
from pygame.locals import *
import random as rd

### Init ###
pg.init()

### Variables ###
_continue = True

_table = [["","",""],
         ["","",""],
         ["","",""]]

_isPlayer1 = True
_actual_sign = ""

_l = 1920
_L = 1080

window = pg.display.set_mode((_l,_L))

_points = [0,0]
_winner = ""

# Mouse Init
_x, _y, _B1, _B2, _B3 = 0, 0, 0, 0, 0

### Images ###
ImgPlaceVoid = pg.image.load(".\Images\Void.png")
ImgPlaceX = pg.image.load(".\Images\Cross.png").convert_alpha()
ImgPlaceO = pg.image.load(".\Images\Circle.png").convert_alpha()
ImgTable = pg.image.load("#")

### Fonts ###
# A Faire

### Definitions###
# Game
def WinnerTest():
    if _points[0] == 3:
        _winner = "P1"
        _continue = False

    elif _points[1] == 3:
        _winner = "P2"
        _continue = False

    return _winner, _continue

def VoidTable():
    pass

def PlaceSymbol(symbol = "C"):
    pass

# Menu
def PrintMenu():
    pass

def PrintSettings():
    pass

# Mouse's detection
def Mouse():
    # Position
    _x, _y = pg.mouse.get_pos()

    # Clicks
    _B1, _B2, _B3 = pg.mouse.get_pressed()

    return _x, _y, _B1, _B2, _B3


### Start of the project ###
while _continue:

    # Winner verification
    WinnerTest()

    # Events
    for event in pg.event.get():
        if event.type == QUIT:
            _continue = False

        elif event.type == KEYDOWN:
            #Escape
            if event.key in [K_ESCAPE]:
                _continue = False

# Quit the game
pg.quit()