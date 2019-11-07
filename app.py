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

_coords = [[(15,15),(365,15),(715,15)],
            [(15,365),(365,365),(715,365)],
            [(15,715),(365,715),(715,715)]]

_coords_test = [[0,0,357,375],[357,0,707,357],[707,0,1080,375],
                [0,357,357,707],[357,357,707,707],[707,357,1080,707],
                [0,707,375,1080],[357,707,707,1080],[707,707,1080,1080]]

_isPlayer1 = True
_actual_sign = ""

_l = 1080
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
    global _coords, _table

    # Background
    # Returning the table w\ symbol in it
    _table = [["","",""],
            ["","",""],
            ["","",""]]

    # Graphic
    # Flip w\ symbols
    for place in _coords:
        for x, y in place:
            window.blit(ImgPlaceVoid,(x,y))

    pg.display.flip()

def PlaceSymbol(x, y, symbol = "C"):
    # Background
    # Coords of the img placement
    for place in _coords_test:

        _x1, _x2, _y1, _y2 = place[0], place[1], place[2], place[3]

        # In the screen
        if x >= 0 and x <= 1080:
            if y >= 0 and y <= 1080:

                # In each case, x and y
                if x >= _x1 and x <= _x2:
                    if y >= _y1 and y <= _y2:

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

VoidTable()
### Start of the project ###
while _continue:

    # Winner verification
    WinnerTest()

    # Event clic
    if Mouse()[3] == 1:
        PlaceSymbol(Mouse()[0],Mouse()[1],_actual_sign)


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