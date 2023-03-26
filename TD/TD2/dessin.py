import tkinter as tk


def dessiner_cercle():
    x = canvas.winfo_width() / 2
    y = canvas.winfo_height() / 2
    canvas.create_oval(x-50, y-50, x+50, y+50, fill="#00f", outline="#00f")


def dessiner_carre():
    x = canvas.winfo_width() / 2
    y = canvas.winfo_height() / 2
    canvas.create_rectangle(x-50, y-50, x+50, y+50, fill="#f00",\
                            outline="#f00")


def dessiner_croix():
    x = canvas.winfo_width() / 2
    y = canvas.winfo_height() / 2
    canvas.create_rectangle(x-50, y-50, x+50, y+50, fill="", outline="#ff0")
    canvas.create_line(x-40, y, x+40, y, fill="#ff0", width=5)
    canvas.create_line(x, y-40, x, y+40, fill="#ff0", width=5)


# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Ma fenêtre graphique")

# Création du Canvas avec un fond noir
canvas = tk.Canvas(fenetre, bg="black", width=500, height=500, bd=5,\
                    relief=tk.RIDGE)
canvas.pack(side=tk.LEFT)

# Création du cadre pour les boutons 1, 2 et 3
frame_boutons = tk.Frame(fenetre)
frame_boutons.pack(side=tk.LEFT, padx=10)

# Création des 3 boutons en colonne
bouton1 = tk.Button(frame_boutons, text="cercle",font=('helvetica','10'), command=dessiner_cercle)
bouton1.pack(side=tk.TOP, pady=10)
bouton2 = tk.Button(frame_boutons, text="carré",font=('helvetica','10'), command=dessiner_carre)
bouton2.pack(side=tk.TOP, pady=10)
bouton3 = tk.Button(frame_boutons, text="croix",font=('helvetica','10'), command=dessiner_croix)
bouton3.pack(side=tk.TOP, pady=10)

# Création du bouton en haut centré et décalé à droite
bouton4 = tk.Button(fenetre, text="choisir une couleur",font=('helvetica','10'))
bouton4.pack(side=tk.TOP, pady=10)
canvas.create_window(canvas.winfo_width() / 2 + 250, 20, window=bouton4)

# Lancement de la boucle principale de la fenêtre
fenetre.mainloop()