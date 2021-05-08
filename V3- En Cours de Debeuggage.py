# Jeu fait par Arthur Nordmann (Tous droits reserves)
### IMPORT ###
import pygame as pg
from pygame.locals import *
pg.init()



### VARS ###

#Joueurs
j1 = "X"
j2 = "O"

#Tableau de signes
tableau = ["","","",
            "","","",
            "","",""]

verif_cases = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(3,4,6))

signe_actuel = j1

fin_jeu = False
choix_fait = False
tours = 0

coords_imgs = [(15,15),(365,15),(715,15),
               (15,365),(365,365),(715,365),
               (15,715),(365,715),(715,715)]

coords_test = [[(0,0),(357,375),0],[(357,0),(707,357),1],[(707,0),(1080,375),2],
               [(0,357),(357,707),3],[(357,357),(707,707),4],[(707,357),(1080,707),5],
               [(0,707),(375,1080),6],[(357,707),(707,1080),7],[(707,707),(1080,1080),8]]



### PYGAME ###
window = pg.display.set_mode((1080,1080), FULLSCREEN)

# Mouse Init
x, y, B1 = 0, 0, 0

position = False

### Images ###
# In Game
ImgPlaceVoid = pg.image.load(".\Images\Void.png")
ImgPlaceX = pg.image.load(".\Images\Cross.png").convert_alpha()
ImgPlaceO = pg.image.load(".\Images\Circle.png").convert_alpha()

# Menu
ImgVersus = pg.image.load(".\Images\Versus.png")
ImgComputer = pg.image.load(".\Images\Computer.png")
coords_menu = [[(15,15),0,0,1080,540],[(15,547),0,540,1080,1080]]



### DEFS ###
def PrintTableau():
    print(tableau[0], tableau[1], tableau[2])
    print(tableau[3], tableau[4], tableau[5])
    print(tableau[6], tableau[7], tableau[8])

def DrawTableau():
    placement = 0
    for case in coords_imgs:
        if tableau[placement] == "":
            img_case = ImgPlaceVoid
        elif tableau[placement] == "X":
            img_case = ImgPlaceX
        else:
            img_case = ImgPlaceO

        window.blit(img_case,case)
        placement += 1

    pg.display.flip()

def DrawMenu():
    pass

def PosSymboleTableau(joueur = j1):
    # Input de l'utilisateur (LV1)
    """
    pos = int(input("Quel position ?"))
    if tableau[pos-1] == "":
        tableau[pos-1] = joueur

    else:
        print("mauvaise position")
        PosSymboleTableau(joueur)
    """

    # Input Souris
    x, y, B1, R1 = Mouse()
    for case in coords_test:
        if x >= case[0][0] and x <= case[1][0]:
            if y >= case[0][1] and y <= case[1][1]:
                tableau[case[2]] = joueur
                return True
    return False

# NE CHANGE PAS ENTRE LES VERSIONS
def VerificationTableau():
    for cas in verif_cases:
        if tableau[cas[0]] == signe_actuel:
            if tableau[cas[1]] == signe_actuel:
                if tableau[cas[2]] == signe_actuel:
                    print("Joueur ", signe_actuel, " a gagne !")
                    return True

    return False

#NE CHANGE PAS ENTRE LES VERSIONS
def Mouse():
    # Position
    x, y = pg.mouse.get_pos()

    # Clicks
    R = pg.mouse.get_rel()
    R1 = R[0]

    B = pg.mouse.get_pressed()
    B1 = B[0]


    return x, y, B1, R1



### ORDI ###
def ordinateur():
    pass



### GAME ###
a = 0
# Menu de choix
window.blit(ImgVersus, coords_menu[0][0])
window.blit(ImgComputer, coords_menu[1][0])
pg.display.flip()

while not choix_fait:
    x, y, B1, R1 = Mouse()
    #Versus
    if B1 == 1 and x >= coords_menu[0][1] and x <= coords_menu[0][2] and y >= coords_menu[0][3] and y <= coords_menu[0][4] :
        choix_fait = True
        while not fin_jeu:
            # Affichage Graphique
            # PrintTableau()
            DrawTableau()

            # Choix du joueur
            while not position:
                x, y, B1, R1 = Mouse()

                if B1 == 1:
                    if signe_actuel == j1 and a == 0:
                        position = PosSymboleTableau(j1)
                        # Verification de fin de jeu
                        fin_jeu = VerificationTableau()
                        signe_actuel = j2
                        tours += 1
                        if position:
                            a += 1
                    elif signe_actuel == j2 and a == 0:
                        position = PosSymboleTableau(j2)
                        # Verification de fin de jeu
                        fin_jeu = VerificationTableau()
                        signe_actuel = j1
                        tours += 1
                        if position:
                            a += 1

                if R1 == 1:
                    a = 0

                # Events
                for event in pg.event.get():
                    if event.type == QUIT:
                        fin_jeu = True
                        position = True

                    elif event.type == KEYDOWN:
                        # Escape
                        if event.key in [K_q]:
                            fin_jeu = True
                            position = True

            position = False

            # Tours
            if tours == 9:
                print("Egalite")
                fin_jeu = True

            # Events
            for event in pg.event.get():
                if event.type == QUIT:
                    fin_jeu = True

                elif event.type == KEYDOWN:
                    # Escape
                    if event.key in [K_q]:
                        fin_jeu = True

        # Quit the game
        pg.quit()

    #Computer
    if B1 == 1 and x >= coords_menu[1][1] and x <= coords_menu[1][2] and y >= coords_menu[1][3] and y <= coords_menu[1][4] :
        choix_fait = True
        while not fin_jeu:
            # Affichage Graphique
            # PrintTableau()
            DrawTableau()

            # Choix du joueur
            while not position:
                x, y, B1, R1 = Mouse()

                if B1 == 1:
                    if signe_actuel == j1 and a == 0:
                        position = PosSymboleTableau(j1)
                        # Verification de fin de jeu
                        fin_jeu = VerificationTableau()
                        signe_actuel = j2
                        tours += 1
                        if position:
                            a += 1
                    elif signe_actuel == j2 and a == 0:
                        position = PosSymboleTableau(j2)
                        # Verification de fin de jeu
                        fin_jeu = VerificationTableau()
                        signe_actuel = j1
                        tours += 1
                        if position:
                            a += 1

                if R1 == 1:
                    a = 0

                # Events
                for event in pg.event.get():
                    if event.type == QUIT:
                        fin_jeu = True
                        position = True

                    elif event.type == KEYDOWN:
                        # Escape
                        if event.key in [K_q]:
                            fin_jeu = True
                            position = True

            position = False

            # Tours
            if tours == 9:
                print("Egalite")
                fin_jeu = True

            # Events
            for event in pg.event.get():
                if event.type == QUIT:
                    fin_jeu = True

                elif event.type == KEYDOWN:
                    # Escape
                    if event.key in [K_q]:
                        fin_jeu = True

        # Quit the game
        pg.quit()

    # Events
    for event in pg.event.get():
        if event.type == QUIT:
            fin_jeu = True
            position = True

        elif event.type == KEYDOWN:
            # Escape
            if event.key in [K_q]:
                fin_jeu = True
                position = True