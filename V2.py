
#Start = 16:49
### Import + Init ###
import pygame as pg
from pygame.locals import *
pg.init()

### Vars ###

_table = [" ", " ", " ",
          " ", " ", " ",
          " ", " ", " "]

_continue = True
_verif_cases = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(3,4,6))

_coords_imgs = [(15,15),(365,15),(715,15),
            (15,365),(365,365),(715,365),
            (15,715),(365,715),(715,715)]

_coords_test = [[0,0,357,375,0],[357,0,707,357,1],[707,0,1080,375,2],
                [0,357,357,707,3],[357,357,707,707,4],[707,357,1080,707,5],
                [0,707,375,1080,6],[357,707,707,1080,7],[707,707,1080,1080,8]]

_j1 = "X"
_j2 = "O"

_actual_player = _j1

# Pygame
window = pg.display.set_mode((1080, 1080),FULLSCREEN)
ImgPlaceVoid = pg.image.load(".\Images\Void.png")
ImgPlaceX = pg.image.load(".\Images\Cross.png").convert_alpha()
ImgPlaceO = pg.image.load(".\Images\Circle.png").convert_alpha()

# Mouse
_x, _y, _B1, _B2, _B3 = 0, 0, 0, 0, 0


### Defs ###
def DrawTable():
    # Last version w/ Pygame #
    """
    print(_table[0], "|", _table[1], "|", _table[2])
    print("---------")
    print(_table[3], "|", _table[4], "|", _table[5])
    print("---------")
    print(_table[6], "|", _table[7], "|", _table[8])
    """
    # Actual Version #
    for case in range(9):
        if _table[case] == " ":
            window.blit(ImgPlaceVoid, _coords_imgs[case])
        elif _table[case] == "X":
            window.blit(ImgPlaceX, _coords_imgs[case])
        elif _table[case] == "O":
            window.blit(ImgPlaceO, _coords_imgs[case])

    pg.display.flip()

def PosSymbolTable(px_player = "1"):
    global _continue
    played = False

    while not played:
        x = Mouse()[0]
        y = Mouse()[1]

        if Mouse()[2] == 1:
            for place in _coords_test:
                _x1, _x2, _y1, _y2, place_table = place[0], place[1], place[2], place[3], place[4]

                # In the screen
                if x >= 0 and x <= 1080:
                    if y >= 0 and y <= 1080:

                        # In each case, x and y
                        if x >= _x1 and x <= _x2:
                            if y >= _y1 and y <= _y2:
                                # In the Table
                                if _table[place_table] == " ":
                                    pos = place_table

                                    if px_player == "1":
                                        _table[pos] = _j1
                                        print(pos)
                                        print(_x1, _x2, _y1, _y2)
                                        played = True
                                    elif px_player == "2":
                                        _table[pos] = _j2
                                        print(pos)
                                        print(_x1, _x2, _y1, _y2)
                                        played = True
                                    else:
                                        played = False

        # Events
        for event in pg.event.get():
            if event.type == QUIT:
                played = True
                _continue = False

            elif event.type == KEYDOWN:
                # Escape
                if event.key in [K_ESCAPE]:
                    played = True
                    _continue = False

def VerifTable(px_symbol):
  for case in _verif_cases:
    if _table[case[0]] == px_symbol:
      if _table[case[1]] == px_symbol:
        if _table[case[2]] == px_symbol:
          print("Le joueur ",px_symbol," a gagné !")
          _continue = False
          return _continue
  _continue = True
  return _continue

def Mouse():
    # Position
    _x, _y = pg.mouse.get_pos()

    # Clicks
    _B1, _B2, _B3 = pg.mouse.get_pressed()

    return _x, _y, _B1, _B2, _B3

DrawTable()
### Game ###
while _continue:

    # Change of player
    if _actual_player == _j1:
        PosSymbolTable("1")
        DrawTable()
        _continue = VerifTable(_j1)
        _actual_player = _j2
    else:
        PosSymbolTable("2")
        DrawTable()
        _continue = VerifTable(_j2)
        _actual_player = _j1

    # Verif Table Complete
    count = 0
    for i in range(0, 9):
        if _table[i] != " ":
            count += 1
    if count == 9:
        _continue = False

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