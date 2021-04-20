############################################
# groupe BI 2
# Olivier COTTIN
# Clément LUKACS
# Lara ESPINASSE   
# Gabriel HAMOUCH
# Hugo NAZAC
# https://github.com/uvsq22000753/Snake.git
#############################################

######################
# Import des librairie

import tkinter as tk
from random import randint

######################
# CONSTANTES

WIDTH = 500
HEIGHT = 500
carre = 11

######################
# Variables globale

x, y = WIDTH / carre, HEIGHT / carre

direct = "none"
vitesse = 100
jouable = 'True'

carte = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
         ]

objets = []

######################
# Fonction

def affichage():
    global objets
    if len(objets) != 0:
        for elem in objets:
            canvas.delete(elem)
        objets = []
    for i in range(len(carte)):
        for j in range(len(carte[0])):
            if carte[j][i] == 1:
                mur = canvas.create_rectangle(x * i, y * j, (x * i) + x, (y * j) + y, fill="wheat2",outline="black")
                objets.append(mur)
            elif carte[j][i] == 0:
                herbe = canvas.create_rectangle(x * i, y * j, (x * i) + x, (y * j) + y, fill="pale green", outline="pale green")
                objets.append(herbe)
            elif carte[j][i] == 2:
                pomme1 = canvas.create_rectangle(x * i, y * j, (x * i) + x, (y * j) + y, fill="pale green",outline="pale green")
                pomme2 = canvas.create_oval((x * i) +10, (y * j) + 10, ((x * i) + x) - 10, ((y * j) + y) - 10, fill="firebrick2")
                objets.append(pomme1)
                objets.append(pomme2)
            elif carte[j][i] == 3:
                tete = canvas.create_rectangle(x * i, y * j, (x * i) + x, (y * j) + y, fill="springgreen4",outline="springgreen4")
                objets.append(tete)


def generation_pomme():
    alun = randint(1, 9)
    aldeux = randint(1, 9)
    carte[alun][aldeux] = 2
    affichage()


def snake():
    carte[7][6] = 3
    affichage()


def mouvement(*args):
    global direct
    global jouable
    if jouable == 'True':
        if direct == "haut":
            for i in range(len(carte)):
                for j in range(len(carte[0])):
                    if carte[j][i] == 3:
                        temp1, temp2 = i, j
            if carte[temp2 - 1][temp1] == 1:
                jouable = 'False'
            carte[temp2][temp1] = 0
            carte[temp2-1][temp1] = 3

        if direct == "bas":
            for i in range(len(carte)):
                for j in range(len(carte[0])):
                    if carte[j][i] == 3:
                        temp1, temp2 = i, j
            if carte[temp2 + 1][temp1] == 1:
                jouable = 'False'
            carte[temp2][temp1] = 0
            carte[temp2+1][temp1] = 3

        if direct == "gauche":
            for i in range(len(carte)):
                for j in range(len(carte[0])):
                    if carte[j][i] == 3:
                        temp1, temp2 = i, j
            if carte[temp2][temp1 - 1] == 1:
                jouable = 'False'
            carte[temp2][temp1] = 0
            carte[temp2][temp1-1] = 3

        if direct == "droite":
            for i in range(len(carte)):
                for j in range(len(carte[0])):
                    if carte[j][i] == 3:
                        temp1, temp2 = i, j
            if carte[temp2][temp1 + 1] == 1:
                jouable= 'False'
            carte[temp2][temp1] = 0
            carte[temp2][temp1+1] = 3
        affichage()
        print(direct)
        racine.after(vitesse,mouvement)


def haut(*args):
    global direct
    direct = "haut"


def bas(*args):
    global direct
    direct = "bas"


def gauche(*args):
    global direct
    direct = "gauche"


def droite(*args):
    global direct
    direct = "droite"

######################
# Programme principal

racine = tk.Tk()

racine.title("project snake")

#######################
# Création des widgets

canvas = tk.Canvas(racine, width=str(WIDTH), heigh=str(HEIGHT), bg="black")
canvas.grid()

#######################
# Appel des fonctions

affichage()
generation_pomme()
snake()
mouvement()


racine.bind("<Up>",haut)
racine.bind("<Down>",bas)
racine.bind("<Left>",gauche)
racine.bind("<Right>",droite)
racine.resizable(False, False)

racine.mainloop()
