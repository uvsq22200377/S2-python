import tkinter as tk

class DessinApp(tk.Frame):

    def init(self, master=None):

        super().init(master)
        self.master = master
        self.pack()
        self.mode_dessin = False
        self.points = []
        self.creer_widgets()

    def creer_widgets(self):

        self.dessin_canvas = tk.Canvas(self, width=400, height=400)
        self.dessin_canvas.pack(side="top")
        self.dessin_canvas.bind("<Button-1>", self.commencer_dessin)
        self.dessin_canvas.bind("<B1-Motion>", self.dessiner_point)
        self.dessin_canvas.bind("<ButtonRelease-1>", self.arreter_dessin)
        self.bouton = tk.Button(self, text="Activer le mode dessin", command=self.changer_mode)
        self.bouton.pack(side="bottom")

    def changer_mode(self):

        self.mode_dessin = not self.mode_dessin
        if self.mode_dessin:
            self.bouton.config(text="Désactiver le mode dessin")
        else:
            self.bouton.config(text="Activer le mode dessin")

    def commencer_dessin(self, event):

        if self.mode_dessin:
            self.points.append((event.x, event.y))

    def dessiner_point(self, event):

        if self.mode_dessin:
            self.points.append((event.x, event.y))
        self.dessin_canvas.create_oval(event.x-3, event.y-3, event.x+3, event.y+3, fill="black")

    def arreter_dessin(self, event):

        if self.mode_dessin:
            self.points.append((event.x, event.y))
        self.dessiner_nuage()

    def dessiner_nuage(self):

        self.dessin_canvas.delete("nuage")
        for x, y in self.points:
            self.dessin_canvas.create_oval(x-3, y-3, x+3, y+3, tags="nuage", fill="black")

    if __name__ == "__main__":
        root = tk.Tk()
app = DessinApp
app.mainloop()
