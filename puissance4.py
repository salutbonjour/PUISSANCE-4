# PUISSANCE 4 REMAKE (Version 1)
# by : salut bonjour
# twitter : @saiutbonjour

# notes :

# c'est uniquement un test pour m'entraîner et je sais que c'est pas optimisé, et qu'en plus le jeu est pas vrmt fini
# sachant qu'il indique pas quand qql gagne (ce qui, avec la facon dont j'ai fait le code, est imposible à faire a
# part en testant toutes les possibilités, ce qui ferais un code de 428 GO. donc peut etre que je reeserais
# avec pygame de faire qql chose de plus fini, on vera !
#
#aussi si sur les anotations c pas les bonnes lignes bah jen ai rien a foutre bande de fils de pute arretez de vous plaindre

import os
import time
import keyboard


# \RELOAD() / L15-L67/ :
# >>>1.Remet toutes les variables du jeu à la variable vide.
def reload():
    global vide
    global a_six, b_six, c_six, d_six, e_six, f_six, g_six  # 6
    global a_five, b_five, c_five, d_five, e_five, f_five, g_five  # 5
    global a_four, b_four, c_four, d_four, e_four, f_four, g_four  # 4
    global a_three, b_three, c_three, d_three, e_three, f_three, g_three  # 3
    global a_two, b_two, c_two, d_two, e_two, f_two, g_two  # 2
    global a_one, b_one, c_one, d_one, e_one, f_one, g_one  # 1
    vide = " "
    a_six = vide
    b_six = vide
    c_six = vide
    d_six = vide
    e_six = vide
    f_six = vide
    g_six = vide
    a_five = vide
    b_five = vide
    c_five = vide
    d_five = vide
    e_five = vide
    f_five = vide
    g_five = vide
    a_four = vide
    b_four = vide
    c_four = vide
    d_four = vide
    e_four = vide
    f_four = vide
    g_four = vide
    a_three = vide
    b_three = vide
    c_three = vide
    d_three = vide
    e_three = vide
    f_three = vide
    g_three = vide
    a_two = vide
    b_two = vide
    c_two = vide
    d_two = vide
    e_two = vide
    f_two = vide
    g_two = vide
    a_one = vide
    b_one = vide
    c_one = vide
    d_one = vide
    e_one = vide
    f_one = vide
    g_one = vide


# \CLEAR() / L70-L71/ :
# >>>1.Efface toutes les valeurs présentes à l'écran.
def clear():
    os.system('cd C:\\Windows|cls' if os.name == 'nt' else 'clear')


# \AVANTJEU() / L80-L93/ :
# >>>1.Demande le nom du joueur 1 et 2.
# >>>2.Indique qui aura quel pion.
# >>>3.Appelle la fonction draw().
def avantjeu():
    reload()
    clear()
    global joueur1
    global joueur2
    global tour
    time.sleep(1)
    joueur1 = input("Veuillez entrer le nom du joueur 1.\n")
    print("{} aura les pions X ".format(joueur1))
    joueur2 = input("Veuillez entrer le nom du joueur 2.")
    print("{} aura les pions O ".format(joueur2))
    time.sleep(0.3)
    print("C'est {} qui commence".format(joueur1))
    time.sleep(2)
    tour = 'O'
    draw()


# \PLACER() / L100-L299/ :
# >>>1.Vérifie si le tour est au joueur 1 ou 2 puis dit a qui est le tour.
# >>>2.Demande d'insérer une valer entre 'a' et 'g'.
# >>>3.En fonction de la valeur donnée, voit si on peut poser a la premiere case, si oui on pose, sinon on regarde la deuxième, la troisème, etc.
def placer():
    global a_six, b_six, c_six, d_six, e_six, f_six, g_six  # 6
    global a_five, b_five, c_five, d_five, e_five, f_five, g_five  # 5
    global a_four, b_four, c_four, d_four, e_four, f_four, g_four  # 4
    global a_three, b_three, c_three, d_three, e_three, f_three, g_three  # 3
    global a_two, b_two, c_two, d_two, e_two, f_two, g_two  # 2
    global a_one, b_one, c_one, d_one, e_one, f_one, g_one  # 1
    if tour == 'X':
        print("C'est au tour de {} |{}| ".format(joueur1, tour))
    elif tour == 'O':
        print("C'est au tour de {} |{}| ".format(joueur2, tour))
    while True:
        choix = input("Où désirez vous placer votre pion\n")
        if choix == 'fin':
            start()
        if choix == 'reload':
            reload()
            draw()
        if choix == 'a':
            if a_one != " ":
                if a_two != " ":
                    if a_three != " ":
                        if a_four != " ":
                            if a_five != " ":
                                if a_six != " ":
                                    print("Toute la ligne A est prise, veuillez en choisir une autre !")
                                elif a_six == " ":
                                    a_six = tour
                                    break
                            elif a_five == " ":
                                a_five = tour
                                break
                        elif a_four == " ":
                            a_four = tour
                            break
                    elif a_three == " ":
                        a_three = tour
                        break
                elif a_two == " ":
                    a_two = tour
                    break
            elif a_one == " ":
                a_one = tour
                break
        if choix == 'b':
            if b_one != " ":
                if b_two != " ":
                    if b_three != " ":
                        if b_four != " ":
                            if b_five != " ":
                                if b_six != " ":
                                    print("Toute la ligne B est prise, veuillez en choisir une autre !")
                                elif b_six == " ":
                                    b_six = tour
                                    break
                            elif b_five == " ":
                                b_five = tour
                                break
                        elif b_four == " ":
                            b_four = tour
                            break
                    elif b_three == " ":
                        b_three = tour
                        break
                elif b_two == " ":
                    b_two = tour
                    break
            elif b_one == " ":
                b_one = tour
                break
        if choix == 'c':
            if c_one != " ":
                if c_two != " ":
                    if c_three != " ":
                        if c_four != " ":
                            if c_five != " ":
                                if c_six != " ":
                                    print("Toute la ligne C est prise, veuillez en choisir une autre !")
                                elif c_six == " ":
                                    c_six = tour
                                    break
                            elif c_five == " ":
                                c_five = tour
                                break
                        elif c_four == " ":
                            c_four = tour
                            break
                    elif c_three == " ":
                        c_three = tour
                        break
                elif c_two == " ":
                    c_two = tour
                    break
            elif c_one == " ":
                c_one = tour
                break
        if choix == 'd':
            if d_one != " ":
                if d_two != " ":
                    if d_three != " ":
                        if d_four != " ":
                            if d_five != " ":
                                if d_six != " ":
                                    print("Toute la ligne D est prise, veuillez en choisir une autre !")
                                elif d_six == " ":
                                    d_six = tour
                                    break
                            elif d_five == " ":
                                d_five = tour
                                break
                        elif d_four == " ":
                            d_four = tour
                            break
                    elif d_three == " ":
                        d_three = tour
                        break
                elif d_two == " ":
                    d_two = tour
                    break
            elif d_one == " ":
                d_one = tour
                break
        if choix == 'e':
            if e_one != " ":
                if e_two != " ":
                    if e_three != " ":
                        if e_four != " ":
                            if e_five != " ":
                                if e_six != " ":
                                    print("Toute la ligne E est prise, veuillez en choisir une autre !")
                                elif e_six == " ":
                                    e_six = tour
                                    break
                            elif e_five == " ":
                                e_five = tour
                                break
                        elif e_four == " ":
                            e_four = tour
                            break
                    elif e_three == " ":
                        e_three = tour
                        break
                elif e_two == " ":
                    e_two = tour
                    break
            elif e_one == " ":
                e_one = tour
                break
        if choix == 'f':
            if f_one != " ":
                if f_two != " ":
                    if f_three != " ":
                        if f_four != " ":
                            if f_five != " ":
                                if f_six != " ":
                                    print("Toute la ligne F est prise, veuillez en choisir une autre !")
                                elif f_six == " ":
                                    f_six = tour
                                    break
                            elif f_five == " ":
                                f_five = tour
                                break
                        elif f_four == " ":
                            f_four = tour
                            break
                    elif f_three == " ":
                        f_three = tour
                        break
                elif f_two == " ":
                    f_two = tour
                    break
            elif f_one == " ":
                f_one = tour
                break
        if choix == 'g':
            if g_one != " ":
                if g_two != " ":
                    if g_three != " ":
                        if g_four != " ":
                            if g_five != " ":
                                if g_six != " ":
                                    print("Toute la ligne G est prise, veuillez en choisir une autre !")
                                elif g_six == " ":
                                    g_six = tour
                                    break
                            elif g_five == " ":
                                g_five = tour
                                break
                        elif g_four == " ":
                            g_four = tour
                            break
                    elif g_three == " ":
                        g_three = tour
                        break
                elif g_two == " ":
                    g_two = tour
                    break
            elif g_one == " ":
                g_one = tour
                break
    draw()


# \DRAW() / L305-L20/ :
# >>>1.Change de tour.
# >>>2.Réecrit le tableau avec les valeurs données par placer().
# >>>3.Renvoie a la fonction placer, créant ainsi une boucle.
def draw():
    global tour
    if tour == 'X':
        tour = 'O'
    elif tour == 'O':
        tour = 'X'
    clear()
    print("")
    print("6|{}|{}|{}|{}|{}|{}|{}|".format(a_six, b_six, c_six, d_six, e_six, f_six, g_six))
    print("5|{}|{}|{}|{}|{}|{}|{}|".format(a_five, b_five, c_five, d_five, e_five, f_five, g_five))
    print("4|{}|{}|{}|{}|{}|{}|{}|".format(a_four, b_four, c_four, d_four, e_four, f_four, g_four))
    print("3|{}|{}|{}|{}|{}|{}|{}|".format(a_three, b_three, c_three, d_three, e_three, f_three, g_three))
    print("2|{}|{}|{}|{}|{}|{}|{}|".format(a_two, b_two, c_two, d_two, e_two, f_two, g_two))
    print("1|{}|{}|{}|{}|{}|{}|{}|".format(a_one, b_one, c_one, d_one, e_one, f_one, g_one))
    print("  a b c d e f g \n\n")
    placer()


# \MENU() / L322-L350/ :
# >>>1.Bannière ASCII "PUISSANCE 4".
# >>>2. Attends la pression de la touche entrée vant de renvoyer à la fonction avantjeu().
def menu():
    clear()
    time.sleep(0.1)
    print(" \n"
          " PPPPPP  UU   UU IIIII  SSSSS   SSSSS    AAA   NN   NN  CCCCC  EEEEEEE     \n"
          " PP   PP UU   UU  III  SS      SS       AAAAA  NNN  NN CC    C EE          \n"
          " PPPPPP  UU   UU  III   SSSSS   SSSSS  AA   AA NN N NN CC      EEEEE       \n"
          " PP      UU   UU  III       SS      SS AAAAAAA NN  NNN CC    C EE          \n"
          " PP       UUUUU  IIIII  SSSSS   SSSSS  AA   AA NN   NN  CCCCC  EEEEEEE     \n"
          "                                                                           \n"
          "                                   4                                       \n"
          "                                 4 4                                       \n"
          "                                4  4                                       \n"
          "                               4   4                                       \n"
          "                              444444                                       \n"
          "                                  44                                       \n"
          "                                  44                                       \n"
          )
    time.sleep(2)
    avantjeu()


# \START() / L354-355/ :
# >>>1.Lance le jeu en renvoyant vers la fonction menu().
def start():
    menu()


start()  # Appelle à la fonction start, lance le jeu.
