import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Ventana con botones")
        self.seleccion=tk.IntVar()
        self.seleccion.set(1)
        self.radio1=tk.Radiobutton(self.ventana1, text="Rojo", variable=self.seleccion, value=1, command=self.cambio_color)
        self.radio1.grid(column=0, row=0)
        self.radio2=tk.Radiobutton(self.ventana1, text="Verde", variable=self.seleccion, value=2, command=self.cambio_color)
        self.radio2.grid(column=1, row=0)
        self.radio3=tk.Radiobutton(self.ventana1, text="Azul", variable=self.seleccion, value=3, command=self.cambio_color)
        self.radio3.grid(column=2, row=0)
        self.ventana1.mainloop()

    def cambio_color(self):
        if self.seleccion.get()==1:
            self.ventana1.configure(bg="red")
        elif self.seleccion.get()==2:
            self.ventana1.configure(bg="green")
        else:
            self.ventana1.configure(bg="blue")

aplicacion1=Aplicacion()