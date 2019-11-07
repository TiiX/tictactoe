
#Start = 16:49
### Import + Init ###
import pygame as pg
from pygame.locals import *
pg.init()

### Vars ###

_table = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
_continue = True
_verif_cases = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(3,4,6))

# Choice of the symbol for the player 1 and 2
choice = str(input("X or O ?").upper())
if choice == "X":
    _j1 = "X"
    _j2 = "O"
else:
    _j1 = "O"
    _j2 = "X"

_actual_player = _j1

# Pygame
window = pg.display.set_mode((1080, 1080),FULLSCREEN)



### Defs ###
def DrawTable():
    #Last version w/ Pygame#
    """
    print(_table[0], "|", _table[1], "|", _table[2])
    print("---------")
    print(_table[3], "|", _table[4], "|", _table[5])
    print("---------")
    print(_table[6], "|", _table[7], "|", _table[8])
    """

def PosSymbol(px_player="1"):
    played = False
    while not played:
        pos = int(input("What position ?"))
        pos -= 1
        if px_player == "1" and _table[pos] == " ":
            _table[pos] = _j1
            played = True
        elif px_player == "2" and _table[pos] == " ":
            _table[pos] = _j2
            played = True
        else:
            print("Change your position")
            played = False

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



### Game ###
while _continue:

    # Change of player
    if _actual_player == _j1:
        PosSymbol("1")
        DrawTable()
        _continue = VerifTable(_j1)
        _actual_player = _j2
    else:
        PosSymbol("2")
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