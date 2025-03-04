import random
import tkinter as tk


ordonnés = []
abscisse = []
nombre_de_point = 0
L = 600
H = 600
racine = tk.Tk()
racine.title("graphique")
canvas = tk.Canvas(racine, bg="white", width=L, height=H)
canvas.pack()
canvas.grid()


def cree_fichier_alea(nb, nomfichier):
    with open(nomfichier, 'w')as f:
        for i in range(nb):
            x = random.uniform(0, 500)
            y = random.uniform(0, 500)
            f.write(f"{x} {y}\n")


def lit_fichier(nomfic):
    abscisse = []
    ordonnés = []
    with open(nomfic, 'r') as f:
        ligne = f.readline()
        while ligne:
            x, y = ligne.split(' ')
            abscisse.append(float(x))
            ordonnés.append(float(y))
            ligne = f.readline()
    return abscisse, ordonnés


def trace_Nuage(nomf):
    abscisse, ordonnés = lit_fichier(nomf)
    nombre_de_point = len(abscisse)
    for i in range(len(abscisse)):
        canvas.create_oval(abscisse[i] - 1, ordonnés[i] - 1, abscisse[i] + 1, ordonnés[i] + 1, fill='black')
    print(nombre_de_point)


def trace_droite(a, b):
    x1 = 0
    y1 = b
    x2 = 1
    y2 = a + b
    print("Point 1 : ({}, {})".format(x1, y1))
    print("Point 2 : ({}, {})".format(x2, y2))


def moyenne(serie):
    somme = sum(serie)
    moy = somme / len(serie)
    return moy


def variance(serie):
    somme = sum(serie)
    variance = (somme - moyenne(serie))**2 / len(serie)
    return variance


def covariance(serieX, serieY):
    sommeX = sum(serieX)
    sommeY = sum(serieY)
    covariance = (sommeX - moyenne(serieX))(sommeY - moyenne(serieY)) / len(serieY)
    return covariance


def correlation(serieX, serieY):
    correlation = covariance(serieX, serieY)/(((variance(serieX))(variance(serieY)))**0.5)
    return correlation


def fortecorrelation(serieX, serieY):
    cor = correlation(serieX, serieY)
    if cor > 0.8 or cor < -0.8:
        return True
    else:
        return False


def droite_reg(serieX, serieY):
    a = covariance(serieX, serieY)/variance(serieX)
    b = moyenne(serieY) - a*moyenne(serieX)
    tuple = [a, b]
    return tuple


fenetre = tk.Tk()
fenetre.title("fenêtre graphique")




cree_fichier_alea(5, 'teststat')
lit_fichier('teststat')
trace_Nuage('teststat')
racine.mainloop()
