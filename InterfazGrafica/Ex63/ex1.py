import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Ventana con botones")
        self.label1=tk.Label(self.ventana1, text="Frutas:")
        self.label1.grid(column=0, row=0)
        self.listbox1=tk.Listbox(self.ventana1, height=3)
        self.listbox1.grid(column=1, row=0)
        self.listbox1.insert(0, "Manzana")
        self.listbox1.insert(1, "Pera")
        self.listbox1.insert(2, "Banana")
        self.boton1=tk.Button(self.ventana1, text="Mostrar", command=self.mostrar)
        self.boton1.grid(column=1, row=2)
        self.ventana1.mainloop()

    def mostrar(self):
        cadena=self.listbox1.get(tk.ACTIVE)
        self.ventana1.title(cadena)

ap1=Aplicacion()