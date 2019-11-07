# Jeu fait par Arthur Nordmann (19h25 -> 20h35)

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
tours = 0

### DEFS ###
def PrintTableau():
    print(tableau[0], tableau[1], tableau[2])
    print(tableau[3], tableau[4], tableau[5])
    print(tableau[6], tableau[7], tableau[8])

def PosSymboleTableau(joueur = j1):
    #Input de l'utilisateur
    pos = int(input("Quel position ?"))
    if tableau[pos-1] == "":
        tableau[pos-1] = joueur
    else:
        print("mauvaise position")
        PosSymboleTableau(joueur)

def VerificationTableau():
    for cas in verif_cases:
        if tableau[cas[0]] == signe_actuel:
            if tableau[cas[1]] == signe_actuel:
                if tableau[cas[2]] == signe_actuel:
                    print("Joueur ", signe_actuel, " a gagne !")
                    return True
    return False

### GAME ###
while fin_jeu == False:

    #Affichage Graphique
    PrintTableau()

    #Choix du joueur
    if signe_actuel == j1:
        PosSymboleTableau(j1)
        # Verification de fin de jeu
        fin_jeu = VerificationTableau()
        signe_actuel = j2
        tours += 1
    elif signe_actuel == j2:
        PosSymboleTableau(j2)
        # Verification de fin de jeu
        fin_jeu = VerificationTableau()
        signe_actuel = j1
        tours += 1

    #Tours
    if tours == 9:
        print("Egalite")
        fin_jeu = True

