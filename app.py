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

_coords = [[(0,0),(357.5,0),(707.5,0)],
            [(0,357.5),(357.5,357.5),(707.5,357.5)],
            [(0,707.5),(357.5,707.5),(707.5,707.5)]]

_isPlayer1 = True
_actual_sign = ""

_l = 1920
_L = 1080

window = pg.display.set_mode((_l,_L), FULLSCREEN)

_points = [0,0]
_winner = ""

# Mouse Init
_x, _y, _B1, _B2, _B3 = 0, 0, 0, 0, 0

### Images ###
ImgPlaceVoid = pg.image.load(".\Images\Void.png")
ImgPlaceX = pg.image.load(".\Images\Cross.png").convert_alpha()
ImgPlaceO = pg.image.load(".\Images\Circle.png").convert_alpha()

### Fonts ###
# A Faire

### Definitions###
# Game
def WinnerTest():
    # Globals
    global _winner, _continue

    if _points[0] == 3:
        _winner = "P1"
        _continue = False

    elif _points[1] == 3:
        _winner = "P2"
        _continue = False


def VoidTable():
    # Background
    # Returning the table w\ symbol in it
    _table = [["","",""],
            ["","",""],
            ["","",""]]
    return _table

    # Graphic
    # Flip w\ symbols
    for place in _coords:
        for x, y in place:
           window.blit(ImgPlaceVoid,(x,y))
            
    pg.display.flip()

def PlaceSymbol(symbol = "C"):
    # Background
    #######A FAIRE#######

    # Graphic
    # Coords of the img placement
    for place in _coords:
        for x, y in place:
            if _x <= x:
                if _y <= y:
                    img_coords = (x, y)

    # Choice of the symbol bcs of the parameter
    if symbol == "C":
        img = ImgPlaceX
    else:
        img = ImgPlaceO

    # Placement of the symbol
    window.blit(img, img_coords)

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

    # Void test
    VoidTable()

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