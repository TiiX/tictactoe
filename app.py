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

window = pg.display.set_mode((l,L), pg.FULLSCREEN)

points = [0,0]



###Definitions###



###Start of the project###
while _continue or points[0] != 3 or points[1] != 3:

    # Verification events
    for event in pg.event.get():
        if event.type == QUIT:
            _continue = False
            print("Hey !")

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                _continue = False

#Quit the game
pg.quit()